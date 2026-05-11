"""
Module 1 Pydantic Models — Person 1
Request/response shapes for Pre-Meeting Intelligence endpoints.
"""

from pydantic import BaseModel


class ReconRequest(BaseModel):
    company_name: str


class ReconResponse(BaseModel):
    company_name: str
    industry: str
    likely_tech_stack: list[str]
    team_size_estimate: str
    key_findings: list[str]


class BriefingRequest(BaseModel):
    company_name: str
    recon_data: dict = {}


class BriefingResponse(BaseModel):
    briefing_markdown: str
    probing_questions: list[str]


class KnowledgeMatch(BaseModel):
    project_name: str
    score: float
    summary: str


class KnowledgeSearchResponse(BaseModel):
    matches: list[KnowledgeMatch]
