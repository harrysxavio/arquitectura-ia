# Project Facts

> Ejemplo rellenado. Hechos vigentes del proyecto.

## Stack

- Backend: Python simple con biblioteca estandar.
- Frontend: no definido.
- Base de datos: JSON runtime local en `data/requests.json`.
- Hosting: no definido.

## Integraciones

- No hay integraciones productivas.
- MarkItDown puede usarse para convertir insumos externos a Markdown antes de resumirlos en documentos canonicos.
- Graphify se ejecuta para este proyecto instanciado con `graphify update .` desde `SAMPLE_PROJECT/`.

## Entornos

- Desarrollo: carpeta local del repo.
- Produccion: no aplica.

## Proveedores Aprobados

- GitHub para versionar documentos.
- Markdown como formato documental principal.

## Auth

- No aplica en este ejemplo.

## Restricciones Estructurales

- `SAMPLE_PROJECT/` es ejemplo instanciado, no template.
- `SAMPLE_PROJECT/` es funcional pero pedagogico; no es plantilla de produccion.
- `src/` contiene la automatizacion minima alineada con Markdown canonico.
- `data/requests.json` es persistencia runtime, no fuente canonica.
- `graphify-out/*` es derivado y vive solo dentro de `SAMPLE_PROJECT/` como output operativo.

## Nota de uso

Si un hecho cambia por decision, actualizar tambien `decisions/decision_log.md`. Si una restriccion estructural limita implementaciones futuras, reflejarla tambien en `memory/constraints.md`.
