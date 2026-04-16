# Support Requests Spec

> Canonical functional source for the SAMPLE_PROJECT support request flow.

## Purpose

Define how internal support requests are created, classified, prioritized, assigned and closed in the pedagogical CLI app.

## Actors

- Internal requester: reports an operational need.
- Operations coordinator: classifies and assigns the request.
- Assigned owner: resolves, blocks or escalates the request.

## Scope

- Create requests with title, description, area and type.
- Classify type as support, access, data, security or other.
- Track priority as low, medium, high or critical.
- Track status as new, triage, assigned, blocked or closed.
- Assign an owner when needed.
- Close a request with a short closing note.
- Use local JSON only as runtime persistence for the example.

## Out of Scope

- Contractual SLA.
- Automatic notifications.
- Required attachments.
- Production web portal.
- External integrations.
- Treating runtime JSON as project authority.

## Requirements

### Requirement: Create support request

The system SHALL create an internal support request with title, description, requesting area and request type.

#### Scenario: Access request is created

- WHEN a requester creates an access request
- THEN the request is stored with type `access`
- AND the initial status is available for triage

### Requirement: Prioritize security requests

The system SHALL start every security request with high priority.

#### Scenario: Security request starts high

- WHEN a requester creates a request with type `security`
- THEN the request priority is `high`

### Requirement: Require owner before critical request leaves triage

The system SHALL require an owner before a critical request can leave triage.

#### Scenario: Critical request without owner stays in triage

- WHEN a critical request has no owner
- THEN it must not move to assigned work

### Requirement: Require blocked reason

The system SHALL require a clear reason when a request is blocked.

#### Scenario: Owner cannot continue

- WHEN an owner marks a request as blocked
- THEN the request records the blocking reason

### Requirement: Require closing note

The system SHALL require a short note when a request is closed.

#### Scenario: Request is closed

- WHEN an owner closes a request with a note
- THEN the request status becomes closed

#### Scenario: Close without note is rejected

- WHEN an owner closes a request without a note
- THEN the system rejects the close operation

### Requirement: Manual priority changes are documented

The system SHALL allow manual priority changes only when the coordinator records the reason.

#### Scenario: Coordinator changes priority

- WHEN the coordinator changes priority manually
- THEN the reason is documented with the request or change record
