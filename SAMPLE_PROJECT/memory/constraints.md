# Restricciones

> Restricciones compactas para el ejemplo de mesa de soporte de SAMPLE_PROJECT.

## Tecnicas

- No convertir el ejemplo en app productiva.
- No agregar dependencias de ejecucion para la mini app.
- Mantener el codigo pequeno y alineado con OpenSpec.
- No tratar JSON de ejecucion como canonico.
- No tratar salida de Graphify como fuente de verdad.

## Negocio

- Cubrir solo solicitudes internas de soporte operativo.
- No modelar soporte a clientes externos.
- No almacenar datos reales de personas, clientes ni incidentes.

## Seguridad

- No almacenar credenciales, tokens ni secretos en Markdown.
- `.env.example` puede contener solo nombres de variables dummy.

## Costo

- No agregar servicios pagos ni hosting.
