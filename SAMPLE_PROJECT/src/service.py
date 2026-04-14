"""Application service for support desk requests."""

from __future__ import annotations

from pathlib import Path

from .enums import Priority, RequestStatus, RequestType
from .models import SupportRequest
from .storage import JsonRequestStore
from .triage import initial_priority, next_status_for_owner
from .utils import make_request_id, now_utc, require_text


class RequestNotFoundError(ValueError):
    """Raised when a request id is not present in storage."""


class SupportDeskService:
    def __init__(self, store: JsonRequestStore):
        self.store = store

    @classmethod
    def from_path(cls, path: Path) -> "SupportDeskService":
        return cls(JsonRequestStore(path))

    def create_request(
        self,
        title: str,
        description: str,
        area: str,
        request_type: str | RequestType,
        owner: str | None = None,
        priority: str | Priority | None = None,
        priority_reason: str | None = None,
    ) -> SupportRequest:
        clean_title = require_text(title, "title")
        clean_description = require_text(description, "description")
        clean_area = require_text(area, "area")
        clean_owner = owner.strip() if owner and owner.strip() else None

        parsed_type = (
            request_type
            if isinstance(request_type, RequestType)
            else RequestType.from_value(str(request_type))
        )
        suggested_priority = initial_priority(parsed_type)
        parsed_priority = (
            suggested_priority
            if priority is None
            else Priority.from_value(str(priority))
        )
        clean_reason = priority_reason.strip() if priority_reason and priority_reason.strip() else None
        if parsed_priority != suggested_priority and not clean_reason:
            raise ValueError("priority_reason is required when overriding triage priority")

        timestamp = now_utc()
        request = SupportRequest(
            id=make_request_id(),
            title=clean_title,
            description=clean_description,
            area=clean_area,
            request_type=parsed_type,
            priority=parsed_priority,
            status=next_status_for_owner(clean_owner),
            owner=clean_owner,
            priority_reason=clean_reason,
            created_at=timestamp,
            updated_at=timestamp,
        )

        requests = self.store.load()
        requests.append(request)
        self.store.save(requests)
        return request

    def list_requests(self) -> list[SupportRequest]:
        return self.store.load()

    def close_request(self, request_id: str, note: str) -> SupportRequest:
        clean_id = require_text(request_id, "id")
        clean_note = require_text(note, "note")
        requests = self.store.load()

        for index, request in enumerate(requests):
            if request.id == clean_id:
                request.status = RequestStatus.CERRADA
                request.closing_note = clean_note
                request.updated_at = now_utc()
                requests[index] = request
                self.store.save(requests)
                return request

        raise RequestNotFoundError(f"No existe solicitud con id '{clean_id}'")
