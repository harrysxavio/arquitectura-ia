# Estructura Ejemplo de Proyecto OpenSpec-First

## Estructura Minima

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- openspec/
|   |-- specs/<capability>/spec.md
|   `-- changes/
|-- docs/architecture/system.md
|-- decisions/decision_log.md
`-- memory/
    |-- facts.md
    |-- constraints.md
    `-- patterns.md
```

Esta estructura basta para operar con una fuente funcional clara, cambios trazables y memoria compacta.

## Estructura Estandar

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- openspec/
|   |-- specs/<capability>/spec.md
|   |-- changes/<change-id>/
|   |   |-- proposal.md
|   |   |-- design.md
|   |   |-- tasks.md
|   |   `-- specs/<capability>/spec.md
|   `-- archive/
|-- docs/architecture/system.md
|-- decisions/
|   |-- decision_log.md
|   `-- adr/
|-- memory/
|   |-- facts.md
|   |-- constraints.md
|   |-- patterns.md
|   `-- glossary.md
`-- graphify-out/
```

## Flujo de Adopcion

1. Completar `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
2. Crear specs por capability en `openspec/specs/`.
3. Crear changes para trabajo activo en `openspec/changes/`.
4. Mantener arquitectura estable en `docs/architecture/system.md`.
5. Registrar decisiones breves y usar ADRs solo cuando aporten.
6. Mantener memoria breve y separada.
7. Consultar Graphify solo si reduce exploracion o aclara impacto.

## Cuando Usar Graphify

Usarlo para onboarding tecnico, impacto multiarchivo, refactors y tareas ambiguas.

No usarlo como paso obligatorio en cambios locales, ajustes triviales o cuando el archivo afectado ya esta claro.
