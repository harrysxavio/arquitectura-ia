# Arquitectura del Sistema

> Arquitectura tecnica estable para el ejemplo de mesa de soporte de SAMPLE_PROJECT.

## Proposito

Describe la forma tecnica estable de la app CLI de ejemplo sin duplicar reglas funcionales. El comportamiento funcional vive en `openspec/specs/support-requests/spec.md`; los cambios activos viven en `openspec/changes/*`.

## Contexto

`SAMPLE_PROJECT/` es un proyecto pedagogico pequeno, no una plantilla productiva. Demuestra como documentacion, codigo, decisiones, memoria, tests y Graphify pueden coexistir con contexto compacto.

## Componentes

| Componente | Rol |
|---|---|
| `app.py` | Entry point CLI para `demo`, `create`, `list` y `close`. |
| `src/enums.py` | Enums de dominio para tipo, prioridad y estado. |
| `src/models.py` | Modelo de datos de solicitud. |
| `src/triage.py` | Logica auxiliar de prioridad inicial y siguiente estado. |
| `src/service.py` | Servicio de aplicacion para operaciones de crear, listar y cerrar. |
| `src/storage.py` | Persistencia JSON de ejecucion. |
| `src/reporter.py` | Formato de salida de texto. |
| `tests/` | Tests unitarios para comportamiento de triage, servicio y almacenamiento. |
| `data/requests.json` | Datos de ejecucion de ejemplo; no canonicos. |
| `graphify-out/` | Contexto estructural derivado; no canonico. |

## Contratos

Una solicitud de soporte contiene titulo, descripcion, area, tipo, prioridad, estado, responsable opcional, nota de cierre opcional y timestamps. El comportamiento aprobado lo gobierna OpenSpec.

## Datos

No hay base de datos productiva ni sistema de migraciones. `data/requests.json` existe solo para ejecutar el ejemplo local.

## Riesgos

- Tratar el ejemplo como app productiva.
- Tratar JSON de ejecucion como autoridad.
- Tratar salida de Graphify como fuente de verdad.

## Validacion

Desde `SAMPLE_PROJECT/`:

```bash
python -B -m unittest discover -s tests
python -B app.py demo
```

Graphify puede regenerarse cuando este disponible, pero su salida sigue siendo derivada.
