# CONTEXT_ROUTER.md - Router de Contexto OpenSpec-First

Este archivo es la autoridad para decidir que contexto debe cargar un agente.

## Proposito

El router existe para evitar dos fallas comunes: leer demasiado y leer lo incorrecto. Un agente no debe abrir carpetas completas por costumbre; debe justificar cada fuente que carga segun la tarea.

Para una persona no tecnica, este archivo responde "por donde empiezo a mirar?". Para una persona tecnica o un agente, responde "que documentos son suficientes para actuar sin romper autoridad documental?".

## Como Usarlo

1. Clasifica la tarea: bug, funcionalidad, refactor, docs, revision o investigacion.
2. Estima riesgo y amplitud: local, funcional, estructural o ambiguo.
3. Carga el contexto base del proyecto.
4. Agrega solo las fuentes que cambian la decision.
5. Antes de cerrar, verifica que la fuente de autoridad usada sea la correcta.

El router no reemplaza criterio. Lo ordena.

## Relacion con Archivos Base

- `AGENTS.md` dice como debe comportarse el agente en ese proyecto.
- `PROJECT_GUIDE.md` explica identidad, alcance y stack.
- `CONTEXT_INDEX.md` indica que fuente oficial leer para cada pregunta.
- OpenSpec gobierna comportamiento funcional.
- `docs/architecture/system.md` gobierna estructura tecnica estable.

El router usa esos archivos como escalera de lectura: primero orientacion, luego autoridad especifica, despues contexto adicional si hace falta.

## Protocolo Base

1. Identificar tipo de tarea y complejidad.
2. Cargar `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md` al trabajar dentro de un proyecto.
3. Para comportamiento, cargar la spec relevante en `openspec/specs/*/spec.md`.
4. Para trabajo activo, cargar el cambio relevante en `openspec/changes/*`.
5. Agregar arquitectura, decisiones, memoria o Graphify solo cuando este justificado.

## Niveles

| Nivel | Criterio | Contexto requerido |
|---|---|---|
| 1 | Local, claro, bajo riesgo | Contexto base + archivo afectado |
| 2 | Funcional o multarchivo | Contexto base + spec/cambio OpenSpec relevante |
| 3 | Estructural, ambiguo o amplio | Nivel 2 + `docs/architecture/system.md` + decisiones/memoria + Graphify si aporta |

## Señales Para Subir de Nivel

Sube de nivel cuando una respuesta local no basta: aparecen varios modulos, una regla funcional no esta clara, hay impacto de datos, una decision previa puede aplicar o no sabes que componente posee el comportamiento.

No subas de nivel por ansiedad. Si la tarea es corregir un typo o ajustar un texto local con fuente clara, Graphify y memoria probablemente agregan ruido.

## Matriz de Tareas

| Tipo | Empezar con | Agregar cuando haga falta |
|---|---|---|
| bug | archivo afectado, tests, spec relevante | `memory/facts.md`, Graphify si el impacto es amplio |
| funcionalidad | spec relevante y cambio activo | arquitectura, decisiones, patrones |
| refactor | arquitectura y modulos afectados | Graphify para impacto entre modulos |
| docs | documento objetivo y fuente canonica | OpenSpec o arquitectura como fuente |
| revision | diff y spec/cambio relevante | decisiones, arquitectura, tests |
| investigacion | objetivo y fuente | resultado compacto en memoria o docs si se vuelve canonico |

## Ejemplos de Decision

- Si una regla de negocio cambia, empezar por OpenSpec aunque el codigo parezca obvio.
- Si cambia un contrato tecnico entre componentes, agregar `docs/architecture/system.md`.
- Si una restriccion previa puede bloquear el cambio, revisar `memory/constraints.md`.
- Si no sabes que modulo tocar, usar Graphify como mapa derivado y validar luego en archivos fuente.
- Si el trabajo es documental, usar la fuente canonica que el documento debe explicar o enlazar.

## Orden de Autoridad

1. `AGENTS.md`
2. `openspec/changes/*` activo
3. `openspec/specs/*/spec.md`
4. `docs/architecture/system.md`
5. `decisions/decision_log.md`
6. `decisions/adr/*.md`
7. `memory/constraints.md`
8. `memory/facts.md`
9. `memory/patterns.md`
10. `graphify-out/*` solo como contexto derivado

## Prohibiciones

- No cargar carpetas amplias por defecto.
- No duplicar reglas funcionales fuera de OpenSpec.
- No usar Graphify como autoridad.
- No usar material heredado archivado como fuente activa.

## Cierre Esperado

Al terminar una tarea, el agente deberia poder decir: que tipo de tarea era, que nivel aplico, que fuentes cargo, que fuente mando y que validacion realizo. Si no puede explicarlo, probablemente cargo contexto por costumbre y no por necesidad.
