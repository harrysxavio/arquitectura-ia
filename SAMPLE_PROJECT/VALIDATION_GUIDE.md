# VALIDATION_GUIDE.md

> Guia practica para validar la mini app, la documentacion, la arquitectura y el valor de Graphify dentro de este ejemplo pedagogico.

## Proposito

Comprobar que `SAMPLE_PROJECT/` funciona como laboratorio real del framework: ejecuta una mini app, mantiene fuentes canonicas claras, evita cargar contexto innecesario y usa Graphify solo como contexto derivado.

## Validacion Funcional

Desde `SAMPLE_PROJECT/`:

```bash
python -B -m unittest discover -s tests
python -B app.py demo
python -B app.py create --title "Acceso VPN" --description "Alta para equipo operaciones" --area "Operaciones" --type acceso
python -B app.py list
python -B app.py close --id <id> --note "Resuelto con alta manual"
```

Verifica:

- Los tests pasan.
- `demo` crea un flujo pequeno con una solicitud cerrada y una de seguridad en triage.
- `create`, `list` y `close` funcionan sobre `data/requests.json`.
- Una solicitud de tipo `seguridad` parte con prioridad `alta`.
- El cierre sin nota falla.
- Cerrar un id inexistente falla con mensaje claro.
- Al terminar la prueba, `data/requests.json` puede volver a `[]` porque es persistencia runtime, no fuente canonica.

## Validacion Documental

Revisa:

- `CONTEXT_INDEX.md` dirige a fuentes canonicas, codigo y Graphify con roles distintos.
- `docs/product/spec.md` gobierna reglas funcionales.
- `docs/architecture/sdd.md` gobierna diseno tecnico y limites de la automatizacion minima.
- `decisions/` explica por que las reglas viven primero en Markdown y luego se reflejan en codigo.
- `memory/` mantiene hechos, restricciones, patrones, problemas y glosario vigentes sin duplicar specs completas.
- `SAMPLE_PROJECT/` conserva la forma de `PROJECT_TEMPLATE/`: `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `AGENTS.md`, `tasks/current/`, `decisions/`, `docs/`, `memory/` y `graphify-out/`.
- `VALIDATION_GUIDE.md`, `ARCHITECTURE_VALIDATION.md`, `CHAT_SCENARIOS.md`, `app.py`, `src/`, `tests/` y `data/` son extras pedagogicos del laboratorio, no estandar obligatorio del template.

## Validacion de Arquitectura

Prueba este flujo de lectura:

```text
README.md
-> PROJECT_GUIDE.md
-> CONTEXT_INDEX.md
-> tasks/current/active_task.md
-> docs/product/spec.md o docs/architecture/sdd.md
-> decisions/ y memory/
-> graphify-out/ si la tarea es estructural, transversal o ambigua
```

La arquitectura funciona bien si:

- puedes explicar el alcance del proyecto sin leer todo el repo;
- `CONTEXT_INDEX.md` te dice que fuente abrir para cada pregunta;
- los cambios funcionales empiezan en `spec.md`;
- los cambios tecnicos revisan `sdd.md` y tests;
- las decisiones duraderas quedan en `decisions/`;
- la memoria conserva solo conocimiento vigente y accionable;
- Graphify orienta navegacion sin reemplazar fuentes canonicas.

La arquitectura esta fallando si necesitas abrir carpetas completas por defecto, si dos documentos gobiernan la misma regla de forma distinta, o si `graphify-out/*` se usa para decidir sin validar contra fuentes canonicas.

## Validacion Graphify

Desde `SAMPLE_PROJECT/`, ejecuta el comando publico:

```bash
graphify update .
```

El output minimo esperado vive en:

```text
graphify-out/
|-- GRAPH_REPORT.md
`-- graph.json
```

`graph.html` es opcional. Si no aparece, no es falla del ejemplo salvo que la tarea requiera visualizacion HTML.

Lee `graphify-out/GRAPH_REPORT.md` y verifica que mencione nodos reales del proyecto, por ejemplo `SupportDeskService`, `SupportRequest`, `RequestType`, tests y CLI.

## EXTRACTED vs INFERRED

| Tipo | Que significa | Como usarlo |
|---|---|---|
| `EXTRACTED` | Relacion detectada desde senales estructurales como imports, llamadas, clases, tests o rutas. | Sirve como pista fuerte, pero se verifica si la decision cambia codigo o docs canonicos. |
| `INFERRED` | Relacion deducida por Graphify a partir de nombres, texto o semantica. | Es una hipotesis. Antes de decidir, abre los archivos citados y confirma la relacion. |

Para validar una inferencia:

1. Abre los archivos que Graphify conecta.
2. Busca el simbolo, regla, import, llamada o test mencionado.
3. Confirma si la relacion existe en codigo o documentacion canonica.
4. Si la relacion debe gobernar el proyecto, registra el hallazgo en `docs/architecture/sdd.md`, `decisions/decision_log.md` o `memory/patterns.md`.

## Comparacion Manual vs Graphify

Usa esta tabla durante una prueba real:

| Modo | Archivos abiertos | Contexto cargado | Contexto evitado | Aporto valor |
|---|---|---|---|---|
| Manual | `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `tasks/current/active_task.md`, `docs/product/spec.md` | Identidad, mapa, tarea y regla funcional | `src/`, `tests/`, `memory/` hasta confirmar impacto | Si la tarea era funcional y acotada. |
| Con Graphify | Base + `graphify-out/GRAPH_REPORT.md` | Mapa estructural, nodos centrales y posibles modulos impactados | Exploracion manual de todo `src/` | Si redujo busqueda o revelo archivos relevantes. |

Graphify aporta valor si reduce archivos abiertos, aclara relaciones multiarchivo o cambia positivamente la ruta de investigacion. No aporta suficiente si solo repite nombres obvios, agrega ruido o sus inferencias no se pueden validar.

## Prueba Comparativa

1. Sin Graphify, responde: "Si cambia la regla de prioridad de seguridad, que archivos debo revisar?"
2. Registra archivos abiertos, contexto cargado y contexto evitado.
3. Ejecuta `graphify update .`.
4. Abre `graphify-out/GRAPH_REPORT.md` y repite la pregunta.
5. Compara si el reporte redujo exploracion, aclaro relaciones entre codigo/docs o no aporto suficiente valor.

Resultado esperado: Graphify debe orientar navegacion e impacto, pero la decision final debe validarse contra `docs/product/spec.md`, `docs/architecture/sdd.md`, `decisions/`, `memory/` y codigo.
