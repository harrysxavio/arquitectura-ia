# Spec de Capacidad de Ejemplo

> Plantilla OpenSpec. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Describe el comportamiento aprobado y visible para usuarios de una capacidad del proyecto.

Esta spec de ejemplo muestra la convencion de idioma del framework: el contenido humano esta en español y las keywords estructurales de OpenSpec pueden mantenerse en ingles por compatibilidad.

## Como Usarla

Copiar esta estructura para una capacidad real y reemplazar el ejemplo por reglas del dominio. Cada requirement debe describir una obligacion del sistema; cada scenario debe mostrar una situacion verificable.

No usar la spec para detallar arquitectura interna, librerias o decisiones de implementacion. Esos detalles viven en `docs/architecture/system.md` o en el `design.md` de un cambio.

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

## Checklist de Calidad

- El lector entiende que capacidad se gobierna.
- Los requirements son observables.
- Los scenarios tienen condiciones y resultados claros.
- No hay detalles tecnicos que pertenezcan a arquitectura.
