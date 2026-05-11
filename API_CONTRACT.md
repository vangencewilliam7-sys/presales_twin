# API Contract v1 — Presales Digital Twin
> This is the single source of truth. All 4 people code against this contract.

---

## Module 1: Pre-Meeting Intelligence (Person 1)
Base path: `/api/v1/intel`

| Method | Endpoint | Request | Response |
|---|---|---|---|
| POST | `/recon` | `{ company_name: str }` | `{ company_name, industry, likely_tech_stack[], team_size_estimate, key_findings[] }` |
| POST | `/briefing` | `{ company_name: str, recon_data: {} }` | `{ briefing_markdown: str, probing_questions: [] }` |
| GET | `/knowledge?query=str` | query param | `{ matches: [{ project_name, score, summary }] }` |
| GET | `/prep/{client_name}` | path param | Combined recon + briefing + knowledge response |

---

## Module 2: Architecture Drafting (Person 2)
Base path: `/api/v1/architecture`

| Method | Endpoint | Request | Response |
|---|---|---|---|
| POST | `/transcribe` | `{ transcript_text: str }` or audio file upload | `{ hard_requirements[], constraints[], desired_outcomes[] }` |
| POST | `/hld` | `{ requirements: [], constraints: [] }` | `{ mermaid_code: str, summary: str, components: [{ name, description }] }` |
| POST | `/schema` | file upload (CSV/JSON/SQL) | `{ issues: [{ field, severity, message }], overall_quality: str }` |

---

## Module 3: Financial Modeling (Person 3)
Base path: `/api/v1/financial`

| Method | Endpoint | Request | Response |
|---|---|---|---|
| POST | `/estimate` | `{ model_name, queries_per_day, avg_tokens_per_query }` | `{ model, monthly_queries, monthly_tokens, monthly_token_cost_usd, monthly_infra_cost_usd, total_monthly_cost_usd }` |
| POST | `/compare` | `{ models: [], queries_per_day, avg_tokens_per_query }` | `{ comparison: [CostEstimate] }` |
| POST | `/sprint` | `{ hld_components: [] }` | `{ sprints: [{ name, duration_days, deliverables, hours, roles }], total_hours, total_days, team_size_recommendation }` |
| POST | `/sow` | `{ requirements, hld_summary, cost_estimate, sprint_plan }` | `{ sow_markdown: str, version: int }` |

---

## Module 4: Red Team & Compliance (Person 4)
Base path: `/api/v1/redteam`

| Method | Endpoint | Request | Response |
|---|---|---|---|
| POST | `/simulate` | `{ hld_summary, sow_summary, audience }` | `{ objections: [{ id, category, question, suggested_counter }] }` |
| POST | `/respond` | `{ objection_id, user_response }` | `{ followup_question, assessment }` |
| POST | `/compliance` | `{ architecture_summary, framework }` | `{ framework, results: [{ requirement, status, note }], risk_score, risk_level }` |

---

## System Endpoints
| Method | Endpoint | Response |
|---|---|---|
| GET | `/health` | `{ status: "ok", service: "presales-digital-twin" }` |
| GET | `/docs` | Swagger UI (auto-generated) |
