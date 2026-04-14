# Open Questions

> Ejemplo rellenado. Incluye preguntas que afectan alcance o reglas.

## Preguntas

- La prioridad de una solicitud debe calcularse automaticamente o asignarse manualmente?
- Las solicitudes de seguridad deben tener una categoria propia?
- El cierre requiere evidencia obligatoria?

## Respuestas

- 2026-04-13: Para este ejemplo, la prioridad se asigna manualmente con criterios documentados en `docs/product/spec.md`.
- 2026-04-13: Seguridad se modela como tipo de solicitud y siempre parte con prioridad alta.
- 2026-04-13: El cierre requiere una nota breve, pero no adjuntos obligatorios.
- 2026-04-13: La interfaz ejecutable sera una CLI simple en `app.py`.
- 2026-04-13: `data/requests.json` sera persistencia runtime del ejemplo, no fuente canonica.
- 2026-04-13: Graphify se ejecutara con `graphify update .` desde `SAMPLE_PROJECT/`.

## Nota de uso

Si una respuesta cambia una regla funcional, actualizar `docs/product/spec.md`. Si cambia una decision duradera, registrar en `decisions/decision_log.md`.
