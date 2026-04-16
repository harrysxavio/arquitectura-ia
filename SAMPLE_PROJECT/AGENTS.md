# AGENTS.md

> Guia local de agentes para SAMPLE_PROJECT.

## Orden de Contexto

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `openspec/specs/support-requests/spec.md`
4. `openspec/changes/add-security-priority/` cuando se discuta el cambio de ejemplo
5. `docs/architecture/system.md` para estructura tecnica
6. `decisions/decision_log.md` y `memory/*` solo cuando haga falta
7. `graphify-out/*` para navegacion derivada en trabajo amplio o ambiguo

## Notas de Rol

- Manager: clasificar la tarea y elegir contexto minimo.
- Coder: implementar solo dentro de los limites aprobados por OpenSpec y arquitectura.
- Reviewer: verificar cambios contra OpenSpec, arquitectura, decisiones y tests.
- Debugger: inspeccionar sintomas, codigo y memoria compacta antes de ampliar alcance.

## Reglas

- No usar JSON de ejecucion como autoridad.
- No usar Graphify como autoridad.
- No expandir el ejemplo a sistema productivo sin un nuevo cambio aprobado.
