"""Triage rules aligned with OpenSpec support request behavior."""

from __future__ import annotations

from .enums import Priority, RequestStatus, RequestType


def initial_priority(request_type: RequestType) -> Priority:
    if request_type == RequestType.SEGURIDAD:
        return Priority.ALTA
    if request_type == RequestType.OTRO:
        return Priority.BAJA
    return Priority.MEDIA


def next_status_for_owner(owner: str | None) -> RequestStatus:
    return RequestStatus.ASIGNADA if owner else RequestStatus.EN_TRIAGE
