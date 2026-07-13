# 🎥 Chat with YouTube Video

> AI-powered Retrieval-Augmented Generation (RAG) application that lets users chat with any YouTube video using natural language.

---

## 📌 Problem Statement

YouTube contains hours of valuable educational content, but finding a specific piece of information often requires watching the entire video.

For example:

- What did the speaker say about AI?
- Summarize the complete video.
- Explain a specific topic discussed in the video.
- Ask questions in Hindi or English.

Watching the complete video just to find one answer is time-consuming and inefficient.

---

# 💡 Solution

This project converts a YouTube video into an intelligent searchable knowledge base.

Instead of manually searching through a long video, users simply paste the YouTube link and ask questions in natural language.

The application extracts the transcript, builds semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant information, and finally generates an accurate answer using Google's Gemini LLM.

---

# 🚀 Features

- 🎥 Chat with any YouTube Video
- 📄 Automatic Transcript Extraction
- 🧠 Semantic Search using Vector Embeddings
- ⚡ Fast Retrieval using FAISS
- 🤖 Gemini LLM powered answers
- 🌍 Supports English and Hindi questions
- 💬 Interactive Streamlit Chat Interface

---

# 🏗️ Project Workflow

```text
                 YouTube URL
                      │
                      ▼
         YouTube Transcript API
                      │
                      ▼
            Transcript Extraction
                      │
                      ▼
               Text Chunking
                      │
                      ▼
      Sentence Transformer Embeddings
                      │
                      ▼
           FAISS Vector Database
                      │
                      ▼
         Top Relevant Chunks Retrieved
                      │
                      ▼
             Google Gemini LLM
                      │
                      ▼
             Natural Language Answer
```

---

# ⚙️ Tech Stack

### Programming Language

- Python

### Framework

- Streamlit

### LLM

- Google Gemini

### Embedding Model

- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database

- FAISS

### Transcript Extraction

- youtube-transcript-api

### NLP

- NLTK

### Environment Management

- Python Virtual Environment (venv)

---

# 🧠 Models Used

## Embedding Model

**all-MiniLM-L6-v2**

- Embedding Dimension: 384
- Converts text chunks into dense vector representations for semantic similarity search.

---

## Large Language Model

**Google Gemini**

Responsible for:

- Understanding user questions
- Using retrieved context
- Generating accurate answers

---

# 📂 Project Structure

```text
chat-with-youtube-video/

│
├── src/
│   ├── app.py
│   ├── transcript.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   └── youtube_utils.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/sanskarshinde2906/chat-with-youtube-video.git
```

Move into project directory

```bash
cd chat-with-youtube-video
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m streamlit run src/app.py
```

---

# 📸 Demo

(Add screenshots here)

---

# 🔮 Future Improvements

- LangChain RecursiveCharacterTextSplitter
- Chat Memory
- Multi-video support
- Hybrid Search
- Timestamp-based Answers
- Streaming Responses
- Better UI
- Conversation History

---

# 👨‍💻 Author

**Sanskar Shinde**

B.Tech Computer Science (AI & ML)

GitHub

https://github.com/sanskarshinde2906

---

# ⭐ If you found this project useful, consider giving it a star.