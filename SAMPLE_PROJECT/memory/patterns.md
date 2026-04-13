# Patterns

> Ejemplo rellenado. Patrones aprobados y anti-patrones del proyecto.

## Patrones Aprobados

- Documentar reglas funcionales primero en `docs/product/spec.md`.
- Registrar decisiones duraderas en `decisions/decision_log.md`.
- Usar ADR cuando una decision tenga alternativas, impacto o riesgo.
- Mantener memoria breve, vigente y accionable.
- Convertir insumos externos a Markdown con MarkItDown solo si aportan contexto real.
- Usar Graphify para orientacion estructural, no para gobernar reglas.

## Anti-Patrones

- Implementar una API antes de estabilizar reglas de triage.
- Copiar contenido convertido por MarkItDown directamente a memoria canonica sin revisar.
- Tratar `src/` como parte obligatoria del framework.
- Usar `graphify-out/*` como fuente de verdad.
- Duplicar teoria de `THEORY/` dentro del proyecto ejemplo.

## Nota de uso

Si un patron nace de una decision relevante, registrar tambien la decision en `decisions/decision_log.md`.

