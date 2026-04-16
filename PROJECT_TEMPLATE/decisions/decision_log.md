# Registro de Decisiones

> Plantilla. Indice breve de decisiones aprobadas y vigentes.

Este archivo resume decisiones durables sin convertir cada una en un documento largo. Debe permitir entender que direccion esta aprobada, que impacto tiene y donde leer mas si hace falta.

## Que Contiene

Una tabla breve de decisiones vigentes: fecha, decision, impacto y referencia. No contiene backlog ni discusion extensa.

## Orden de Uso

Consultar antes de cambiar arquitectura, herramientas, costos, seguridad o convenciones importantes. Actualizar cuando se aprueba una direccion durable.

## Relacion con Otros Documentos

ADRs amplian decisiones complejas. OpenSpec justifica cambios funcionales activos. Memoria puede registrar restricciones derivadas de una decision.

| Fecha | Decision | Impacto | Referencia |
|---|---|---|---|
| YYYY-MM-DD | Por definir | Por definir | `decisions/adr/...` u `openspec/changes/...` |

## Ejemplo Minimo

```markdown
| Fecha | Decision | Impacto | Referencia |
|---|---|---|---|
| 2026-01-15 | Usar SQLite en la primera version. | Reduce infraestructura inicial; puede requerir migracion futura. | `decisions/adr/0001-usar-sqlite-inicialmente.md` |
| 2026-01-20 | Mantener cambios funcionales en OpenSpec. | Evita reglas dispersas en README y memoria. | `openspec/changes/...` |
```

## Regla

Mantener este archivo breve. Usar ADRs para decisiones estructurales o de alto impacto y cambios OpenSpec para la justificacion de cambios activos.

## Cuando Agregar una Decision

Agregar una fila cuando el equipo elige una direccion que afectara trabajo futuro: arquitectura, herramienta, restriccion, proceso o estrategia. No registrar tareas pequenas ni conversaciones transitorias.

## Cuando Crear un ADR

Crear un ADR si la decision necesita contexto, alternativas, compensaciones o consecuencias. Si una fila basta para entenderla, no hace falta ADR.

## Regla Breve

El registro evita rediscutir decisiones; no reemplaza OpenSpec ni backlog.
