GitHub RAG Assistant

---

**Overview**

GitHub RAG Assistant is an AI-powered system that enables natural language interaction with any GitHub repository. It uses Retrieval-Augmented Generation (RAG) to analyze codebases and generate context-aware responses.

---

**Key Highlights**

* Enables querying entire repositories using natural language
* Combines semantic search with large language models
* Provides context-aware explanations instead of generic answers
* Designed with modular and scalable architecture
* Implements industry-relevant RAG pipeline

---

**Problem Statement**

Understanding large or unfamiliar codebases is time-consuming and inefficient. Developers often need to manually navigate multiple files to understand functionality.

---

**Solution**

This system retrieves relevant portions of a repository and uses a language model to generate accurate, context-driven explanations. It reduces the effort required to understand complex projects.

---

**System Architecture**

User Query
→ Streamlit Interface
→ RAG Pipeline
→ GitHub API (Fetch Files)
→ Text Chunking
→ Embedding Generation
→ FAISS Vector Store
→ Similarity Search
→ LLM (Groq - Llama 3.1)
→ Response Generation

---

**Tech Stack**

Backend
Python

Frontend
Streamlit

AI / ML
Groq API (Llama 3.1-8B-Instant)
Sentence Transformers (all-MiniLM-L6-v2)

Vector Database
FAISS

Integration
GitHub REST API

---

**Core Features**

* Repository indexing and semantic search
* Context-aware code understanding
* Query-based summarization
* Multi-repository support with dynamic indexing
* Efficient retrieval using vector similarity

---

**Input**

* GitHub Owner (e.g., RadheyaGaikwad)
* Repository Name (e.g., Fire-Detection-Project)
* User Query (e.g., "Provide a summary of this project")

---

**Output**

* Structured project summaries
* Code explanations
* Functional insights
* Context-driven answers derived from repository data

---

**Workflow**

1. User provides repository details
2. System fetches repository files
3. Files are divided into manageable chunks
4. Each chunk is converted into vector embeddings
5. Embeddings are stored in FAISS
6. Query is converted into embedding
7. Relevant chunks are retrieved
8. LLM generates final response

---

**Setup Instructions**

Clone repository
git clone https://github.com/RadheyaGaikwad/GitHub_RAG_Assistant.git
cd GitHub_RAG_Assistant

Install dependencies
pip install -r requirements.txt

Configure environment
Create a .env file and add:
GROQ_API_KEY=your_api_key_here

Run application
streamlit run app/ui.py

---

**Key Learnings**

* Practical implementation of RAG architecture
* Integration of LLMs with external data sources
* Semantic search using vector databases
* End-to-end AI application development

---

**Future Improvements**

* File-level explanation
* Enhanced UI with repository navigation
* Cloud deployment
* Streaming responses

---

**Author**

Radheya Gaikwad
Artificial Intelligence and Data Science Engineering

---

This project demonstrates a practical approach to combining retrieval systems with large language models to solve real-world software engineering challenges.
