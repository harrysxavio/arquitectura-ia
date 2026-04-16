# Decision Log

> Short index of approved, current decisions for SAMPLE_PROJECT.

| Date | Decision | Impact | Reference |
|---|---|---|---|
| 2026-04-13 | Keep functional behavior in versioned project docs before automation. | The CLI implements approved behavior instead of governing it. | `decisions/adr/0001-documentar-triage-en-markdown.md` |
| 2026-04-13 | Treat Graphify as derived context only. | `graphify-out/` can guide navigation but cannot override OpenSpec or decisions. | `GRAPHIFY/GRAPHIFY_POLICY.md` |
| 2026-04-13 | Keep the automation minimal and pedagogical. | `app.py`, `src/`, `tests/` and `data/` remain example assets, not production scaffolding. | `docs/architecture/system.md` |
| 2026-04-16 | Adopt OpenSpec-first architecture for the sample. | Functional authority moves to `openspec/specs/support-requests/spec.md`; active change flow moves to `openspec/changes/*`. | `openspec/changes/add-security-priority/proposal.md` |

## Rule

Keep this file as a short index. Use ADRs for structural decisions and OpenSpec changes for active change rationale.
