# AGENTS.md

> Local agent guidance for SAMPLE_PROJECT.

## Context Order

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `openspec/specs/support-requests/spec.md`
4. `openspec/changes/add-security-priority/` when discussing the example change
5. `docs/architecture/system.md` for technical structure
6. `decisions/decision_log.md` and `memory/*` only when needed
7. `graphify-out/*` for derived navigation on broad or ambiguous work

## Role Notes

- Manager: classify the task and choose minimal context.
- Coder: implement only within the approved OpenSpec and architecture boundaries.
- Reviewer: verify changes against OpenSpec, architecture, decisions and tests.
- Debugger: inspect symptoms, code and compact memory before widening scope.

## Rules

- Do not use runtime JSON as authority.
- Do not use Graphify as authority.
- Do not expand the sample into a production system without a new approved change.
