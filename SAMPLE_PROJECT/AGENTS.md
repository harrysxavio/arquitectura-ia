# AGENTS.md

> Adaptacion local del proyecto ejemplo. No reemplaza los contratos globales de `OPERACION/AGENTS/*.md`.

## Proposito

Definir como se aplican los roles base del framework dentro de la Mesa Interna de Soporte Operativo.

## Relacion con los agentes globales

Los contratos oficiales viven en la raiz del framework:

- `OPERACION/AGENTS/manager.md`
- `OPERACION/AGENTS/coder.md`
- `OPERACION/AGENTS/reviewer.md`
- `OPERACION/AGENTS/debugger.md`

Este archivo solo agrega contexto local. Si contradice los contratos globales, gana el contrato global salvo decision documentada.

## Contexto base local

Todo agente debe empezar con:

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`

Despues debe cargar solo los documentos que correspondan segun el tipo y nivel de tarea.

## Roles Base

- Manager: clasifica tarea y contexto.
- Coder: implementa cambios documentales o codigo minimo dentro del alcance.
- Reviewer: revisa calidad, coherencia y evidencia.
- Debugger: investiga fallos o contradicciones con evidencia.

## Ajustes Locales

- Manager:
  - confirmar si la tarea es documental, funcional, tecnica o de memoria;
  - no cargar `graphify-out/` salvo tarea estructural o ambigua;
  - usar `CONTEXT_INDEX.md` para decidir fuentes.
- Coder:
  - tratar `docs/product/spec.md` como verdad funcional;
  - tratar `docs/architecture/sdd.md` como verdad tecnica cuando aplique;
  - mantener `src/` como ilustrativo y opcional.
- Reviewer:
  - validar que cambios de reglas tambien actualicen decision o memoria si corresponde;
  - verificar que Graphify no se use como fuente canonica;
  - revisar que el ejemplo siga alineado con `PROJECT_TEMPLATE/`.
- Debugger:
  - revisar primero `memory/known_issues.md`;
  - documentar causa raiz si un fallo se vuelve relevante para futuras tareas;
  - no convertir un bug puntual en redisenio amplio.

## Nota de uso

No crear agentes nuevos para este ejemplo. Si aparece una necesidad repetible, documentarla como patron o workflow antes de convertirla en rol.

