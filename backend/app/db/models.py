"""
Database ORM Models — Person 3 owns this file.
===============================================
SQLAlchemy table definitions used by all modules.

TODO (Person 3): Add all tables here.
After defining, run: alembic revision --autogenerate -m "initial"
Then: alembic upgrade head
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    industry = Column(String(100))
    tech_stack = Column(JSONB, default=[])
    created_at = Column(DateTime, default=datetime.utcnow)


class Meeting(Base):
    __tablename__ = "meetings"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    meeting_type = Column(String(50))
    date = Column(DateTime)
    transcript = Column(Text)
    tagged_data = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)


class Project(Base):
    __tablename__ = "projects"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"))
    name = Column(String(255))
    status = Column(String(50), default="drafting")
    hld_mermaid = Column(Text)
    hld_summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class CostEstimate(Base):
    __tablename__ = "cost_estimates"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    model_name = Column(String(50))
    queries_per_day = Column(Integer)
    tokens_per_query = Column(Integer)
    monthly_token_cost = Column(Numeric(10, 2))
    monthly_infra_cost = Column(Numeric(10, 2))
    total_monthly_cost = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=datetime.utcnow)


class SprintPlan(Base):
    __tablename__ = "sprint_plans"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    sprints = Column(JSONB)
    total_hours = Column(Integer)
    duration_days = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)


class SOWDocument(Base):
    __tablename__ = "sow_documents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    version = Column(Integer, default=1)
    content_markdown = Column(Text)
    status = Column(String(20), default="draft")
    approved_by = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)


class RedTeamSession(Base):
    __tablename__ = "red_team_sessions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    audience = Column(String(50))
    objections = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)


class ComplianceCheck(Base):
    __tablename__ = "compliance_checks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    framework = Column(String(50))
    findings = Column(JSONB)
    risk_level = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)


class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    action = Column(String(100))
    module = Column(String(20))
    was_blocked = Column(Boolean, default=False)
    reason = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
