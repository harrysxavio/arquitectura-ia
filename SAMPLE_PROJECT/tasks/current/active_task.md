# Active Task

> Ejemplo rellenado. Representa una tarea activa dentro del proyecto ejemplo.

## Tarea

Definir y documentar el flujo de triage de solicitudes internas.

## Tipo

`docs`

## Nivel

`2`

## Objetivo

Dejar una version breve y operable del flujo que explique como una solicitud interna pasa de entrada a clasificacion, asignacion y cierre.

## Alcance

- Actualizar la spec funcional del flujo de soporte.
- Registrar la decision de mantener el triage en Markdown antes de automatizar.
- Mantener memoria breve sobre restricciones y patrones.
- Usar `src/sample_flow.py` solo como apoyo ilustrativo.

## No Alcance

- Construir una API real.
- Crear interfaz web.
- Agregar base de datos.
- Integrar sistemas externos.
- Generar un grafo real de Graphify.

## Estado

`en progreso`

## Contexto Cargado

- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `docs/product/spec.md`
- `docs/architecture/sdd.md`
- `decisions/decision_log.md`
- `memory/constraints.md`
- `memory/patterns.md`

## Notas

La tarea es Nivel 2 porque toca varios documentos y una decision, pero no requiere exploracion estructural amplia. Graphify se deja como placeholder pedagogico.

## Nota de uso

Al cerrar esta tarea, mover conocimiento duradero a decisiones, memoria o docs segun corresponda. No usar este archivo como backlog.

