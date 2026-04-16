# ADR 0001 - Markdown-first triage documentation

## Status

Accepted, updated for OpenSpec-first architecture.

## Context

The sample needs visible, versioned rules before automation. The approved functional rules now live in OpenSpec. The CLI remains an implementation of those rules, not the authority.

## Decision

Use OpenSpec as the functional source and keep stable technical architecture in `docs/architecture/system.md`. Keep the CLI small and pedagogical.

## Consequences

- Functional changes start in `openspec/changes/*`.
- Approved behavior is archived into `openspec/specs/*`.
- Code and tests should trace back to OpenSpec.
- Runtime JSON and Graphify output are not canonical.
