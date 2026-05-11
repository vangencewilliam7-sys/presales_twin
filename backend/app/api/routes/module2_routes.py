"""
Module 2: Automated Architecture Drafting — API Routes
======================================================
Owner: Person 2
Endpoints:
  POST /transcribe     → Process call transcript (audio or text)
  POST /hld            → Generate HLD architecture diagram (Mermaid.js)
  POST /schema         → Analyze uploaded data schema

Instructions for Person 2:
  1. Import your agents from app.agents.transcribe_agent, hld_agent, schema_agent
  2. Build out each endpoint below
  3. Use Pydantic models from app.models.architecture_models for request/response shapes
  4. Use `from app.utils.llm_wrapper import call_llm` for any LLM calls
"""

from fastapi import APIRouter, UploadFile, File

router = APIRouter()


# ============================================================
#  ENDPOINT 1: Transcribe & Tag
# ============================================================
@router.post("/transcribe")
async def transcribe_and_tag(transcript_text: str = "", audio_file: UploadFile | None = File(None)):
    """
    Person 2: Replace this stub.
    Input: raw transcript text OR audio file upload
    Output: { hard_requirements[], constraints[], desired_outcomes[] }
    """
    return {
        "status": "stub",
        "message": "TODO: Process transcript and extract tagged requirements",
        "module": 2,
    }


# ============================================================
#  ENDPOINT 2: HLD Generator
# ============================================================
@router.post("/hld")
async def generate_hld(requirements: list[str] = [], constraints: list[str] = []):
    """
    Person 2: Replace this stub.
    Input: tagged requirements + constraints from /transcribe
    Output: { mermaid_code: str, summary: str, components: [] }
    """
    return {
        "status": "stub",
        "message": "TODO: Generate Mermaid.js HLD diagram from requirements",
        "module": 2,
    }


# ============================================================
#  ENDPOINT 3: Schema Analyzer
# ============================================================
@router.post("/schema")
async def analyze_schema(file: UploadFile = File(...)):
    """
    Person 2: Replace this stub.
    Input: CSV / JSON / SQL file upload
    Output: { issues: [{ field, severity, message }] }
    """
    return {
        "status": "stub",
        "message": "TODO: Analyze uploaded schema for data quality issues",
        "module": 2,
    }
