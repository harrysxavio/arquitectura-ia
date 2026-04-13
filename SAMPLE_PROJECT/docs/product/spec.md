# SPEC - Mesa Interna de Soporte Operativo

> Ejemplo rellenado. Verdad funcional del flujo de solicitudes internas.

## Objetivo

Definir como se registran, clasifican, priorizan, asignan y cierran solicitudes internas de soporte operativo.

## Problema

Las solicitudes llegan por canales distintos y se pierden criterios de prioridad, responsables y cierre. El equipo necesita una forma simple de operar y documentar decisiones antes de automatizar.

## Usuario / Actor

- Solicitante interno: persona que reporta una necesidad operativa.
- Coordinador de operaciones: persona que clasifica y asigna la solicitud.
- Responsable asignado: persona que resuelve o escala la solicitud.

## Alcance

- Crear una solicitud con titulo, descripcion, area y tipo.
- Clasificarla por tipo: soporte, acceso, datos, seguridad u otro.
- Asignar prioridad: baja, media, alta o critica.
- Asignar responsable.
- Registrar estado: nueva, en triage, asignada, bloqueada, cerrada.
- Cerrar con una nota breve de resultado.

## No Alcance

- SLA contractual.
- Notificaciones automaticas.
- Adjuntos obligatorios.
- Portal web productivo.
- Integraciones con sistemas externos.

## Reglas de Negocio

- Una solicitud de tipo seguridad parte con prioridad alta.
- Una solicitud critica debe tener responsable asignado antes de salir de triage.
- Una solicitud bloqueada debe registrar motivo de bloqueo.
- Una solicitud cerrada debe incluir nota de cierre.
- La prioridad puede ajustarse manualmente si el coordinador documenta el motivo.

## Casos de Uso

- Solicitante crea solicitud de acceso -> coordinador clasifica como acceso, prioridad media y asigna responsable.
- Solicitante reporta incidente de seguridad -> sistema o coordinador la marca como seguridad y prioridad alta.
- Responsable no puede avanzar -> solicitud pasa a bloqueada con motivo claro.
- Responsable resuelve -> solicitud pasa a cerrada con nota de cierre.

## Criterios de Aceptacion

- [x] El flujo permite distinguir solicitudes nuevas, en triage, asignadas, bloqueadas y cerradas.
- [x] Las solicitudes de seguridad parten en prioridad alta.
- [x] El cierre requiere nota breve.
- [x] El ejemplo deja claro que el codigo en `src/` no es implementacion productiva.
- [x] Las reglas funcionales no dependen de Graphify.

## Riesgos Funcionales

- Prioridad manual puede generar criterios inconsistentes si no se revisa periodicamente.
- Una categoria "otro" demasiado usada puede ocultar necesidades de nuevas categorias.
- El flujo documentado puede quedar stale si se automatiza sin actualizar la spec.

## Dependencias

- `PROJECT_GUIDE.md`
- `docs/architecture/sdd.md`
- `decisions/decision_log.md`
- `memory/constraints.md`

## Nota de uso

Si una decision funcional cambia arquitectura, crear o actualizar tambien `docs/architecture/sdd.md` y `decisions/decision_log.md`.

