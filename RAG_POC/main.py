import sys
import argparse
from src.llm import LocalLLM
from src.retriever import VectorStoreRetriever
from src.agent import RAGAgent
from src.ingest import ingest_data

def main():
    parser = argparse.ArgumentParser(description="Simple Modular RAG Agent")
    parser.add_argument("--ingest", action="store_true", help="Ingest documents from the data folder before running")
    args = parser.parse_args()

    if args.ingest:
        ingest_data(data_dir="./data", store_path="./vector_store")

    print("Initializing LLM API and Vector Store...")
    try:
        # The model_path should match the one you are actually using in the models directory
        llm = LocalLLM(model_path="./models/qwen2.5-0.5b-instruct-q4_k_m.gguf")
        retriever = VectorStoreRetriever(store_path="./vector_store")
        agent = RAGAgent(llm=llm, retriever=retriever)
    except Exception as e:
        print(f"Error initializing components: {e}")
        print("Make sure you have your model in ./models and have ingested data.")
        sys.exit(1)

    print("\nRAG Agent ready! Type 'exit' or 'quit' to stop.")
    while True:
        try:
            query = input("\nUser: ")
            if query.lower() in ["exit", "quit"]:
                break
            if not query.strip():
                continue
                
            print("Agent: Thinking...")
            response = agent.ask(query)
            print(f"\nAgent: {response}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()