"""
Transcribe Agent — Person 2
============================
Processes call transcripts (audio or text) and extracts tagged requirements.

Dependencies: deepgram-sdk, app.utils.llm_wrapper
"""

from app.utils.llm_wrapper import call_llm_json


async def transcribe_audio(audio_bytes: bytes) -> str:
    """
    TODO (Person 2): Implement this function.
    
    Steps:
      1. Send audio_bytes to Deepgram API
      2. Return the transcript text
    """
    # STUB
    return "Stub: transcription not yet implemented"


async def tag_transcript(transcript: str) -> dict:
    """
    TODO (Person 2): Implement this function.
    
    Steps:
      1. Send transcript to LLM with a prompt asking to extract:
         - hard_requirements: things the client MUST have
         - constraints: budget, timeline, tech limitations
         - desired_outcomes: what success looks like
      2. Return as structured JSON
    
    Expected output:
    {
        "hard_requirements": ["Must integrate with SAP", "Real-time processing"],
        "constraints": ["Budget under $50k", "Must use Azure"],
        "desired_outcomes": ["Reduce manual review by 80%"]
    }
    """
    # STUB
    return {
        "hard_requirements": ["Stub requirement"],
        "constraints": ["Stub constraint"],
        "desired_outcomes": ["Stub outcome"],
    }
