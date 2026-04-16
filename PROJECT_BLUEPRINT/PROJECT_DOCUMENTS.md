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
| `openspec/changes/*/tasks.md` | Lista de ejecucion. | Durante implementacion y validacion. |
| `docs/architecture/system.md` | Arquitectura estable. | En cambios estructurales o incorporacion tecnica. |
| `decisions/decision_log.md` | Indice breve de decisiones. | Para entender decisiones vigentes. |
| `decisions/adr/*.md` | Decisiones de alto impacto. | Cuando una decision necesita contexto y compensaciones explicitas. |
| `memory/facts.md` | Hechos confirmados. | Para no redescubrir contexto. |
| `memory/constraints.md` | Restricciones vigentes. | Antes de decidir o ampliar alcance. |
| `memory/patterns.md` | Patrones aprobados. | Al implementar o revisar consistencia. |
| `memory/glossary.md` | Terminos del dominio. | Solo si evita ambiguedad real. |
| `graphify-out/*` | Contexto derivado. | Para navegacion e impacto, no para autoridad. |

## Reparto de Autoridad

OpenSpec responde que debe hacer el sistema y que cambio se esta proponiendo.

`docs/architecture/system.md` responde como esta construido de forma estable.

`decisions/` responde por que se aprobo una direccion vigente.

`memory/` responde que hechos, restricciones y patrones conviene recordar sin releer todo.

`graphify-out/` responde donde mirar, no que decidir.

## Regla de No Duplicacion

Si una regla funcional vive en OpenSpec, otros documentos pueden enlazarla o resumir su impacto, pero no competir como fuente principal.
