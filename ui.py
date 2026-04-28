import streamlit as st
from app.rag.rag_pipeline import index_repo, answer_question

# -----------------------------
# STREAMLIT CONFIG
# -----------------------------
st.set_page_config(page_title="GitHub RAG Assistant")

st.title("💬 GitHub RAG Assistant")

# -----------------------------
# SESSION STATE
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "repo_loaded" not in st.session_state:
    st.session_state.repo_loaded = False

# -----------------------------
# INPUTS
# -----------------------------
owner = st.text_input("GitHub Owner", "RadheyaGaikwad")
repo = st.text_input("Repository Name", "")

# -----------------------------
# LOAD REPO
# -----------------------------
if st.button("Load Repository"):

    if repo.strip() == "":
        st.error("Please enter repository name")
    else:
        with st.spinner("Indexing repository..."):
            index_repo(owner, repo)

        st.session_state.repo_loaded = True
        st.session_state.chat = []

        st.success(f"Loaded repo: {owner}/{repo}")

st.markdown("---")

# -----------------------------
# CHAT INPUT
# -----------------------------
user_input = st.text_input("Ask something about the repo...")

if st.button("Send") and user_input:

    if not st.session_state.repo_loaded:
        st.warning("Please load a repository first")
    else:
        with st.spinner("Thinking..."):
            response = answer_question(user_input)

        st.session_state.chat.append(("user", user_input))
        st.session_state.chat.append(("bot", response))

# -----------------------------
# CHAT DISPLAY
# -----------------------------
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f"🧑‍💻 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")