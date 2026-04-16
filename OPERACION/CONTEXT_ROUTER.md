# CONTEXT_ROUTER.md - OpenSpec-First Context Router

This file is the authority for deciding what context an agent should load.

## Base Protocol

1. Identify task type and complexity.
2. Load `PROJECT_GUIDE.md` and `CONTEXT_INDEX.md` when working inside a project.
3. For behavior, load the relevant `openspec/specs/*/spec.md`.
4. For active work, load the relevant `openspec/changes/*`.
5. Add architecture, decisions, memory or Graphify only when justified.

## Levels

| Level | Criteria | Required context |
|---|---|---|
| 1 | Local, clear, low risk | Base context + affected file |
| 2 | Functional or multi-file | Base context + relevant OpenSpec spec/change |
| 3 | Structural, ambiguous or broad | Level 2 + `docs/architecture/system.md` + decisions/memory + Graphify if useful |

## Task Matrix

| Type | Start With | Add When Needed |
|---|---|---|
| bug | affected file, tests, relevant spec | `memory/facts.md`, Graphify for broad impact |
| feature | relevant spec and active change | architecture, decisions, patterns |
| refactor | architecture and affected modules | Graphify for cross-module impact |
| docs | target doc and canonical source | OpenSpec or architecture as source |
| review | diff and relevant spec/change | decisions, architecture, tests |
| research | objective and source | compact result in memory or docs if it becomes canonical |

## Authority Order

1. `AGENTS.md`
2. Active `openspec/changes/*`
3. `openspec/specs/*/spec.md`
4. `docs/architecture/system.md`
5. `decisions/decision_log.md`
6. `decisions/adr/*.md`
7. `memory/constraints.md`
8. `memory/facts.md`
9. `memory/patterns.md`
10. `graphify-out/*` as derived context only

## Prohibitions

- Do not load broad folders by default.
- Do not duplicate functional rules outside OpenSpec.
- Do not use Graphify as authority.
- Do not use archived legacy as an active source.
