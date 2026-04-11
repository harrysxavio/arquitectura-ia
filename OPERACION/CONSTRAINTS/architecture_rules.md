# CONSTRAINTS: Arquitectura y Estructura

## Separacion Obligatoria

- El framework global reusable vive en este repo.
- Un proyecto activo real vive en un repo instanciado desde `PROJECT_TEMPLATE/`.
- `PROJECT_TEMPLATE/` es molde, no fuente de verdad operativa.
- Obsidian y NotebookLM son conocimiento satelite, no nucleo oficial.

## Proyecto Activo

Todo proyecto instanciado debe tener:

- `AGENTS.md`
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `tasks/current/active_task.md`
- `decisions/decision_log.md`
- `memory/project_facts.md`

Si falta alguno, el proyecto esta incompleto para operacion disciplinada.

## Fuente de Verdad

- Estructura del proyecto: `PROJECT_GUIDE.md`
- Ruta de consulta: `CONTEXT_INDEX.md`
- Trabajo actual: `tasks/current/active_task.md`
- Decisiones: `decisions/decision_log.md`
- Hechos vigentes: `memory/project_facts.md`
- Diseno tecnico: `docs/architecture/sdd.md`
- Contexto estructural derivado: `graphify-out/*`

## Graphify

- Graphify puede orientar exploracion arquitectonica, onboarding y refactors.
- Graphify no reemplaza SDD, decision log, spec ni memoria.
- En tareas estructurales, usar Graphify antes de exploracion amplia de modulos.

## No Ruido

- No crear documentos que ningun agente o humano usara.
- Todo documento operativo debe aparecer en `CONTEXT_INDEX.md`.
- No mantener duplicacion por respeto historico.

## Seguridad Basica

- No guardar credenciales reales en Markdown, logs o decisiones.
- Referenciar secretos, no escribirlos.
- Mantener `.env.example` con valores dummy cuando aplique.
- Excluir `.env`, `.env.*` y credenciales locales cuando el proyecto use Git.
