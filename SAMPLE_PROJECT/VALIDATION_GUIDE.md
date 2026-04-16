# VALIDATION_GUIDE.md

> Practical validation guide for the OpenSpec-first sample.

## Functional Validation

From `SAMPLE_PROJECT/`:

```bash
python -B -m unittest discover -s tests
python -B app.py demo
python -B app.py create --title "Acceso VPN" --description "Alta para equipo operaciones" --area "Operaciones" --type acceso
python -B app.py list
```

Check that:

- Tests pass.
- The demo runs a small support flow.
- Security requests start with high priority.
- Closing without a note fails.
- Runtime JSON is not treated as authority.

## Document Validation

Check that:

- Functional behavior is in `openspec/specs/support-requests/spec.md`.
- Active change flow is in `openspec/changes/add-security-priority/`.
- Stable architecture is in `docs/architecture/system.md`.
- `decisions/decision_log.md` is a short index.
- `memory/` is compact and separated into facts, constraints and patterns.
- Graphify is marked as derived context.

## Graphify Validation

Graphify can be regenerated when available:

```bash
graphify update .
```

If regeneration is unavailable, existing output must be treated as stale derived context. It never replaces OpenSpec, decisions, architecture or memory.

## Failure Signals

The architecture is failing if a user or agent must load broad folders by default, if a functional rule appears as authority outside OpenSpec, or if derived context is used to decide behavior.
