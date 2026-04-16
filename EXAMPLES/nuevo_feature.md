# Ejemplo: Nueva Funcionalidad

## Contexto

Una funcionalidad empieza como cambio OpenSpec.

## Problema que Resuelve

Este flujo evita que una feature empiece directamente en codigo. Primero se documenta intencion, alcance y delta funcional; luego se diseña e implementa.

## Flujo

1. Crear o seleccionar `openspec/changes/<change-id>/proposal.md`.
2. Agregar deltas funcionales bajo `openspec/changes/<change-id>/specs/`.
3. Agregar `design.md` si cambian arquitectura, datos o contratos.
4. Registrar la ejecucion en `tasks.md` dentro del cambio.
5. Actualizar las specs estables despues de aprobacion/archivo.
6. Mantener memoria y decisiones compactas.

## Cierre

La funcionalidad queda lista cuando el cambio OpenSpec, la implementacion y la validacion cuentan la misma historia.
