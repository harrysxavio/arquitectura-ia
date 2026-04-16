# Implementation Plan

> Ejemplo rellenado. Guia la consolidacion documental y de validacion del laboratorio.

## Estado Base Validado

- `SAMPLE_PROJECT/` ya tiene mini app CLI con `demo`, `create`, `list` y `close`.
- `src/`, `tests/` y `data/requests.json` existen como extras pedagogicos del laboratorio.
- `graphify update .` genera contexto derivado en `SAMPLE_PROJECT/graphify-out/`.
- `data/requests.json` se documenta como runtime, no canonico.

## Pasos de Consolidacion

1. Corregir referencias desactualizadas sobre outputs Graphify y `graph.html` opcional.
2. Separar estructura estandar de `PROJECT_TEMPLATE/` de extras pedagogicos del sample.
3. Fortalecer `VALIDATION_GUIDE.md` con validacion funcional, documental, arquitectonica y Graphify.
4. Crear `ARCHITECTURE_VALIDATION.md` para probar la arquitectura como sistema completo.
5. Crear `CHAT_SCENARIOS.md` con prompts, trazas sin/con Graphify y comparaciones.
6. Registrar criterios practicos para decidir si Graphify aporta valor o si agrega ruido.
7. Ejecutar pruebas funcionales y regenerar Graphify desde `SAMPLE_PROJECT/`.

## Validacion

- `python -B -m unittest discover -s tests` pasa.
- `python -B app.py demo` ejecuta un flujo real.
- `graphify update .` actualiza `GRAPH_REPORT.md` y `graph.json`.
- `VALIDATION_GUIDE.md` incluye tabla manual vs Graphify.
- `ARCHITECTURE_VALIDATION.md` incluye senales de fallo de la arquitectura.
- `CHAT_SCENARIOS.md` incluye al menos un caso donde Graphify no debe usarse.
- `SAMPLE_PROJECT/` sigue reconocible como instancia de `PROJECT_TEMPLATE/` y sus extras quedan marcados como pedagogicos.

## Riesgos

- Que `SAMPLE_PROJECT/` parezca plantilla de produccion.
- Que `data/requests.json` se interprete como fuente canonica.
- Que Graphify se interprete como fuente canonica.
- Que guias pedagogicas del laboratorio se traten como estandar obligatorio.

## Criterio de Cierre

La tarea se considera cerrada cuando un principiante puede ejecutar la mini app, correr tests, probar la arquitectura completa y comparar trabajo manual vs con Graphify sin confundir fuentes canonicas con contexto derivado.

## Nota de uso

Este plan guia la consolidacion actual. Si queda una regla duradera, debe vivir en spec, SDD, decision o memoria.
