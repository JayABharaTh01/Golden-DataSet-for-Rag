# Golden-DataSet-for-Rag

This project implements a Retrieval-Augmented Generation (RAG) system designed to answer questions based on YouTube video transcripts and a curated golden dataset. The system leverages vector embeddings for efficient retrieval and a large language model (LLM) for generating contextually relevant answers.

## Overview

The RAG system combines the strengths of retrieval-based methods and generative models:
- **Retrieval**: Searches a vector database of document chunks to find relevant context.
- **Generation**: Uses an LLM to synthesize answers based on the retrieved context.

This approach ensures answers are grounded in the provided data, reducing hallucinations and improving accuracy.

## Project Structure

```
├── config/
│   └── settings.yaml          # Configuration file for models, API keys, and parameters
├── data/
│   └── transcripts/           # Directory containing YouTube transcript text files
├── src/
│   ├── ingestion/             # (Commented out) Code for fetching YouTube transcripts
│   ├── processing/            # Text chunking utilities
│   ├── retrieval/             # Vector store and retrieval logic
│   ├── generation/            # Prompt building and answer generation
│   ├── evaluation/            # (Empty) Placeholder for evaluation scripts
│   └── utils/                 # Configuration loading utilities
├── vector_store/              # Directory for FAISS index (if used)
├── app/
│   └── streamlit_app.py       # Web interface for querying the system
├── golden_dataset.json        # Curated Q&A pairs for testing and evaluation
├── run_pipeline.py            # Script to ingest data and populate the vector store
├── test_rag.py                # Test script for querying the RAG system
├── requirement.txt            # Python dependencies
└── README.md                  # This file
```

## Workflow

### 1. Data Ingestion
- **Transcripts**: The system processes pre-downloaded YouTube video transcripts stored in `data/transcripts/`. Each transcript is a text file (e.g., `aircAruvnKk.txt`).
- **Golden Dataset**: A JSON file (`golden_dataset.json`) containing question-answer pairs. This serves as ground truth for evaluation and is ingested into the vector store for retrieval.
- **Pipeline Execution**: Run `python run_pipeline.py` to:
  - Load and chunk transcript texts.
  - Load answers from the golden dataset.
  - Generate embeddings using SentenceTransformers.
  - Store chunks and embeddings in a persistent ChromaDB vector store.

### 2. Data Processing
- **Chunking**: Text is split into overlapping chunks (default: 300 words with 50-word overlap) to fit within embedding model limits and improve retrieval granularity.
- **Embedding**: Each chunk is converted to a vector representation using the `all-MiniLM-L6-v2` model.

### 3. Retrieval
- **Vector Store**: Uses ChromaDB for storing and querying embeddings.
- **Search**: For a user query, the system:
  - Embeds the query.
  - Retrieves the top-k most similar chunks (default: 5).
  - Optionally reranks results (reranker code is commented out).
- **Metadata**: Each chunk includes metadata like source file or question for traceability.

### 4. Generation
- **Prompt Building**: Constructs a prompt with retrieved context and the query, instructing the LLM to answer only using the context or say "I don't know" if not found.
- **LLM Integration**: Uses OpenRouter API with GPT-4o-mini model for answer generation.
- **Output**: Returns the generated answer along with source metadata.

### 5. User Interface
- **Streamlit App**: A simple web app (`app/streamlit_app.py`) for interactive querying.
- Run with `streamlit run app/streamlit_app.py`.

### 6. Evaluation
- The golden dataset can be used to evaluate system performance by comparing generated answers to expected answers.
- (Evaluation code is not implemented yet.)

## Setup Instructions

### Prerequisites
- Python 3.8+
- Internet connection for downloading models and API access

### Installation
1. Clone or download the repository.
2. Install dependencies:
   ```
   pip install -r requirement.txt
   ```
3. Configure API keys in `config/settings.yaml`:
   - `llm.api_key`: Your OpenRouter API key.
   - Other settings like model names and parameters.

### Running the System
1. **Populate the Vector Store**:
   ```
   python run_pipeline.py
   ```
   This may take time on first run due to model downloads.

2. **Test the System**:
   ```
   python test_rag.py
   ```
   This queries with a sample question and prints the answer.

3. **Launch the Web App**:
   ```
   streamlit run app/streamlit_app.py
   ```
   Open the provided URL in a browser to ask questions interactively.

## Configuration

Key settings in `config/settings.yaml`:
- `llm`: API provider, key, base URL, model.
- `embedding_model`: SentenceTransformer model (e.g., "all-MiniLM-L6-v2").
- `chunk_size`, `chunk_overlap`: Text chunking parameters.
- `top_k`: Number of chunks to retrieve.
- `collection_name`: ChromaDB collection name.

## Example Usage

Query: "Why are activation functions important?"

Expected Output:
- Answer: "They introduce non-linearity."
- Sources: Metadata from retrieved chunks (e.g., golden_dataset).

If no relevant context is found, the system responds: "I don't know."

## Future Improvements
- Implement reranking for better retrieval.
- Add evaluation metrics using the golden dataset.
- Support for dynamic transcript fetching.
- Expand to other data sources.

## Dependencies
- streamlit: Web app framework.
- openai: LLM API client.
- chromadb: Vector database.
- sentence-transformers: Embedding model.
- youtube-transcript-api: For transcript fetching (commented out).
- rank-bm25: For potential reranking.
- numpy, pyyaml: Utilities.

## License
[Add license if applicable]