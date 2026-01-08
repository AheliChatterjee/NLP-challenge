import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

def create_vector_store(chunks):
    client = chromadb.Client()

    collection = client.create_collection(
        name="hcltech_report"
    )

    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    texts = [c["text"] for c in chunks]
    metadatas = [{"page": c["page"]} for c in chunks]
    ids = [str(i) for i in range(len(chunks))]

    embeddings = embedder.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    return collection
