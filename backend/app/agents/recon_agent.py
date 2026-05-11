"""
Recon Agent — Person 1
======================
Scrapes public info about a company to detect their tech stack, industry, and team size.

Dependencies: serpapi or tavily-python, beautifulsoup4, httpx
"""

from app.utils.llm_wrapper import call_llm_json


async def run_recon(company_name: str) -> dict:
    """
    TODO (Person 1): Implement this function.
    
    Steps:
      1. Search the web for "{company_name} tech stack" using SerpAPI or Tavily
      2. Check if they have a public GitHub org → list top repos → detect languages
      3. Search LinkedIn job postings → detect tools mentioned (AWS, Azure, Kubernetes, etc.)
      4. Feed all gathered info to LLM → ask it to summarize into structured JSON
    
    Expected output:
    {
        "company_name": "Acme Corp",
        "industry": "FinTech",
        "likely_tech_stack": ["Python", "AWS", "PostgreSQL", "React"],
        "team_size_estimate": "50-100 engineers",
        "key_findings": ["They have a data engineering team", "Using microservices"]
    }
    """
    # STUB — replace with real implementation
    return {
        "company_name": company_name,
        "industry": "Unknown",
        "likely_tech_stack": [],
        "team_size_estimate": "Unknown",
        "key_findings": ["Stub: not yet implemented"],
    }
