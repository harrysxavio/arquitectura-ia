# Documentos de un Proyecto OpenSpec-First

## Documentos Base

| Documento | Rol | Cuando se consulta |
|---|---|---|
| `PROJECT_GUIDE.md` | Identidad, alcance y estructura. | Al iniciar o entender el proyecto. |
| `CONTEXT_INDEX.md` | Mapa de fuentes oficiales. | Antes de escalar lectura. |
| `AGENTS.md` | Reglas locales de agentes. | Al operar con agentes. |
| `openspec/specs/*/spec.md` | Verdad funcional vigente. | En cambios de comportamiento. |
| `openspec/changes/*/proposal.md` | Intencion y alcance del cambio. | En trabajo activo. |
| `openspec/changes/*/design.md` | Diseno tecnico del cambio. | Si afecta arquitectura, datos o contratos. |
| `openspec/changes/*/tasks.md` | Checklist de ejecucion. | Durante implementacion y validacion. |
| `docs/architecture/system.md` | Arquitectura estable. | En cambios estructurales o onboarding tecnico. |
| `decisions/decision_log.md` | Indice breve de decisiones. | Para entender decisiones vigentes. |
| `decisions/adr/*.md` | Decisiones de alto impacto. | Cuando una decision necesita contexto y tradeoffs. |
| `memory/facts.md` | Hechos confirmados. | Para no redescubrir contexto. |
| `memory/constraints.md` | Restricciones vigentes. | Antes de decidir o ampliar alcance. |
| `memory/patterns.md` | Patrones aprobados. | Al implementar o revisar consistencia. |
| `graphify-out/*` | Contexto derivado. | Para navegacion e impacto, no para autoridad. |

## Relacion

OpenSpec gobierna comportamiento y cambios. Arquitectura estable explica el sistema. Decisiones y memoria comprimen contexto duradero. Graphify ayuda a navegar.
