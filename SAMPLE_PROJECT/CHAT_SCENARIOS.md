# CHAT_SCENARIOS.md

> Escenarios de chat para probar como la arquitectura ayuda a cargar menos contexto, elegir mejores fuentes y usar Graphify con criterio.

## Como Usar Este Documento

Para cada escenario, copia el prompt exacto en el chat/agente y revisa si la traza esperada se parece al comportamiento real. Las trazas son ejemplos manuales, no integracion con un sistema externo.

## Tabla de Comparacion

Usa esta tabla para registrar evidencia en cada corrida:

| Modo | Archivos abiertos | Contexto cargado | Contexto evitado | Aporto valor |
|---|---|---|---|---|
| Sin Graphify |  |  |  |  |
| Con Graphify |  |  |  |  |

## Escenario 1: Cambio Funcional

Prompt exacto:

```text
Quiero cambiar la regla de prioridad de solicitudes de seguridad.
```

Contexto minimo:

- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `tasks/current/active_task.md`
- `docs/product/spec.md`

Contexto adicional si hay impacto tecnico:

- `docs/architecture/sdd.md`
- `decisions/decision_log.md`
- `memory/constraints.md`
- `memory/patterns.md`
- `src/triage.py`
- `tests/test_triage.py`

Contexto evitado al inicio:

- `data/requests.json`
- Todo `memory/`
- Todo `decisions/`
- Todo `src/`
- `graphify-out/` si la ruta de archivos ya es clara

Traza sin Graphify:

```text
usuario: Quiero cambiar la regla de prioridad de solicitudes de seguridad.
contexto minimo cargado: PROJECT_GUIDE.md, CONTEXT_INDEX.md, active_task.md, spec.md
decision: la fuente funcional es docs/product/spec.md
contexto adicional cargado: sdd.md porque la regla se refleja en src/triage.py; test_triage.py para cobertura
contexto evitado: graphify-out, data/requests.json, memoria completa
archivos finales impactados probables: docs/product/spec.md, src/triage.py, tests/test_triage.py, sdd.md si cambia diseno
por que fue eficiente: la ruta salio del indice y de la spec sin explorar todo el repo
```

Traza con Graphify:

```text
usuario: Quiero cambiar la regla de prioridad de solicitudes de seguridad.
contexto minimo cargado: PROJECT_GUIDE.md, CONTEXT_INDEX.md, active_task.md
decision Graphify: usar solo si no es claro que modulo implementa prioridad
contexto Graphify cargado: graphify-out/GRAPH_REPORT.md
hallazgo: RequestType, Priority y SupportDeskService aparecen como nodos centrales; se valida contra src/triage.py y tests
contexto adicional cargado: spec.md, sdd.md, src/triage.py, tests/test_triage.py
contexto evitado: exploracion completa de src y tests
archivos finales impactados probables: docs/product/spec.md, src/triage.py, tests/test_triage.py
por que fue eficiente: Graphify puede confirmar modulos, pero la decision funcional sigue en spec.md
```

Comparacion breve:

| Modo | Archivos abiertos | Contexto cargado | Contexto evitado | Aporto valor |
|---|---|---|---|---|
| Sin Graphify | 6 | Fuentes canonicas y archivos obvios | Grafo, datos runtime, carpetas completas | Si, porque el cambio era claro. |
| Con Graphify | 7 | Base, reporte y modulos confirmados | Exploracion manual de todo `src/` | Aporta si habia duda del modulo; si no, puede ser extra. |

## Escenario 2: Cambio Tecnico

Prompt exacto:

```text
Quiero cambiar la forma en que se persisten las solicitudes.
```

Contexto minimo:

- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `tasks/current/active_task.md`
- `docs/architecture/sdd.md`

Contexto adicional:

- `docs/product/spec.md`
- `decisions/decision_log.md`
- `memory/constraints.md`
- `src/storage.py`
- `src/service.py`
- `app.py`
- `tests/test_storage.py`
- `tests/test_service.py`

Contexto evitado al inicio:

- `data/requests.json` como fuente de regla
- `docs/product/spec.md` hasta confirmar comportamiento observable
- `THEORY/`
- `PROJECT_TEMPLATE/`

Traza sin Graphify:

```text
usuario: Quiero cambiar la forma en que se persisten las solicitudes.
contexto minimo cargado: PROJECT_GUIDE.md, CONTEXT_INDEX.md, active_task.md, sdd.md
decision: el cambio es tecnico y la fuente principal es docs/architecture/sdd.md
contexto adicional cargado: memory/constraints.md para confirmar que JSON es runtime; storage.py y test_storage.py
contexto adicional cargado despues: service.py y test_service.py porque el servicio usa el store
contexto evitado: PROJECT_TEMPLATE, THEORY, graphify-out inicialmente
archivos finales impactados probables: sdd.md, src/storage.py, src/service.py, tests/test_storage.py, tests/test_service.py
por que fue eficiente: empezo por SDD y constraints antes de tocar persistencia
```

Traza con Graphify:

```text
usuario: Quiero cambiar la forma en que se persisten las solicitudes.
contexto minimo cargado: PROJECT_GUIDE.md, CONTEXT_INDEX.md, active_task.md, sdd.md
decision Graphify: usar porque persistencia cruza storage, service, CLI y tests
contexto Graphify cargado: graphify-out/GRAPH_REPORT.md
hallazgo: JsonRequestStore, SupportDeskService y tests aparecen conectados; las relaciones INFERRED se validan abriendo los archivos citados
contexto adicional cargado: src/storage.py, src/service.py, tests/test_storage.py, tests/test_service.py, app.py si cambia CLI
contexto evitado: lectura completa de src, docs no relacionadas y THEORY
archivos finales impactados probables: sdd.md, src/storage.py, src/service.py, tests/test_storage.py, tests/test_service.py
por que fue eficiente: Graphify ayudo a confirmar frontera de impacto multi-modulo
```

Comparacion breve:

| Modo | Archivos abiertos | Contexto cargado | Contexto evitado | Aporto valor |
|---|---|---|---|---|
| Sin Graphify | 8 | SDD, constraints, storage, service y tests | THEORY, template, docs no relacionadas | Si, pero requiere inferir impacto manualmente. |
| Con Graphify | 9 | Base, SDD, reporte, modulos y tests conectados | Exploracion completa de `src/` | Si, porque el cambio era tecnico y transversal. |

## Escenario 3: Onboarding

Prompt exacto:

```text
Soy nuevo en este proyecto, por donde parto para entenderlo sin leer todo?
```

Contexto minimo:

- `README.md`
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`

Contexto adicional:

- `tasks/current/active_task.md`
- `VALIDATION_GUIDE.md`
- `graphify-out/GRAPH_REPORT.md` si la persona quiere mapa estructural de codigo

Contexto evitado al inicio:

- `src/`
- `tests/`
- `data/requests.json`
- `decisions/adr/`
- `THEORY/`

Traza sin Graphify:

```text
usuario: Soy nuevo en este proyecto, por donde parto para entenderlo sin leer todo?
contexto minimo cargado: README.md, PROJECT_GUIDE.md, CONTEXT_INDEX.md
decision: responder con ruta de lectura, no con analisis de codigo
contexto adicional cargado: active_task.md para estado actual y VALIDATION_GUIDE.md para probar el laboratorio
contexto evitado: src, tests, data, ADRs, graphify-out
archivos finales impactados probables: ninguno
por que fue eficiente: resolvio onboarding con documentos de entrada
```

Traza con Graphify:

```text
usuario: Soy nuevo en este proyecto, por donde parto para entenderlo sin leer todo?
contexto minimo cargado: README.md, PROJECT_GUIDE.md, CONTEXT_INDEX.md
decision Graphify: opcional; usar si la persona pide mapa tecnico o relaciones de codigo
contexto Graphify cargado: graphify-out/GRAPH_REPORT.md
hallazgo: SupportDeskService, SupportRequest y RequestType aparecen como nodos centrales
contexto adicional cargado: ninguno salvo que se pida detalle tecnico
contexto evitado: lectura completa de src y tests
archivos finales impactados probables: ninguno
por que fue eficiente: Graphify aporta mapa tecnico, pero no reemplaza onboarding documental
```

Comparacion breve:

| Modo | Archivos abiertos | Contexto cargado | Contexto evitado | Aporto valor |
|---|---|---|---|---|
| Sin Graphify | 4 | Entrada, guia, indice y tarea | Codigo, tests, datos, grafo | Si, para onboarding operativo. |
| Con Graphify | 5 | Base + mapa estructural | Exploracion manual de codigo | Si la persona quiere mapa tecnico; no es obligatorio. |

## Escenario 4: Cambio Local Donde Graphify No Debe Usarse

Prompt exacto:

```text
Corrige un typo en README.md.
```

Contexto minimo:

- `README.md`

Contexto adicional:

- Ninguno, salvo que el typo cambie una regla o una ruta.

Contexto evitado:

- `graphify-out/`
- `docs/`
- `memory/`
- `decisions/`
- `src/`
- `tests/`

Traza sin Graphify:

```text
usuario: Corrige un typo en README.md.
contexto minimo cargado: README.md
decision: cambio local Nivel 1
contexto adicional cargado: ninguno
contexto evitado: graphify-out, docs, memory, decisions, src, tests
archivos finales impactados probables: README.md
por que fue eficiente: el archivo objetivo ya estaba claro
```

Traza con Graphify:

```text
usuario: Corrige un typo en README.md.
decision Graphify: no usar
motivo: el cambio es local, claro y de bajo riesgo
contexto Graphify cargado: ninguno
contexto evitado: GRAPH_REPORT.md y graph.json
archivos finales impactados probables: README.md
por que fue eficiente: evito costo de lectura que no cambia la decision
```

Comparacion breve:

| Modo | Archivos abiertos | Contexto cargado | Contexto evitado | Aporto valor |
|---|---|---|---|---|
| Sin Graphify | 1 | Solo README.md | Todo lo demas | Si, ruta correcta. |
| Con Graphify | 1 | Ningun grafo | Graphify completo | No aplica; la buena decision fue no usarlo. |

## Validar INFERRED Antes de Decidir

Cuando `GRAPH_REPORT.md` muestre una conexion `INFERRED`:

1. Abre ambos archivos citados por la relacion.
2. Busca imports, llamadas, clases, nombres de tests o reglas documentadas.
3. Confirma si la relacion existe o si solo es una similitud semantica.
4. Si la inferencia afecta una decision, registra la conclusion en `sdd.md`, `decision_log.md` o `memory/patterns.md`.

Nunca uses una inferencia como unica razon para cambiar una regla funcional.
