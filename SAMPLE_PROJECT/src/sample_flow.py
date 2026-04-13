"""Small illustrative flow for SAMPLE_PROJECT.

This module is not a production implementation. The canonical functional
rules live in docs/product/spec.md.
"""

from dataclasses import dataclass


@dataclass
class SupportRequest:
    title: str
    request_type: str
    priority: str = "media"
    status: str = "nueva"
    owner: str | None = None
    closing_note: str | None = None


def triage(request: SupportRequest, owner: str | None = None) -> SupportRequest:
    """Apply the smallest illustrative triage rule from the spec."""
    if request.request_type == "seguridad":
        request.priority = "alta"

    request.status = "asignada" if owner else "en triage"
    request.owner = owner
    return request


def close_request(request: SupportRequest, note: str) -> SupportRequest:
    if not note.strip():
        raise ValueError("closing_note is required")

    request.status = "cerrada"
    request.closing_note = note
    return request

