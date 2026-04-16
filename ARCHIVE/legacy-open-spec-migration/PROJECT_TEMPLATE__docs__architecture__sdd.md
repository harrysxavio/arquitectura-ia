# SDD - Diseno Tecnico

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Describir el diseno tecnico vigente o propuesto para un cambio estructural, multiarchivo o de impacto relevante.

## Como llenarlo

Usar para decisiones tecnicas que afectan componentes, contratos, datos, migraciones, integraciones o riesgos. No repetir la spec funcional; enlazarla cuando corresponda.

## Ejemplo minimo

```text
Decision tecnica: Mover validacion de estado de cliente al servicio de ordenes.
Impacto: API y tests del servicio de ordenes.
Validacion: Tests unitarios y caso de rechazo.
```

## Contexto

## Referencias

- Spec:
- Decision:

## Decision Tecnica

## Arquitectura Propuesta

## Componentes Impactados

## Contratos / Interfaces

## Datos y Migraciones

## Riesgos

## Validacion

## Nota de uso

Si el diseno se aprueba, registrar la decision en `decisions/decision_log.md` o una ADR.
