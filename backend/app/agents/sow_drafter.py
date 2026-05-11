"""
SOW Drafter — Person 3
======================
Generates the Technical Scope section of the Statement of Work.

Dependencies: app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm


async def draft_sow(requirements: list[str], hld_summary: str, cost_estimate: dict, sprint_plan: dict) -> dict:
    """
    TODO (Person 3): Implement this function.
    
    Steps:
      1. Combine all inputs into a comprehensive prompt
      2. Ask LLM to generate a Technical SOW section including:
         - In-scope features with acceptance criteria
         - Out-of-scope items
         - HITL checkpoints
         - Assumptions & dependencies
         - Delivery milestones
      3. Return as markdown
    
    Expected output:
    {
        "sow_markdown": "# Technical Statement of Work\\n\\n## 1. Scope\\n...",
        "version": 1
    }
    """
    # STUB
    return {"sow_markdown": "# SOW\\n\\nStub: not yet implemented", "version": 1}
