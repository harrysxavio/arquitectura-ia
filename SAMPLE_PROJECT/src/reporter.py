"""Formatting helpers for CLI output."""

from __future__ import annotations

from .models import SupportRequest


def format_request(request: SupportRequest) -> str:
    owner = request.owner or "-"
    closing_note = request.closing_note or "-"
    return (
        f"id: {request.id}\n"
        f"title: {request.title}\n"
        f"area: {request.area}\n"
        f"type: {request.request_type.value}\n"
        f"priority: {request.priority.value}\n"
        f"status: {request.status.value}\n"
        f"owner: {owner}\n"
        f"closing_note: {closing_note}"
    )


def format_request_list(requests: list[SupportRequest]) -> str:
    if not requests:
        return "No hay solicitudes registradas."

    rows = [
        (
            request.id,
            request.title,
            request.area,
            request.request_type.value,
            request.priority.value,
            request.status.value,
            request.owner or "-",
        )
        for request in requests
    ]
    headers = ("id", "titulo", "area", "tipo", "prioridad", "estado", "owner")
    widths = [
        max(len(str(row[index])) for row in rows + [headers])
        for index in range(len(headers))
    ]

    def render(row: tuple[str, ...]) -> str:
        return " | ".join(str(value).ljust(widths[index]) for index, value in enumerate(row))

    separator = tuple("-" * width for width in widths)
    return "\n".join([render(headers), render(separator)] + [render(row) for row in rows])
