# CONTEXT_INDEX.md

> Mapa de fuentes oficiales de `SAMPLE_PROJECT/`.

| Necesidad | Archivo | Uso |
|---|---|---|
| Onboarding | `README.md` | Entrada rapida para humanos. |
| Identidad y alcance | `PROJECT_GUIDE.md` | Que es y que no es el ejemplo. |
| Reglas locales de agentes | `AGENTS.md` | Como operar agentes dentro del sample. |
| Verdad funcional | `openspec/specs/support-requests/spec.md` | Comportamiento aprobado del flujo de solicitudes. |
| Cambio activo | `openspec/changes/add-security-priority/proposal.md` | Intencion y alcance del cambio ejemplo. |
| Diseno del cambio | `openspec/changes/add-security-priority/design.md` | Diseno tecnico del cambio ejemplo. |
| Tareas del cambio | `openspec/changes/add-security-priority/tasks.md` | Checklist ejecutable. |
| Arquitectura estable | `docs/architecture/system.md` | CLI, modulos, datos y tests. |
| Decisiones | `decisions/decision_log.md` | Indice breve de decisiones. |
| ADRs | `decisions/adr/*.md` | Decisiones estructurales. |
| Hechos | `memory/facts.md` | Hechos confirmados y problemas vigentes. |
| Restricciones | `memory/constraints.md` | Limites actuales. |
| Patrones | `memory/patterns.md` | Patrones y anti-patrones aprobados. |
| Glosario | `memory/glossary.md` | Terminos del dominio. |
| CLI | `app.py` | Demo y comandos ejecutables. |
| Codigo | `src/*.py` | Implementacion. |
| Tests | `tests/*.py` | Validacion automatizada. |
| Datos runtime | `data/requests.json` | Datos locales de ejecucion, no canonicos. |
| Graphify | `graphify-out/GRAPH_REPORT.md` | Contexto derivado, no canonico. |
| Guia de validacion | `VALIDATION_GUIDE.md` | Como validar el ejemplo y el valor de Graphify. |

## Regla

Para comportamiento, empezar por OpenSpec. Para trabajo en curso, abrir el change activo. Usar Graphify solo para orientar navegacion e impacto.
