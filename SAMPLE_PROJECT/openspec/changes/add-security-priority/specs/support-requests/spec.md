# Delta de Spec de Solicitudes de Soporte

## ADDED Requirements

### Requirement: Solicitudes de seguridad empiezan con prioridad alta

El sistema SHALL asignar prioridad alta a toda nueva solicitud de seguridad.

#### Scenario: Nueva solicitud de seguridad

- WHEN se crea una solicitud con tipo `seguridad`
- THEN su prioridad inicial es `alta`
