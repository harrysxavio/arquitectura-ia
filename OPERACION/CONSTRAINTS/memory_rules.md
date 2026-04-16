# RESTRICCIONES: Memoria

## Memoria Oficial

- `memory/facts.md`: hechos confirmados y problemas vigentes.
- `memory/constraints.md`: limites tecnicos, de negocio, seguridad y costo vigentes.
- `memory/patterns.md`: patrones y antipatrones aprobados.
- `memory/glossary.md`: terminos opcionales del dominio.
- `decisions/decision_log.md`: indice breve de decisiones aprobadas.

## Reglas

- La memoria es compacta, vigente y accionable.
- La memoria no duplica OpenSpec ni arquitectura.
- El contexto derivado debe validarse antes de convertirse en memoria.

## Que Debe Entrar

Entra conocimiento que evita redescubrimiento futuro: restricciones reales, decisiones ya asumidas, patrones de implementacion y hechos confirmados del proyecto. Debe ser corto y util para una tarea futura.

## Que No Debe Entrar

No entra backlog, diario de sesion, ideas sin validar, reglas funcionales completas ni historia archivada. Si algo describe comportamiento del sistema, debe ir a OpenSpec. Si describe estructura estable, debe ir a arquitectura.

## Regla Breve

Memoria no es donde se guarda todo; es donde se guarda lo que conviene recordar para decidir mejor.
