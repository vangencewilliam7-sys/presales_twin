"""
Objection Simulator — Person 4
===============================
Simulates a skeptical CTO asking tough questions about the proposed solution.

Dependencies: app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm_json


async def simulate_objections(hld_summary: str, sow_summary: str, audience: str = "CTO") -> dict:
    """
    TODO (Person 4): Implement this function.
    
    Steps:
      1. Build a system prompt: "You are a {audience} evaluating an AI solution proposal."
      2. Feed the HLD + SOW as context
      3. Ask LLM to generate 10-15 tough objections grouped by category
      4. For each objection, also generate a suggested counter-argument
    
    Expected output:
    {
        "objections": [
            { "id": "obj_1", "category": "Security", 
              "question": "How do you handle PII in the RAG pipeline?",
              "suggested_counter": "We implement field-level encryption and..." },
            ...
        ]
    }
    """
    # STUB
    return {"objections": []}
