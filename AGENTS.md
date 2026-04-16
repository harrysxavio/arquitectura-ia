# AGENTS.md

> Instruccion local de tooling para este repo-framework. No reemplaza `OPERACION/AGENTS/*.md` ni la plantilla `PROJECT_TEMPLATE/AGENTS.md`.

## graphify

This project has a graphify knowledge graph at graphify-out/.

> [!NOTE]
> Usa esta seccion solo cuando `graphify-out/` exista en el proyecto activo.

Reglas:
- Antes de responder preguntas de arquitectura o codigo, lee graphify-out/GRAPH_REPORT.md para identificar god nodes y estructura de comunidades
- Si graphify-out/wiki/index.md existe, navega esa wiki en vez de leer archivos crudos
- Despues de modificar archivos de codigo en esta sesion, ejecuta `python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"` para mantener el grafo actualizado
