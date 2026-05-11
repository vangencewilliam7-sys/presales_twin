"""
Module 1: Pre-Meeting Intelligence — API Routes
================================================
Owner: Person 1
Endpoints:
  POST /recon          → Run company reconnaissance
  POST /briefing       → Generate briefing note
  GET  /knowledge      → Search past projects (RAG)
  GET  /prep/{client}  → Get full pre-meeting package

Instructions for Person 1:
  1. Import your agents from app.agents.recon_agent, briefing_agent, knowledge_agent
  2. Build out each endpoint below
  3. Use Pydantic models from app.models.intel_models for request/response shapes
  4. Use `from app.utils.llm_wrapper import call_llm` for any LLM calls
"""

from fastapi import APIRouter

router = APIRouter()


# ============================================================
#  ENDPOINT 1: Company Reconnaissance
# ============================================================
@router.post("/recon")
async def run_recon(company_name: str = ""):
    """
    Person 1: Replace this stub.
    Input: company name or URL
    Output: { company_name, industry, tech_stack[], team_size_estimate }
    """
    return {
        "status": "stub",
        "message": f"TODO: Run recon on '{company_name}'",
        "module": 1,
    }


# ============================================================
#  ENDPOINT 2: Briefing Note Generation
# ============================================================
@router.post("/briefing")
async def generate_briefing(company_name: str = ""):
    """
    Person 1: Replace this stub.
    Input: company name + recon data
    Output: { briefing_markdown, probing_questions[] }
    """
    return {
        "status": "stub",
        "message": f"TODO: Generate briefing for '{company_name}'",
        "module": 1,
    }


# ============================================================
#  ENDPOINT 3: Internal Knowledge Search (RAG)
# ============================================================
@router.get("/knowledge")
async def search_knowledge(query: str = ""):
    """
    Person 1: Replace this stub.
    Input: search query
    Output: { matches: [{ project_name, score, summary }] }
    """
    return {
        "status": "stub",
        "message": f"TODO: Search knowledge base for '{query}'",
        "module": 1,
    }


# ============================================================
#  ENDPOINT 4: Full Pre-Meeting Package
# ============================================================
@router.get("/prep/{client_name}")
async def get_prep_package(client_name: str):
    """
    Person 1: Replace this stub.
    Combines recon + briefing + knowledge search into one response.
    """
    return {
        "status": "stub",
        "message": f"TODO: Full prep package for '{client_name}'",
        "module": 1,
    }
