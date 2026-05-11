"""
Module 3 Pydantic Models — Person 3
Request/response shapes for Financial Modeling endpoints.
"""

from pydantic import BaseModel


class CostEstimateRequest(BaseModel):
    model_name: str = "gpt-4o"
    queries_per_day: int = 1000
    avg_tokens_per_query: int = 500


class CostEstimateResponse(BaseModel):
    model: str
    monthly_queries: int
    monthly_tokens: int
    monthly_token_cost_usd: float
    monthly_infra_cost_usd: float
    total_monthly_cost_usd: float


class ModelComparisonRequest(BaseModel):
    models: list[str] = ["gpt-4o", "claude-sonnet", "llama-3-70b"]
    queries_per_day: int = 1000
    avg_tokens_per_query: int = 500


class SprintRequest(BaseModel):
    hld_components: list[str]


class Sprint(BaseModel):
    name: str
    duration_days: int
    deliverables: list[str]
    hours: int
    roles: list[str] = []


class SprintPlanResponse(BaseModel):
    sprints: list[Sprint]
    total_hours: int
    total_days: int
    team_size_recommendation: int


class SOWRequest(BaseModel):
    requirements: list[str]
    hld_summary: str
    cost_estimate: dict = {}
    sprint_plan: dict = {}


class SOWResponse(BaseModel):
    sow_markdown: str
    version: int
