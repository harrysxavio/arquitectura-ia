"""JSON storage for the runtime example data."""

from __future__ import annotations

import json
from pathlib import Path

from .models import SupportRequest


class JsonRequestStore:
    def __init__(self, path: Path):
        self.path = path

    def load(self) -> list[SupportRequest]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as file:
            raw = json.load(file)
        if not isinstance(raw, list):
            raise ValueError(f"{self.path} debe contener una lista JSON")
        return [SupportRequest.from_dict(item) for item in raw]

    def save(self, requests: list[SupportRequest]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [request.to_dict() for request in requests]
        temp_path = self.path.with_suffix(f"{self.path.suffix}.tmp")
        with temp_path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2, ensure_ascii=True)
            file.write("\n")
        temp_path.replace(self.path)
