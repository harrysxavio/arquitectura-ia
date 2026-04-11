# Politica Oficial de Graphify

## Rol

Graphify es la capa central de contexto estructural persistente. Su funcion es orientar navegacion, onboarding, investigacion interna, analisis de impacto y refactors amplios.

Sus outputs son derivados. Ayudan a leer mejor el repo, pero no reemplazan documentos canonicos.

## Prioridad

Usar Graphify con prioridad alta en:

- arquitectura,
- onboarding,
- investigacion interna del repo,
- impacto transversal,
- refactors amplios,
- tareas ambiguas,
- revision multi-modulo.

No usarlo por defecto en:

- typos,
- cambios locales obvios,
- ajustes visuales menores,
- renombres acotados,
- fixes con archivo afectado ya claro.

## Orden en Tareas Estructurales

Para tareas estructurales o ambiguas, Graphify entra despues del contexto base y del router, pero antes de exploracion amplia:

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`
4. `OPERACION/CONTEXT_ROUTER.md`
5. `graphify-out/GRAPH_REPORT.md` o `graphify-out/graph.json`
6. `docs/product/spec.md`
7. `docs/architecture/sdd.md`
8. `decisions/decision_log.md`
9. `memory/constraints.md` y `memory/patterns.md`
10. Modulos impactados

## Limites

- No es fuente de verdad oficial.
- No reemplaza `PROJECT_GUIDE.md`.
- No reemplaza `CONTEXT_INDEX.md`.
- No reemplaza `spec.md`, `sdd.md`, `decision_log.md` ni memoria oficial.
- Si esta desactualizado, debe marcarse como stale y regenerarse antes de usarlo para decisiones estructurales.

## Gobernanza

Si Graphify revela una relacion o patron que debe gobernar el proyecto, registrar esa informacion en:

- `CONTEXT_INDEX.md`,
- `docs/architecture/sdd.md`,
- `decisions/decision_log.md`,
- `memory/patterns.md`.
