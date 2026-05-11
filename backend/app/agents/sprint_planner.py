"""
Sprint Planner — Person 3
==========================
Breaks HLD components into a 90-day sprint roadmap.

Dependencies: app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm_json


async def plan_sprints(hld_components: list[str]) -> dict:
    """
    TODO (Person 3): Implement this function.
    
    Steps:
      1. Send HLD components to LLM
      2. Ask it to break into 2-week sprints with: name, deliverables, hours, required roles
      3. Calculate total man-hours and duration
    
    Expected output:
    {
        "sprints": [
            { "name": "Sprint 1: Infrastructure Setup", "duration_days": 14, 
              "deliverables": ["Cloud setup", "CI/CD pipeline"], "hours": 80, "roles": ["DevOps", "Backend"] },
            ...
        ],
        "total_hours": 480,
        "total_days": 90,
        "team_size_recommendation": 3
    }
    """
    # STUB
    return {"sprints": [], "total_hours": 0, "total_days": 0, "team_size_recommendation": 0}
