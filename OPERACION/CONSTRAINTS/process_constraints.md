# CONSTRAINTS: Flow and Execution

## Base Flow

1. Classify task type and risk.
2. Load minimal context through `OPERACION/CONTEXT_ROUTER.md`.
3. Use OpenSpec specs for approved behavior.
4. Use OpenSpec changes for active work.
5. Validate with tests or document checks.
6. Update decisions or memory only when durable knowledge changed.

## Rules

- Functional changes require a relevant OpenSpec spec or change.
- Structural changes require architecture context and, when durable, a decision entry or ADR.
- Do not close broad work without validation.
