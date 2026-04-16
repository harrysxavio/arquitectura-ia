# RESTRICCIONES: Flujo y Ejecucion

Estas restricciones definen como avanzar desde una solicitud hasta un cierre verificable.

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

## Validacion Esperada

La validacion puede ser test automatizado, ejecucion manual, revision documental o chequeo de consistencia. Lo importante es que sea proporcional al riesgo y que quede claro que se verifico.

Para cambios documentales, validar significa revisar que no se duplican autoridades, que los enlaces conceptuales son correctos y que el documento ayuda a decidir o entender.

## Cierre Minimo

Al cerrar, registrar que cambio se hizo, que fuente lo justifico y como se valido. Si no se pudo validar, decirlo explicitamente.

## Regla Breve

Una tarea no termina cuando se edita un archivo; termina cuando el cambio queda entendible y verificable.
