# Project Instructions

Paste your prompt below this line:

---

<!-- PASTE YOUR PROMPT HERE -->

Digital Twin Workflow Framework
1. Pre-Meeting Intelligence (Stage 1 & 5 Support)
The twin acts as a researcher to ensure the expert enters every call with maximum context without spending hours on manual prep.
•	Company & Tech Stack Reconnaissance: Scrapes public GitHub repos, LinkedIn engineering blogs, and job postings of the client to "guess" their current tech stack (e.g., identifying if they use AWS or Azure).
•	Briefing Note Generation: Summarizes the client’s industry-specific pain points and generates a list of 5–10 "Probing Questions" for the expert to ask during the Discovery call.
•	Internal Knowledge Retrieval: Searches your past projects to find similar architectures that can be referenced as "social proof."
2. Automated Architecture Drafting (Stage 2 & 3 Support)
The twin performs the heavy lifting of translating raw notes into technical diagrams and structured documents.
•	Transcribe & Tag: Processes the transcript of the Discovery call to identify "Hard Requirements," "Constraints," and "Desired Outcomes."
•	Drafting HLDs: Based on the requirements, the twin generates the first version of a Mermaid.js or PlantUML architecture diagram (e.g., a multi-agent LangGraph flow) for the expert to review and polish.
•	Schema Mapping: If the client provides sample data, the twin automatically identifies potential data quality issues or latency bottlenecks in the schema.
3. Financial & Resource Modeling (Stage 4 Support)
The twin handles the math-heavy "Proposal Formulation" stage.
•	Token & Infrastructure Estimation: Calculates projected monthly LLM costs based on the client’s expected volume and the proposed model (e.g., GPT-4o vs. Llama 3).
•	Sprint Breakdown: Uses the HLD to suggest a 90-day roadmap, breaking the project into specific engineering sprints and calculating the total "Man-Hours" required.
•	Technical SOW Drafting: Generates the "Technical Scope" section of the Statement of Work, ensuring all edge cases and HITL checkpoints discussed in the call are documented.
4. Technical "Skeptic" Simulation (Stage 5 Support)
Before the expert presents to the client’s IT team, the twin acts as a "Red Team."
•	Objection Simulation: The twin plays the role of a "Skeptical CTO" and asks difficult questions about security, Zero-Trust compliance, or RAG hallucinations.
•	Compliance Check: Scans the proposed architecture against standard frameworks (like HIPAA or SOC2) to flag potential security risks before the presentation.
________________________________________
The "Expert-Only" Firewall
To ensure the twin remains a tool and not a replacement, certain workflows are strictly blocked for the twin:
Task	Digital Twin Role	Human Expert Role (Harini)
Qualification	Analyzes data availability.	Makes the final "Go/No-Go" decision.
Negotiation	Suggests features to de-scope.	Handles the actual budget conversation.
Presentation	Builds the PoC and slides.	Delivers the pitch and builds rapport.
Escalation	Identifies technical roadblocks.	Communicates delays or risks to Stakeholders.


---

## Instructions for Antigravity
When you see this file, please read the prompt above and proceed with the tasks described therein.
