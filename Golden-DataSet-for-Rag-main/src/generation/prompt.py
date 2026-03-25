def build_prompt(query, context):
    return f"""
Answer using ONLY the context.
If not found, say "I don't know".

Context:
{context}

Question:
{query}
"""