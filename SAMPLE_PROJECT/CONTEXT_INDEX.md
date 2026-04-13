# CONTEXT_INDEX.md

> Ejemplo rellenado. Mapea fuentes oficiales para cargar solo el contexto necesario.

## Proposito

Indicar que documento consultar segun la necesidad de trabajo dentro de la Mesa Interna de Soporte Operativo.

## Fuentes Oficiales

| Necesidad | Archivo | Uso |
|---|---|---|
| Onboarding del ejemplo | `README.md` | Guia paso a paso para principiantes. |
| Identidad del proyecto | `PROJECT_GUIDE.md` | Entrada base del proyecto y alcance. |
| Reglas locales de agentes | `AGENTS.md` | Ajustes locales sin reemplazar `OPERACION/AGENTS/*.md`. |
| Tarea actual | `tasks/current/active_task.md` | Alcance y estado del trabajo activo. |
| Plan actual | `tasks/current/implementation_plan.md` | Secuencia de ejecucion de la tarea activa. |
| Preguntas abiertas | `tasks/current/open_questions.md` | Dudas que bloquean o cambian alcance. |
| Decisiones | `decisions/decision_log.md` | Decisiones aprobadas y su impacto. |
| ADRs | `decisions/adr/*.md` | Decisiones arquitectonicas extensas. |
| Hechos vigentes | `memory/project_facts.md` | Datos confirmados del proyecto. |
| Restricciones | `memory/constraints.md` | Limites tecnicos, negocio, seguridad y costo. |
| Problemas conocidos | `memory/known_issues.md` | Bugs, deuda o workarounds vigentes. |
| Patrones aprobados | `memory/patterns.md` | Formas aceptadas de implementar y documentar. |
| Glosario | `memory/glossary.md` | Terminos del dominio de soporte operativo. |
| Spec funcional | `docs/product/spec.md` | Verdad funcional del flujo de solicitudes. |
| Diseno tecnico | `docs/architecture/sdd.md` | Diseno tecnico e integracion con codigo ilustrativo. |
| Graphify | `graphify-out/GRAPH_REPORT.md` | Contexto estructural derivado y pedagogico. No canonico. |
| Codigo ilustrativo | `src/README.md` | Explica el alcance opcional de `src/`. |

## Nota de uso

Para tareas simples, empezar por `PROJECT_GUIDE.md`, este indice y `tasks/current/active_task.md`. Escalar a `spec.md`, `sdd.md`, decisiones, memoria o Graphify solo cuando la tarea lo justifique.

Graphify orienta navegacion, pero no reemplaza spec, SDD, decision log ni memoria canonica.

