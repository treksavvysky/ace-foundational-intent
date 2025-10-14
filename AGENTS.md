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

## 🧬 Repository Structure

ace-foundational-intent/
├── src/scaffold/ # FastAPI app and routing logic
├── schemas/ # Pydantic models and JSON schemas
├── docs/ # Foundational and design documents
├── tests/ # Unit and integration tests
├── docker/ # Container and deployment configs
└── AGENTS.md # This file


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
