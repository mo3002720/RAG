from fastapi import FastAPI
from pydantic import BaseModel
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

app = FastAPI()

embedding_func = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = Chroma(collection_name="rag_collection", persist_directory="./chroma_db", embedding_function=embedding_func)
llm = OllamaLLM(model="llama3")

class DocumentRequest(BaseModel):
    text: str
    doc_id: str

class QueryRequest(BaseModel):
    question: str

@app.post("/index")
def index_document(doc: DocumentRequest):
    vector_store.add_texts(texts=[doc.text], ids=[doc.doc_id])
    return {"success": True, "message": f"Document {doc.doc_id} indexed."}

@app.post("/search")
def search_document(query: QueryRequest):
    docs = vector_store.similarity_search(query.question, k=1)
    matched_text = docs[0].page_content if docs else "No documents found."
    return {"success": True, "documents": matched_text}

@app.post("/ask")
def ask_llm(query: QueryRequest):
    docs = vector_store.similarity_search(query.question, k=1)
    context = docs[0].page_content if docs else "No context found."
    
    prompt = f"Use the following context to answer the question: {context}\n\nQuestion: {query.question}"
    answer = llm.invoke(prompt)
    
    return {"success": True, "answer": answer}