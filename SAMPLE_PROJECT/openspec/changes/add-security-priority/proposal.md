# Propuesta: Agregar Prioridad de Seguridad

## Resumen

Usar cambios OpenSpec como flujo de cambio activo para el ejemplo y demostrar un cambio funcional sobre prioridad de solicitudes de seguridad.

## Problema

El flujo heredado guardaba tarea activa, plan de implementacion y preguntas abiertas en archivos de tareas separados. Eso duplicaba el rol de OpenSpec y obligaba a los agentes a cargar contexto extra.

## Objetivos

- Representar el cambio activo en OpenSpec.
- Mantener el comportamiento aprobado en la spec de solicitudes de soporte.
- Mostrar como se propone, disena y valida un cambio de regla funcional.
- Mantener el ejemplo pedagogico, no productivo.

## No Objetivos

- Construir una API productiva.
- Agregar una UI web.
- Agregar una base de datos productiva.
- Agregar integraciones externas.

## Alcance

- Confirmar que las solicitudes de seguridad empiezan con prioridad alta.
- Mantener JSON de ejecucion como datos de ejemplo no canonicos.
- Validar la CLI y los tests contra la spec aprobada.
