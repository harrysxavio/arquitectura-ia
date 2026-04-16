# ADR 0001 - Documentacion de triage Markdown-first

## Estado

Aceptada, actualizada para arquitectura OpenSpec-first.

## Contexto

El ejemplo necesita reglas visibles y versionadas antes de automatizar. Las reglas funcionales aprobadas ahora viven en OpenSpec. La CLI sigue siendo una implementacion de esas reglas, no la autoridad.

## Decision

Usar OpenSpec como fuente funcional y mantener arquitectura tecnica estable en `docs/architecture/system.md`. Mantener la CLI pequena y pedagogica.

## Consecuencias

- Los cambios funcionales empiezan en `openspec/changes/*`.
- El comportamiento aprobado se archiva en `openspec/specs/*`.
- Codigo y tests deben trazar hacia OpenSpec.
- JSON de ejecucion y salida de Graphify no son canonicos.
