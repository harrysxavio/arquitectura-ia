"""Enumerations for the support desk domain."""

from __future__ import annotations

from enum import Enum


class TextEnum(str, Enum):
    """String enum with a compact parser for CLI and JSON inputs."""

    @classmethod
    def from_value(cls, value: str) -> "TextEnum":
        normalized = value.strip().lower()
        for item in cls:
            if item.value == normalized:
                return item
        allowed = ", ".join(item.value for item in cls)
        raise ValueError(f"Valor invalido '{value}'. Valores permitidos: {allowed}")

    def __str__(self) -> str:
        return self.value


class RequestType(TextEnum):
    SOPORTE = "soporte"
    ACCESO = "acceso"
    DATOS = "datos"
    SEGURIDAD = "seguridad"
    OTRO = "otro"


class Priority(TextEnum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"
    CRITICA = "critica"


class RequestStatus(TextEnum):
    NUEVA = "nueva"
    EN_TRIAGE = "en triage"
    ASIGNADA = "asignada"
    BLOQUEADA = "bloqueada"
    CERRADA = "cerrada"
