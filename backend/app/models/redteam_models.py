"""
Module 4 Pydantic Models — Person 4
Request/response shapes for Red Team & Compliance endpoints.
"""

from pydantic import BaseModel


class SimulateRequest(BaseModel):
    hld_summary: str
    sow_summary: str = ""
    audience: str = "CTO"  # CTO, VP_Engineering, Security_Lead


class Objection(BaseModel):
    id: str
    category: str  # Security, Scalability, Cost, Feasibility
    question: str
    suggested_counter: str


class SimulateResponse(BaseModel):
    objections: list[Objection]


class RespondRequest(BaseModel):
    objection_id: str
    user_response: str


class RespondResponse(BaseModel):
    followup_question: str
    assessment: str  # "strong", "adequate", "weak"


class ComplianceRequest(BaseModel):
    architecture_summary: str
    framework: str = "SOC2"  # SOC2, HIPAA, GDPR, PCI-DSS, ISO27001


class ComplianceResult(BaseModel):
    requirement: str
    status: str  # "pass", "warning", "fail"
    note: str


class ComplianceResponse(BaseModel):
    framework: str
    results: list[ComplianceResult]
    risk_score: int  # 0-100
    risk_level: str  # "low", "medium", "high", "critical"
