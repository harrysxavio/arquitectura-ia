# Patrones

> Patrones compactos de implementacion y documentacion.

Este archivo registra formas aprobadas de trabajar que conviene repetir. Sirve para consistencia, no para reemplazar arquitectura ni OpenSpec.

## Que Contiene

Patrones aprobados y antipatrones que el equipo quiere evitar. Deben ser accionables y repetibles.

## Orden de Uso

Consultar durante implementacion o revision cuando haga falta consistencia. Actualizar solo cuando un patron ya fue validado por uso real.

## Relacion con Otros Documentos

Arquitectura describe estructura; patrones describen formas habituales de trabajar. OpenSpec sigue gobernando comportamiento funcional.

## Aprobados

- Poner comportamiento funcional en `openspec/specs/*/spec.md`.
- Poner trabajo de cambio activo en `openspec/changes/*`.
- Poner arquitectura estable en `docs/architecture/system.md`.
- Mantener `decision_log.md` breve y vigente.
- Usar Graphify solo como contexto de navegacion derivado.

## Evitar

- Duplicar reglas funcionales fuera de OpenSpec.
- Usar memoria como backlog.
- Tratar salidas derivadas como autoridad.

## Ejemplo Minimo

```markdown
## Aprobados

- Toda regla funcional nueva empieza en `openspec/changes/*`.
- Los tests de dominio usan nombres alineados con los escenarios OpenSpec.
- Los ADRs se usan solo para decisiones estructurales durables.

## Evitar

- Crear documentos paralelos para cambios activos.
- Guardar tareas pendientes en memoria.
```

## Cuando Actualizar

Actualizar cuando el equipo descubre una forma de trabajo que se repite y reduce errores: estructura de tests, forma de documentar cambios, convenciones de modulos o patrones de validacion.

No actualizar por cada preferencia puntual. Un patron debe ser estable, util y accionable.

## Regla Breve

Un patron dice "asi trabajamos normalmente"; si define comportamiento del sistema, pertenece a OpenSpec.
