from rag.llm_client import call_llm

if __name__ == "__main__":
    reply = call_llm("Answer in one sentence: What is an enterprise assistant?")
    print(reply)
