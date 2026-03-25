from rank_bm25 import BM25Okapi

class HybridRetriever:
    def __init__(self, chunks):
        self.chunks = chunks
        tokenized = [c.split() for c in chunks]
        self.bm25 = BM25Okapi(tokenized)

    def search(self, query, k=5):
        scores = self.bm25.get_scores(query.split())
        idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self.chunks[i] for i in idx]