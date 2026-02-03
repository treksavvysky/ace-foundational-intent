# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ACE Foundational Intent** is Phase 0 of the Autonomous Cognitive Entity (ACE) Framework — establishing signal and perception before intelligence. This repository implements the **Telemetry Ingest Service**, ACE's first living subsystem that enables it to perceive events and metrics.

The project philosophy: **Signal before intelligence. Learn first, plan second, react when necessary.**

## Essential Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run a single test
pytest tests/test_ingest.py::test_healthz_liveness -v

# Run service locally (development)
uvicorn src.scaffold.main:app --host 0.0.0.0 --port 8000 --reload

# Docker operations
docker compose up --build      # Build and run (port 8760 -> 8000)
docker compose up -d           # Run in background
docker compose logs -f         # View logs
docker compose down            # Stop service

# Test endpoints (Docker)
curl http://localhost:8760/healthz
curl http://localhost:8760/schemas
curl -X POST http://localhost:8760/v1/ingest \
  -H "Content-Type: application/json" \
  -d '{"source":"test","metric":"value","value":42.0,"timestamp":"2025-01-01T00:00:00Z"}'
```

## Architecture

### Current Implementation (Phase 0)

The Telemetry Ingest Service is a FastAPI microservice with three endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/healthz` | GET | Health probe (must respond < 100ms) |
| `/schemas` | GET | Returns JSON schema for valid telemetry events |
| `/v1/ingest` | POST | Accepts and validates telemetry payloads |

**Key Files:**

- `src/scaffold/main.py` — FastAPI app with route definitions
- `schemas/telemetry.py` — Pydantic `TelemetryEvent` model with `extra="forbid"` (rejects unknown fields)
- `tests/test_ingest.py` — Pytest suite using FastAPI TestClient

**TelemetryEvent Schema:**
- `source` (str, 1-128 chars) — System emitting the event
- `metric` (str, 1-128 chars) — Metric identifier
- `value` (float) — Numeric measurement
- `timestamp` (datetime) — ISO 8601 timestamp

### Test Setup Note

Tests in `tests/test_ingest.py` manually insert the project root into `sys.path` to resolve imports. This is due to the `src/scaffold/` layout without a package install step.

## Development Conventions

### Code Style

- **PEP 8** compliance with descriptive docstrings
- **Type hints** using `from __future__ import annotations`
- **Pydantic models** for all data validation
- FastAPI routes must include tags, summary, and description for OpenAPI docs

### Performance Requirements

- `/healthz` must respond within 100ms
- All ingestion events logged with timestamp and validation result (structured logging)

## Commit Protocol

**All commits must follow the agent commit format:**

```
[AgentName] [category]: [short summary]

Body:
- What changed
- Why it was done
- Validation or test details
- Any downstream impact
```

**Categories:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

**Agent names:** `[Codex]`, `[Jules]`, `[Claude]`, `[Gemini]`, etc.

### CHANGELOG.md Rules

**CRITICAL:** `CHANGELOG.md` is **append-only** — ACE's cognitive timeline:
- Append new entries to the **end** of the file only
- Never rewrite, rebase, squash, or reorder entries
- Never insert entries in the middle
- Edits allowed only for typos/formatting — not to alter meaning or remove events

## Key Documentation

| Document | Purpose |
|----------|---------|
| `docs/FOUNDATIONAL_INTENT.md` | Philosophy — "signal before intelligence" principle |
| `docs/DESIGN.md` | Full cognitive architecture specification (SOAR, ACT-R, CLARION integration roadmap) |
| `AGENTS.md` | Operational guidelines for autonomous coding agents |

## Future Integration

This service will connect to:
- **ACE Northbound Bus** — Distributed telemetry aggregation
- **ACE Memory Layer** — Contextual storage of ingested metrics
- **Jules-Control-Tower** — Agent orchestration and DevOps automation

Document architectural decisions in `/docs` for future cognitive layers.
