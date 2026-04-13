# Implementation Plan

> Ejemplo rellenado. Guia la ejecucion de la tarea activa.

## Pasos

1. Confirmar alcance del flujo de triage en `PROJECT_GUIDE.md`.
2. Documentar reglas funcionales en `docs/product/spec.md`.
3. Describir el diseno tecnico minimo en `docs/architecture/sdd.md`.
4. Registrar la decision en `decisions/decision_log.md`.
5. Crear una ADR para explicar por que el triage vive primero en Markdown.
6. Actualizar `memory/constraints.md` y `memory/patterns.md` con conocimiento vigente.
7. Mantener `src/sample_flow.py` como ejemplo opcional, sin convertirlo en sistema productivo.

## Validacion

- La spec describe entrada, clasificacion, prioridad, asignacion y cierre.
- La SDD no promete una app completa.
- La decision y la ADR apuntan al mismo criterio.
- La memoria contiene solo hechos vigentes, restricciones y patrones breves.
- `graphify-out/*` queda marcado como placeholder pedagogico.

## Riesgos

- Que `src/` parezca parte obligatoria del framework.
- Que Graphify se interprete como fuente canonica.
- Que el ejemplo copie teoria ya documentada en `THEORY/`.

## Criterio de Cierre

La tarea se considera cerrada cuando un principiante puede leer el README del ejemplo, entender el flujo de documentos y saber donde documentar un cambio de regla sin cargar todo el repo.

## Nota de uso

Este plan guia la tarea actual. Si queda una regla duradera, debe vivir en spec, SDD, decision o memoria.

