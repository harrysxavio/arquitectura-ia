# Decision Log

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Registrar decisiones aprobadas de forma cronologica y ligera.

## Como llenarlo

Agregar una fila por decision. Usar ADR cuando la decision requiera contexto, alternativas o impacto amplio.

## Ejemplo minimo

| Fecha | Decision | Motivo | Impacto | Referencia |
|---|---|---|---|---|
| 2026-01-15 | Validar permisos en servicio, no en UI. | Evita bypass desde clientes externos. | Ajusta tests de API. | `decisions/adr/0001-auth-boundary.md` |

## Registro

| Fecha | Decision | Motivo | Impacto | Referencia |
|---|---|---|---|---|
| YYYY-MM-DD |  |  |  |  |

## Detalle Opcional

Usar este bloque solo cuando una decision necesita contexto breve, pero no justifica una ADR completa.

```text
Fecha: YYYY-MM-DD
Decision:
Alternativas consideradas:
Impacto:
Referencia:
```

## Nota de uso

No registrar conversaciones ni ideas descartadas sin decision. Si una decision crea una restriccion vigente, actualizar tambien `memory/constraints.md`.
