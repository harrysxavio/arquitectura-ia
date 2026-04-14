# ADR: Documentar triage en Markdown antes de automatizar

## Estado

`aceptada`

## Contexto

La Mesa Interna de Soporte Operativo necesita ordenar solicitudes, prioridades y cierres. No hay evidencia suficiente para justificar una app completa, una base de datos productiva o integraciones externas.

El mayor riesgo es automatizar reglas que no tengan fuente canonica. El equipo necesita una fuente simple y versionada para discutir el flujo con agentes y personas, y tambien un laboratorio pequeno para validar Graphify sobre codigo real.

## Decision

Mantener el flujo de triage como documentacion canonica en Markdown antes de construir automatizaciones tecnicas.

La verdad funcional vive en `docs/product/spec.md`. El diseno tecnico vive en `docs/architecture/sdd.md` cuando el cambio tenga impacto tecnico. La automatizacion minima en `app.py` y `src/` debe alinearse con esos documentos, no gobernarlos.

`data/requests.json` es persistencia runtime del ejemplo. No es fuente canonica del proyecto.

## Alternativas consideradas

- Construir primero una API pequena: descartado porque aumenta costo antes de validar reglas.
- Usar una hoja de calculo como fuente principal: descartado porque separa decisiones y memoria del repo.
- Documentar el flujo en Markdown: aceptado porque mantiene trazabilidad y es facil de leer por humanos y agentes.
- Implementar una CLI minima despues de documentar: aceptado para validar Graphify y ejecucion real sin volver el ejemplo producto grande.

## Consecuencias

- Las reglas deben actualizarse en `docs/product/spec.md` antes de tocar codigo.
- Las decisiones relevantes deben registrarse en `decisions/decision_log.md`.
- Los cambios de patron o restriccion deben reflejarse en `memory/`.
- La automatizacion futura tendra una base documental clara.
- La CLI y los modulos Python deben mantenerse pequenos, pedagogicos y sin dependencias runtime externas.

## Referencias

- `docs/product/spec.md`
- `docs/architecture/sdd.md`
- `decisions/decision_log.md`
- `memory/patterns.md`

## Nota de uso

Si en el futuro se decide construir una app real, crear una ADR nueva para stack, persistencia, despliegue y contratos.
