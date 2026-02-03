"""FastAPI application for the ACE Telemetry Ingest Service."""

from __future__ import annotations

import logging
import uuid
from contextvars import ContextVar
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, Request, Response
from fastapi.encoders import jsonable_encoder
from pythonjsonlogger import jsonlogger

from schemas.telemetry import TelemetryEvent
from src.scaffold.config import settings

# Context variable to hold the current request ID
request_id_ctx: ContextVar[str] = ContextVar("request_id", default="-")


class RequestIdFilter(logging.Filter):
    """Logging filter that adds request_id to log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id_ctx.get()
        return True


def configure_logging() -> logging.Logger:
    """Configure JSON logging with request ID support."""
    logger = logging.getLogger(settings.service_name)
    logger.setLevel(settings.log_level.upper())

    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()

    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(name)s %(request_id)s %(message)s",
        rename_fields={"asctime": "timestamp", "levelname": "level"},
    )
    handler.setFormatter(formatter)
    handler.addFilter(RequestIdFilter())
    logger.addHandler(handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


logger = configure_logging()

app = FastAPI(
    title="ACE Telemetry Ingest Service",
    description="Initial perceptual subsystem enabling ACE to receive telemetry events.",
    version=settings.schema_version,
)


@app.middleware("http")
async def request_id_middleware(request: Request, call_next: Any) -> Response:
    """Add request ID to each request for tracing."""
    # Use provided X-Request-ID header or generate a new one
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request_id_ctx.set(request_id)

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id

    return response


@app.get(
    "/healthz",
    tags=["ops"],
    summary="Health probe",
    description="Returns the liveness status of the Telemetry Ingest Service.",
)
def healthz() -> dict[str, str]:
    """Report basic service health."""
    logger.debug("Health check requested")
    return {"status": "alive"}


@app.get(
    "/schemas",
    tags=["telemetry"],
    summary="Telemetry schema",
    description="Expose the JSON schema describing valid telemetry events.",
)
def get_schema() -> dict[str, Any]:
    """Return the JSON schema for telemetry events."""
    logger.debug("Schema requested")
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
    logger.info(
        "Telemetry event ingested",
        extra={
            "event": serialized_event,
            "schema_validation": "passed",
            "ingested_at": datetime.now(tz=timezone.utc).isoformat(),
        },
    )
    return {"received": True}


__all__ = ["app"]
