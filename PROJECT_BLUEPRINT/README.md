# PROJECT_BLUEPRINT

Guia compacta para adoptar la arquitectura OpenSpec-first en un proyecto real.

## Rol

`PROJECT_BLUEPRINT/` explica como leer y adoptar el modelo. No es plantilla copiable completa y no reemplaza `PROJECT_TEMPLATE/`.

## Ruta

```text
framework -> PROJECT_BLUEPRINT -> PROJECT_TEMPLATE -> SAMPLE_PROJECT -> proyecto activo
```

## Fuentes Principales

- Verdad funcional: `openspec/specs/*/spec.md`
- Cambio activo: `openspec/changes/*`
- Arquitectura estable: `docs/architecture/system.md`
- Decisiones: `decisions/decision_log.md` y ADRs
- Memoria compacta: `memory/facts.md`, `memory/constraints.md`, `memory/patterns.md`
- Contexto derivado: `graphify-out/*`

## Regla

Blueprint orienta; el template moldea; el proyecto activo decide con sus fuentes canonicas.
