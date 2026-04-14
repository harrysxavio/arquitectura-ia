# Active Task

> Ejemplo rellenado. Representa una tarea activa dentro del proyecto ejemplo.

## Tarea

Convertir `SAMPLE_PROJECT/` en una mini app funcional y pedagogica para probar Graphify.

## Tipo

`code+docs`

## Nivel

`3`

## Objetivo

Implementar una mesa interna de soporte operativo pequena, ejecutable por CLI, con persistencia JSON runtime, tests basicos y documentacion alineada con el framework.

## Alcance

- Crear app CLI con comandos `demo`, `create`, `list` y `close`.
- Implementar modulos Python pequenos en `src/`.
- Agregar tests con `unittest`.
- Documentar que `data/requests.json` es runtime y no canonico.
- Usar `graphify update .` desde `SAMPLE_PROJECT/` como comando principal de Graphify.
- Mantener `SAMPLE_PROJECT/` como ejemplo pedagogico, no plantilla de produccion.

## No Alcance

- Construir una API real.
- Crear interfaz web.
- Agregar base de datos productiva.
- Integrar sistemas externos.
- Modificar `PROJECT_TEMPLATE/`.

## Estado

`validado`

## Contexto Cargado

- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `docs/product/spec.md`
- `docs/architecture/sdd.md`
- `decisions/decision_log.md`
- `memory/constraints.md`
- `memory/patterns.md`
- `GRAPHIFY/GRAPHIFY_POLICY.md`
- `GRAPHIFY/OUTPUT_CONTRACT.md`

## Notas

La tarea es Nivel 3 porque toca codigo, docs, memoria, decisiones, tests y contexto derivado. Graphify debe enfocarse operativamente en `SAMPLE_PROJECT/`.

## Nota de uso

Al cerrar esta tarea, mover conocimiento duradero a decisiones, memoria o docs segun corresponda. No usar este archivo como backlog.
