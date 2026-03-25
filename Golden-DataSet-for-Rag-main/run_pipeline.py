import os
import json
from src.processing.chunk import chunk_text
from src.retrieval.vector_store import VectorStore
from src.utils.config_loader import load_config
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

config = load_config()
vs = VectorStore(config)

all_chunks = []
meta = []

# Ingest transcripts
for file in os.listdir("data/transcripts"):
    with open(f"data/transcripts/{file}", encoding="utf-8") as f:
        text = f.read()
        chunks = chunk_text(text)

        for c in chunks:
            all_chunks.append(c)
            meta.append({"source": file})

# Ingest golden dataset
with open("golden_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    for item in data:
        all_chunks.append(item["answer"])
        meta.append({"question": item["question"], "source": "golden_dataset"})

vs.add(all_chunks, meta)

print("✅ Embedding + Storage Done")