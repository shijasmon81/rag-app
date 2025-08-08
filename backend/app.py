from fastapi import FastAPI
from pydantic import BaseModel
from vector_store import load_vectorstore
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS (especially important if frontend is calling this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the FAISS vector store
vectorstore = load_vectorstore()

# Define the request model
class QuestionRequest(BaseModel):
    question: str

# Define the API endpoint
@app.post("/ask")
def ask_question(req: QuestionRequest):
    results = vectorstore.similarity_search(req.question, k=3)
    
    formatted_chunks = []
    for i, r in enumerate(results, 1):
        source = r.metadata.get("source", "Unknown source")
        chunk = f"**Source {i}:** {source}\n{r.page_content.strip()}"
        formatted_chunks.append(chunk)
    
    combined_answer = "\n\n---\n\n".join(formatted_chunks)
    return {"answer": combined_answer}


