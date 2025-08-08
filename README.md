# 🧠 RAG Application – Fullstack (Backend + Frontend)

This is a multi-container Retrieval-Augmented Generation (RAG) application built with:

- 🧩 FastAPI backend using LangChain + FAISS for document embeddings
- 🌐 React frontend for querying the RAG pipeline
- 🐳 Docker Compose for container orchestration

---

## 📦 Project Structure

rag-app/
├── backend/
│ ├── app.py
│ ├── ingest.py
│ ├── vectorstore/
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
| ├── Dockerfile
│ └── ...
├── docker-compose.yml
├── README.md



docker-compose up --build
This will:

Run ingest.py once in the backend to prepare vectorstore

Start FastAPI backend on port 8000

Start React frontend on port 3000

🔗 Access Points
Service	URL
Frontend	http://localhost:3000
Backend	http://localhost:8000
Health	http://localhost:8000/health
Chat API	POST /chat endpoint

▶️ Ingesting Documents
ingest.py is executed automatically at backend container startup. You can re-run it with:


docker-compose exec backend python ingest.py

curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the content about?"}'


🧼 Clean Up
To stop all containers:
docker-compose down


To rebuild everything from scratch:
docker-compose up --build


📃 License
This project is open-source and free to use for educational and personal experimentation.
