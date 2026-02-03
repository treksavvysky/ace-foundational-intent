"""Configuration settings for the ACE Telemetry Ingest Service."""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_prefix="ACE_",
        case_sensitive=False,
    )

    service_name: str = "ace-telemetry-ingest"
    service_port: int = 8000
    log_level: str = "INFO"
    schema_version: str = "0.1.0"


settings = Settings()

__all__ = ["Settings", "settings"]
