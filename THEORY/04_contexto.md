# Modulo 4 - Contexto, Memoria y Conocimiento Satelite

Este modulo explica la logica del sistema. No es una matriz de runtime. La decision concreta de que leer vive en `OPERACION/CONTEXT_ROUTER.md`.

## 1. Principio del Contexto

El contexto no debe ser abundante. Debe ser preciso.

Un agente trabaja mejor cuando recibe:

- una tarea clara,
- fuentes de verdad bien separadas,
- documentos pequenos y relevantes,
- memoria canonica,
- y un mapa estructural cuando la tarea lo necesita.

## 2. Contexto vs Memoria

| Concepto | Definicion | Ejemplo |
|---|---|---|
| Contexto | Informacion cargada para resolver una tarea puntual | `active_task.md`, archivo afectado, spec puntual |
| Memoria | Informacion persistente para no redescubrir lo mismo | `decision_log.md`, `project_facts.md`, `patterns.md` |
| Mapa estructural | Representacion derivada de relaciones del repo | `graphify-out/GRAPH_REPORT.md` |

La memoria no se carga completa siempre. Se consulta por necesidad.

## 3. Tres Niveles

- Nivel 1: contexto minimo para tareas simples y locales.
- Nivel 2: contexto dirigido para cambios funcionales o multiarchivo.
- Nivel 3: contexto estructural para arquitectura, ambiguedad o impacto transversal.

En Nivel 3, Graphify debe entrar temprano para orientar la navegacion antes de leer mucha documentacion o muchos modulos.

## 4. Graphify

Graphify es la capa central de contexto estructural persistente del framework.

Su valor es ayudar a responder:

- donde esta el nucleo del repo,
- que modulos estan relacionados,
- que archivos pueden verse afectados por un cambio,
- que rutas conviene leer primero,
- donde hay acoplamiento o impacto transversal.

Graphify no reemplaza documentos canonicos. Si el grafo contradice `spec.md`, `sdd.md`, `decision_log.md` o memoria oficial, gana el documento canonico.

## 5. Obsidian

Obsidian es una interfaz humana de conocimiento satelite.

Puede contener:

- notas personales,
- mapas conceptuales,
- comparativas,
- research transversal,
- visualizaciones exportadas de Graphify,
- conexiones entre ideas.

No debe contener:

- tarea activa oficial,
- decisiones oficiales,
- memoria oficial,
- documentacion tecnica que el agente deba obedecer,
- reglas de operacion.

## 6. NotebookLM

NotebookLM sirve para research sobre fuentes externas. El resultado util debe comprimirse y volver al repo como documento canonico o derivado, segun corresponda.

## 7. Fuente de Verdad

| Tipo | Fuente |
|---|---|
| Trabajo actual | `tasks/current/active_task.md` |
| Decisiones | `decisions/decision_log.md` |
| Hechos vigentes | `memory/project_facts.md` |
| Restricciones | `memory/constraints.md` |
| Diseno tecnico | `docs/architecture/sdd.md` |
| Verdad funcional | `docs/product/spec.md` |
| Mapa estructural derivado | `graphify-out/*` |
| Explicacion del framework | `THEORY/*.md` |

## 8. Cierre

La meta no es que el agente lea mas. La meta es que el agente lea lo correcto, en el orden correcto, con autoridad documental clara.
