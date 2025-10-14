"""FastAPI application for the ACE Telemetry Ingest Service."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from schemas.telemetry import TelemetryEvent

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s :: %(message)s")
logger = logging.getLogger("ace.telemetry.ingest")

app = FastAPI(
    title="ACE Telemetry Ingest Service",
    description="Initial perceptual subsystem enabling ACE to receive telemetry events.",
    version="0.1.0",
)


@app.get(
    "/healthz",
    tags=["ops"],
    summary="Health probe",
    description="Returns the liveness status of the Telemetry Ingest Service.",
)
def healthz() -> dict[str, str]:
    """Report basic service health."""

    return {"status": "alive"}


@app.get(
    "/schemas",
    tags=["telemetry"],
    summary="Telemetry schema",
    description="Expose the JSON schema describing valid telemetry events.",
)
def get_schema() -> dict[str, Any]:
    """Return the JSON schema for telemetry events."""

    return TelemetryEvent.json_schema()


@app.post(
    "/v1/ingest",
    tags=["telemetry"],
    summary="Ingest telemetry event",
    description="Validate and ingest telemetry payloads emitted by ACE subsystems.",
)
def ingest(event: TelemetryEvent) -> dict[str, bool]:
    """Validate the telemetry event and log it for downstream processing."""

    serialized_event = jsonable_encoder(event, exclude_none=True)
    log_record = {
        "event": serialized_event,
        "schema_validation": "passed",
        "ingested_at": datetime.now(tz=timezone.utc).isoformat(),
    }
    logger.info("Telemetry event ingested", extra={"telemetry_event": log_record})
    return {"received": True}


__all__ = ["app"]
