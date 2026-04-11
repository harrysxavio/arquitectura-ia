# Ejemplo: Nuevo Feature

> Caso prÃ¡ctico que muestra cÃ³mo el framework maneja una nueva funcionalidad.

## SituaciÃ³n
"Agregar validaciÃ³n para no permitir Ã³rdenes de clientes bloqueados."

## ClasificaciÃ³n por el Manager
- **Tipo**: Feature.
- **Nivel**: 2 (funcionalidad media, requiere spec).
- **Agente asignado**: Coder â†’ Reviewer.

## Contexto Cargado (segÃºn OPERACION/CONTEXT_ROUTER.md)

### Contexto mÃ­nimo (siempre)
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `active_task.md`

### Contexto dirigido (Nivel 2)
- `docs/product/spec.md`
- `OPERACION/CONSTRAINTS/process_constraints.md`
- `skills/plan-change.md`
- `skills/python-backend.md`
- `docs/engineering/coding_standards.md`
- Archivos afectados del caso de uso.

## Flujo de EjecuciÃ³n

1. **Manager** clasifica como feature Nivel 2.
2. **Manager** verifica que existe `spec.md` actualizada con la regla de negocio.
3. **Coder** lee spec: `Si customer.status = blocked â†’ orden rechazada con mensaje`.
4. **Coder** implementa validaciÃ³n en el servicio de Ã³rdenes.
5. **Coder** agrega test unitario para el caso.
6. **Reviewer** valida:
   - âœ… Cumple la regla de negocio.
   - âœ… No afecta flujo de clientes activos.
   - âœ… Mensaje de error es claro.
   - âœ… Test cubre ambos escenarios.

## Post-EjecuciÃ³n
- Se actualiza `memory/patterns.md` si la validaciÃ³n establece un nuevo patrÃ³n.
- Se registra en `decision_log.md`: "ValidaciÃ³n de bloqueo implementada a nivel de servicio, no de base de datos."

