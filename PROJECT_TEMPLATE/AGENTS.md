# AGENTS.md

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Definir como se aplican en este proyecto los roles base del framework sin duplicar los contratos oficiales de `OPERACION/AGENTS/`.

## Como llenarlo

Indicar ajustes locales, limites especificos del proyecto y rutas relevantes. No redefinir misiones completas si ya existen en el framework global.

## Ejemplo minimo

```text
Manager: usa PROJECT_GUIDE.md, CONTEXT_INDEX.md y active_task.md como contexto base.
Coder: no modifica migraciones sin revisar docs/architecture/sdd.md.
```

## Roles Base

- Manager: clasifica tarea y contexto.
- Coder: implementa dentro del alcance.
- Reviewer: revisa calidad y riesgo.
- Debugger: investiga causa raiz.

## Ajustes Locales

- Manager:
- Coder:
- Reviewer:
- Debugger:

## Nota de uso

Si este archivo contradice `OPERACION/AGENTS/*.md`, gana el contrato global salvo decision documentada.
