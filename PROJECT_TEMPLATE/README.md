# PROJECT_TEMPLATE

Molde reusable para crear un proyecto con arquitectura OpenSpec-first.

## Estructura

```text
PROJECT_TEMPLATE/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- openspec/
|   |-- specs/example-capability/spec.md
|   |-- changes/.gitkeep
|   `-- archive/.gitkeep
|-- docs/architecture/system.md
|-- decisions/decision_log.md
|-- decisions/adr/ADR_TEMPLATE.md
|-- memory/facts.md
|-- memory/constraints.md
|-- memory/patterns.md
|-- memory/glossary.md
`-- graphify-out/
```

## Uso

1. Copiar o adaptar el template en un proyecto real.
2. Completar `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
3. Crear specs por capability en `openspec/specs/`.
4. Usar `openspec/changes/` para cambios activos.
5. Mantener memoria compacta y Graphify derivado.
