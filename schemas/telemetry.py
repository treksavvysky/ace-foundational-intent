"""Telemetry schema definitions for the ACE Telemetry Ingest Service."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class TelemetryEvent(BaseModel):
    """Represents a single telemetry signal ingested by ACE."""

    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)

    source: str = Field(
        ...,
        min_length=1,
        max_length=128,
        description="Originating system emitting the telemetry event",
        examples=["perception-probe"],
    )
    metric: str = Field(
        ...,
        min_length=1,
        max_length=128,
        description="Metric name or identifier",
        examples=["latency_ms"],
    )
    value: float = Field(
        ...,
        description="Numeric measurement associated with the metric",
        examples=[12.3],
    )
    timestamp: datetime = Field(
        ...,
        description="ISO 8601 timestamp when the event was recorded",
        examples=["2025-10-14T00:00:00+00:00"],
    )

    @classmethod
    def json_schema(cls) -> dict[str, Any]:
        """Return the JSON schema for telemetry events."""

        return cls.model_json_schema()


__all__ = ["TelemetryEvent"]
