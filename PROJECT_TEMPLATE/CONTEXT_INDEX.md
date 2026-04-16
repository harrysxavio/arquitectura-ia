# CONTEXT_INDEX.md

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Fuentes Oficiales

| Necesidad | Archivo | Uso |
|---|---|---|
| Identidad y alcance | `PROJECT_GUIDE.md` | Entrada base del proyecto. |
| Reglas locales de agentes | `AGENTS.md` | Guia de agentes especifica del proyecto. |
| Verdad funcional vigente | `openspec/specs/*/spec.md` | Comportamiento aprobado. |
| Cambio activo | `openspec/changes/<change-id>/proposal.md` | Intencion, alcance y no alcance. |
| Diseno del cambio | `openspec/changes/<change-id>/design.md` | Diseno tecnico del cambio. |
| Tareas del cambio | `openspec/changes/<change-id>/tasks.md` | Checklist ejecutable. |
| Arquitectura estable | `docs/architecture/system.md` | Componentes, contratos y datos estables. |
| Decisiones | `decisions/decision_log.md` | Indice breve de decisiones aprobadas. |
| ADRs | `decisions/adr/*.md` | Decisiones estructurales o de alto impacto. |
| Hechos | `memory/facts.md` | Contexto confirmado. |
| Restricciones | `memory/constraints.md` | Limites vigentes. |
| Patrones | `memory/patterns.md` | Formas aprobadas de trabajar. |
| Glosario | `memory/glossary.md` | Terminos opcionales del dominio. |
| Graphify | `graphify-out/GRAPH_REPORT.md` | Contexto derivado, no canonico. |

## Regla

El comportamiento funcional empieza en OpenSpec. Graphify ayuda a navegar, pero nunca reemplaza fuentes canonicas.
