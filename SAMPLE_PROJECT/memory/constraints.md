# Constraints

> Ejemplo rellenado. Restricciones vigentes que limitan decisiones.

## Tecnicas

- No construir una app completa dentro de `SAMPLE_PROJECT/`.
- No agregar dependencias tecnicas salvo que sean necesarias para explicar el flujo.
- Mantener `src/` como apoyo ilustrativo y opcional.
- No usar `graphify-out/*` como fuente de verdad.

## Negocio

- El ejemplo cubre solo solicitudes internas de operaciones.
- No modelar soporte a clientes finales.
- No registrar datos reales de personas, clientes ni incidentes.

## Seguridad

- No guardar credenciales, tokens ni secretos en Markdown.
- `.env.example` puede mostrar nombres de variables ficticias, nunca valores reales.
- Solicitudes de seguridad deben partir con prioridad alta.

## Costo

- No agregar servicios pagos ni hosting.
- No asumir herramientas externas como obligatorias salvo Markdown, Git y el agente principal elegido por el usuario.

## Nota de uso

Cuando una restriccion provenga de una decision, enlazar o mencionar la referencia en `decisions/decision_log.md`.

