import streamlit as st
from src.retrieval.vector_store import VectorStore
#from src.retrieval.reranker import reranker
from src.generation.prompt import build_prompt
from src.generation.generate import generate_answer
from src.utils.config_loader import load_config

config = load_config()
vs = VectorStore(config)
#reranker = Reranker()

st.title("🚀 YouTube RAG System")

query = st.text_input("Ask question:")

if query:
    docs, meta = vs.search(query, config["top_k"])
#    docs = reranker.rerank(query, docs, config["rerank_top_n"])

    context = "\n\n".join(docs)
    prompt = build_prompt(query, context)

    answer = generate_answer(prompt)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for m in meta:
        st.write(m)