"""Small utilities for the support desk example."""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4


def now_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def make_request_id() -> str:
    return f"req-{uuid4().hex[:8]}"


def require_text(value: str, field_name: str) -> str:
    clean = value.strip()
    if not clean:
        raise ValueError(f"{field_name} is required")
    return clean
