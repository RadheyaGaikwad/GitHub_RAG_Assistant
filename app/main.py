from fastapi import FastAPI
from app.rag.rag_pipeline import index_repo, answer_question

# ✅ Create FastAPI app FIRST
app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "GitHub RAG running"}

# Load GitHub repo
@app.get("/load_repo")
def load_repo(owner: str, repo: str):
    try:
        index_repo(owner, repo)
        return {"message": "Repository indexed successfully"}
    except Exception as e:
        return {"error": str(e)}

# Ask question
@app.get("/ask")
def ask(q: str):
    try:
        answer = answer_question(q)
        return {"answer": answer}
    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}