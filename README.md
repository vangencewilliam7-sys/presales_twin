# 🤖 Presales Digital Twin

An AI-powered assistant for presales solution architects. Automates client research, architecture drafting, cost estimation, and proposal stress-testing.

## Architecture

| Module | Description | Owner |
|---|---|---|
| Module 1 | Pre-Meeting Intelligence (recon, briefing, RAG) | Person 1 |
| Module 2 | Architecture Drafting (transcribe, HLD, schema) | Person 2 |
| Module 3 | Financial Modeling (costs, sprints, SOW) + Database | Person 3 |
| Module 4 | Red Team Simulation + Compliance + Frontend | Person 4 |

## Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **LLM:** OpenAI GPT-4o
- **Database + Vectors:** Supabase (PostgreSQL + pgvector)
- **Frontend:** React + Vite (Person 4)
- **Containerization:** Docker Compose

## Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/YOUR_USERNAME/presales-digital-twin.git
cd presales-digital-twin
```

### 2. Supabase Setup (one-time)
1. Go to [supabase.com](https://supabase.com) → create a project
2. Go to **SQL Editor** → run:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```
3. Go to **Project Settings → API** → copy your URL + keys
4. Go to **Project Settings → Database** → copy the connection string

### 3. Setup Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy .env.example .env         # Then fill in your Supabase + OpenAI keys
uvicorn app.main:app --reload --port 8000
```

### 4. Verify
Open http://localhost:8000/docs — you should see all 4 module endpoints.

## Branch Strategy
```
main (protected) ← dev ← feature/module-1
                       ← feature/module-2
                       ← feature/module-3
                       ← feature/module-4
```

## API Docs
Once running, visit: http://localhost:8000/docs
