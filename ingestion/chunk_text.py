from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_pages(pages: List[dict]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for page in pages:
        page_chunks = splitter.split_text(page["text"])
        for chunk in page_chunks:
            chunks.append({
                "page": page["page"],
                "text": chunk
            })

    return chunks