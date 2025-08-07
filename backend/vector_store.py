import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def save_vectorstore(vectorstore, path="./faiss_store"):
    if not os.path.exists(path):
        os.makedirs(path)
    vectorstore.save_local(path)

def load_vectorstore(path="./faiss_store"):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(path, embeddings=embedding_model, allow_dangerous_deserialization=True)
