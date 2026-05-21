"""
Ask My Resume — a RAG chatbot grounded in Abhinav Pabba's resume.

Free stack:
  - LLM:        Groq (Llama 3.3 70B) — free API, blazing fast
  - Embeddings: fastembed (BAAI/bge-small-en-v1.5) — runs locally, no API
  - Vector DB:  FAISS — local, in-memory
  - UI:         Streamlit

How it works (3 steps):
  1. ONE-TIME: read resume.md, chunk it, embed each chunk locally with fastembed,
     store the vectors in a FAISS index.
  2. PER QUESTION: embed the question, find the top-K most similar chunks in FAISS.
  3. Send Groq's Llama a prompt with the retrieved chunks and ask it to answer
     using ONLY those excerpts.
"""

import os
from pathlib import Path

import faiss
import numpy as np
import streamlit as st
from dotenv import load_dotenv
from fastembed import TextEmbedding
from groq import Groq

# Load API key from .env
load_dotenv()

# ------------------------------------------------------------------
# Config
# ------------------------------------------------------------------
RESUME_PATH = "resume.md"
CHAT_MODEL = "llama-3.3-70b-versatile"          # Groq's flagship general model
EMBED_MODEL_NAME = "BAAI/bge-small-en-v1.5"     # 384-dim, fast on CPU
CHUNK_SIZE = 250                                 # words per chunk
CHUNK_OVERLAP = 50                               # words shared between chunks
TOP_K = 4                                        # retrieved chunks per question

# Initialize clients
groq_client = Groq()


# ------------------------------------------------------------------
# 1. Chunk the resume
# ------------------------------------------------------------------
def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping word-windowed chunks.

    Overlap matters: a fact at a chunk boundary would otherwise be split between
    two chunks and lose context. Overlap means each fact appears whole in at
    least one chunk.
    """
    words = text.split()
    step = chunk_size - overlap
    chunks = []
    for i in range(0, len(words), step):
        chunk = " ".join(words[i : i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks


# ------------------------------------------------------------------
# 2. Build the FAISS index (runs once, cached by Streamlit)
# ------------------------------------------------------------------
@st.cache_resource(show_spinner="Loading embedding model + indexing resume (first run downloads ~150MB)...")
def build_index() -> tuple[faiss.Index, list[str], TextEmbedding]:
    """Read resume, chunk it, embed every chunk locally, store in FAISS."""
    text = Path(RESUME_PATH).read_text(encoding="utf-8")
    chunks = chunk_text(text)

    # fastembed downloads the ONNX model on first run, then runs locally on CPU
    embedder = TextEmbedding(model_name=EMBED_MODEL_NAME)

    # Embed all chunks (fastembed yields generators; we materialize to a list)
    embeddings = np.array(list(embedder.embed(chunks)), dtype="float32")

    # Normalize + inner product == cosine similarity (faster than IndexFlatL2 here)
    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    return index, chunks, embedder


# ------------------------------------------------------------------
# 3. Retrieve top-K chunks for a question
# ------------------------------------------------------------------
def retrieve(query: str, index: faiss.Index, chunks: list[str], embedder: TextEmbedding, k: int = TOP_K) -> list[str]:
    """Embed the query and return the K most similar resume chunks."""
    q_vec = np.array(list(embedder.embed([query])), dtype="float32")
    faiss.normalize_L2(q_vec)
    _scores, indices = index.search(q_vec, k)
    return [chunks[i] for i in indices[0]]


# ------------------------------------------------------------------
# 4. Ask the LLM, grounded in retrieved chunks
# ------------------------------------------------------------------
def answer(query: str, contexts: list[str]) -> str:
    """Build a grounded prompt and call Groq's Llama 3.3."""
    context_block = "\n\n---\n\n".join(
        f"[Excerpt {i + 1}]\n{c}" for i, c in enumerate(contexts)
    )

    system_prompt = (
        "You are answering questions about Abhinav Pabba's professional background "
        "for recruiters and hiring managers. Use ONLY the resume excerpts provided. "
        "If the answer isn't in the excerpts, say so honestly — do not invent details. "
        "Be concise, specific, and factual. Cite the excerpt number when helpful."
    )

    user_prompt = f"RESUME EXCERPTS:\n{context_block}\n\nQUESTION: {query}\n\nANSWER:"

    response = groq_client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=1024,
        temperature=0.2,
    )
    return response.choices[0].message.content


# ------------------------------------------------------------------
# 5. Streamlit UI
# ------------------------------------------------------------------
st.set_page_config(page_title="Ask My Resume", page_icon="💼")
st.title("Ask My Resume")
st.caption(
    "RAG chatbot grounded in Abhinav Pabba's resume — built with Groq (Llama 3.3 70B), "
    "fastembed (local), and FAISS."
)

# Build (or fetch cached) index
index, chunks, embedder = build_index()

with st.sidebar:
    st.subheader("Try asking")
    st.markdown(
        "- What's his experience with LangGraph?\n"
        "- Tell me about his Citi project.\n"
        "- What healthcare AI work has he done?\n"
        "- Does he know AWS?\n"
        "- How many years of experience does he have?"
    )
    st.markdown("---")
    st.caption(f"{len(chunks)} resume chunks indexed.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if query := st.chat_input("Ask anything about Abhinav's background..."):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Searching resume and calling Llama 3.3 via Groq..."):
            contexts = retrieve(query, index, chunks, embedder)
            response = answer(query, contexts)
            st.write(response)
            with st.expander("Sources used (top retrieved chunks)"):
                for i, c in enumerate(contexts, 1):
                    st.text_area(
                        f"Excerpt {i}",
                        c,
                        height=120,
                        key=f"src_{len(st.session_state.messages)}_{i}",
                    )

    st.session_state.messages.append({"role": "assistant", "content": response})
