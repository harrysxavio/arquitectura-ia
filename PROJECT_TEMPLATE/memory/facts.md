# Hechos

> Hechos confirmados y compactos para un proyecto instanciado desde esta plantilla.

Este archivo guarda informacion estable que una persona o agente no deberia redescubrir cada vez que trabaja. Debe ser breve, verificable y vigente.

## Que Contiene

Hechos confirmados del proyecto, entornos, integraciones y datos de ejecucion que afectan trabajo futuro.

## Orden de Uso

Completar despues de que existan hechos reales. Consultar cuando una tarea pueda depender de contexto previo o problemas conocidos.

## Relacion con Otros Documentos

No duplica OpenSpec ni arquitectura. Si un hecho se vuelve regla funcional, moverlo a OpenSpec. Si describe estructura estable, moverlo a `docs/architecture/system.md`. Si es un problema vigente, registrarlo en `memory/known_issues.md`.

## Proyecto

- Nombre: Por definir
- Usuario principal: Por definir
- Entornos de ejecucion: Por definir
- Integraciones: Por definir

## Datos de Ejecucion

- Por definir

## Integraciones

- Por definir

## Ejemplo Minimo

```markdown
## Proyecto

- Nombre: Portal Interno de Solicitudes.
- Usuario principal: coordinadores de operaciones.
- Entornos de ejecucion: local y staging.
- Integraciones: correo interno para notificaciones.

## Datos de Ejecucion

- Staging usa fixtures controlados; no contiene datos productivos.
```

## Criterio de Entrada

Agregar un hecho solo si esta confirmado y cambia decisiones futuras. Si es una opinion, una tarea pendiente, una hipotesis o un problema por resolver, no pertenece aqui.

## Regla Breve

Hechos es memoria de trabajo durable, no historia completa.
