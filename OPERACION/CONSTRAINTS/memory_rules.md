# CONSTRAINTS: Memoria y Persistencia

## Fuentes Oficiales de Memoria

- `memory/project_facts.md`: hechos vigentes.
- `memory/constraints.md`: restricciones tecnicas, de negocio, acceso, seguridad o costo.
- `memory/known_issues.md`: problemas conocidos y workarounds.
- `memory/patterns.md`: patrones aprobados.
- `memory/glossary.md`: terminos del dominio.
- `decisions/decision_log.md`: decisiones cronologicas.

## Regla de No Duplicacion

Una idea debe vivir en un solo lugar canonico. Si aparece en Graphify, Obsidian o research externo y debe gobernar el proyecto, debe volver al repo en la fuente oficial correspondiente.

## Graphify

- `graphify-out/*` es memoria estructural derivada, no memoria canonica.
- Puede ayudar a descubrir relaciones, dependencias y zonas de impacto.
- No debe usarse para sustituir decisiones, hechos, restricciones o patrones aprobados.

## Conocimiento Satelite

- Obsidian: notas personales, mapas, comparativas y visualizacion humana. No es fuente oficial.
- NotebookLM: research sobre fuentes externas. No es memoria viva del repo.
- El repo del proyecto activo es siempre la fuente oficial para tareas, decisiones, memoria y documentacion tecnica.

## Actualizacion

Al cerrar una tarea importante, evaluar si corresponde actualizar:

- `decisions/decision_log.md`
- `memory/project_facts.md`
- `memory/constraints.md`
- `memory/known_issues.md`
- `memory/patterns.md`
- `CONTEXT_INDEX.md`
