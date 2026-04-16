# Support Requests Spec Delta

## ADDED Requirements

### Requirement: Security requests start high priority

The system SHALL assign high priority to every newly created security request.

#### Scenario: New security request

- WHEN a request is created with type `security`
- THEN its initial priority is `high`
