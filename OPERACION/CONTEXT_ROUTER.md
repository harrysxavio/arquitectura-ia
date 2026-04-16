# CONTEXT_ROUTER.md - Router de Contexto OpenSpec-First

Este archivo es la autoridad para decidir que contexto debe cargar un agente.

## Protocolo Base

1. Identificar tipo de tarea y complejidad.
2. Cargar `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md` al trabajar dentro de un proyecto.
3. Para comportamiento, cargar la spec relevante en `openspec/specs/*/spec.md`.
4. Para trabajo activo, cargar el cambio relevante en `openspec/changes/*`.
5. Agregar arquitectura, decisiones, memoria o Graphify solo cuando este justificado.

## Niveles

| Nivel | Criterio | Contexto requerido |
|---|---|---|
| 1 | Local, claro, bajo riesgo | Contexto base + archivo afectado |
| 2 | Funcional o multarchivo | Contexto base + spec/cambio OpenSpec relevante |
| 3 | Estructural, ambiguo o amplio | Nivel 2 + `docs/architecture/system.md` + decisiones/memoria + Graphify si aporta |

## Matriz de Tareas

| Tipo | Empezar con | Agregar cuando haga falta |
|---|---|---|
| bug | archivo afectado, tests, spec relevante | `memory/facts.md`, Graphify si el impacto es amplio |
| funcionalidad | spec relevante y cambio activo | arquitectura, decisiones, patrones |
| refactor | arquitectura y modulos afectados | Graphify para impacto entre modulos |
| docs | documento objetivo y fuente canonica | OpenSpec o arquitectura como fuente |
| revision | diff y spec/cambio relevante | decisiones, arquitectura, tests |
| investigacion | objetivo y fuente | resultado compacto en memoria o docs si se vuelve canonico |

## Orden de Autoridad

1. `AGENTS.md`
2. `openspec/changes/*` activo
3. `openspec/specs/*/spec.md`
4. `docs/architecture/system.md`
5. `decisions/decision_log.md`
6. `decisions/adr/*.md`
7. `memory/constraints.md`
8. `memory/facts.md`
9. `memory/patterns.md`
10. `graphify-out/*` solo como contexto derivado

## Prohibiciones

- No cargar carpetas amplias por defecto.
- No duplicar reglas funcionales fuera de OpenSpec.
- No usar Graphify como autoridad.
- No usar material heredado archivado como fuente activa.
