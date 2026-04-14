# Patterns

> Ejemplo rellenado. Patrones aprobados y anti-patrones del proyecto.

## Patrones Aprobados

- Documentar reglas funcionales primero en `docs/product/spec.md`.
- Reflejar reglas documentadas en automatizacion minima solo despues de fijar la fuente canonica.
- Registrar decisiones duraderas en `decisions/decision_log.md`.
- Usar ADR cuando una decision tenga alternativas, impacto o riesgo.
- Mantener memoria breve, vigente y accionable.
- Convertir insumos externos a Markdown con MarkItDown solo si aportan contexto real.
- Usar Graphify para orientacion estructural, no para gobernar reglas.
- Usar `graphify update .` desde `SAMPLE_PROJECT/` como comando principal de regeneracion Graphify.
- Usar `unittest` y biblioteca estandar para mantener bajo el costo del ejemplo.

## Anti-Patrones

- Implementar una API antes de estabilizar reglas de triage.
- Tratar `data/requests.json` como fuente canonica.
- Copiar contenido convertido por MarkItDown directamente a memoria canonica sin revisar.
- Tratar `SAMPLE_PROJECT/` como plantilla de produccion.
- Usar `graphify-out/*` como fuente de verdad.
- Duplicar teoria de `THEORY/` dentro del proyecto ejemplo.

## Nota de uso

Si un patron nace de una decision relevante, registrar tambien la decision en `decisions/decision_log.md`.
