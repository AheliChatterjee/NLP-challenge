ACTION_KEYWORDS = [
    "schedule",
    "create",
    "raise",
    "book",
    "assign",
    "generate ticket",
    "open ticket"
]

def is_action_request(user_input: str) -> bool:
    text = user_input.lower()
    return any(keyword in text for keyword in ACTION_KEYWORDS)
