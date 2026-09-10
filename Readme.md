# 🤖 AI Document Copilot — Full-Stack RAG Chatbot

A full-stack **Retrieval-Augmented Generation (RAG)** chatbot that allows users to interact with their own PDF and text documents using **Google Gemini**.

The application combines a **FastAPI backend**, **Streamlit frontend**, **FAISS vector search**, and **PostgreSQL** to provide context-aware answers with **persistent, user-specific conversation memory**.

---

## 🚀 Features

* 📄 **Document-based Question Answering** — Ask questions about custom PDF and `.txt` documents.
* 🧠 **RAG Pipeline** — Retrieves relevant document context before generating answers.
* 🔍 **Semantic Search** — Uses Hugging Face embeddings with FAISS for efficient similarity search.
* 💬 **Conversational Memory** — Maintains chat history across conversations.
* 👤 **User Login** — Simple user authentication system.
* 💾 **Persistent Memory** — Stores users and conversation history in PostgreSQL.
* ⚡ **REST API Backend** — FastAPI handles authentication, queries, and chat history.
* 🖥️ **Interactive UI** — Streamlit provides the frontend chat interface.
* 🔗 **Frontend–Backend Architecture** — Streamlit communicates with the FastAPI backend through REST APIs.

---

## 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │     User / Client    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Streamlit Frontend  │
                 │   Chat Interface     │
                 └──────────┬───────────┘
                            │ REST API
                            ▼
                 ┌──────────────────────┐
                 │    FastAPI Backend   │
                 │                      │
                 │  Authentication      │
                 │  Query Processing    │
                 │  Chat History        │
                 │  RAG Pipeline        │
                 └───────┬───────┬──────┘
                         │       │
              ┌──────────┘       └────────────┐
              ▼                               ▼
     ┌─────────────────┐             ┌─────────────────┐
     │   FAISS Vector  │             │   PostgreSQL    │
     │      Store      │             │    Database     │
     │                 │             │                 │
     │ HuggingFace     │             │ Users           │
     │ Embeddings      │             │ Chat History    │
     └────────┬────────┘             └─────────────────┘
              │
              ▼
     ┌─────────────────┐
     │ Relevant Context│
     └────────┬────────┘
              │
              ▼
     ┌─────────────────┐
     │ LangChain +     │
     │ Google Gemini   │
     └────────┬────────┘
              │
              ▼
        Generated Answer
```

---

## 🔄 RAG Pipeline

The application follows a typical Retrieval-Augmented Generation workflow:

```text
PDF / TXT Documents
        │
        ▼
 Document Loading
        │
        ▼
 Text Splitting
        │
        ▼
 Hugging Face Embeddings
        │
        ▼
   FAISS Vector Store
        │
        │
        ▼
     User Query
        │
        ▼
 Semantic Retrieval
        │
        ▼
 Relevant Documents
        │
        ▼
 LangChain RAG Chain
        │
        ▼
 Google Gemini
        │
        ▼
 Context-Aware Answer
```

---

## 🧠 How It Works

### 1. Document Ingestion

Custom PDF and text documents are loaded and processed before being added to the knowledge base.

### 2. Text Processing

Documents are split into smaller chunks to make retrieval more effective.

### 3. Embedding Generation

Each document chunk is converted into a numerical vector using:

```text
HuggingFace
sentence-transformers/all-MiniLM-L6-v2
```

### 4. Vector Storage

The generated embeddings are stored in **FAISS**, allowing the application to perform semantic similarity searches.

### 5. Query Processing

When a user asks a question:

1. The query is received by the FastAPI backend.
2. Relevant document chunks are retrieved from FAISS.
3. Chat history is incorporated for conversational context.
4. The retrieved context is passed to the RAG chain.
5. Google Gemini generates the final response.

### 6. Persistent Chat Memory

User information and conversation history are stored in **PostgreSQL**, allowing conversations to persist beyond a single session.

---

## 🛠️ Tech Stack

| Category              | Technology                           |
| --------------------- | ------------------------------------ |
| Language              | Python                               |
| Backend               | FastAPI                              |
| Server                | Uvicorn                              |
| Frontend              | Streamlit                            |
| API Communication     | Requests                             |
| RAG Framework         | LangChain                            |
| LLM                   | Google Gemini                        |
| Embeddings            | Hugging Face / Sentence Transformers |
| Vector Store          | FAISS                                |
| Database              | PostgreSQL                           |
| Database Driver       | psycopg2                             |
| Environment Variables | python-dotenv                        |

---

## 📁 Project Structure

```text
AI-Document-Copilot/
│
├── backend/
│   ├── main.py
│   └── ...
│
├── frontend/
│   ├── app.py
│   └── ...
│
├── data/
│   ├── documents/
│   └── ...
│
├── vectorstore/
│   └── ...
│
├── requirements.txt
├── .env
└── README.md
```

> Project structure may vary depending on your implementation.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Document-Copilot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Add any other environment variables required by your implementation.

---

## ▶️ Running the Application

### Start the FastAPI backend

```bash
uvicorn main:app --reload
```

### Start the Streamlit frontend

```bash
streamlit run app.py
```

Then open the Streamlit application in your browser.

---

## 💡 Example Use Cases

The chatbot can be used to interact with personal or project-specific documents.

Example questions:

```text
"What are the key points discussed in this document?"

"Explain the main concept mentioned in section 3."

"What does the document say about the project requirements?"

"Summarize the important information from these documents."
```

---

## 🔑 Key Concepts Demonstrated

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Large Language Model integration
* Semantic search
* Text embeddings
* Vector databases
* Document ingestion
* REST API development
* Backend/frontend separation
* Database integration
* Persistent conversational memory
* User authentication
* Multi-turn conversations

---

## 📌 Future Improvements

Potential improvements include:

* 🔐 JWT-based authentication
* 📚 Support for additional document formats
* 🔎 Hybrid keyword + semantic search
* 📊 Retrieval and response evaluation
* 🧾 Source citations for retrieved document chunks
* ☁️ Cloud deployment
* 🐳 Docker containerization
* ⚡ Redis-based caching
* 🔄 Background document processing

---

## 👨‍💻 Project

**AI Document Copilot — Full-Stack RAG Application**

Built using **Python, FastAPI, Streamlit, LangChain, Google Gemini, Hugging Face, FAISS, and PostgreSQL.**

---

⭐ If you found this project useful, consider giving the repository a star!
