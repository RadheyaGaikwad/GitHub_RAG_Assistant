from app.github.loader import get_repo_files
from app.rag.chunking import chunk_text
from app.rag.embedding import create_embedding
from app.rag.vector_store import add_chunks, search, reset_index
from app.llm.llm import ask_llm

# -----------------------------
# INDEX REPO (IMPORTANT FIX)
# -----------------------------
def index_repo(owner, repo):

    # 🔥 RESET OLD REPO DATA
    reset_index()

    files = get_repo_files(owner, repo)

    all_chunks = []

    for file in files:
        chunks = chunk_text(file["content"])
        all_chunks.extend(chunks)

    embeddings = [create_embedding(chunk) for chunk in all_chunks]

    add_chunks(all_chunks, embeddings)

# -----------------------------
# ASK QUESTION
# -----------------------------
def answer_question(query):

    query_embedding = create_embedding(query)
    docs = search(query_embedding)

    if not docs:
        return "No relevant data found in repository"

    context = "\n".join(docs)

    prompt = f"""
You are a senior software engineer.

Explain the GitHub repository based on the context.

Context:
{context}

Question:
{query}

Give a clear structured answer.
"""

    return ask_llm(prompt)