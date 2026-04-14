# Constraints

> Ejemplo rellenado. Restricciones vigentes que limitan decisiones.

## Tecnicas

- No construir una app completa ni productiva dentro de `SAMPLE_PROJECT/`.
- No agregar dependencias runtime externas para la mini app.
- Mantener `src/` pequeno y alineado con la documentacion canonica.
- No tratar `data/requests.json` como fuente canonica.
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
- No asumir servicios pagos ni hosting. Graphify puede requerir instalacion local para regenerar `graphify-out/`.

## Nota de uso

Cuando una restriccion provenga de una decision, enlazar o mencionar la referencia en `decisions/decision_log.md`.
