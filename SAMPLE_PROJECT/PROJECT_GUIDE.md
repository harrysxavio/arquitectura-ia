# PROJECT_GUIDE.md

> Canonical identity and scope for SAMPLE_PROJECT.

## Identity

- Name: Mesa Interna de Soporte Operativo.
- Primary user: operations coordinators and internal teams requesting support.
- Problem solved: centralize internal requests, classify priority and keep traceability.

## Scope

Included:

- Manual registration of internal requests.
- Request type, area, status and priority tracking.
- Basic CLI flow for create, list, demo and close.
- OpenSpec documentation for approved behavior and active changes.
- Runtime JSON persistence for the example.

Out of scope:

- Real authentication.
- External help desk integration.
- Production database.
- Automatic notifications.
- Full web interface.
- Production template for new systems.

## Structure

- `openspec/`: functional truth and active changes.
- `docs/architecture/system.md`: stable technical architecture.
- `decisions/`: short decision index and ADRs.
- `memory/`: compact facts, constraints, patterns and glossary.
- `app.py`, `src/`, `tests/`, `data/`: pedagogical CLI app.
- `graphify-out/`: derived structural context.
- `ARCHIVE/legacy-open-spec-migration/`: historical migration evidence at repo root.

## Stack

- Backend: Python standard library.
- Frontend: none.
- Data: local JSON runtime file.
- Hosting: none.

## Constraints

- Keep the sample small and pedagogical.
- Do not treat runtime data as authority.
- Do not treat Graphify output as authority.
- Do not store real secrets or personal data.

## Rule

Functional behavior lives in OpenSpec. This guide explains identity and scope only.
