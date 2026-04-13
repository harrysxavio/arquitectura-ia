# Graph Report - .  (2026-04-13)

## Corpus Check
- 1 files · ~21,111 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 6 nodes · 5 edges · 2 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]

## God Nodes (most connected - your core abstractions)
1. `triage()` - 2 edges
2. `SupportRequest` - 1 edges
3. `Small illustrative flow for SAMPLE_PROJECT.  This module is not a production imp` - 1 edges
4. `Apply the smallest illustrative triage rule from the spec.` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Community 0"
Cohesion: 0.5
Nodes (2): Small illustrative flow for SAMPLE_PROJECT.  This module is not a production imp, SupportRequest

### Community 1 - "Community 1"
Cohesion: 1.0
Nodes (2): Apply the smallest illustrative triage rule from the spec., triage()

## Knowledge Gaps
- **3 isolated node(s):** `SupportRequest`, `Small illustrative flow for SAMPLE_PROJECT.  This module is not a production imp`, `Apply the smallest illustrative triage rule from the spec.`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 1`** (2 nodes): `Apply the smallest illustrative triage rule from the spec.`, `triage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `triage()` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.400) - this node is a cross-community bridge._
- **What connects `SupportRequest`, `Small illustrative flow for SAMPLE_PROJECT.  This module is not a production imp`, `Apply the smallest illustrative triage rule from the spec.` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._