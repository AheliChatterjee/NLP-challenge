from huggingface_hub import InferenceClient
import os

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.2
    )

    return response.choices[0].message.content
