# 📘 Presales Digital Twin: Developer Handbook
> Welcome to the team! This document contains everything you need to know about your module: what you are building, what API keys you need, and exactly which files you are allowed to edit.

---

## 🚀 Quick Setup (Everyone)

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/vangencewilliam7-sys/presales_twin.git
   cd presales_twin/backend
   ```
2. **Environment & Keys:**
   - Run `copy .env.example .env`
   - Ask the Lead for the **Supabase API Keys**, **OpenAI Key**, and **Deepgram/SerpAPI Keys**.
   - **One-time Supabase Setup:** The Lead must run `CREATE EXTENSION IF NOT EXISTS vector;` in the Supabase SQL editor.
3. **Install Dependencies:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```
4. **Golden Rule of Collaboration:**
   **ONLY edit the files listed under your module below.** Do not touch `main.py` or files belonging to other people. If you need a shared utility, ask the Lead to add it to `app/utils/`.

---

## 👤 Person 1: Pre-Meeting Intelligence

**Goal:** Build AI agents that research clients before a meeting.

### What You Are Building:
1. **Recon Agent:** Scrapes web (GitHub, LinkedIn) to guess the client's tech stack and team size.
2. **Briefing Generator:** Uses LLM to create a 1-page summary and probing questions.
3. **Knowledge Retriever (RAG):** Embeds past project documents into Supabase (pgvector) and retrieves similar past projects.

### Dependencies & Services:
- **SerpAPI / Tavily:** For web search (add key to `.env`)
- **Supabase (pgvector):** For storing and querying document embeddings.
- **OpenAI:** For summarization and embeddings.

### Files You Own (Edit These):
- `backend/app/agents/recon_agent.py`
- `backend/app/agents/briefing_agent.py`
- `backend/app/agents/knowledge_agent.py`
- `backend/app/api/routes/module1_routes.py` (Wire up your endpoints here)
- `backend/app/models/intel_models.py` (Define your request/response JSON shapes here)

---

## 👤 Person 2: Automated Architecture Drafting

**Goal:** Turn raw discovery call notes/audio into technical architecture diagrams.

### What You Are Building:
1. **Transcribe & Tag:** Converts audio to text (Deepgram) and extracts hard requirements and constraints using LLM.
2. **HLD Generator:** Takes requirements and generates a Mermaid.js architecture diagram.
3. **Schema Analyzer:** Analyzes uploaded CSV/JSON/SQL schemas for data quality issues.

### Dependencies & Services:
- **Deepgram API:** For fast audio transcription (add key to `.env`).
- **OpenAI:** For requirement extraction and Mermaid.js generation.
- **Mermaid.js:** Output format for the architecture diagrams.

### Files You Own (Edit These):
- `backend/app/agents/transcribe_agent.py`
- `backend/app/agents/hld_agent.py`
- `backend/app/agents/schema_agent.py`
- `backend/app/api/routes/module2_routes.py` (Wire up your endpoints here)
- `backend/app/models/architecture_models.py` (Define your request/response JSON shapes here)

---

## 👤 Person 3: Financial Modeling & Database Core

**Goal:** Calculate LLM costs, generate Sprint roadmaps, draft the SOW, and manage the Database.

### What You Are Building:
1. **Database Setup:** Define the SQLAlchemy ORM models that all modules will use.
2. **Cost Estimator:** Calculates token/infrastructure costs based on model choice and volume.
3. **Sprint Planner:** Breaks HLD components into a 90-day sprint roadmap.
4. **SOW Drafter:** Uses LLM to write the "Technical Scope" Markdown document based on all previous data.

### Dependencies & Services:
- **Supabase (PostgreSQL):** You own the relational database schema. You don't need Docker; the `DATABASE_URL` connects directly to Supabase.
- **OpenAI:** For sprint planning and SOW drafting.
- **SQLAlchemy / Alembic:** For database ORM and migrations.

### Files You Own (Edit These):
- `backend/app/agents/token_calculator.py`
- `backend/app/agents/sprint_planner.py`
- `backend/app/agents/sow_drafter.py`
- `backend/app/api/routes/module3_routes.py` (Wire up your endpoints here)
- `backend/app/models/financial_models.py` (Define your request/response JSON shapes here)
- `backend/app/db/models.py` (Define the database tables here)
- `backend/app/db/session.py` (Manage the database connection here)

---

## 👤 Person 4: Technical Skeptic Simulation & Frontend

**Goal:** Build the Red Team "devil's advocate" simulator and the entire Frontend UI.

### What You Are Building:
1. **Objection Simulator:** An LLM that role-plays as a skeptical CTO to attack the proposed solution.
2. **Compliance Checker:** Uses Supabase RAG to scan the architecture against SOC2, HIPAA, etc.
3. **Frontend Dashboard:** A React application that consumes the APIs from Modules 1, 2, 3, and 4.

### Dependencies & Services:
- **Supabase (pgvector):** For RAG-based compliance document retrieval.
- **OpenAI:** For the "Skeptical CTO" roleplay.
- **React / Vite:** For the frontend UI.
- **Mermaid.js / Recharts:** To render Person 2's diagrams and Person 3's cost data on the frontend.

### Files You Own (Edit These):
- `backend/app/agents/objection_simulator.py`
- `backend/app/agents/compliance_checker.py`
- `backend/app/api/routes/module4_routes.py` (Wire up your endpoints here)
- `backend/app/models/redteam_models.py` (Define your request/response JSON shapes here)
- `frontend/` (You own the entire React application)

---

## 🤝 How Modules Connect (The Data Flow)

The entire application is a pipeline. Your module relies on the output of the module before you:

1. **Person 1 (Intel)** discovers the client's tech stack.
2. **Person 2 (Architecture)** uses that tech stack to draw an HLD diagram.
3. **Person 3 (Financial)** uses that HLD diagram to plan sprints and calculate costs.
4. **Person 4 (Red Team)** attacks the HLD and Costs using the Skeptic Simulator.

Check `API_CONTRACT.md` to see the exact JSON shapes that each module expects to receive and return.
