# Decision Log

> Ejemplo rellenado. Registro cronologico de decisiones aprobadas.

## Registro

| Fecha | Decision | Motivo | Impacto | Referencia |
|---|---|---|---|---|
| 2026-04-13 | Mantener el flujo de triage en Markdown canonico antes de automatizar. | El equipo necesita claridad operativa antes de implementar comportamiento. | `docs/product/spec.md` gobierna reglas; la automatizacion minima debe alinearse con esa fuente. | `decisions/adr/0001-documentar-triage-en-markdown.md` |
| 2026-04-13 | Tratar Graphify como contexto derivado, no como fuente de verdad. | Evita que un reporte stale contradiga la spec o memoria vigente. | `graphify-out/*` vive en `SAMPLE_PROJECT/` como output derivado. | `GRAPHIFY/GRAPHIFY_POLICY.md` |
| 2026-04-13 | Implementar automatizacion minima alineada con Markdown canonico. | Se necesita un laboratorio real para validar Graphify sin construir producto grande. | `app.py`, `src/`, `tests/` y `data/requests.json` pasan a existir como ejemplo funcional pedagogico. | `decisions/adr/0001-documentar-triage-en-markdown.md` |
| 2026-04-13 | Mantener guias de validacion como extras pedagogicos del sample. | Validan el framework sin convertir el template en app ni en suite obligatoria. | `VALIDATION_GUIDE.md`, `ARCHITECTURE_VALIDATION.md` y `CHAT_SCENARIOS.md` no se agregan a `PROJECT_TEMPLATE/`. | `PROJECT_BLUEPRINT/PROJECT_STRUCTURE_EXAMPLE.md` |

## Detalle Opcional

La primera decision evita automatizar reglas no documentadas. La automatizacion minima actual no reemplaza la spec: la implementa para validar el framework y Graphify en un proyecto pequeno.

## Nota de uso

No registrar conversaciones ni ideas descartadas sin decision. Si una decision crea una restriccion vigente, actualizar tambien `memory/constraints.md`.
