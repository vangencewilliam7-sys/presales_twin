"""
HLD Agent — Person 2
====================
Generates a High-Level Design architecture diagram in Mermaid.js format.

Dependencies: app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm


async def generate_hld(requirements: list[str], constraints: list[str] = []) -> dict:
    """
    TODO (Person 2): Implement this function.
    
    Steps:
      1. Build a prompt with the requirements + constraints
      2. Ask LLM to generate:
         - A Mermaid.js flowchart/graph showing the architecture
         - A written summary of each component
         - A list of components with descriptions
      3. Validate the Mermaid syntax (basic check)
    
    Expected output:
    {
        "mermaid_code": "graph TD\\n    A[API Gateway] --> B[RAG Engine]\\n    ...",
        "summary": "The proposed architecture consists of...",
        "components": [
            { "name": "API Gateway", "description": "Handles incoming requests..." },
            { "name": "RAG Engine", "description": "Retrieves relevant context..." }
        ]
    }
    """
    # STUB
    return {
        "mermaid_code": "graph TD\n    A[Stub] --> B[Not Implemented]",
        "summary": "Stub: HLD generation not yet implemented",
        "components": [],
    }
