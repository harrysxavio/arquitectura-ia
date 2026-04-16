# Graph Report - .  (2026-04-16)

## Corpus Check
- 13 files · ~41,282 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 72 nodes · 83 edges · 11 communities detected
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]

## God Nodes (most connected - your core abstractions)
1. `TextEnum` - 8 edges
2. `SupportDeskServiceTest` - 7 edges
3. `SupportDeskService` - 5 edges
4. `TriageTest` - 5 edges
5. `RequestNotFoundError` - 4 edges
6. `JsonRequestStore` - 4 edges
7. `Triage rules aligned with OpenSpec support request behavior.` - 4 edges
8. `main()` - 3 edges
9. `RequestType` - 3 edges
10. `Priority` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Triage rules aligned with OpenSpec support request behavior.` --uses--> `RequestType`  [INFERRED]
  SAMPLE_PROJECT\src\triage.py → src\enums.py
- `Triage rules aligned with OpenSpec support request behavior.` --uses--> `Priority`  [INFERRED]
  SAMPLE_PROJECT\src\triage.py → src\enums.py
- `Triage rules aligned with OpenSpec support request behavior.` --uses--> `RequestStatus`  [INFERRED]
  SAMPLE_PROJECT\src\triage.py → src\enums.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.26
Nodes (9): Enum, Priority, Enumerations for the support desk domain., String enum with a compact parser for CLI and JSON inputs., RequestStatus, RequestType, TextEnum, str (+1 more)

### Community 1 - "Community 1"
Cohesion: 0.22
Nodes (5): Application service for support desk requests., Raised when a request id is not present in storage., RequestNotFoundError, SupportDeskService, ValueError

### Community 2 - "Community 2"
Cohesion: 0.22
Nodes (3): Data models for the support desk example., SupportRequest, Formatting helpers for CLI output.

### Community 3 - "Community 3"
Cohesion: 0.43
Nodes (1): SupportDeskServiceTest

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (2): JsonRequestStore, JSON storage for the runtime example data.

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (1): TriageTest

### Community 6 - "Community 6"
Cohesion: 0.6
Nodes (4): build_parser(), main(), CLI for the SAMPLE_PROJECT support desk example., run_demo()

### Community 7 - "Community 7"
Cohesion: 0.4
Nodes (1): Small utilities for the support desk example.

### Community 8 - "Community 8"
Cohesion: 0.5
Nodes (1): JsonRequestStoreTest

### Community 9 - "Community 9"
Cohesion: 0.67
Nodes (0): 

### Community 10 - "Community 10"
Cohesion: 0.67
Nodes (1): Tests for SAMPLE_PROJECT.

## Knowledge Gaps
- **9 isolated node(s):** `CLI for the SAMPLE_PROJECT support desk example.`, `Enumerations for the support desk domain.`, `String enum with a compact parser for CLI and JSON inputs.`, `Data models for the support desk example.`, `Formatting helpers for CLI output.` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `CLI for the SAMPLE_PROJECT support desk example.`, `Enumerations for the support desk domain.`, `String enum with a compact parser for CLI and JSON inputs.` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._