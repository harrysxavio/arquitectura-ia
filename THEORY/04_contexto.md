# Modulo 4 - Contexto, Memoria y Conocimiento Satelite

## 1. Proposito

Este modulo explica la logica del contexto. La decision concreta de que leer por tipo de tarea vive en `OPERACION/CONTEXT_ROUTER.md`.

La regla principal es simple: el agente no debe leer mas; debe leer mejor.

> [!IMPORTANT]
> La decision concreta de que leer por tipo de tarea vive en `OPERACION/CONTEXT_ROUTER.md`.

## 2. Contexto vs Memoria vs Mapa

| Concepto | Funcion | Ejemplo |
|---|---|---|
| Contexto | Informacion cargada para resolver una tarea puntual | `active_task.md`, archivo afectado, spec puntual |
| Memoria | Informacion persistente para no redescubrir lo mismo | `project_facts.md`, `constraints.md`, `known_issues.md` |
| Decision | Registro de una eleccion relevante y su razon | `decisions/decision_log.md` |
| Mapa estructural | Representacion derivada de relaciones del repo | `graphify-out/GRAPH_REPORT.md` |
| Conocimiento satelite | Material externo o humano que ayuda a pensar | Obsidian, NotebookLM |

La memoria no se carga completa por defecto. Se consulta segun tipo, nivel y riesgo.

## 3. Contexto Base

En un proyecto activo, el contexto base es:

1. `PROJECT_GUIDE.md`.
2. `CONTEXT_INDEX.md`.
3. `tasks/current/active_task.md`.

En este repo framework, cuando no se trabaja sobre un proyecto instanciado, el fallback es:

1. `README.md`.
2. `OPERACION/CONTEXT_ROUTER.md`.
3. `PROJECT_TEMPLATE/` solo como molde.

## 4. Niveles de Contexto

| Nivel | Cuando aplica | Que leer |
|---|---|---|
| Nivel 1 | Cambio simple, local y claro | Contexto base + archivo afectado |
| Nivel 2 | Cambio funcional, multiarchivo o riesgo moderado | Nivel 1 + constraint, spec o memoria puntual segun router |
| Nivel 3 | Cambio estructural, ambiguo, transversal o de alto impacto | Contexto base + router + Graphify vigente + docs/decisiones necesarias |

Nivel 3 no es modo normal. Se usa cuando el cambio puede afectar arquitectura, multiples modulos, contratos o decisiones.

## 5. Graphify

> [!NOTE]
> Graphify es contexto estructural persistente y derivado, no fuente canonica.

Ayuda a responder:

- donde esta el nucleo del repo,
- que modulos se relacionan,
- que archivos pueden verse afectados,
- que rutas conviene leer primero,
- donde hay acoplamiento o impacto transversal.

Orden recomendado en tareas estructurales:

1. `PROJECT_GUIDE.md`.
2. `CONTEXT_INDEX.md`.
3. `tasks/current/active_task.md`.
4. `OPERACION/CONTEXT_ROUTER.md`.
5. `graphify-out/GRAPH_REPORT.md` o `graphify-out/graph.json` si existe y esta vigente.
6. `docs/product/spec.md`.
7. `docs/architecture/sdd.md`.
8. `decisions/decision_log.md`.
9. `memory/constraints.md` y `memory/patterns.md`.
10. Modulos impactados concretos.

Graphify no reemplaza `spec.md`, `sdd.md`, `decision_log.md`, memoria oficial ni `CONTEXT_INDEX.md`.

## 6. Obsidian

Obsidian es una interfaz humana de conocimiento satelite. Puede contener:

- notas personales,
- mapas conceptuales,
- comparativas,
- research transversal,
- visualizaciones exportadas de Graphify,
- hipotesis no aprobadas,
- material de aprendizaje.

No debe contener como autoridad:

- tarea activa oficial,
- decisiones oficiales,
- memoria oficial,
- restricciones oficiales,
- documentacion tecnica que el agente deba obedecer,
- reglas de operacion.

Si una nota de Obsidian se vuelve decision, restriccion, patron o hecho vigente, debe volver al repo en la fuente canonica correspondiente.

## 7. NotebookLM

NotebookLM sirve para research sobre fuentes externas: PDFs, documentacion de terceros, papers, links y material largo.

Flujo correcto:

1. Definir preguntas de investigacion.
2. Cargar fuentes externas.
3. Generar sintesis accionable.
4. Volver al repo con artefacto comprimido.
5. Registrar decisiones o restricciones si cambia el proyecto.

NotebookLM no es memoria viva del repo y no reemplaza `decision_log.md`, `project_facts.md`, `spec.md` ni `sdd.md`.

## 8. Jerarquia Conceptual

| Si hay conflicto entre... | Gana... |
|---|---|
| Graphify y spec | `docs/product/spec.md` |
| Graphify y SDD | `docs/architecture/sdd.md` |
| Graphify y decision | `decisions/decision_log.md` |
| Obsidian y repo | Repo canonico |
| NotebookLM y decision aprobada | Decision aprobada |
| `THEORY/` y `OPERACION/` | `OPERACION/` para runtime |
| `PROJECT_TEMPLATE/` y proyecto activo | Proyecto activo |

## 9. Regla Final

El contexto correcto es pequeno, vigente y autorizado. Todo lo demas es apoyo, no gobierno.
