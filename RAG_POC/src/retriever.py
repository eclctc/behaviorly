import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from typing import List

class VectorStoreRetriever:
    def __init__(self, store_path: str = "./vector_store", embedding_model: str = "all-MiniLM-L6-v2"):
        self.store_path = store_path
        self.index_path = os.path.join(store_path, "index.faiss")
        self.docs_path = os.path.join(store_path, "documents.pkl")
        self.embedding_model = SentenceTransformer(embedding_model)
        
        self.index = None
        self.documents = []
        
        if os.path.exists(self.index_path) and os.path.exists(self.docs_path):
            self.load()

    def add_documents(self, documents: List[str]):
        if not documents:
            return
            
        embeddings = self.embedding_model.encode(documents, convert_to_numpy=True)
        dimension = embeddings.shape[1]
        
        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)
            
        self.index.add(embeddings) # type: ignore
        self.documents.extend(documents)

    def search(self, query: str, top_k: int = 3) -> List[str]:
        if self.index is None or not self.documents:
            return []
            
        query_embedding = self.embedding_model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for idx in indices[0]:
            if idx != -1 and idx < len(self.documents):
                results.append(self.documents[idx])
        return results

    def save(self):
        os.makedirs(self.store_path, exist_ok=True)
        if self.index is not None:
            faiss.write_index(self.index, self.index_path)
        with open(self.docs_path, "wb") as f:
            pickle.dump(self.documents, f)

    def load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.docs_path, "rb") as f:
            self.documents = pickle.load(f)
