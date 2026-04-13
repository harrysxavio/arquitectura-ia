# CONSTRAINTS: Reglas de Higiene Contextual

Este archivo define reglas generales de contexto. La matriz concreta de que leer por tipo de tarea vive solo en `OPERACION/CONTEXT_ROUTER.md`.

## Principio

> [!IMPORTANT]
> No cargar contexto por disponibilidad. Cargarlo por necesidad.

- El contexto minimo es el punto de partida.
- Cada escalamiento debe justificarse por alcance, riesgo o ambiguedad.

## Niveles

| Nivel | Uso | Regla |
|---|---|---|
| 1 | Tarea simple y local | Leer contexto base y archivo afectado |
| 2 | Cambio funcional o multiarchivo | Agregar spec, constraint o memoria puntual segun router |
| 3 | Cambio estructural, ambiguo o transversal | Consultar Graphify vigente antes de exploracion amplia |

## Graphify

> [!TIP]
> En Nivel 3, consulta Graphify vigente antes de explorar documentacion amplia o modulos completos.

- Graphify es contexto estructural persistente y derivado.
- En Nivel 3 debe consultarse antes de leer documentacion amplia o modulos completos.
- No se usa por defecto en microcambios locales.
- Si Graphify contradice una fuente canonica, gana la fuente canonica.
- Si Graphify revela informacion que debe gobernar el proyecto, esa informacion debe registrarse en `CONTEXT_INDEX.md`, `docs/architecture/sdd.md`, `decisions/decision_log.md` o `memory/patterns.md`.

## Compresion

- Si una investigacion larga produce conocimiento reutilizable, convertirla en artefacto comprimido.
- Formatos validos: `GRAPH_REPORT.md`, `repo-summary.md`, `module-map.md`, `incident-summary.md`, `decision-summary.md`.
- No obligar al agente a releer material completo si ya existe un resumen vigente.

## Prohibiciones

> [!WARNING]
> Estas reglas evitan que el agente use contexto excesivo o fuentes no canonicas.

- Prohibido cargar todo el repo por defecto.
- Prohibido cargar toda la carpeta `docs/` por defecto.
- Prohibido cargar todas las decisiones o memorias por si acaso.
- Prohibido usar `THEORY/` como instruccion de runtime tecnico.
- Prohibido tratar `PROJECT_TEMPLATE/` como proyecto activo.
