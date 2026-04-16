# Spec de Solicitudes de Soporte

> Fuente funcional canonica del flujo de solicitudes de `SAMPLE_PROJECT/`.

## Proposito

Definir como se crean, clasifican, priorizan, asignan y cierran solicitudes internas de soporte operativo en la mini app pedagogica por CLI.

## Actores

- Solicitante interno: reporta una necesidad operativa.
- Coordinador de operaciones: clasifica y asigna la solicitud.
- Responsable asignado: resuelve, bloquea o escala la solicitud.

## Alcance

- Crear solicitudes con titulo, descripcion, area y tipo.
- Clasificar tipo como `soporte`, `acceso`, `datos`, `seguridad` u `otro`.
- Registrar prioridad como `baja`, `media`, `alta` o `critica`.
- Registrar estado como `nueva`, `en triage`, `asignada`, `bloqueada` o `cerrada`.
- Asignar responsable cuando corresponda.
- Cerrar una solicitud con una nota breve.
- Usar JSON local solo como persistencia de ejecucion del ejemplo.

## Fuera de Alcance

- SLA contractual.
- Notificaciones automaticas.
- Adjuntos obligatorios.
- Portal web productivo.
- Integraciones externas.
- Tratar el JSON de ejecucion como autoridad del proyecto.

## Requirements

### Requirement: Crear solicitud de soporte

El sistema SHALL crear una solicitud interna con titulo, descripcion, area solicitante y tipo de solicitud.

#### Scenario: Se crea una solicitud de acceso

- WHEN un solicitante crea una solicitud de acceso
- THEN la solicitud queda registrada con tipo `acceso`
- AND el estado inicial permite triage

### Requirement: Priorizar solicitudes de seguridad

El sistema SHALL iniciar toda solicitud de seguridad con prioridad alta.

#### Scenario: Solicitud de seguridad inicia alta

- WHEN se crea una solicitud con tipo `seguridad`
- THEN la prioridad inicial es `alta`

### Requirement: Exigir responsable antes de sacar solicitud critica de triage

El sistema SHALL exigir responsable antes de que una solicitud critica salga de triage.

#### Scenario: Solicitud critica sin responsable permanece en triage

- WHEN una solicitud critica no tiene responsable
- THEN no debe avanzar a trabajo asignado

### Requirement: Exigir motivo de bloqueo

El sistema SHALL exigir un motivo claro cuando una solicitud se marca como bloqueada.

#### Scenario: Responsable no puede avanzar

- WHEN un responsable marca una solicitud como bloqueada
- THEN la solicitud registra el motivo de bloqueo

### Requirement: Exigir nota de cierre

El sistema SHALL exigir una nota breve al cerrar una solicitud.

#### Scenario: Solicitud cerrada con nota

- WHEN un responsable cierra una solicitud con nota
- THEN el estado de la solicitud pasa a `cerrada`

#### Scenario: Cierre sin nota rechazado

- WHEN un responsable intenta cerrar una solicitud sin nota
- THEN el sistema rechaza la operacion

### Requirement: Documentar cambios manuales de prioridad

El sistema SHALL permitir cambios manuales de prioridad solo cuando el coordinador registre el motivo.

#### Scenario: Coordinador cambia prioridad

- WHEN el coordinador cambia la prioridad manualmente
- THEN el motivo queda documentado en la solicitud o en el registro del cambio
