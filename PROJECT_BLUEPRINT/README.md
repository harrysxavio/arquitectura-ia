# PROJECT_BLUEPRINT

Guia compacta para adoptar la arquitectura OpenSpec-first en un proyecto real.

## Rol

`PROJECT_BLUEPRINT/` explica como pasar del framework al uso practico. No es una plantilla copiable completa y no reemplaza `PROJECT_TEMPLATE/`.

## Ruta de Adopcion

```text
framework -> PROJECT_BLUEPRINT -> PROJECT_TEMPLATE -> SAMPLE_PROJECT -> proyecto activo
```

- `framework`: define reglas, capas y politica general.
- `PROJECT_BLUEPRINT/`: explica como se reparte la autoridad documental.
- `PROJECT_TEMPLATE/`: entrega el molde reusable para iniciar un proyecto.
- `SAMPLE_PROJECT/`: muestra el molde aplicado en un caso ejecutable.
- `proyecto activo`: adapta la plantilla y se gobierna por sus propias fuentes canonicas.

## Autoridad Documental

| Tipo de informacion | Fuente |
|---|---|
| Comportamiento funcional vigente | `openspec/specs/*/spec.md` |
| Cambio activo | `openspec/changes/*` |
| Arquitectura estable | `docs/architecture/system.md` |
| Decisiones vigentes | `decisions/decision_log.md` y ADRs |
| Memoria compacta | `memory/facts.md`, `memory/constraints.md`, `memory/patterns.md` |
| Navegacion derivada | `graphify-out/*` |

## Graphify

Graphify entra cuando reduce exploracion: incorporacion tecnica, impacto transversal, refactors amplios o tareas ambiguas.

Graphify no entra por defecto en cambios locales, typos, ajustes claros o cuando OpenSpec ya indica exactamente que revisar.

## Regla

Blueprint orienta; la plantilla moldea; el ejemplo demuestra; el proyecto activo decide con sus fuentes canonicas.
