"""
Shared LLM Wrapper — ALL modules use this to call the LLM.
DO NOT write your own OpenAI calls. Import and use these functions.

Usage:
    from app.utils.llm_wrapper import call_llm, call_llm_json

    result = call_llm("You are a helpful assistant", "Summarize this text...")
    data = call_llm_json("You are a JSON generator", "Generate a list of...")
"""

import json
import openai
from app.config import settings

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)


def call_llm(
    system_prompt: str,
    user_prompt: str,
    model: str | None = None,
    temperature: float = 0.7,
    max_tokens: int = 4096,
) -> str:
    """Call the LLM and return the text response."""
    response = client.chat.completions.create(
        model=model or settings.DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def call_llm_json(
    system_prompt: str,
    user_prompt: str,
    model: str | None = None,
) -> dict:
    """Call the LLM and parse the response as JSON."""
    response_text = call_llm(
        system_prompt=system_prompt + "\n\nRespond ONLY with valid JSON. No markdown, no explanation.",
        user_prompt=user_prompt,
        model=model,
        temperature=0.3,
    )
    # Strip markdown code fences if present
    cleaned = response_text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1]
    if cleaned.endswith("```"):
        cleaned = cleaned.rsplit("```", 1)[0]
    return json.loads(cleaned.strip())


def get_embedding(text: str, model: str = "text-embedding-3-small") -> list[float]:
    """
    Generate an embedding vector for the given text.
    These embeddings are stored in Supabase (pgvector) for RAG / similarity search.
    """
    response = client.embeddings.create(model=model, input=text)
    return response.data[0].embedding
