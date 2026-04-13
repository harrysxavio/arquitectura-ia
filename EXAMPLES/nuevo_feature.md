# Ejemplo: Nuevo Feature

> [!NOTE]
> Caso practico que muestra como el framework maneja una nueva funcionalidad.

## Situacion
"Agregar validacion para no permitir ordenes de clientes bloqueados."

## Clasificacion por el Manager
- **Tipo**: Feature.
- **Nivel**: 2 (funcionalidad media, requiere spec).
- **Agente asignado**: Coder -> Reviewer.

## Contexto Cargado (segun OPERACION/CONTEXT_ROUTER.md)

### Contexto minimo (siempre)
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

## Flujo de Ejecucion

1. **Manager** clasifica como feature Nivel 2.
2. **Manager** verifica que existe `spec.md` actualizada con la regla de negocio.
3. **Coder** lee spec: `Si customer.status = blocked -> orden rechazada con mensaje`.
4. **Coder** implementa validacion en el servicio de ordenes.
5. **Coder** agrega test unitario para el caso.
6. **Reviewer** valida:
   - Cumple la regla de negocio.
   - No afecta flujo de clientes activos.
   - Mensaje de error es claro.
   - Test cubre ambos escenarios.

## Post-Ejecucion
- Se actualiza `memory/patterns.md` si la validacion establece un nuevo patron.
- Se registra en `decision_log.md`: "Validacion de bloqueo implementada a nivel de servicio, no de base de datos."
