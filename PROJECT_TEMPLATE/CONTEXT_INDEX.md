# CONTEXT_INDEX.md

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

Este archivo es el mapa de fuentes oficiales. Su trabajo es decir donde mirar segun la pregunta, no explicar todo el proyecto.

## Proposito

Sin un indice de contexto, humanos y agentes tienden a abrir carpetas completas. Este archivo reduce busqueda y ruido: para cada necesidad, indica el documento que tiene autoridad o utilidad principal.

## Que Contiene

Una tabla de necesidades, rutas y usos. No contiene la explicacion completa de cada fuente; solo indica donde leer.

## Orden de Uso

Se completa despues de `PROJECT_GUIDE.md` y se actualiza cada vez que aparece una fuente oficial nueva, una spec relevante o un cambio estable de rutas.

## Relacion con Otros Documentos

`AGENTS.md` usa este indice para orientar agentes. `OPERACION/CONTEXT_ROUTER.md` usa el mismo criterio a nivel framework. OpenSpec, arquitectura, decisiones y memoria son las fuentes que este indice ayuda a ubicar.

## Fuentes Oficiales

| Necesidad | Archivo | Uso |
|---|---|---|
| Identidad y alcance | `PROJECT_GUIDE.md` | Entrada base del proyecto. |
| Reglas locales de agentes | `AGENTS.md` | Guia de agentes especifica del proyecto. |
| Verdad funcional vigente | `openspec/specs/*/spec.md` | Comportamiento aprobado. |
| Cambio activo | `openspec/changes/<change-id>/proposal.md` | Intencion, alcance y no alcance. |
| Diseno del cambio | `openspec/changes/<change-id>/design.md` | Diseno tecnico del cambio. |
| Tareas del cambio | `openspec/changes/<change-id>/tasks.md` | Lista ejecutable. |
| Arquitectura estable | `docs/architecture/system.md` | Componentes, contratos y datos estables. |
| Decisiones | `decisions/decision_log.md` | Indice breve de decisiones aprobadas. |
| ADRs | `decisions/adr/*.md` | Decisiones estructurales o de alto impacto. |
| Hechos | `memory/facts.md` | Contexto confirmado. |
| Restricciones | `memory/constraints.md` | Limites vigentes. |
| Patrones | `memory/patterns.md` | Formas aprobadas de trabajar. |
| Glosario | `memory/glossary.md` | Terminos opcionales del dominio. |
| Problemas conocidos | `memory/known_issues.md` | Problemas confirmados que siguen afectando trabajo futuro. |
| Graphify | `graphify-out/GRAPH_REPORT.md` | Contexto derivado, no canonico. |

## Regla

El comportamiento funcional empieza en OpenSpec. Graphify ayuda a navegar, pero nunca reemplaza fuentes canonicas.

## Ejemplo Minimo

```markdown
| Necesidad | Archivo | Uso |
|---|---|---|
| Identidad y alcance | `PROJECT_GUIDE.md` | Entrada base del proyecto. |
| Solicitudes | `openspec/specs/requests/spec.md` | Comportamiento aprobado de solicitudes. |
| Cambio activo | `openspec/changes/add-request-priority/proposal.md` | Alcance del cambio actual. |
| Arquitectura | `docs/architecture/system.md` | Componentes, datos y validacion. |
| Restricciones | `memory/constraints.md` | Limites vigentes de seguridad y costo. |
```

## Como Mantenerlo

Actualizar este indice cuando una fuente canonica cambia de ruta, aparece una nueva capacidad OpenSpec o se agrega una pieza estable de arquitectura. No agregar archivos temporales, notas personales ni salidas derivadas como autoridad.

## Senal de Buen Uso

Si un agente puede responder "que debo leer para esta tarea?" usando este archivo, el indice esta cumpliendo su funcion.
