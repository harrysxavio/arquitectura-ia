# RESTRICCIONES: Flujo y Ejecucion

## Flujo Base

1. Clasificar tipo de tarea y riesgo.
2. Cargar contexto minimo mediante `OPERACION/CONTEXT_ROUTER.md`.
3. Usar specs OpenSpec para comportamiento aprobado.
4. Usar cambios OpenSpec para trabajo activo.
5. Validar con tests o revisiones documentales.
6. Actualizar decisiones o memoria solo cuando cambie conocimiento durable.

## Reglas

- Los cambios funcionales requieren una spec o cambio OpenSpec relevante.
- Los cambios estructurales requieren contexto de arquitectura y, si son durables, una entrada de decision o ADR.
- No cerrar trabajo amplio sin validacion.
