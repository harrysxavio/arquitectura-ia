# Patrones

> Patrones y antipatrones aprobados y compactos para el ejemplo de mesa de soporte de SAMPLE_PROJECT.

## Aprobados

- Documentar comportamiento funcional en `openspec/specs/support-requests/spec.md`.
- Representar trabajo activo en `openspec/changes/*`.
- Reflejar comportamiento funcional aprobado en la automatizacion CLI pequena.
- Mantener decisiones breves en `decisions/decision_log.md` y usar ADRs para decisiones estructurales.
- Mantener memoria breve, vigente y accionable.
- Usar Graphify solo para navegacion y analisis de impacto.
- Usar `unittest` y la biblioteca estandar de Python.

## Evitar

- Construir una API o UI productiva dentro del ejemplo.
- Tratar JSON de ejecucion como canonico.
- Copiar investigacion externa directamente a docs canonicos sin revision.
- Tratar `SAMPLE_PROJECT/` como plantilla productiva.
- Duplicar teoria dentro del ejemplo.
