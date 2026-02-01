def generate_response(query, context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
Answer the question strictly using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt
