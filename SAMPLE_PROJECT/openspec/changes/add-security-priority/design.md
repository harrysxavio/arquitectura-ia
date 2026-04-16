# Design: Add Security Priority

## Context

The sample app is a small Python CLI with standard-library modules. The stable architecture lives in `docs/architecture/system.md`; this file covers only the active change.

## Decision

Keep the security priority rule in OpenSpec and reflect it in the existing triage function. Do not introduce API, database migration or new dependency.

## Impact

- `src/triage.py` owns the initial priority calculation.
- `tests/test_triage.py` validates the security priority rule.
- `app.py` demonstrates the flow through `demo`, `create`, `list` and `close`.

## Data

No persistent schema change. `data/requests.json` remains runtime example data.

## Validation

- Run unit tests from `SAMPLE_PROJECT/`.
- Run the CLI demo.
- Confirm Graphify remains derived context only.
