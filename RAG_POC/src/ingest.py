import os
from src.retriever import VectorStoreRetriever

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    # Simple character-based chunking
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - overlap)
    return chunks

def ingest_data(data_dir: str = "./data", store_path: str = "./vector_store"):
    print(f"Loading documents from {data_dir}...")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created {data_dir}. Please add text files to it.")
        return

    documents = []
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        if os.path.isfile(filepath) and filepath.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                chunks = chunk_text(content)
                documents.extend(chunks)

    if not documents:
        print("No .txt documents found to ingest.")
        return

    print(f"Created {len(documents)} chunks. Building vector store...")
    retriever = VectorStoreRetriever(store_path=store_path)
    
    # Reset existing memory for fresh run
    retriever.documents = []
    retriever.index = None
    
    retriever.add_documents(documents)
    retriever.save()
    print("Ingestion complete. Vector store saved.")
