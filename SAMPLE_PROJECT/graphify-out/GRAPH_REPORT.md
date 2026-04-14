# Graph Report - .  (2026-04-13)

## Corpus Check
- 13 files · ~12,630 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 72 nodes · 130 edges · 9 communities detected
- Extraction: 63% EXTRACTED · 37% INFERRED · 0% AMBIGUOUS · INFERRED: 48 edges (avg confidence: 0.5)
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

## God Nodes (most connected - your core abstractions)
1. `RequestType` - 13 edges
2. `SupportRequest` - 13 edges
3. `Priority` - 12 edges
4. `RequestStatus` - 12 edges
5. `SupportDeskService` - 12 edges
6. `SupportDeskServiceTest` - 12 edges
7. `RequestNotFoundError` - 11 edges
8. `JsonRequestStore` - 10 edges
9. `TextEnum` - 8 edges
10. `JsonRequestStoreTest` - 8 edges

## Surprising Connections (you probably didn't know these)
- `SupportRequest` --uses--> `Formatting helpers for CLI output.`  [INFERRED]
  src\models.py → src\reporter.py
- `SupportRequest` --uses--> `JSON storage for the runtime example data.`  [INFERRED]
  src\models.py → src\storage.py
- `CLI for the SAMPLE_PROJECT support desk example.` --uses--> `RequestType`  [INFERRED]
  app.py → src\enums.py
- `CLI for the SAMPLE_PROJECT support desk example.` --uses--> `RequestNotFoundError`  [INFERRED]
  app.py → src\service.py
- `CLI for the SAMPLE_PROJECT support desk example.` --uses--> `SupportDeskService`  [INFERRED]
  app.py → src\service.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.25
Nodes (11): Priority, RequestStatus, RequestType, Data models for the support desk example., SupportRequest, Application service for support desk requests., Raised when a request id is not present in storage., RequestNotFoundError (+3 more)

### Community 1 - "Community 1"
Cohesion: 0.2
Nodes (5): Enum, Enumerations for the support desk domain., String enum with a compact parser for CLI and JSON inputs., TextEnum, str

### Community 2 - "Community 2"
Cohesion: 0.22
Nodes (2): Formatting helpers for CLI output., JSON storage for the runtime example data.

### Community 3 - "Community 3"
Cohesion: 0.43
Nodes (1): SupportDeskServiceTest

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (2): SupportDeskService, ValueError

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
Cohesion: 0.67
Nodes (1): Tests for SAMPLE_PROJECT.

## Knowledge Gaps
- **3 isolated node(s):** `Enumerations for the support desk domain.`, `String enum with a compact parser for CLI and JSON inputs.`, `Small utilities for the support desk example.`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SupportDeskServiceTest` connect `Community 3` to `Community 0`, `Community 4`?**
  _High betweenness centrality (0.176) - this node is a cross-community bridge._
- **Why does `RequestType` connect `Community 0` to `Community 1`, `Community 3`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.166) - this node is a cross-community bridge._
- **Why does `SupportDeskService` connect `Community 4` to `Community 0`, `Community 2`, `Community 3`, `Community 6`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `RequestType` (e.g. with `CLI for the SAMPLE_PROJECT support desk example.` and `SupportRequest`) actually correct?**
  _`RequestType` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `SupportRequest` (e.g. with `Priority` and `RequestStatus`) actually correct?**
  _`SupportRequest` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `Priority` (e.g. with `SupportRequest` and `Data models for the support desk example.`) actually correct?**
  _`Priority` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `RequestStatus` (e.g. with `SupportRequest` and `Data models for the support desk example.`) actually correct?**
  _`RequestStatus` has 10 INFERRED edges - model-reasoned connections that need verification._