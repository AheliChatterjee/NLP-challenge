def format_context(docs, metadatas):
    context = ""
    for doc, meta in zip(docs, metadatas):
        context += f"[Page {meta['page']}]\n{doc}\n\n"
    return context
