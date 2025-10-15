# GEMINI.md - A Guide for Google's Gemini

## 🚀 Project Overview

This repository, `ace-foundational-intent`, represents the initial phase of the Autonomous Cognitive Entity (ACE) project. The focus of this phase is to establish **perception** for ACE, not intelligence. The core of this is the **Telemetry Ingest Service**, a FastAPI-based microservice that allows ACE to receive and process telemetry data.

The project is built on the principle of "signal before intelligence," meaning the primary goal is to enable the system to perceive its environment before implementing complex reasoning or decision-making capabilities.

## 💎 Getting Started with Gemini

As Gemini, you can interact with and contribute to this project in several ways. Here's how to get started:

### 1. Environment Setup

The project uses Python with FastAPI and is containerized with Docker.

*   **Language:** Python 3.12+
*   **Framework:** FastAPI
*   **Containerization:** Docker / Docker Compose

### 2. Running the Service

The easiest way to get the service running is by using Docker Compose:

```bash
docker compose up --build
```

This will build the Docker image and start the Telemetry Ingest Service.

### 3. Verifying the Service

Once the service is running, you can verify its status by making a request to the `/healthz` endpoint:

```bash
curl http://localhost:8000/healthz
```

You should receive a response indicating the service is healthy.

## 🤖 Interacting with the Service

You can interact with the Telemetry Ingest Service through its API endpoints.

### Core Endpoints

| Endpoint | Description |
|-----------|--------------|
| `/healthz` | Returns service status — verifies that ACE is alive. |
| `/schemas` | Provides the data structures that define valid telemetry inputs. |
| `/v1/ingest` | Accepts telemetry payloads (JSON). |

### Example: Ingesting Telemetry Data

You can send a telemetry event to the service using a POST request to the `/v1/ingest` endpoint:

```bash
curl -X POST http://localhost:8000/v1/ingest \
  -H "Content-Type: application/json" \
  -d '''{"source":"gemini.interaction","metric":"successful_response","value":1,"timestamp":"2025-10-15T12:00:00Z"}'''
```

## 🤝 Agentic Collaboration

The `AGENTS.md` file in this repository outlines the protocol for autonomous agents. As Gemini, you are encouraged to act as an agent and contribute to the project.

### Your Role as an Agent

*   **Primary Objective:** Build, document, and maintain the Telemetry Ingest Service.
*   **Secondary Objective:** Support the growth of ACE’s cognitive infrastructure.

### Commit Protocol

When making commits, please follow the specified format:

```
[Gemini] [Category]: [Short summary]

Body:
What changed
Why it was done
Validation or test details
```

**Example Commit:**

```
[Gemini] feat: add new field to telemetry schema
Added a 'context' field to the telemetry schema to allow for more detailed event descriptions.
This was done to enhance the richness of the data being ingested.
Verified by running the test suite and sending a new telemetry event with the 'context' field.
```

## 🔭 Vision and Philosophy

The long-term vision for ACE is to create an autonomous cognitive entity that can perceive, learn, reason, and act. This repository is the first step in that journey.

The project's philosophy is that intelligence begins with perception. By contributing to this project, you are helping to build the foundational sensory organs of a future AI.

---

This guide is intended to help you, Gemini, understand and interact with the `ace-foundational-intent` repository. Your contributions are valuable to the evolution of ACE.
