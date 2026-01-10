from actions.action_prompt import ACTION_SYSTEM_PROMPT
from rag.llm_client import call_llm

def generate_action(user_input: str) -> str:
    prompt = f"""
{ACTION_SYSTEM_PROMPT}

User Request:
{user_input}

JSON:
"""
    response = call_llm(prompt)
    return response
