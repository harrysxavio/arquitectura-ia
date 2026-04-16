# Patterns

> Compact approved patterns and anti-patterns for the SAMPLE_PROJECT support desk example.

## Approved

- Document functional behavior in `openspec/specs/support-requests/spec.md`.
- Represent active work in `openspec/changes/*`.
- Reflect approved functional behavior in the small CLI automation.
- Keep decisions brief in `decisions/decision_log.md` and use ADRs for structural decisions.
- Keep memory short, current and actionable.
- Use Graphify for navigation and impact analysis only.
- Use `unittest` and the Python standard library.

## Avoid

- Building a production API or UI inside the sample.
- Treating runtime JSON as canonical.
- Copying external research directly into canonical docs without review.
- Treating `SAMPLE_PROJECT/` as a production template.
- Duplicating theory inside the sample.
