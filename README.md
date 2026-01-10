# Agentic Enterprise Assistant

A reliability-first AI assistant that combines Retrieval-Augmented Generation (RAG) with lightweight agentic routing to answer enterprise document queries with page-level citations and generate structured JSON outputs for workflow automation commands.

---

## Key Features

* Citation-grounded document question answering
* Hallucination guardrails for safe responses
* Intent-based routing between information and action modes
* Deterministic JSON outputs for enterprise workflows
* Simple Streamlit-based user interface

---

## Tech Stack

* **IDE:** GitHub Codespaces
* **UI:** Streamlit
* **PDF Parsing:** PyPDF
* **Chunking:** LangChain Text Splitters
* **Embeddings:** sentence-transformers/all-MiniLM-L6-v2
* **Vector Database:** ChromaDB
* **LLM:** Hugging Face Inference API (Mistral-7B-Instruct)
* **Agent Logic:** Custom Python routing

---

## Project Structure

```
agentic-enterprise-assistant/
├── app.py                 # Streamlit UI
├── requirements.txt       # Dependencies
├── data/                  # PDF documents
├── ingestion/             # PDF loading and chunking
├── rag/                   # Vector store and RAG pipeline
├── agent/                 # Intent router and controller
├── actions/               # Action prompts and handlers
└── README.md              # Project summary
```

---

## Setup

1. Open the repository in **GitHub Codespaces**
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add Hugging Face token as Codespaces secret:

```
HF_TOKEN=<your_token>
```

4. Run the application:

```
streamlit run app.py
```

---

## How It Works

1. User enters a query in the Streamlit interface
2. Intent router classifies query:

   * Informational → RAG pipeline
   * Action → JSON action generator
3. RAG retrieves relevant document chunks from ChromaDB
4. LLM generates citation-grounded response
5. Action requests return structured JSON

---

## Demo Queries

### Document Queries

* What are the key risks mentioned in the report?
* What initiatives are mentioned for digital transformation?

### Action Commands

* Schedule a meeting with HR tomorrow at 3 PM
* Create an IT ticket for laptop not turning on, high priority

### Hallucination Guardrail

* Who is the CEO of Google?

---

## Output Examples

### Citation-Grounded Answer

"The report identifies key risks including global economic uncertainty and market volatility, discussed on Pages 45 and 46."

### Action JSON

```
{
  "action": "create_it_ticket",
  "issue": "Laptop not turning on",
  "priority": "High"
}
```

---

## Conclusion

The Agentic Enterprise Assistant demonstrates an enterprise-ready AI system that ensures accuracy, transparency, and deterministic automation through RAG and agentic control.
