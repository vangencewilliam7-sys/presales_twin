"""
Module 3: Financial & Resource Modeling — API Routes
====================================================
Owner: Person 3
Endpoints:
  POST /estimate   → Calculate token & infrastructure costs
  POST /compare    → Compare costs across multiple LLM models
  POST /sprint     → Generate 90-day sprint breakdown
  POST /sow        → Draft technical Statement of Work

Instructions for Person 3:
  1. Import your agents from app.agents.token_calculator, sprint_planner, sow_drafter
  2. Build out each endpoint below
  3. Use Pydantic models from app.models.financial_models for request/response shapes
  4. Use `from app.utils.llm_wrapper import call_llm` for sprint planner and SOW drafter
  5. YOU also own the database setup — see app/db/ folder
"""

from fastapi import APIRouter

router = APIRouter()


# ============================================================
#  ENDPOINT 1: Token & Infrastructure Cost Estimate
# ============================================================
@router.post("/estimate")
async def estimate_costs(
    model_name: str = "gpt-4o",
    queries_per_day: int = 1000,
    avg_tokens_per_query: int = 500,
):
    """
    Person 3: Replace this stub.
    Input: model choice, daily volume, tokens per query
    Output: { monthly_token_cost, monthly_infra_cost, total_monthly_cost, breakdown }
    """
    return {
        "status": "stub",
        "message": f"TODO: Calculate costs for {model_name} at {queries_per_day} queries/day",
        "module": 3,
    }


# ============================================================
#  ENDPOINT 2: Multi-Model Cost Comparison
# ============================================================
@router.post("/compare")
async def compare_models(
    models: list[str] = ["gpt-4o", "claude-sonnet", "llama-3-70b"],
    queries_per_day: int = 1000,
    avg_tokens_per_query: int = 500,
):
    """
    Person 3: Replace this stub.
    Input: list of model names + volume
    Output: { comparison: [{ model, monthly_cost, pros, cons }] }
    """
    return {
        "status": "stub",
        "message": f"TODO: Compare costs for {models}",
        "module": 3,
    }


# ============================================================
#  ENDPOINT 3: Sprint Breakdown Planner
# ============================================================
@router.post("/sprint")
async def plan_sprints(hld_components: list[str] = []):
    """
    Person 3: Replace this stub.
    Input: list of HLD components (from Module 2)
    Output: { sprints: [{ name, duration_days, deliverables, hours }], total_hours, roadmap_days }
    """
    return {
        "status": "stub",
        "message": f"TODO: Break {len(hld_components)} components into sprints",
        "module": 3,
    }


# ============================================================
#  ENDPOINT 4: Technical SOW Drafter
# ============================================================
@router.post("/sow")
async def draft_sow(
    requirements: list[str] = [],
    hld_summary: str = "",
    cost_estimate: dict = {},
    sprint_plan: dict = {},
):
    """
    Person 3: Replace this stub.
    Input: requirements + HLD + costs + sprints (from other endpoints)
    Output: { sow_markdown: str, version: int }
    """
    return {
        "status": "stub",
        "message": "TODO: Generate technical SOW document",
        "module": 3,
    }
