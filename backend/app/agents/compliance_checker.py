"""
Compliance Checker — Person 4
==============================
Scans proposed architecture against compliance frameworks (SOC2, HIPAA, GDPR, etc.)

Dependencies: supabase-py, app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm_json, get_embedding
from app.config import settings
from supabase import create_client

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

SUPPORTED_FRAMEWORKS = ["SOC2", "HIPAA", "GDPR", "PCI-DSS", "ISO27001"]


async def check_compliance(architecture_summary: str, framework: str) -> dict:
    """
    TODO (Person 4): Implement this function.
    
    Steps:
      1. Validate framework is supported
      2. Load the framework checklist — either:
         a) Hardcoded rules in a dict, OR
         b) Store framework docs in Supabase 'documents' table and search with pgvector
      3. For each requirement, ask LLM: "Does this architecture satisfy {requirement}?"
      4. Return pass/warn/fail for each + overall risk score
    
    For RAG-based compliance checking (using Supabase):
      query_embedding = get_embedding(f"{framework} {architecture_summary}")
      result = supabase.rpc("match_documents", {
          "query_embedding": query_embedding,
          "match_count": 10
      }).execute()
    
    Expected output:
    {
        "framework": "SOC2",
        "results": [
            { "requirement": "Data encryption at rest", "status": "pass", "note": "AES-256 specified" },
            { "requirement": "Access logging", "status": "warning", "note": "Not mentioned in HLD" },
            { "requirement": "Incident response plan", "status": "fail", "note": "Missing entirely" }
        ],
        "risk_score": 65,
        "risk_level": "medium"
    }
    """
    # STUB
    return {"framework": framework, "results": [], "risk_score": 0, "risk_level": "stub"}
