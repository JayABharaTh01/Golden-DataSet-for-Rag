from openai import OpenAI

client = OpenAI(
    api_key="your_openrouter_api_key",
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.choices[0].message.content)