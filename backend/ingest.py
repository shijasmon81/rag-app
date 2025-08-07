import os
from newspaper import Article
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from vector_store import save_vectorstore

# ✅ 1. Define URL(s)
urls = [
    "https://huggingface.co/blog",
    "https://fastapi.tiangolo.com/",
    "https://react.dev/learn"
]

# ✅ 2. Scrape articles
documents = []

for url in urls:
    try:
        article = Article(url)
        article.download()
        article.parse()
        content = article.text.strip()
        if content:
            documents.append(Document(page_content=content, metadata={"source": url}))
        else:
            print(f"⚠️ No content found at {url}")
    except Exception as e:
        print(f"❌ Failed to scrape {url}: {str(e)}")

# ✅ 3. Check if documents were fetched
if not documents:
    raise ValueError("❌ No articles were successfully scraped.")

# ✅ 4. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(documents)

# ✅ 5. Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ✅ 6. Vector store
vectorstore = FAISS.from_documents(chunks, embedding_model)

# ✅ 7. Save vectorstore to disk
save_vectorstore(vectorstore, "./faiss_store")

print(f"✅ Scraped {len(documents)} articles. Stored {len(chunks)} chunks in FAISS.")
