import os
from dotenv import load_dotenv
import validators
import streamlit as st
from langchain_groq import ChatGroq
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import UnstructuredURLLoader


load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")


st.set_page_config(page_title="Youtube and Website Summarization app",page_icon=":pencil:")

st.title(":pencil: Youtube or Website Summarizer")
st.write("This app summarizes your youtube or Website contents")

st.sidebar.title("About the app")
st.sidebar.info("This app provides a detailed and concise summary of your youtube or website contents. To make use of the contents, make sure you have your groq API key and provide the correct link.")

with st.sidebar:
    groq_api_key = st.text_input("GROQ_API_KEY",value="",type="password")


model = ChatGroq(model="llama-3.2-3b-preview", groq_api_key=groq_api_key)

prompt = """
In 300 words, summarize the content provided as if you are summarizing it so that the person will not have need to watch the video. 
Make it as detailed as possible.
Content: {text}
"""

chain = PromptTemplate(template=prompt,input_variables = ["text"])

chain_llm = load_summarize_chain(model, chain_type="stuff", prompt=chain)

def get_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = "\n".join(item['text'] for item in transcript)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=100)
        splitted_docs = text_splitter.split_text(text)
        doc = [Document(page_content=chunk) for chunk in splitted_docs]
        return doc
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

option = st.sidebar.radio("Choose your option", ['Youtube','Website'])



if option == 'Youtube':
    youtube_url = st.text_input("Input the Youtube URL")
    if st.button ("Submit"):
        if not groq_api_key:
            st.error("Provide your Groq API key")
        elif not youtube_url:
            st.error("Provide the video url")
        else:
            video_id = get_video_id(youtube_url)

            if not video_id:
            
                st.error("Invalid Youtube URL")
            else:
                with st.spinner("Fetching video details"):
                    transcript = fetch_transcript(video_id)
                    summary = chain_llm.run(transcript)
                    st.write(summary)
elif option == "Website":
    website_url = st.text_input("Input the Website URL")

    if st.button("Submit"):
        if not groq_api_key:
            st.error("Please provide your Groq API key")
    
        elif not website_url:
            st.error("Provide a Website URL")
        
        elif validators.url(website_url):
                
                with st.spinner("Summarizing Web Content"):
                    try:
                        loader = UnstructuredURLLoader(urls=[website_url])
                        docs = loader.load()
                        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=100)
                        splitted_docs = text_splitter.split_documents(docs)
                        summary = chain_llm.run(splitted_docs)
                        st.write(summary)
                    except Exception as e:
                        st.error (f"Error summarizing website: {str(e)}")
        else:
            st.error("Provide a valid URL")

                    

