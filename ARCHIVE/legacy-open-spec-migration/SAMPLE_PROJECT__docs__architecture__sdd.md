# SDD - Mesa Interna de Soporte Operativo

> Ejemplo rellenado. Diseno tecnico minimo e ilustrativo.

## Contexto

Este ejemplo entrega una mini app funcional, pequena y pedagogica. La arquitectura prioriza documentacion canonica y trazabilidad, y luego implementa una automatizacion minima alineada con esa documentacion.

`app.py` y `src/*.py` permiten crear, listar y cerrar solicitudes. No convierten `SAMPLE_PROJECT/` en plantilla de produccion y no reemplazan `docs/product/spec.md`.

## Referencias

- Spec: `docs/product/spec.md`
- Decision: `decisions/decision_log.md`
- ADR: `decisions/adr/0001-documentar-triage-en-markdown.md`

## Decision Tecnica

Mantener las reglas primero en Markdown canonico y reflejarlas en una automatizacion minima por CLI. No introducir API, base de datos productiva ni frontend.

## Arquitectura Propuesta

```text
SAMPLE_PROJECT/
|-- docs/product/spec.md        # verdad funcional
|-- docs/architecture/sdd.md    # diseno tecnico
|-- decisions/                  # decisiones aprobadas
|-- memory/                     # conocimiento vigente
|-- app.py                      # CLI demo/create/list/close
|-- src/                        # modulos funcionales pequenos
|-- tests/                      # unittest basico
|-- data/requests.json          # persistencia runtime, no canonica
`-- graphify-out/               # contexto derivado de Graphify
```

## Componentes Impactados

- Documentacion funcional: `docs/product/spec.md`.
- Memoria de patrones y restricciones: `memory/patterns.md`, `memory/constraints.md`.
- CLI: `app.py`.
- Codigo funcional: `src/enums.py`, `src/models.py`, `src/storage.py`, `src/triage.py`, `src/service.py`, `src/reporter.py`, `src/utils.py`.
- Tests: `tests/*.py`.
- Graphify: `graphify-out/*`, output derivado del proyecto instanciado.

## Contratos / Interfaces

El ejemplo conceptual usa una solicitud con estos campos:

| Campo | Descripcion |
|---|---|
| `title` | Titulo breve de la solicitud. |
| `request_type` | Tipo: soporte, acceso, datos, seguridad u otro. |
| `priority` | Prioridad: baja, media, alta o critica. |
| `status` | Estado del flujo. |
| `owner` | Responsable asignado, si existe. |
| `closing_note` | Nota requerida para cerrar. |
| `created_at` / `updated_at` | Timestamps runtime para trazabilidad basica. |

## Datos y Migraciones

No hay base de datos productiva ni migraciones. `data/requests.json` es persistencia runtime del ejemplo, no fuente canonica ni contrato externo.

## Riesgos

- Confundir `SAMPLE_PROJECT/` con plantilla de produccion.
- Tratar `data/requests.json` como canonico.
- Usar Graphify como fuente de verdad en vez de contexto derivado.

## Validacion

- Revisar que reglas de negocio vivan en `docs/product/spec.md`.
- Ejecutar `python -m unittest discover -s tests`.
- Ejecutar `python app.py demo`.
- Revisar que decisiones duraderas vivan en `decisions/`.
- Revisar que hechos y patrones vigentes vivan en `memory/`.
- Ejecutar `graphify update .` desde `SAMPLE_PROJECT/` cuando se quiera regenerar contexto derivado.

## Nota de uso

Si el diseno se aprueba para produccion, registrar la decision en `decisions/decision_log.md` o una ADR nueva.
