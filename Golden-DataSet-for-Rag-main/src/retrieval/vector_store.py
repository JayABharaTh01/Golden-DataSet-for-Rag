import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, config):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection(
            name=config["collection_name"]
        )
        self.model = SentenceTransformer(config["embedding_model"])

    # def add(self, docs, metadata):
    #     embeddings = self.model.encode(docs).tolist()

    #     self.collection.add(
    #         documents=docs,
    #         embeddings=embeddings,
    #         metadatas=metadata,
    #         ids=[str(i) for i in range(len(docs))]
    #     )
    def add(self, docs, metadata):
        embeddings = self.model.encode(docs).tolist()

        self.collection.add(
            documents=docs,
            embeddings=embeddings,
            metadatas=metadata,   # ✅ THIS IS REQUIRED
            ids=[str(i) for i in range(len(docs))]
        )

    # def search(self, query, k):
    #     q_emb = self.model.encode([query]).tolist()

    #     res = self.collection.query(
    #         query_embeddings=q_emb,
    #         n_results=k
    #     )

    #     return res["documents"][0], res["metadatas"][0]
    
    def search(self, query, k):
        q_emb = self.model.encode([query]).tolist()

        res = self.collection.query(
            query_embeddings=q_emb,
            n_results=k
        )

        docs = res.get("documents", [[]])[0]

        # 🔥 SAFE handling
        if "metadatas" in res and res["metadatas"]:
            meta = res["metadatas"][0]
        else:
            meta = [{"source": "unknown"} for _ in docs]

        return docs, meta