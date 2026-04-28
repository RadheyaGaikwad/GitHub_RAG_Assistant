import faiss
import numpy as np

# -----------------------------
# GLOBAL STORAGE
# -----------------------------
dimension = 384
index = faiss.IndexFlatL2(dimension)
stored_chunks = []

# -----------------------------
# RESET VECTOR DB (IMPORTANT)
# -----------------------------
def reset_index():
    global index, stored_chunks
    index = faiss.IndexFlatL2(dimension)
    stored_chunks = []

# -----------------------------
# ADD DATA
# -----------------------------
def add_chunks(chunks, embeddings):
    global index, stored_chunks

    embeddings = np.array(embeddings).astype("float32")

    index.add(embeddings)
    stored_chunks.extend(chunks)

# -----------------------------
# SEARCH
# -----------------------------
def search(query_embedding, k=3):
    global index, stored_chunks

    query_embedding = np.array(query_embedding).astype("float32").reshape(1, -1)

    if index.ntotal == 0:
        return []

    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        if 0 <= idx < len(stored_chunks):
            results.append(stored_chunks[idx])

    return results