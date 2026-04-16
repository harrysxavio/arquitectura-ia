# Tarea Activa

Esta ruta existe solo como compatibilidad para equipos o herramientas que esperan `tasks/current/`. En el modelo OpenSpec-first, el trabajo activo debe vivir en `openspec/changes/<change-id>/`.

## Uso Recomendado

No usar este archivo como fuente principal. Si se conserva, debe enlazar al cambio OpenSpec activo.

```text
Trabajo activo actual: `openspec/changes/<change-id>/`
```

## Ejemplo Minimo

```markdown
Trabajo activo actual: `openspec/changes/add-request-priority/`

Este archivo no contiene tareas. Consultar `proposal.md`, `design.md` y `tasks.md` dentro del cambio.
```

## Regla Breve

La tarea activa no debe competir con OpenSpec.
