# Hechos

> Hechos confirmados y compactos para un proyecto instanciado desde esta plantilla.

Este archivo guarda informacion estable que una persona o agente no deberia redescubrir cada vez que trabaja. Debe ser breve, verificable y vigente.

## Que Contiene

Hechos confirmados del proyecto, entornos, integraciones, datos de ejecucion y problemas vigentes que afectan trabajo futuro.

## Orden de Uso

Completar despues de que existan hechos reales. Consultar cuando una tarea pueda depender de contexto previo o problemas conocidos.

## Relacion con Otros Documentos

No duplica OpenSpec ni arquitectura. Si un hecho se vuelve regla funcional, moverlo a OpenSpec. Si describe estructura estable, moverlo a `docs/architecture/system.md`.

## Proyecto

- Nombre: Por definir
- Usuario principal: Por definir
- Entornos de ejecucion: Por definir
- Integraciones: Por definir

## Datos de Ejecucion

- Por definir

## Integraciones

- Por definir

## Problemas Vigentes

Registrar solo problemas que sigan siendo relevantes para investigacion, implementacion o soporte.

| Problema | Impacto | Mitigacion |
|---|---|---|
| Por definir | Por definir | Por definir |

## Ejemplo Minimo

```markdown
## Proyecto

- Nombre: Portal Interno de Solicitudes.
- Usuario principal: coordinadores de operaciones.
- Entornos de ejecucion: local y staging.
- Integraciones: correo interno para notificaciones.

## Problemas Vigentes

| Problema | Impacto | Mitigacion |
|---|---|---|
| El entorno staging no tiene datos representativos. | Las pruebas manuales pueden ser incompletas. | Usar fixtures controlados antes de validar releases. |
```

## Criterio de Entrada

Agregar un hecho solo si esta confirmado y cambia decisiones futuras. Si es una opinion, una tarea pendiente o una hipotesis, no pertenece aqui.

## Regla Breve

Hechos es memoria de trabajo durable, no historia completa.
