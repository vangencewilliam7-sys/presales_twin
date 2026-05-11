"""
Briefing Agent — Person 1
=========================
Generates a pre-meeting briefing note with pain points and probing questions.

Dependencies: app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm


async def generate_briefing(company_name: str, recon_data: dict) -> dict:
    """
    TODO (Person 1): Implement this function.

    Steps:
      1. Take the recon_data from recon_agent
      2. Build a prompt asking the LLM to generate:
         - 2-3 sentence company overview
         - Industry-specific pain points (bullet list)
         - 5-10 probing questions for the discovery call
      3. Return as structured data

    Expected output:
    {
        "briefing_markdown": "## Company Overview\n...",
        "probing_questions": [
            "What is your current data pipeline latency?",
            "Have you explored RAG-based approaches before?"
        ]
    }
    """
    # STUB
    return {
        "briefing_markdown": f"# Briefing: {company_name}\n\nStub: not yet implemented.",
        "probing_questions": ["Stub question 1", "Stub question 2"],
    }
