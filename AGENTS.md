# AGENTS.md

> Instruccion local de tooling para este repo-framework. No reemplaza `OPERACION/AGENTS/*.md` ni la plantilla `PROJECT_TEMPLATE/AGENTS.md`.

## Proposito

Este archivo contiene instrucciones locales para agentes que trabajan en este repositorio framework. Su funcion es recordar reglas de tooling propias del repo, no explicar todo el modelo operativo.

Para reglas de roles, revisar `OPERACION/AGENTS/`. Para el router de contexto, revisar `OPERACION/CONTEXT_ROUTER.md`. Para la plantilla reusable, revisar `PROJECT_TEMPLATE/AGENTS.md`.

## Prioridades Locales

- No tocar `SAMPLE_PROJECT/` salvo que la tarea lo pida explicitamente.
- Mantener la arquitectura OpenSpec-first.
- No reintroducir material heredado como fuente activa.
- Usar Graphify como contexto derivado, no como autoridad.

## graphify

Este proyecto tiene un grafo de conocimiento Graphify en `graphify-out/`.

> [!NOTE]
> Usa esta seccion solo cuando `graphify-out/` exista en el proyecto activo.

Reglas:
- Antes de responder preguntas de arquitectura o codigo, lee graphify-out/GRAPH_REPORT.md para identificar god nodes y estructura de comunidades
- Si graphify-out/wiki/index.md existe, navega esa wiki en vez de leer archivos crudos
- Despues de modificar archivos de codigo en esta sesion, ejecuta `python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"` para mantener el grafo actualizado

## Regla Breve

Este archivo ajusta el comportamiento del agente dentro de este repo; no reemplaza las fuentes documentales del framework.
