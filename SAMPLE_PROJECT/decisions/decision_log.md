# Decision Log

> Ejemplo rellenado. Registro cronologico de decisiones aprobadas.

## Registro

| Fecha | Decision | Motivo | Impacto | Referencia |
|---|---|---|---|---|
| 2026-04-13 | Mantener el flujo de triage en Markdown canonico antes de automatizar. | El equipo necesita claridad operativa antes de invertir en implementacion tecnica. | `docs/product/spec.md` gobierna reglas; `src/` queda ilustrativo. | `decisions/adr/0001-documentar-triage-en-markdown.md` |
| 2026-04-13 | Tratar Graphify como contexto derivado, no como fuente de verdad. | Evita que un reporte stale contradiga la spec o memoria vigente. | `graphify-out/*` se marca como placeholder pedagogico. | `GRAPHIFY/GRAPHIFY_POLICY.md` |

## Detalle Opcional

La primera decision evita construir una app prematura. Si el flujo se estabiliza y hay usuarios reales, se podra crear una ADR nueva para elegir stack, almacenamiento y automatizaciones.

## Nota de uso

No registrar conversaciones ni ideas descartadas sin decision. Si una decision crea una restriccion vigente, actualizar tambien `memory/constraints.md`.

