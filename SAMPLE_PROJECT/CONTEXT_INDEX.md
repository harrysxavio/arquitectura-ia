# CONTEXT_INDEX.md

> Ejemplo rellenado. Mapea fuentes oficiales para cargar solo el contexto necesario.

## Proposito

Indicar que documento consultar segun la necesidad de trabajo dentro de la Mesa Interna de Soporte Operativo funcional y pedagogica.

## Fuentes Oficiales

| Necesidad | Archivo | Uso |
|---|---|---|
| Onboarding del ejemplo | `README.md` | Guia paso a paso para principiantes. |
| Identidad del proyecto | `PROJECT_GUIDE.md` | Entrada base del proyecto y alcance. |
| Reglas locales de agentes | `AGENTS.md` | Ajustes locales sin reemplazar `OPERACION/AGENTS/*.md`. |
| Validacion del ejemplo | `VALIDATION_GUIDE.md` | Pruebas funcionales, documentales y comparativa con Graphify. |
| Validacion arquitectonica | `ARCHITECTURE_VALIDATION.md` | Prueba del sistema completo: contexto, docs, memoria, decisiones y Graphify. |
| Escenarios de chat | `CHAT_SCENARIOS.md` | Prompts y trazas para comparar rutas con y sin Graphify. |
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
| Diseno tecnico | `docs/architecture/sdd.md` | Diseno tecnico e integracion con la mini app. |
| App CLI | `app.py` | Punto de entrada ejecutable para demo, create, list y close. |
| Codigo funcional | `src/*.py` | Automatizacion minima alineada con spec y SDD. |
| Tests | `tests/*.py` | Validacion basica de triage, servicio y storage. |
| Datos runtime | `data/requests.json` | Persistencia local del ejemplo. No canonica. |
| Graphify | `graphify-out/GRAPH_REPORT.md` | Contexto estructural derivado. No canonico. |

## Nota de uso

Para tareas simples, empezar por `PROJECT_GUIDE.md`, este indice y `tasks/current/active_task.md`. Escalar a `spec.md`, `sdd.md`, decisiones, memoria, codigo o Graphify solo cuando la tarea lo justifique.

Graphify orienta navegacion, pero no reemplaza spec, SDD, decision log ni memoria canonica. `data/requests.json` tampoco es canonico: solo refleja datos runtime del ejemplo.

`VALIDATION_GUIDE.md`, `ARCHITECTURE_VALIDATION.md` y `CHAT_SCENARIOS.md` son guias pedagogicas del laboratorio `SAMPLE_PROJECT/`; no son requisitos obligatorios de `PROJECT_TEMPLATE/`.
