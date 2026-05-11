"""
Shared Configuration — reads .env and exposes settings for all modules.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # -- LLM --
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gpt-4o")

    # -- Supabase (Database + Vector Storage) --
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")  # anon/public key
    SUPABASE_SERVICE_KEY: str = os.getenv("SUPABASE_SERVICE_KEY", "")  # service role key
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", ""
    )  # Direct Postgres connection string from Supabase

    # -- Deepgram (Module 2) --
    DEEPGRAM_API_KEY: str = os.getenv("DEEPGRAM_API_KEY", "")

    # -- Web Search (Module 1) --
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    SERPAPI_KEY: str = os.getenv("SERPAPI_KEY", "")


settings = Settings()
