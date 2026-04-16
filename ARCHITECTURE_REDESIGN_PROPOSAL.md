# Architecture Redesign Proposal

> Decision aprobada. Esta es la arquitectura objetivo OpenSpec-first para este repo-framework.

## Diagnostico

La arquitectura anterior era consistente, pero repartia autoridad entre demasiadas fuentes: `tasks/current/*`, `docs/product/spec.md`, `docs/architecture/sdd.md`, `decisions/*`, `memory/*`, `PROJECT_BLUEPRINT/`, `PROJECT_TEMPLATE/`, `SAMPLE_PROJECT/` y reglas globales en `OPERACION/`.

El problema principal era la duplicacion de roles:

| Tema | Antes | Objetivo |
|---|---|---|
| Verdad funcional | `docs/product/spec.md` | `openspec/specs/*/spec.md` |
| Cambio activo | `tasks/current/*` | `openspec/changes/*` |
| Diseno de cambio | `docs/architecture/sdd.md` | `openspec/changes/*/design.md` |
| Arquitectura estable | SDD mezclado | `docs/architecture/system.md` |
| Decisiones | Log y ADRs sin indice claro | `decision_log.md` breve + ADRs para alto impacto |
| Memoria | Cinco archivos estandar | `facts.md`, `constraints.md`, `patterns.md`, `glossary.md` opcional |

## Arquitectura Objetivo

La arquitectura aprobada adopta OpenSpec como centro funcional y de cambio:

- `openspec/specs/*/spec.md` es la verdad funcional vigente.
- `openspec/changes/*/proposal.md` define intencion, alcance y no alcance del cambio activo.
- `openspec/changes/*/design.md` define diseno tecnico del cambio activo cuando aplica.
- `openspec/changes/*/tasks.md` reemplaza el plan/tarea activa legacy.
- `docs/architecture/system.md` describe arquitectura tecnica estable.
- `decisions/decision_log.md` queda como indice corto obligatorio de decisiones aprobadas y vigentes.
- `decisions/adr/*` queda reservado para decisiones estructurales o de alto impacto.
- `memory/` se compacta, pero sigue separada por tipo minimo de conocimiento.
- `graphify-out/*` se mantiene como contexto derivado, nunca como autoridad.

Estructura objetivo de un proyecto activo:

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- openspec/
|   |-- specs/
|   |   `-- <capability>/spec.md
|   |-- changes/
|   |   `-- <change-id>/
|   |       |-- proposal.md
|   |       |-- design.md
|   |       |-- tasks.md
|   |       `-- specs/<capability>/spec.md
|   `-- archive/
|-- docs/
|   `-- architecture/system.md
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

## Decisiones

- Mantener `PROJECT_BLUEPRINT/` durante esta migracion y redefinirlo como guia compacta OpenSpec-first.
- Mantener `decisions/decision_log.md` como indice breve obligatorio.
- Mantener memoria compacta pero separada: `facts.md`, `constraints.md`, `patterns.md`; `glossary.md` solo si aporta al dominio.
- Retirar `tasks/current/*`, `docs/product/spec.md` y `docs/architecture/sdd.md` de las rutas activas.
- Mantener Graphify como derivado: orienta navegacion e impacto, pero no gobierna comportamiento.

## Reglas de Autoridad

| Prioridad | Fuente | Autoridad |
|---|---|---|
| 1 | `AGENTS.md` | Reglas locales de operacion del agente |
| 2 | `openspec/changes/<active>/proposal.md` | Intencion, alcance y no alcance del cambio activo |
| 3 | `openspec/changes/<active>/specs/*/spec.md` | Delta funcional propuesto |
| 4 | `openspec/specs/*/spec.md` | Verdad funcional vigente |
| 5 | `openspec/changes/<active>/design.md` | Diseno tecnico del cambio activo |
| 6 | `docs/architecture/system.md` | Arquitectura tecnica estable |
| 7 | `decisions/decision_log.md` | Indice corto de decisiones aprobadas y vigentes |
| 8 | `decisions/adr/*.md` | Decisiones estructurales o de alto impacto |
| 9 | `memory/constraints.md` | Restricciones vigentes |
| 10 | `memory/facts.md` | Hechos confirmados |
| 11 | `memory/patterns.md` | Patrones aprobados |
| 12 | `graphify-out/*` | Contexto derivado, sin autoridad |

Regla clave: una regla funcional vive en OpenSpec. Otros documentos pueden enlazarla o explicar como navegarla, pero no duplicarla como autoridad paralela.

## Estructura Raiz Objetivo

```text
/
|-- README.md
|-- AGENTS.md
|-- ARCHITECTURE_REDESIGN_PROPOSAL.md
|-- ARCHITECTURE_MIGRATION_PLAN.md
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

`PROJECT_BLUEPRINT/` no se elimina en esta ejecucion. Su retiro solo puede evaluarse despues de validar que `README.md` y `PROJECT_TEMPLATE/README.md` cubren su rol.
