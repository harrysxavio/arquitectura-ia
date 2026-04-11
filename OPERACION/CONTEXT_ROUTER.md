# CONTEXT_ROUTER.md - Matriz Operativa de Contexto

Este archivo es la autoridad unica para decidir que contexto debe cargar un agente segun tipo y complejidad de tarea.

No explica la filosofia del sistema. No define agentes. No reemplaza constraints. Su funcion es enrutar lectura.

## 1. Protocolo Base

1. Identificar la tarea.
2. Clasificar tipo: `bug`, `feature`, `refactor`, `arquitectura`, `review`, `testing`, `deploy`, `research`, `docs`, `memoria`.
3. Clasificar complejidad: Nivel 1, Nivel 2 o Nivel 3.
4. Cargar solo el contexto indicado.
5. Si falta un documento canonico obligatorio, solicitarlo o instanciarlo desde `PROJECT_TEMPLATE/`.
6. Si hay conflicto documental, obedecer la jerarquia de fuentes.

Regla: prohibido cargar el repo completo por defecto.

## 2. Contexto Base del Proyecto Activo

| Prioridad | Archivo | Uso |
|---|---|---|
| 1 | `PROJECT_GUIDE.md` | Identidad, alcance y estructura del proyecto |
| 2 | `CONTEXT_INDEX.md` | Mapa de fuentes oficiales |
| 3 | `tasks/current/active_task.md` | Trabajo actual, alcance y no alcance |

Fallback cuando se esta trabajando en este framework, no en un proyecto instanciado:

| Prioridad | Archivo | Uso |
|---|---|---|
| 1 | `README.md` | Entrada humana del framework |
| 2 | `OPERACION/CONTEXT_ROUTER.md` | Router de contexto |
| 3 | `PROJECT_TEMPLATE/` | Molde estructural, no verdad operativa |

## 3. Niveles de Contexto

| Nivel | Criterio | Contexto obligatorio | Regla |
|---|---|---|---|
| 1 | Cambio simple, local y claro | Contexto base + archivo afectado | No exigir `spec.md`, Graphify ni SDD |
| 2 | Cambio funcional, varios archivos o riesgo moderado | Nivel 1 + constraint relevante + `docs/product/spec.md` si aplica | Graphify solo si hay incertidumbre de navegacion o varios modulos |
| 3 | Cambio estructural, ambiguo, transversal o de alto impacto | Contexto base + este router + Graphify vigente + docs/decisiones necesarias | Graphify entra antes de exploracion amplia |

## 4. Politica de Graphify en el Router

Graphify se consulta como mapa estructural derivado, no como fuente de verdad.

Ruta para tareas estructurales o ambiguas:

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`
4. `OPERACION/CONTEXT_ROUTER.md`
5. `graphify-out/GRAPH_REPORT.md` o `graphify-out/graph.json`, si existe y esta vigente
6. `docs/product/spec.md`
7. `docs/architecture/sdd.md`
8. `decisions/decision_log.md`
9. `memory/constraints.md` y `memory/patterns.md`
10. Modulos impactados concretos

Graphify entra antes de leer documentacion amplia o explorar modulos completos. No entra antes del contexto base y no reemplaza documentos canonicos.

## 5. Matriz por Tipo de Tarea

| Tipo | Nivel 1 | Nivel 2 | Nivel 3 |
|---|---|---|---|
| `bug` | Contexto base + archivo/log puntual | Nivel 1 + `memory/known_issues.md` + `OPERACION/CONSTRAINTS/agent_rules.md` | Nivel 2 + Graphify si el bug cruza modulos + decision relevante |
| `feature` | Contexto base + archivo local | Nivel 1 + `docs/product/spec.md` + `OPERACION/CONSTRAINTS/process_constraints.md` | Nivel 2 + Graphify + `docs/architecture/sdd.md` + decisiones relevantes |
| `refactor` | Solo si es local y sin cambio de contrato | Contexto base + `docs/architecture/sdd.md` + `architecture_rules.md` | Contexto base + router + Graphify + SDD + decision log + modulos impactados |
| `arquitectura` | No permitido | Solo si es analisis acotado | Contexto base + router + Graphify + SDD + decision log + constraints |
| `review` | Diff + tarea activa | Nivel 1 + spec si hay cambio funcional | Nivel 2 + Graphify si hay impacto multi-modulo + SDD + decision log |
| `testing` | Test puntual + implementacion bajo prueba | Nivel 1 + spec si valida negocio | Nivel 2 + Graphify solo si el test cubre flujo transversal |
| `deploy` | Instruccion local puntual | Nivel 1 + docs operativas + `tooling_rules.md` | Nivel 2 + decisiones + restricciones + runbook |
| `research` | Objetivo + fuente puntual | Nivel 1 + artefacto comprimido si existe | Nivel 2 + Graphify si el research es interno del repo |
| `docs` | Documento objetivo + fuente oficial | Nivel 1 + decision/spec relacionada | Nivel 2 + Graphify si reorganiza docs o arquitectura |
| `memoria` | Archivo de memoria objetivo + fuente puntual | Nivel 1 + decision log si aplica | Nivel 2 + Graphify si resume estructura transversal |

## 6. Jerarquia de Fuentes

| Prioridad | Fuente | Autoridad |
|---|---|---|
| 1 | `OPERACION/CONSTRAINTS/*.md` | Reglas ejecutables |
| 2 | `decisions/decision_log.md` | Decisiones aprobadas |
| 3 | `memory/constraints.md` | Restricciones vigentes |
| 4 | `memory/project_facts.md` | Hechos vigentes |
| 5 | `tasks/current/active_task.md` | Alcance actual |
| 6 | `docs/product/spec.md` | Verdad funcional |
| 7 | `docs/architecture/sdd.md` | Diseno tecnico |
| 8 | `OPERACION/AGENTS/*.md` | Rol y limites del agente |
| 9 | `graphify-out/*` | Contexto estructural derivado |
| 10 | `PROJECT_TEMPLATE/` y `TEMPLATES/` | Formato, no verdad |
| 11 | `THEORY/*.md` | Explicacion humana |

## 7. Prohibiciones

- No cargar `THEORY/*` durante ejecucion tecnica rutinaria.
- No cargar todo `docs/`, toda `memory/` ni todo `decisions/` por si acaso.
- No usar Graphify para sustituir spec, SDD, decision log o memoria canonica.
- No exigir `spec.md` para tareas Nivel 1.
- No operar en Nivel 3 como modo normal.

## 8. Regla Final

El objetivo es leer menos, pero mejor.
