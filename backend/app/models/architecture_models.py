"""
Module 2 Pydantic Models — Person 2
Request/response shapes for Architecture Drafting endpoints.
"""

from pydantic import BaseModel


class TranscribeRequest(BaseModel):
    transcript_text: str = ""


class TaggedTranscript(BaseModel):
    hard_requirements: list[str]
    constraints: list[str]
    desired_outcomes: list[str]


class HLDRequest(BaseModel):
    requirements: list[str]
    constraints: list[str] = []


class HLDComponent(BaseModel):
    name: str
    description: str


class HLDResponse(BaseModel):
    mermaid_code: str
    summary: str
    components: list[HLDComponent]


class SchemaIssue(BaseModel):
    field: str
    severity: str  # "high", "medium", "low"
    message: str


class SchemaAnalysisResponse(BaseModel):
    issues: list[SchemaIssue]
    overall_quality: str
