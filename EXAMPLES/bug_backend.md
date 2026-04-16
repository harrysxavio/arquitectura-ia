# Ejemplo: Investigacion de Bug

## Contexto

Empieza con `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, logs/tests afectados y la spec OpenSpec relevante si hay comportamiento involucrado.

## Problema que Resuelve

Este flujo evita investigar un bug desde el codigo solamente. Primero confirma que se esperaba, luego reproduce, y recien despues cambia archivos.

## Flujo

1. Confirmar el comportamiento esperado en OpenSpec.
2. Reproducir con tests enfocados.
3. Inspeccionar el codigo afectado.
4. Usar memoria compacta solo si importan hechos o restricciones previas.
5. Usar Graphify solo si el impacto es amplio o la propiedad no esta clara.
6. Registrar decisiones durables en `decisions/decision_log.md` o en un ADR.

## Cierre

El bug queda bien cerrado cuando hay evidencia de reproduccion, cambio acotado, validacion y, si corresponde, actualizacion de OpenSpec o memoria.
