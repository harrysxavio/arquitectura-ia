# Architecture Migration Report

## 1. Summary

The repository was migrated to the approved OpenSpec-first architecture. Functional authority now lives in OpenSpec specs, active change flow lives in OpenSpec changes, stable architecture lives in system architecture documents, decisions remain as short indexes, memory is compact but separated, and Graphify remains derived context.

The migration followed the approved phases in `ARCHITECTURE_MIGRATION_PLAN.md`.

## 2. Preserved

- `PROJECT_BLUEPRINT/` was preserved and redefined as a compact OpenSpec-first adoption guide.
- `PROJECT_TEMPLATE/` was preserved as the reusable project mold.
- `SAMPLE_PROJECT/` was preserved as the pedagogical working example.
- `decisions/decision_log.md` was preserved in template and sample as a short decision index.
- `decisions/adr/` was preserved for structural or high-impact decisions.
- `GRAPHIFY/` and `graphify-out/` were preserved as derived context.
- `SAMPLE_PROJECT/app.py`, `src/`, `tests/` and `data/` were preserved as the runnable example.

## 3. Removed From Active Authority

The legacy model was removed from active authority:

- legacy task flow is no longer referenced as active context;
- legacy product spec is no longer referenced as functional authority;
- legacy SDD is no longer referenced as stable architecture;
- legacy project facts and known issues are no longer referenced as active memory.

Some OneDrive reparse-point placeholders could not be physically deleted. Their contents were neutralized and they are not listed as official sources in active routers or indexes.

## 4. Archived

Historical copies were preserved under:

```text
ARCHIVE/legacy-open-spec-migration/
```

Archived material includes prior template docs, sample docs, task files, product specs, technical design docs, memory files and pedagogical validation/tracing docs.

## 5. Merged

- Prior functional content was merged into OpenSpec specs.
- Prior active task, implementation plan and questions were represented in OpenSpec change files.
- Prior stable technical design was moved into `docs/architecture/system.md`.
- Prior facts and still-relevant current issues were compacted into `memory/facts.md`.
- Prior memory patterns and constraints were compacted into their dedicated memory files.
- Prior sample validation content was consolidated into `SAMPLE_PROJECT/VALIDATION_GUIDE.md`.

## 6. Functional Authority

Functional authority now lives in:

```text
PROJECT_TEMPLATE/openspec/specs/example-capability/spec.md
SAMPLE_PROJECT/openspec/specs/support-requests/spec.md
```

The sample's support request behavior is governed by `SAMPLE_PROJECT/openspec/specs/support-requests/spec.md`.

## 7. Change Flow

The active change flow now lives in:

```text
SAMPLE_PROJECT/openspec/changes/add-security-priority/
|-- proposal.md
|-- design.md
|-- tasks.md
`-- specs/support-requests/spec.md
```

Template projects now use `PROJECT_TEMPLATE/openspec/changes/` for future active changes.

## 8. Stable Architecture

Stable architecture now lives in:

```text
PROJECT_TEMPLATE/docs/architecture/system.md
SAMPLE_PROJECT/docs/architecture/system.md
```

These files describe components, runtime data, contracts and validation without duplicating functional requirements.

## 9. Validations Passed

- `python -B -m unittest discover -s tests` passed in `SAMPLE_PROJECT/`.
- `python -B app.py demo` passed in `SAMPLE_PROJECT/`.
- `data/requests.json` was reset to an empty runtime state after the demo.
- `graphify update .` ran at repo root and in `SAMPLE_PROJECT/`.
- Legacy reference validation returned no active matches outside archive/migration docs for:
  - task-flow legacy path
  - product-spec legacy path
  - technical-design legacy path
  - old facts filename
  - old issues filename
- Root and sample Graphify outputs are marked/treated as derived context.
- Stale derived cache files that could not be removed because of OneDrive permissions were neutralized.

## 10. Pending or Follow-up Review

- OneDrive denied physical deletion of some legacy placeholders. They are neutralized and not active, but a manual filesystem cleanup can remove them later if desired.
- `graphify-out/` is derived and should be regenerated again after any future code or broad documentation changes.
- `PROJECT_BLUEPRINT/` should be evaluated in a later phase to decide whether it still adds value or can be folded into README/template docs.
- Git index operations were blocked earlier by local `.git/index.lock` permission behavior, so file deletion state should be reviewed before committing in Git.

## Closure Checklist

| Check | Result |
|---|---|
| OpenSpec specs are active functional authority | Passed |
| OpenSpec changes are active change flow | Passed |
| Stable architecture uses system docs | Passed |
| Decision log is brief and current | Passed |
| Memory is compact and separated | Passed |
| Blueprint preserved and redefined | Passed |
| Template and sample aligned | Passed |
| Graphify derived only | Passed |
| Legacy active references removed | Passed |
| Migration report created | Passed |
