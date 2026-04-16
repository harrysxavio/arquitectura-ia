# PROJECT_GUIDE.md

> Identidad y alcance canonicos para SAMPLE_PROJECT.

## Identidad

- Nombre: Mesa Interna de Soporte Operativo.
- Usuario principal: coordinadores de operaciones y equipos internos que solicitan soporte.
- Problema que resuelve: centralizar solicitudes internas, clasificar prioridad y mantener trazabilidad.

## Alcance

Incluido:

- Registro manual de solicitudes internas.
- Seguimiento de tipo, area, estado y prioridad de solicitudes.
- Flujo CLI basico para `create`, `list`, `demo` y `close`.
- Documentacion OpenSpec para comportamiento aprobado y cambios activos.
- Persistencia JSON de ejecucion para el ejemplo.

Fuera de alcance:

- Autenticacion real.
- Integracion con mesa de ayuda externa.
- Base de datos productiva.
- Notificaciones automaticas.
- Interfaz web completa.
- Plantilla productiva para sistemas nuevos.

## Estructura

- `openspec/`: verdad funcional y cambios activos.
- `docs/architecture/system.md`: arquitectura tecnica estable.
- `decisions/`: indice breve de decisiones y ADRs.
- `memory/`: hechos, restricciones, patrones y glosario compactos.
- `app.py`, `src/`, `tests/`, `data/`: app CLI pedagogica.
- `graphify-out/`: contexto estructural derivado.
- `ARCHIVE/legacy-open-spec-migration/`: evidencia historica de migracion en la raiz del repo.

## Stack

- Backend: biblioteca estandar de Python.
- Frontend: ninguno.
- Datos: archivo JSON de ejecucion local.
- Hosting: ninguno.

## Restricciones

- Mantener el ejemplo pequeno y pedagogico.
- No tratar datos de ejecucion como autoridad.
- No tratar salidas de Graphify como autoridad.
- No almacenar secretos ni datos personales reales.

## Regla

El comportamiento funcional vive en OpenSpec. Esta guia solo explica identidad y alcance.
