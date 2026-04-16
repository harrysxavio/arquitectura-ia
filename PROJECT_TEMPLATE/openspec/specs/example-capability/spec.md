# Example Capability Spec

> OpenSpec template. Becomes canonical only inside an active project.

## Purpose

Describe the approved user-visible behavior for one project capability.

## Requirements

### Requirement: Approved behavior is explicit

The system SHALL keep functional behavior in OpenSpec so humans and agents can find the current rule without loading unrelated documents.

#### Scenario: Successful action

- WHEN the actor performs a supported action
- THEN the system returns the approved result

#### Scenario: Rejected action

- WHEN the actor provides unsupported input
- THEN the system rejects it with a clear outcome

## Notes

Keep implementation details in `docs/architecture/system.md` or in a change design.
