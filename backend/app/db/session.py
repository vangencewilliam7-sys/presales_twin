"""
Database Session — Person 3 owns this file.
============================================
Connects to Supabase's PostgreSQL database via SQLAlchemy.
All modules import `get_db` to access the database.

Note: Supabase IS PostgreSQL. The DATABASE_URL points directly to
Supabase's Postgres instance. No separate DB container needed.

Usage in route files:
    from app.db.session import get_db
    from sqlalchemy.orm import Session
    from fastapi import Depends

    @router.get("/something")
    def my_endpoint(db: Session = Depends(get_db)):
        # use db to query
        pass
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency that provides a database session to endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
