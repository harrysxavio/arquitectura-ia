# Arquitectura Transversal para IA

Framework documental para trabajar con agentes de IA con contexto minimo, fuentes de verdad claras y flujo OpenSpec-first.

Principio rector:

> La calidad del resultado no debe depender del modelo. Debe depender del sistema.

## Organizacion

```text
/
|-- README.md
|-- AGENTS.md
|-- OPERACION/
|-- GRAPHIFY/
|-- PROJECT_BLUEPRINT/
|-- PROJECT_TEMPLATE/
|-- SAMPLE_PROJECT/
|-- EXAMPLES/
|-- SATELLITE/
|-- THEORY/
`-- ARCHIVE/
```

## Modelo OpenSpec-First

En proyectos activos, OpenSpec gobierna comportamiento y cambios:

| Necesidad | Fuente |
|---|---|
| Verdad funcional vigente | `openspec/specs/*/spec.md` |
| Cambio activo | `openspec/changes/*/proposal.md` |
| Diseno del cambio | `openspec/changes/*/design.md` |
| Tareas del cambio | `openspec/changes/*/tasks.md` |
| Arquitectura estable | `docs/architecture/system.md` |
| Decisiones vigentes | `decisions/decision_log.md` |
| Memoria compacta | `memory/facts.md`, `memory/constraints.md`, `memory/patterns.md` |
| Contexto derivado | `graphify-out/*` |

## Capas

| Capa | Proposito | Autoridad |
|---|---|---|
| `OPERACION/` | Router, constraints y contratos de agentes. | Si, para ejecucion. |
| `PROJECT_BLUEPRINT/` | Guia compacta para entender y adoptar el modelo. | Si, para estructura recomendada. |
| `PROJECT_TEMPLATE/` | Molde reusable para iniciar proyectos. | Se vuelve canonico al instanciarse. |
| `SAMPLE_PROJECT/` | Laboratorio pedagogico con codigo, OpenSpec y validacion. | No para otros proyectos; si para el ejemplo. |
| `GRAPHIFY/` | Politica de contexto estructural derivado. | Politica si; outputs no. |
| `THEORY/` | Fundamentos conceptuales. | No para runtime. |
| `SATELLITE/` | Politicas para conocimiento externo. | No gobierna el proyecto activo. |
| `ARCHIVE/` | Historia y legacy no canonico. | No. |

## Ruta Recomendada

```text
framework -> blueprint -> template -> sample -> proyecto activo
```

- Usa `PROJECT_BLUEPRINT/` para entender la arquitectura.
- Usa `PROJECT_TEMPLATE/` para iniciar un proyecto real.
- Usa `SAMPLE_PROJECT/` para ver un ejemplo completo, ejecutable y validable.
- En un proyecto activo, empieza por `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y la fuente OpenSpec relevante.

## Documentacion Interna

Los documentos `ARCHITECTURE_REDESIGN_PROPOSAL.md` y `ARCHITECTURE_MIGRATION_PLAN.md` son historial interno de decision y migracion. No forman parte del mapa principal de uso diario.

## Regla Final

Leer menos, pero leer mejor. Una regla funcional vive en OpenSpec; los demas documentos enlazan, orientan o explican sin duplicar autoridad.
