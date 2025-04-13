#  🧠 Youtube Video and Website Content Summarizer

It's a good time to be a developer. Imagine looking a youtube video and its long and you want to quickly understand what the video is all about or maybe
you saw a web content and quickly wants to get a what the content is all about. This is what this project is all about. The aim of this project is to help user get a summary of a youtube video or Web content. 

## 📌 Features
#### Youtube Summarizer Features
* Extracts youtube transcript from any youtube video
* Splits the text using RecursiveCharacterTextSplitter
* Converts the splitted text to a document
* Summarizes the content using Langchain's load_summarize_chain

#### Website Summarizer Features
* The Website content summarizer of the application also implements the same features. The only change is that it uses validator
  to validate a website url 

## 📦 Tech Stack
| Category        |     Technologies Used |
|------------------|-----------------|
| **Frontend**     | Streamlit  |
| **Backend**      | Python  |
| **AI Model**     | Groq Llama-3 70B |
| **youtube_transcript_api** | Youtube API integration |
| **Unstructed Webloader**         | Loading Web Contents |
| **Environment Management** | dotenv |


## 🚀 Installation of Dependencies and Setup

### 1️⃣ Cloning the Repo/ Installation
```sh
git clone https://github.com/nnemolisastephen/Youtube_Website_Summarizer
cd Youtube_Website_Summarizer
pip install -r requirements.txt
```
### 2️⃣ Run the Application
```sh
streamlit run app.py
```
## 🤝 Contribution
You can open an issue or fork the repo. Pull requests are welcome!

## 📞 Contact
Feel free to reach out [Nnemolisa Stephen](https://github.com/nnemolisastephen) if you have any question.



