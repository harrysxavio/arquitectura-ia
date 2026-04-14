# Implementation Plan

> Ejemplo rellenado. Guia la ejecucion de la tarea activa.

## Pasos

1. Reemplazar el flujo anterior de ejemplo por modulos funcionales en `src/`.
2. Crear `app.py` con CLI `demo`, `create`, `list` y `close`.
3. Agregar persistencia runtime en `data/requests.json`.
4. Agregar tests basicos con `unittest`.
5. Actualizar spec, SDD, decision log, ADR, memoria y agentes locales.
6. Crear `VALIDATION_GUIDE.md` con pruebas funcionales, documentales y comparativa Graphify.
7. Eliminar `src/graphify-out/` residual y usar solo `SAMPLE_PROJECT/graphify-out/`.
8. Ejecutar `graphify update .` desde `SAMPLE_PROJECT/`.

## Validacion

- `python -m unittest discover -s tests` pasa.
- `python app.py demo` ejecuta un flujo real.
- `data/requests.json` se documenta como runtime, no canonico.
- `CONTEXT_INDEX.md` apunta a fuentes, codigo y Graphify con roles claros.
- `VALIDATION_GUIDE.md` permite comparar trabajo sin Graphify vs con `GRAPH_REPORT.md`.

## Riesgos

- Que `SAMPLE_PROJECT/` parezca plantilla de produccion.
- Que `data/requests.json` se interprete como fuente canonica.
- Que Graphify se interprete como fuente canonica.

## Criterio de Cierre

La tarea se considera cerrada cuando un principiante puede ejecutar la mini app, correr tests, entender donde vive cada fuente canonica y usar Graphify como orientacion derivada.

## Nota de uso

Este plan guia la tarea actual. Si queda una regla duradera, debe vivir en spec, SDD, decision o memoria.
