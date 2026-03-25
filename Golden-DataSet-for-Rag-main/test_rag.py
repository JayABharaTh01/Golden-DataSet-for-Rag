from src.retrieval.vector_store import VectorStore
from src.generation.prompt import build_prompt
from src.generation.generate import generate_answer
from src.utils.config_loader import load_config

config = load_config()
vs = VectorStore(config)

query = "Why are activation functions important?"

docs, meta = vs.search(query, config["top_k"])

context = "\n\n".join(docs)
prompt = build_prompt(query, context)

answer = generate_answer(prompt)

print("Query:", query)
print("Answer:", answer)
print("Sources:", meta)