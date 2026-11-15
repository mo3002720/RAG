# RAG
RAG
1) Install and run "ollama run llama3" in terminal
2) RUN-  "pip install fastapi uvicorn pydantic langchain-chroma langchain-ollama langchain-huggingface sentence-transformers"
3) to launch run "uvicorn main:app --reload"
4) go to- http://127.0.0.1:8000/docs
  
5)  Test Indexing in POST/index 
    {
  "text": "The Joel Test is a highly irresponsible, sloppy test to rate the quality of a software team. The great part about it is that it takes about 3 minutes. You get 1 point for every 'yes' answer. A score of 12 is perfect, 11 is tolerable, but 10 or lower and you've got serious problems. The truth is that most software organizations are running at a 2 or 3, and they need serious help, because companies like Microsoft run at 12 full-time.",
  "doc_id": "doc_1"
}


6)Test Retrieval in POST/search 
   {
  "question": "How long does it take to give the test ?"
}


7)Test AI Response in POST/ask
    {
  "question": "According to the blog post, how is the test scored and what does a score of 10 mean?"
}
