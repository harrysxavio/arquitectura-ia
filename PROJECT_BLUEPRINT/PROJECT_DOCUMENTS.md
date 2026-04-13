# Documentos de un Proyecto Instanciado

> Blueprint estructural. Este documento explica la anatomia documental recomendada para un proyecto real que adopta el framework.

## Proposito

Definir que documentos debe tener un proyecto instanciado, donde viven, que autoridad tienen, cuando se consultan y cuando pasan a ser canonicos.

Este documento no es teoria general y no es una plantilla copiable. La teoria vive en `THEORY/`; los archivos copiables viven en `PROJECT_TEMPLATE/`.

> [!NOTE]
> El `AGENTS.md` descrito abajo corresponde a la raiz de un proyecto instanciado. El `AGENTS.md` de la raiz de este repo-framework es una instruccion local de tooling para Codex/Graphify y no reemplaza `OPERACION/AGENTS/*.md` ni `PROJECT_TEMPLATE/AGENTS.md`.

## Documentos base

| Documento | Ubicacion | Rol | Se consulta cuando | Canonico cuando |
|---|---|---|---|---|
| `PROJECT_GUIDE.md` | raiz del proyecto | Identidad, alcance, stack y estructura principal. | Al iniciar una tarea o entender el proyecto. | Esta completo y aprobado dentro del proyecto real. |
| `CONTEXT_INDEX.md` | raiz del proyecto | Mapa de fuentes oficiales. | Antes de escalar lectura documental. | Lista solo documentos usados y vigentes. |
| `AGENTS.md` | raiz del proyecto | Adaptacion local de los roles de agente. | Al configurar o revisar reglas de agentes del proyecto. | No contradice `OPERACION/AGENTS/`. |
| `tasks/current/active_task.md` | `tasks/current/` | Trabajo actual, alcance y contexto cargado. | En cualquier ejecucion activa. | Representa la tarea real en curso. |
| `tasks/current/implementation_plan.md` | `tasks/current/` | Plan de ejecucion para tareas que lo requieren. | En cambios multiarchivo o de riesgo medio/alto. | El plan fue aceptado como guia de la tarea. |
| `tasks/current/open_questions.md` | `tasks/current/` | Dudas que bloquean o cambian el alcance. | Cuando hay ambiguedad que no se resuelve en el repo. | Contiene preguntas reales y respuestas vigentes. |
| `decisions/decision_log.md` | `decisions/` | Registro cronologico de decisiones. | Al revisar por que se tomo una direccion. | Cada fila registra una decision aprobada. |
| `decisions/adr/*.md` | `decisions/adr/` | Decisiones arquitectonicas extensas. | Cuando una decision requiere contexto y alternativas. | La ADR fue aprobada o marcada con estado claro. |
| `docs/product/spec.md` | `docs/product/` | Verdad funcional. | En features, reglas de negocio o criterios de aceptacion. | Describe comportamiento aprobado. |
| `docs/architecture/sdd.md` | `docs/architecture/` | Diseno tecnico. | En cambios estructurales, contratos o migraciones. | Refleja el diseno vigente. |
| `memory/project_facts.md` | `memory/` | Hechos vigentes del proyecto. | Para stack, entornos e integraciones. | Solo contiene hechos confirmados. |
| `memory/constraints.md` | `memory/` | Restricciones tecnicas, negocio, seguridad y costo. | Antes de decisiones o cambios de alcance. | La restriccion esta vigente. |
| `memory/known_issues.md` | `memory/` | Problemas conocidos y workarounds. | Al investigar bugs o regresiones. | El problema sigue siendo relevante. |
| `memory/patterns.md` | `memory/` | Patrones y anti-patrones aprobados. | Al implementar o revisar consistencia. | El patron fue validado por uso o decision. |
| `memory/glossary.md` | `memory/` | Terminos del dominio. | Cuando hay ambiguedad de lenguaje. | El termino esta definido para el proyecto. |
| `graphify-out/*` | `graphify-out/` | Contexto estructural derivado. | En tareas Nivel 3 o exploracion estructural. | Nunca es canonico; siempre es derivado. |

## Relacion entre documentos

`PROJECT_GUIDE.md` define la identidad y el mapa general del proyecto.

`CONTEXT_INDEX.md` no explica el proyecto: dirige a la fuente correcta para cada necesidad.

`tasks/current/*` describe la ejecucion actual y no debe convertirse en memoria historica.

`decisions/` conserva decisiones aprobadas. Si una decision cambia una restriccion o patron, tambien debe actualizarse `memory/constraints.md` o `memory/patterns.md`.

`docs/product/spec.md` describe lo que el sistema debe hacer. `docs/architecture/sdd.md` describe como se disena o modifica tecnicamente.

`memory/` conserva conocimiento vigente y comprimido. No debe duplicar specs, SDDs ni decisiones completas.

`graphify-out/` ayuda a navegar estructura, pero si revela algo que debe gobernar el proyecto, esa informacion debe volver a una fuente canonica.

## Regla de uso

No cargar todos los documentos por defecto. Empezar por `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y `tasks/current/active_task.md`, y escalar segun `OPERACION/CONTEXT_ROUTER.md`.
