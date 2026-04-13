# ADR: Documentar triage en Markdown antes de automatizar

## Estado

`aceptada`

## Contexto

La Mesa Interna de Soporte Operativo necesita ordenar solicitudes, prioridades y cierres. Aun no hay evidencia suficiente para justificar una app completa, una base de datos o integraciones externas.

El mayor riesgo actual es automatizar reglas que todavia no estan claras. El equipo necesita una fuente simple y versionada para discutir el flujo con agentes y personas.

## Decision

Mantener el flujo de triage como documentacion canonica en Markdown antes de construir automatizaciones tecnicas.

La verdad funcional vive en `docs/product/spec.md`. El diseno tecnico vive en `docs/architecture/sdd.md` solo cuando el cambio tenga impacto tecnico. `src/sample_flow.py` queda como ejemplo opcional para explicar el flujo, no como implementacion productiva.

## Alternativas consideradas

- Construir primero una API pequena: descartado porque aumenta costo antes de validar reglas.
- Usar una hoja de calculo como fuente principal: descartado porque separa decisiones y memoria del repo.
- Documentar el flujo en Markdown: aceptado porque mantiene trazabilidad y es facil de leer por humanos y agentes.

## Consecuencias

- Las reglas deben actualizarse en `docs/product/spec.md` antes de tocar codigo.
- Las decisiones relevantes deben registrarse en `decisions/decision_log.md`.
- Los cambios de patron o restriccion deben reflejarse en `memory/`.
- La automatizacion futura tendra una base documental clara.

## Referencias

- `docs/product/spec.md`
- `docs/architecture/sdd.md`
- `decisions/decision_log.md`
- `memory/patterns.md`

## Nota de uso

Si en el futuro se decide construir una app real, crear una ADR nueva para stack, persistencia, despliegue y contratos.

