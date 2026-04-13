# ADR: Titulo de la decision

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Documentar una decision arquitectonica que necesita mas contexto que una fila del `decision_log.md`.

## Como llenarlo

Usar cuando la decision afecta estructura, contratos, datos, integraciones, seguridad o costos. Mantener una ADR por decision principal.

## Ejemplo minimo

```text
Decision: Usar PostgreSQL como base principal.
Motivo: Necesitamos integridad relacional y consultas transaccionales.
Impacto: Los reportes analiticos se resolveran fuera del flujo transaccional.
```

## Estado

`propuesta | aceptada | reemplazada | descartada`

## Contexto

## Decision

## Alternativas consideradas

-

## Consecuencias

## Referencias

## Nota de uso

Si esta ADR reemplaza otra decision, enlazar la decision anterior y actualizar `decisions/decision_log.md`.
