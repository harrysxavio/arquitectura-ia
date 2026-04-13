# SPEC - Especificacion Funcional

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Definir la verdad funcional de una feature, flujo o regla de negocio.

## Como llenarlo

Completar cuando el cambio involucra usuario, comportamiento, regla de negocio o criterio de aceptacion. Mantenerlo orientado a resultado, no a implementacion tecnica.

## Ejemplo minimo

```text
Objetivo: Impedir ordenes de clientes bloqueados.
Regla: Si customer.status = blocked, rechazar la orden.
Criterio: El sistema muestra un mensaje claro y no crea la orden.
```

## Objetivo

## Problema

## Usuario / Actor

## Alcance

## No Alcance

## Reglas de Negocio

-

## Casos de Uso

- Usuario hace X -> Sistema responde Y.
- Usuario hace Z -> Sistema rechaza con mensaje.

## Criterios de Aceptacion

- [ ]

## Riesgos Funcionales

-

## Dependencias

- TBD

## Nota de uso

Si una decision funcional cambia arquitectura, crear o actualizar tambien `docs/architecture/sdd.md` y `decisions/decision_log.md`.
