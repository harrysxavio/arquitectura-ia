# System Architecture

> Stable technical architecture for the SAMPLE_PROJECT support desk example.

## Purpose

Describe the stable technical shape of the sample CLI app without duplicating functional rules. Functional behavior lives in `openspec/specs/support-requests/spec.md`; active changes live in `openspec/changes/*`.

## Context

`SAMPLE_PROJECT/` is a small pedagogical project, not a production template. It demonstrates how documentation, code, decisions, memory, tests and Graphify can coexist with compact context.

## Components

| Component | Role |
|---|---|
| `app.py` | CLI entrypoint for `demo`, `create`, `list` and `close`. |
| `src/enums.py` | Domain enums for type, priority and status. |
| `src/models.py` | Request data model. |
| `src/triage.py` | Initial priority and next-status helper logic. |
| `src/service.py` | Application service for create, list and close operations. |
| `src/storage.py` | JSON runtime persistence. |
| `src/reporter.py` | Text output formatting. |
| `tests/` | Unit tests for triage, service and storage behavior. |
| `data/requests.json` | Runtime example data; not canonical. |
| `graphify-out/` | Derived structural context; not canonical. |

## Contracts

A support request contains title, description, area, type, priority, status, optional owner, optional closing note and timestamps. The approved behavior is governed by OpenSpec.

## Data

There is no production database and no migration system. `data/requests.json` exists only to run the local example.

## Risks

- Treating the sample as a production app.
- Treating runtime JSON as an authority.
- Treating Graphify output as a source of truth.

## Validation

From `SAMPLE_PROJECT/`:

```bash
python -B -m unittest discover -s tests
python -B app.py demo
```

Graphify can be regenerated when available, but its output remains derived.
