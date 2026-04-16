# Spec de Capacidad de Ejemplo

> Plantilla OpenSpec. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Describe el comportamiento aprobado y visible para usuarios de una capacidad del proyecto.

## Requirements

### Requirement: El comportamiento aprobado es explicito

El sistema SHALL mantener comportamiento funcional en OpenSpec para que humanos y agentes encuentren la regla vigente sin cargar documentos no relacionados.

#### Scenario: Accion exitosa

- WHEN el actor realiza una accion soportada
- THEN el sistema devuelve el resultado aprobado

#### Scenario: Accion rechazada

- WHEN el actor entrega una entrada no soportada
- THEN el sistema la rechaza con un resultado claro

## Notas

Mantener detalles de implementacion en `docs/architecture/system.md` o en el `design.md` de un cambio.
