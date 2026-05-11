"""
Schema Agent — Person 2
=======================
Analyzes uploaded data schemas (CSV/JSON/SQL) for quality issues.

Dependencies: pandas, app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm_json


async def analyze_schema(file_content: str, file_type: str) -> dict:
    """
    TODO (Person 2): Implement this function.
    
    Steps:
      1. Parse the file (CSV → pandas, JSON → dict, SQL → text)
      2. Send to LLM asking to identify:
         - Missing fields, nullable issues
         - Data type mismatches
         - Normalization problems
         - Potential latency bottlenecks
      3. Return list of issues with severity
    
    Expected output:
    {
        "issues": [
            { "field": "user_id", "severity": "high", "message": "No index on frequently queried column" },
            { "field": "timestamp", "severity": "medium", "message": "Stored as string, should be TIMESTAMP" }
        ],
        "overall_quality": "moderate"
    }
    """
    # STUB
    return {"issues": [], "overall_quality": "stub"}
