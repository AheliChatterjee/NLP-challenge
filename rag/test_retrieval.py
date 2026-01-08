from ingestion.load_pdf import load_pdf_by_page
from ingestion.chunk_text import chunk_pages
from rag.vector_store import create_vector_store
from rag.rag_answer import format_context

def test_query(query: str):
    pages = load_pdf_by_page("data/Annual-Report-2024-25.pdf")
    chunks = chunk_pages(pages)
    collection = create_vector_store(chunks)

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    context = format_context(
        results["documents"][0],
        results["metadatas"][0]
    )

    print("---- CONTEXT SENT TO LLM ----")
    print(context)

if __name__ == "__main__":
    test_query("What are the key risks mentioned?")