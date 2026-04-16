# Diseno: Agregar Prioridad de Seguridad

## Contexto

La app de ejemplo es una CLI pequena de Python con modulos de biblioteca estandar. La arquitectura estable vive en `docs/architecture/system.md`; este archivo cubre solo el cambio activo.

## Decision

Mantener la regla de prioridad de seguridad en OpenSpec y reflejarla en la funcion de triage existente. No introducir API, migracion de base de datos ni dependencia nueva.

## Impacto

- `src/triage.py` contiene el calculo de prioridad inicial.
- `tests/test_triage.py` valida la regla de prioridad de seguridad.
- `app.py` demuestra el flujo mediante `demo`, `create`, `list` y `close`.

## Datos

No hay cambio de esquema persistente. `data/requests.json` sigue siendo dato de ejecucion de ejemplo.

## Validacion

- Ejecutar tests unitarios desde `SAMPLE_PROJECT/`.
- Ejecutar el demo CLI.
- Confirmar que Graphify sigue siendo solo contexto derivado.
