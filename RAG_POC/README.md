# Simple Modular RAG Agent

This project provides a lightweight, modular Retrieval-Augmented Generation (RAG) agent that runs entirely locally. It uses `llama-cpp-python` for generating responses with local LLMs, `sentence-transformers` for creating document embeddings, and `faiss-cpu` for fast vector similarity search.

## Features

- **Local Execution:** Runs entirely on your local machine using GGUF models.
- **Modular Design:** Core components (`llm`, `retriever`, `agent`, `ingest`) are logically separated in the `src/` directory.
- **Easy Document Ingestion:** Automatically chunk and index text documents placed in the `data/` directory.

## Project Structure

- `data/`: Place your text documents (e.g., `.txt` files) here. They will be processed, chunked, and embedded during the ingestion phase.
- `models/`: Directory to store your local LLM models (in `.gguf` format).
- `vector_store/`: This directory is populated with the FAISS index and chunk metadata after running the ingestion step.
- `src/`: Contains the core Python modules:
  - `agent.py`: Orchestrates the retrieval and generation process.
  - `ingest.py`: Handles reading, chunking, and indexing of text files.
  - `llm.py`: A wrapper for the local LLM using `llama-cpp-python`.
  - `retriever.py`: Manages the vector store and retrieval logic using FAISS and `sentence-transformers`.
- `main.py`: The main entry point. Provides a CLI to run the ingestion pipeline or start the interactive chatbot.
- `requirements.txt`: Project dependencies.

## Setup Instructions

1. **Install Dependencies:**
   It's recommended to use a virtual environment. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download a Local Model:**
   - Create a `models/` directory in the root of the project.
   - Download the specific model file `qwen2.5-0.5b-instruct-q4_k_m.gguf` (e.g., from Hugging Face). 
   - Place the downloaded `.gguf` file inside the newly created `models/` directory.
   - **Note:** By default, `main.py` is configured to look for this exact model. If you use a different model, make sure to update the `model_path` variable in `main.py`.

## Usage

### 1. Ingest Data
Before you can query your documents, you need to build the vector index. Place your text files into the `data/` folder, and then run:
```bash
python main.py --ingest
```
This will read the documents, create embeddings, and save the FAISS index in the `vector_store/` directory.

### 2. Run the Agent
To start chatting with your data, run the main script without any arguments:
```bash
python main.py
```
This will load the vector store and your local LLM, and provide an interactive chat prompt.

Type `exit` or `quit` to stop the application.

