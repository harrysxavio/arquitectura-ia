# Registro de Decisiones

> Indice breve de decisiones aprobadas y vigentes para SAMPLE_PROJECT.

| Fecha | Decision | Impacto | Referencia |
|---|---|---|---|
| 2026-04-13 | Mantener comportamiento funcional en docs versionados del proyecto antes de automatizar. | La CLI implementa comportamiento aprobado en vez de gobernarlo. | `decisions/adr/0001-documentar-triage-en-markdown.md` |
| 2026-04-13 | Tratar Graphify solo como contexto derivado. | `graphify-out/` puede guiar navegacion, pero no reemplazar OpenSpec ni decisiones. | `GRAPHIFY/GRAPHIFY_POLICY.md` |
| 2026-04-13 | Mantener la automatizacion minima y pedagogica. | `app.py`, `src/`, `tests/` y `data/` siguen siendo recursos de ejemplo, no estructura productiva. | `docs/architecture/system.md` |
| 2026-04-16 | Adoptar arquitectura OpenSpec-first para el ejemplo. | La autoridad funcional pasa a `openspec/specs/support-requests/spec.md`; el flujo de cambio activo pasa a `openspec/changes/*`. | `openspec/changes/add-security-priority/proposal.md` |

## Regla

Mantener este archivo como indice breve. Usar ADRs para decisiones estructurales y cambios OpenSpec para justificar cambios activos.
