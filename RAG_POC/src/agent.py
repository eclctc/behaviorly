from src.llm import LocalLLM
from src.retriever import VectorStoreRetriever

class RAGAgent:
    def __init__(self, llm: LocalLLM, retriever: VectorStoreRetriever):
        self.llm = llm
        self.retriever = retriever

    def ask(self, question: str) -> str:
        # 1. Retrieve relevant context
        context_chunks = self.retriever.search(question, top_k=3)
        context_str = "\n---\n".join(context_chunks)

        if not context_chunks:
            context_str = "No relevant context found."

        # 2. Format the prompt
        prompt = f"""You are a helpful assistant. Use the following context to answer the user's question. If the answer is not in the context, say you don't know based on the provided documents.

Context:
{context_str}

Question:
{question}

Answer:
"""
        # 3. Generate response
        response = self.llm.generate(prompt=prompt)
        return response
