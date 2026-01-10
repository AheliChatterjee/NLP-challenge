from rag.rag_pipeline import answer_question

if __name__ == "__main__":
    question = "What are the key risks mentioned in the report?"
    answer = answer_question(question)
    print(answer)
