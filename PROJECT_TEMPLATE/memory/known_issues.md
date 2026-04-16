# Problemas Conocidos

Este archivo es opcional. Usarlo solo si el proyecto necesita separar problemas vigentes de otros hechos de memoria.

## Proposito

Registrar problemas confirmados que afectan investigacion, soporte o priorizacion. Cada problema debe tener impacto y una mitigacion o proximo paso claro.

## Que Contiene

Problemas vigentes, impacto y mitigacion. No contiene historia cerrada ni backlog general.

## Orden de Uso

Consultar al investigar bugs o planificar cambios. Actualizar cuando un problema se confirma, se mitiga o deja de estar vigente.

## Relacion con Otros Documentos

Puede enlazar a OpenSpec si afecta comportamiento, a ADRs si implica decision estructural o a `memory/constraints.md` si crea una restriccion.

## Formato Sugerido

| Problema | Impacto | Mitigacion o seguimiento |
|---|---|---|
| Por definir | Por definir | Por definir |

## Ejemplo Minimo

```markdown
| Problema | Impacto | Mitigacion o seguimiento |
|---|---|---|
| La busqueda por texto no soporta acentos. | Usuarios pueden no encontrar solicitudes. | Crear cambio OpenSpec si se aprueba soporte de normalizacion. |
```

## Relacion con Otras Fuentes

- Si el problema describe comportamiento incorrecto, enlazar a OpenSpec o al cambio que lo corrige.
- Si implica deuda estructural, enlazar a arquitectura o decision.
- Si ya no esta vigente, eliminarlo o moverlo a historial fuera de fuentes activas.

## Regla Breve

Un problema conocido debe ayudar a actuar; si solo archiva historia, no pertenece aqui.
