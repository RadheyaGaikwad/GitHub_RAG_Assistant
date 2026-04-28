GitHub RAG Assistant

Overview
GitHub RAG Assistant is an AI-powered system that enables users to interact with any GitHub repository using natural language queries. It leverages Retrieval-Augmented Generation (RAG) to analyze codebases and generate context-aware responses.

Problem Statement
Understanding large or unfamiliar code repositories is time-consuming. Developers often spend significant effort navigating files and interpreting code structure.

Solution
This project addresses the problem by combining semantic search with large language models. It retrieves relevant code snippets from a repository and generates accurate explanations based on user queries.

System Architecture
User Query → Streamlit Interface → RAG Pipeline → GitHub API → Code Retrieval → Text Chunking → Embedding Generation → FAISS Vector Store → Similarity Search → LLM (Groq) → Response Generation

Tech Stack
Backend: Python
Frontend: Streamlit
LLM: Groq API (Llama 3.1-8B-Instant)
Embeddings: Sentence Transformers (all-MiniLM-L6-v2)
Vector Database: FAISS
API Integration: GitHub REST API

Features

* Natural language interaction with GitHub repositories
* Automated repository indexing
* Context-aware code understanding
* Fast semantic search using FAISS
* Supports multiple repositories with dynamic indexing

Input

* GitHub Owner (e.g., RadheyaGaikwad)
* Repository Name (e.g., Fire-Detection-Project)
* User Query (e.g., “Provide a summary of this project”)

Output

* Project summaries
* Code explanations
* Functional insights
* Context-based answers derived from repository content

Workflow

1. The user provides repository details.
2. The system fetches repository files using the GitHub API.
3. Files are split into smaller chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are stored in a FAISS vector database.
6. User query is converted into an embedding.
7. Relevant chunks are retrieved using similarity search.
8. Retrieved context is passed to the LLM.
9. The LLM generates a structured response.

Setup Instructions

1. Clone the repository
   git clone https://github.com/RadheyaGaikwad/GitHub_RAG_Assistant.git
   cd GitHub_RAG_Assistant

2. Install dependencies
   pip install -r requirements.txt

3. Configure environment variables
   Create a .env file and add:
   GROQ_API_KEY=your_api_key_here

4. Run the application
   streamlit run app/ui.py

Key Learnings

* Implementation of Retrieval-Augmented Generation (RAG)
* Integration of LLMs with external data sources
* Semantic search using vector databases
* End-to-end AI application development

Future Enhancements

* File-level code explanation
* Improved UI with repository navigation
* Deployment for public access
* Streaming responses for better UX

Author
Radheya Gaikwad
Artificial Intelligence and Data Science Engineering Student

This project demonstrates practical implementation of modern AI systems combining retrieval mechanisms with language models to solve real-world developer challenges.
