from pypdf import PdfReader
from ingestion.chunk_text import chunk_pages

def load_pdf_by_page(pdf_path: str):
    reader = PdfReader(pdf_path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages.append({
                "page": i + 1,
                "text": text.strip()
            })

    return pages


if __name__ == "__main__":
    pages = load_pdf_by_page("data/Annual-Report-2024-25.pdf")
    chunks = chunk_pages(pages)

    print(f"Total chunks created: {len(chunks)}")
    print("Sample chunk:")
    print(chunks[0])
