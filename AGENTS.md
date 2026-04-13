# AGENTS.md

> Instruccion local de tooling para este repo-framework. No reemplaza `OPERACION/AGENTS/*.md` ni la plantilla `PROJECT_TEMPLATE/AGENTS.md`.

## graphify

This project has a graphify knowledge graph at graphify-out/.

> [!NOTE]
> Use this section only when `graphify-out/` exists in the active project.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"` to keep the graph current
