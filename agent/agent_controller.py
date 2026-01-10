from agent.intent_router import is_action_request
from rag.rag_pipeline import answer_question
from actions.action_handler import generate_action

def handle_user_input(user_input: str) -> str:
    if is_action_request(user_input):
        return generate_action(user_input)
    else:
        return answer_question(user_input)
