"""
Token Calculator — Person 3
============================
Pricing engine for LLM token costs and infrastructure costs.
"""

# LLM pricing per 1 million tokens (USD)
PRICING_PER_1M_TOKENS = {
    "gpt-4o":        {"input": 2.50,  "output": 10.00},
    "gpt-4o-mini":   {"input": 0.15,  "output": 0.60},
    "gpt-4.1":       {"input": 2.00,  "output": 8.00},
    "claude-sonnet": {"input": 3.00,  "output": 15.00},
    "claude-haiku":  {"input": 0.25,  "output": 1.25},
    "llama-3-70b":   {"input": 0.70,  "output": 0.80},
    "mistral-large": {"input": 2.00,  "output": 6.00},
}

INFRA_MONTHLY_COST = {
    "gpt-4o":        0,       # API-only, no infra
    "gpt-4o-mini":   0,
    "gpt-4.1":       0,
    "claude-sonnet": 0,
    "claude-haiku":  0,
    "llama-3-70b":   2520,    # ~$3.50/hr GPU x 720 hrs/month
    "mistral-large": 1800,
}


def estimate_cost(model_name: str, queries_per_day: int, avg_tokens_per_query: int) -> dict:
    """
    TODO (Person 3): Enhance this function.
    
    Current logic is basic — you should add:
      - Input vs output token split (assume 30% input, 70% output or make configurable)
      - Infrastructure costs for self-hosted models
      - Currency conversion (USD to INR)
      - Margin/buffer percentage
    """
    pricing = PRICING_PER_1M_TOKENS.get(model_name)
    if not pricing:
        return {"error": f"Unknown model: {model_name}"}

    monthly_queries = queries_per_day * 30
    monthly_tokens = monthly_queries * avg_tokens_per_query
    input_tokens = monthly_tokens * 0.3
    output_tokens = monthly_tokens * 0.7

    input_cost = (input_tokens / 1_000_000) * pricing["input"]
    output_cost = (output_tokens / 1_000_000) * pricing["output"]
    infra_cost = INFRA_MONTHLY_COST.get(model_name, 0)

    return {
        "model": model_name,
        "monthly_queries": monthly_queries,
        "monthly_tokens": monthly_tokens,
        "monthly_token_cost_usd": round(input_cost + output_cost, 2),
        "monthly_infra_cost_usd": infra_cost,
        "total_monthly_cost_usd": round(input_cost + output_cost + infra_cost, 2),
    }
