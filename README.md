
# 🔍 Web-Scraped RAG (Retrieval-Augmented Generation) Application

This project is a fullstack **Retrieval-Augmented Generation (RAG)** system that lets users ask questions about the content scraped from a given website. It combines web scraping, semantic search, and large language models to generate relevant answers with real-time data ingestion.

---

## ✨ Features

- 🕸️ **Web Scraping:** Extracts content from webpages using BeautifulSoup.
- 🧠 **Semantic Embedding:** Embeds text using Hugging Face Transformers.
- 🔍 **FAISS Vector Store:** Efficient similarity search over embedded chunks.
- 🤖 **LLM Q&A with LangChain:** Retrieves relevant content and uses LLMs to generate responses.
- 🖥️ **React Frontend:** Clean user interface to ask questions and display answers.
- 🐳 **Dockerized:** Fully containerized using Docker with separate services for frontend and backend.

---

## 🧰 Tech Stack

| Layer        | Tools/Libraries                          |
|--------------|-------------------------------------------|
| **Backend**  | FastAPI, BeautifulSoup, FAISS, LangChain |
| **Frontend** | React.js, Axios                          |
| **Embedding**| Hugging Face Transformers                |
| **DevOps**   | Docker, Docker Compose                   |

---

## 📂 Folder Structure

```

rag-app/
│
├── backend/              # FastAPI app for ingestion and Q\&A
│   ├── app.py            # Main API server
│   ├── ingest.py         # Web scraper and embedding logic
│   ├── vector\_store.py   # FAISS vector DB logic
│   └── requirements.txt  # Python dependencies
│
├── frontend/             # React application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── docker-compose.yml    # Runs frontend and backend containers
├── Dockerfile            # Multi-stage Docker build
└── README.md             # Project documentation

````

---

## ⚙️ How It Works

1. **Web Ingestion:** 
   - `ingest.py` scrapes the webpage and chunks its content.
   - Each chunk is embedded and stored in a FAISS index.

2. **Question Answering:**
   - The user asks a question via the React UI.
   - The backend retrieves similar content chunks from FAISS.
   - LangChain and a local LLM generate a response based on context.

---

## 🚀 Getting Started

### 1. Clone the Repository


git clone https://github.com/yourusername/rag-app.git
cd rag-app
````

### 2. Build and Run with Docker


docker compose up --build
```

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📝 Future Improvements

* Add authentication
* Support for PDF/CSV ingestion
* Deploy to cloud (Render, Railway, etc.)
* Streamlit interface (optional)

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgements

* [Hugging Face Transformers](https://huggingface.co/)
* [LangChain](https://github.com/langchain-ai/langchain)
* [FAISS](https://github.com/facebookresearch/faiss)

---

> Built with ❤️ using Python, React, and LLMs.

```

---

