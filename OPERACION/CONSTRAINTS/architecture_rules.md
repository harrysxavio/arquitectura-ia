# RESTRICCIONES: Arquitectura

Estas reglas mantienen separada la arquitectura estable de las reglas funcionales y de la memoria compacta.

## Base Obligatoria de Proyecto

- `AGENTS.md`
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `openspec/specs/*/spec.md`
- `docs/architecture/system.md`
- `decisions/decision_log.md`
- `memory/facts.md`
- `memory/constraints.md`
- `memory/patterns.md`

## Reglas

- OpenSpec gobierna comportamiento funcional y cambios activos.
- La arquitectura estable vive en un unico documento de sistema.
- Las decisiones se mantienen breves salvo que un ADR este justificado.
- Graphify es derivado y no puede reemplazar fuentes canonicas.

## Como Aplicarlo

`docs/architecture/system.md` debe explicar componentes, limites, contratos, datos, integraciones y validacion tecnica. No debe convertirse en una segunda spec funcional. Si una regla describe que debe hacer el sistema ante un actor o escenario, pertenece a OpenSpec.

Las decisiones estructurales durables deben aparecer en `decisions/decision_log.md`; si requieren contexto, alternativas o compensaciones, usar un ADR.

## Error Comun

Usar arquitectura como cajon general. Cuando un documento de arquitectura contiene reglas funcionales, decisiones historicas, backlog y memoria, deja de orientar. El objetivo es que cada seccion tenga una responsabilidad estable.

## Regla Breve

Arquitectura dice como esta armado; OpenSpec dice que comportamiento debe cumplir.
