# Proposal: Add Security Priority

## Summary

Use OpenSpec changes as the active change flow for the sample project and demonstrate a functional change around security request priority.

## Problem

The legacy flow stored active task, implementation plan and open questions in separate task files. That duplicated OpenSpec's role and forced agents to load extra context.

## Goals

- Represent the active change in OpenSpec.
- Keep the approved behavior in the support requests spec.
- Show how a functional rule change is proposed, designed and validated.
- Keep the sample pedagogical, not production-grade.

## Non Goals

- Build a production API.
- Add a web UI.
- Add a production database.
- Add external integrations.

## Scope

- Confirm security requests start with high priority.
- Keep runtime JSON as non-canonical example data.
- Validate the CLI and tests against the approved spec.
