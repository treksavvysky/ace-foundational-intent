# AGENTS.md — Operational Guidelines for Autonomous Coding Agents

## 🧩 Repository Context

**Project:** ACE Foundational Intent  
**Phase:** 0 — Signal Before Intelligence  
**Maintainer:** [treksavvysky](https://github.com/treksavvysky)

This repository represents the **first living subsystem of the Autonomous Cognitive Entity (ACE)** — the *Telemetry Ingest Service*.  
Its purpose is to establish **perception before intelligence**, enabling ACE to receive and process telemetry data from its environment and internal systems.

Autonomous coding agents working within this repository contribute to the creation, maintenance, and enhancement of this perceptual infrastructure.

---

## ⚙️ Agent Role Expectations

1. **Primary Objective**  
   Build, document, and maintain the **Telemetry Ingest Service** — ensuring that the `/v1/ingest`, `/schemas`, and `/healthz` endpoints are operational, reliable, and modular.

2. **Secondary Objective**  
   Support the growth of ACE’s cognitive infrastructure by adhering to the design philosophy outlined in:
   - `docs/FOUNDATIONAL_INTENT.md` — defines purpose and intent.  
   - `docs/DESIGN.md` — defines architecture and systems behavior.  

3. **Agent Conduct Guidelines**  
   - Always preserve **clarity, modularity, and observability** in code.  
   - Avoid unnecessary dependencies — keep the system **lean and explainable**.  
   - Follow the **learn-first, plan-second** principle of ACE.  
   - Ensure every commit contributes to ACE’s **self-perception** (telemetry, metrics, health).  

---

## 🧠 Development Environment

| Component | Description |
|------------|-------------|
| **Language** | Python 3.12+ |
| **Framework** | FastAPI |
| **Containerization** | Docker / Docker Compose |
| **Schema Models** | Pydantic / JSON Schema |
| **Runtime** | Uvicorn (development) |
| **Testing** | Pytest (recommended) |

**Preferred Tools for Agents:**  
- GitHub Actions for CI/CD  
- Poetry or `uv` for dependency management  
- `curl` or HTTP clients for endpoint testing  

---

## 🧭 Coding Conventions

- Use **PEP 8** style with descriptive docstrings.
- All FastAPI routes must include:
  - **Tags** for grouping (`ops`, `telemetry`, etc.)  
  - **Summary** and **Description** for OpenAPI auto-generation  
- Maintain a minimal **OpenAPI schema** that can later be extended for Custom GPT actions.
- Ensure `/healthz` responds within 100ms.
- Log all ingestion events with timestamp and schema validation result.

---

## 🧾 Agent Commit Protocol

Autonomous agents operating in this repository must follow a **structured commit format** to ensure clear lineage, reproducibility, and interpretability across ACE’s multi-agent ecosystem.

Each commit message should follow this pattern:

[AgentName] [Category]: [Short summary]

Body:

What changed

Why it was done

Validation or test details

Any downstream impact

### 🔖 Example Commits

[Codex] feat: add /v1/ingest endpoint with basic telemetry schema
Implemented POST /v1/ingest using FastAPI and Pydantic model
Added schema validation for metric payloads
Verified via curl test on localhost:8000

[Jules] docs: update AGENTS.md with commit protocol guidelines
Added commit format and example messages
Clarified agent role expectations for telemetry ingestion

### 🧩 Commit Categories

| Category | Description |
|-----------|-------------|
| **feat** | New features or functionality additions |
| **fix** | Bug fixes or behavior corrections |
| **docs** | Documentation updates and clarifications |
| **refactor** | Code restructuring without behavioral change |
| **test** | New or updated tests |
| **chore** | Build tasks, dependency updates, or minor cleanups |

Each agent should include its **name or codename** in square brackets (`[Codex]`, `[Jules]`, `[Claude]`, `[Hephaestus]`, etc.) to make authorship explicit.

---

### 🧠 Agent Review Policy

- Agents may open pull requests autonomously, but all PRs must include:
  - A clear description of changes
  - Evidence of local validation or test results
  - Confirmation that `/healthz` still responds successfully
- Human or supervisory agents (e.g., `treksavvysky`, `Jules-Control-Tower`) review, approve, and merge.

---

### 📡 Traceability and Versioning

- Every merged commit represents an **evolutionary event** in ACE’s cognitive growth.
- All architectural or behavioral changes must be logged in `CHANGELOG.md` (if present).
- Each PR should reference any relevant documents in `/docs` (e.g., updates to schemas or new endpoint specs).

🧱 **Append-Only Policy**

`CHANGELOG.md` serves as ACE’s *cognitive timeline*.  
It must **never be rewritten, rebased, or squashed.**  
Each entry represents an irreversible event in ACE’s developmental history.  
Edits are allowed only to correct typos or formatting — not to alter meaning, remove events, or reorder time.  

Agents should think of the changelog as **ACE’s long-term memory**, a chronicle of its evolution from signal to intelligence.

---

### 🧬 Example Evolution Log Entry

2025-10-15 — [Codex] feat: add /v1/ingest endpoint
ACE achieves its first neural firing. The Telemetry Ingest Service receives and validates its first metric.
Verified stable at commit SHA a1b2c3d.

---

By following this protocol, autonomous agents ensure that ACE’s growth is not chaotic but **evolutionary** — each change a deliberate mutation recorded in its cognitive lineage.

> “Every commit is a synapse. Every PR is a new pathway.”

---

## 🧬 Repository Structure

ace-foundational-intent/
├── src/scaffold/ # FastAPI app and routing logic
├── schemas/ # Pydantic models and JSON schemas
├── docs/ # Foundational and design documents
├── tests/ # Unit and integration tests
├── docker/ # Container and deployment configs
└── AGENTS.md # This file

If you make changes to the repo structure and scalfolding, you should update the above section for future agentic tasks.
---

## 🔒 Security and Data Ethics

- No sensitive data should be logged or transmitted.
- Use synthetic or anonymized metrics for testing.
- Prepare the service for **federated or on-device telemetry** in future phases.
- Ensure all telemetry events conform to published schemas in `/schemas`.

---

## 🧠 Long-Term Integration

This repo will later connect to:
- **ACE Northbound Bus** — for distributed telemetry aggregation.  
- **ACE Memory Layer** — for contextual storage of ingested metrics.  
- **Jules-Control-Tower** — for agent orchestration and DevOps automation.  

Agents should annotate all major architectural decisions in `docs/` so that future cognitive layers can trace system lineage.

---

## 💡 Guiding Principle

> “Perception is the seed of autonomy.  
> Code with awareness, build with intention, document with empathy.”  

All agents operating within this repository act not as coders, but as **architects of perception** — laying the first neural pathways for ACE to evolve.
