from openai import OpenAI
from src.utils.config_loader import load_config

config = load_config()

client = OpenAI(
    api_key=config["llm"]["api_key"],
    base_url=config["llm"]["base_url"],
    default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "RAG Project"
    }
)

def generate_answer(prompt):
    res = client.chat.completions.create(
        model=config["llm"]["model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return res.choices[0].message.content