# ARCHITECTURE_VALIDATION.md

> Prueba de arquitectura total para validar que `SAMPLE_PROJECT/` funciona como sistema documental, operativo y pedagogico.

## Objetivo

Demostrar que la arquitectura ayuda a trabajar con menos contexto, fuentes claras y decisiones verificables. Esta prueba valida el sistema completo, no solo la mini app.

## Que Se Quiere Demostrar

- El flujo de lectura evita cargar todo el repo.
- `CONTEXT_INDEX.md` dirige a la fuente correcta.
- `spec.md`, `sdd.md`, `decisions/` y `memory/` tienen roles distintos.
- La mini app refleja reglas documentadas, pero no las gobierna.
- Graphify ayuda en tareas estructurales sin convertirse en fuente canonica.
- `SAMPLE_PROJECT/` sigue siendo una instancia reconocible de `PROJECT_TEMPLATE/`.

## Prueba 1: Onboarding Minimo

1. Lee `README.md`.
2. Lee `PROJECT_GUIDE.md`.
3. Lee `CONTEXT_INDEX.md`.
4. Lee `tasks/current/active_task.md`.
5. Responde: "Que es este proyecto, que no es y donde debo buscar una regla funcional?"

Resultado esperado:

- Puedes explicar que es una mesa interna de soporte operativo.
- Puedes decir que no es plantilla de produccion.
- Puedes ubicar reglas funcionales en `docs/product/spec.md`.
- No necesitaste abrir `src/`, `tests/`, `memory/` ni `graphify-out/`.

## Prueba 2: Cambio Funcional

Pregunta:

```text
Quiero cambiar la regla de prioridad de solicitudes de seguridad.
```

Ruta esperada:

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`
4. `docs/product/spec.md`
5. `docs/architecture/sdd.md` si el cambio afecta codigo
6. `decisions/decision_log.md` si cambia una decision duradera
7. `memory/constraints.md` o `memory/patterns.md` si aparece una regla vigente
8. `graphify-out/GRAPH_REPORT.md` solo si el impacto sobre modulos no es claro

Resultado esperado:

- La regla se decide en `spec.md`, no en `data/requests.json`.
- Si se toca codigo, los impactos probables son `src/triage.py`, `src/service.py` y tests.
- Graphify puede ayudar a confirmar modulos impactados, pero no gobierna la regla.

## Prueba 3: Cambio Tecnico

Pregunta:

```text
Quiero cambiar la forma en que se persisten las solicitudes.
```

Ruta esperada:

1. Contexto base: `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `tasks/current/active_task.md`
2. `docs/architecture/sdd.md`
3. `docs/product/spec.md` solo para confirmar comportamiento observable
4. `decisions/decision_log.md` y ADR si el cambio altera una decision
5. `memory/constraints.md` para no convertir JSON runtime en base productiva
6. `graphify-out/GRAPH_REPORT.md` porque el cambio cruza storage, servicio, CLI y tests

Resultado esperado:

- La fuente tecnica principal es `sdd.md`.
- Los impactos probables son `src/storage.py`, `src/service.py`, `app.py` si cambia interfaz, y `tests/test_storage.py` o `tests/test_service.py`.
- Cualquier cambio de persistencia debe mantener `data/requests.json` como runtime salvo nueva decision.

## Prueba 4: Decision y Memoria

Pregunta:

```text
Debemos registrar que Graphify no es fuente de verdad?
```

Ruta esperada:

1. `CONTEXT_INDEX.md`
2. `decisions/decision_log.md`
3. `memory/constraints.md`
4. `memory/patterns.md`
5. `GRAPHIFY/GRAPHIFY_POLICY.md` desde la raiz si se revisa politica global

Resultado esperado:

- La decision vive en `decisions/decision_log.md`.
- La restriccion vigente vive en `memory/constraints.md`.
- El patron de uso vive en `memory/patterns.md`.
- No se copia el reporte Graphify como memoria canonica.

## Prueba 5: Instancia de PROJECT_TEMPLATE

Verifica que `SAMPLE_PROJECT/` conserva esta estructura base:

| Elemento | Debe existir | Rol |
|---|---|---|
| `PROJECT_GUIDE.md` | Si | Identidad y alcance |
| `CONTEXT_INDEX.md` | Si | Mapa de fuentes |
| `AGENTS.md` | Si | Adaptacion local |
| `tasks/current/` | Si | Trabajo activo |
| `decisions/` | Si | Decisiones y ADRs |
| `docs/` | Si | Spec y SDD |
| `memory/` | Si | Hechos, restricciones, patrones, glosario |
| `graphify-out/` | Si | Contexto derivado |

Extras pedagogicos del sample:

| Extra | Por que existe | Estandar obligatorio |
|---|---|---|
| `VALIDATION_GUIDE.md` | Validar app, docs, arquitectura y Graphify | No |
| `ARCHITECTURE_VALIDATION.md` | Probar la arquitectura como sistema | No |
| `CHAT_SCENARIOS.md` | Probar prompts y trazas de decision | No |
| `app.py`, `src/`, `tests/`, `data/` | Ejecutar laboratorio funcional | No |

Resultado esperado: el sample sigue siendo reconocible como instancia de `PROJECT_TEMPLATE/`, pero sus extras no obligan a modificar la plantilla.

## Cuando Debe Entrar Graphify

Usa Graphify si la pregunta es estructural, transversal, ambigua, de onboarding amplio o toca varios modulos.

No uses Graphify por defecto si:

- el archivo afectado ya esta claro;
- el cambio es un typo o una frase puntual;
- `CONTEXT_INDEX.md` ya indica una fuente suficiente;
- el costo de leer el reporte supera la duda real.

## Senales de Fallo

La arquitectura esta fallando si aparece cualquiera de estas senales:

| Senal | Como se ve | Correccion esperada |
|---|---|---|
| Fuentes contradictorias | `spec.md` dice una regla y `src/` implementa otra sin decision | Actualizar spec, SDD, decision o codigo segun autoridad |
| Lectura excesiva | El agente abre todo el repo antes del contexto base | Volver a `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y `active_task.md` |
| Graphify como verdad | Una inferencia del grafo decide una regla | Validar contra spec, SDD, decisiones, memoria o codigo |
| Cambio funcional sin spec | Se cambia `src/triage.py` sin tocar `docs/product/spec.md` | Actualizar la fuente funcional primero |
| Cambio tecnico sin SDD/tests | Se cambia persistencia sin revisar `sdd.md` ni tests | Actualizar SDD y pruebas afectadas |
| Memoria duplicada | `memory/` repite specs completas | Comprimir memoria a hechos, restricciones o patrones |
| Extras tratados como template | Se exige `CHAT_SCENARIOS.md` en todo proyecto | Marcarlo como extra pedagogico del sample |
| Datos runtime canonizados | Se usa `data/requests.json` para decidir reglas | Volver a spec, SDD, decisiones y memoria |

## Criterio de Exito

La arquitectura funciona si un agente puede responder que leer, que evitar, cuando usar Graphify y que archivos impactar sin cargar todo el repo ni confundir outputs derivados con fuentes canonicas.
