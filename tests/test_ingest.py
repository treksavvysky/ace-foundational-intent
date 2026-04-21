"""Tests for the ACE Telemetry Ingest Service."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi.testclient import TestClient  # noqa: E402

from src.scaffold.main import app  # noqa: E402

client = TestClient(app)


def test_healthz_liveness() -> None:
    """The /healthz endpoint should return a 200 OK response."""

    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_ingest_accepts_valid_payload() -> None:
    """The ingest endpoint should accept a valid telemetry payload."""

    payload = {
        "source": "unit-test",
        "metric": "latency_ms",
        "value": 12.3,
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
    }

    response = client.post("/v1/ingest", json=payload)
    assert response.status_code == 200
    assert response.json() == {"received": True}


def test_ingest_rejects_missing_fields() -> None:
    """The ingest endpoint should reject payloads missing required fields."""

    payload = {
        "source": "unit-test",
        "metric": "latency_ms",
        "value": 12.3,
    }

    response = client.post("/v1/ingest", json=payload)
    assert response.status_code == 422


def test_ingest_rejects_invalid_timestamp() -> None:
    """The ingest endpoint should reject payloads with invalid timestamp format."""

    payload = {
        "source": "unit-test",
        "metric": "latency_ms",
        "value": 12.3,
        "timestamp": "invalid-timestamp-format",
    }

    response = client.post("/v1/ingest", json=payload)
    assert response.status_code == 422


def test_ingest_rejects_unknown_fields() -> None:
    """The ingest endpoint should reject payloads with unexpected fields."""

    payload = {
        "source": "unit-test",
        "metric": "latency_ms",
        "value": 12.3,
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "extra": "nope",
    }

    response = client.post("/v1/ingest", json=payload)
    assert response.status_code == 422


def test_schema_endpoint_exposes_telemetry_model() -> None:
    """The /schemas endpoint should surface the telemetry JSON schema."""

    response = client.get("/schemas")
    assert response.status_code == 200

    schema = response.json()
    assert schema["title"] == "TelemetryEvent"
    assert set(schema["required"]) == {"source", "metric", "value", "timestamp"}
