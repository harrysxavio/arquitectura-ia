"""Data models for the support desk example."""

from __future__ import annotations

from dataclasses import dataclass

from .enums import Priority, RequestStatus, RequestType


@dataclass
class SupportRequest:
    id: str
    title: str
    description: str
    area: str
    request_type: RequestType
    priority: Priority
    status: RequestStatus
    created_at: str
    updated_at: str
    owner: str | None = None
    closing_note: str | None = None
    priority_reason: str | None = None
    block_reason: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "SupportRequest":
        return cls(
            id=str(data["id"]),
            title=str(data["title"]),
            description=str(data["description"]),
            area=str(data["area"]),
            request_type=RequestType.from_value(str(data["request_type"])),
            priority=Priority.from_value(str(data["priority"])),
            status=RequestStatus.from_value(str(data["status"])),
            created_at=str(data["created_at"]),
            updated_at=str(data["updated_at"]),
            owner=data.get("owner"),
            closing_note=data.get("closing_note"),
            priority_reason=data.get("priority_reason"),
            block_reason=data.get("block_reason"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "area": self.area,
            "request_type": self.request_type.value,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "owner": self.owner,
            "closing_note": self.closing_note,
            "priority_reason": self.priority_reason,
            "block_reason": self.block_reason,
        }
