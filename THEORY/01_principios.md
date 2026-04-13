# Modulo 1 - Principios Rectores y Marco de Decision

## 1. Proposito

Este framework existe para trabajar con agentes de IA sin depender de improvisacion, prompts largos ni memoria mental del usuario.

Su objetivo no es acumular herramientas. Su objetivo es crear un sistema documental y operativo donde cada agente sepa:

- que esta intentando resolver,
- que contexto debe leer,
- que documentos tienen autoridad,
- que rol cumple,
- que no debe tocar,
- cuando debe actualizar memoria o decisiones.

La estructura actual separa ocho zonas:

| Carpeta | Funcion |
|---|---|
| `OPERACION/` | Router, constraints y contratos de agentes para ejecucion diaria |
| `PROJECT_BLUEPRINT/` | Plano documental de un proyecto instanciado |
| `PROJECT_TEMPLATE/` | Molde reusable para instanciar proyectos reales |
| `THEORY/` | Manual pedagogico del framework |
| `GRAPHIFY/` | Politica y contrato del mapa estructural derivado |
| `SATELLITE/` | Politicas de Obsidian y NotebookLM como conocimiento externo al nucleo |
| `EXAMPLES/` | Casos de uso de referencia |
| `ARCHIVE/` | Fuentes historicas no canonicas |

`PROJECT_TEMPLATE/` es la unica fuente de plantillas `.md` del molde propuesto.

## 2. Principio Rector

> [!IMPORTANT]
> La calidad del resultado no debe depender del modelo. Debe depender del sistema.

Un modelo potente falla si el repo no tiene estructura, si las fuentes se contradicen o si el agente debe adivinar que leer. Un modelo mas barato puede rendir bien si recibe una tarea acotada, contexto minimo suficiente y reglas claras.

El framework reduce dependencia del modelo mediante:

- documentos canonicos,
- separacion entre teoria y operacion,
- router de contexto,
- memoria persistente,
- decisiones registradas,
- agentes con limites,
- politicas para herramientas externas.

## 3. Problemas que Resuelve

| Problema | Respuesta del framework |
|---|---|
| Exceso de contexto | Cargar por necesidad, no por disponibilidad |
| Prompts pobres | Convertir intencion del usuario en flujo operativo |
| Documentacion duplicada | Una fuente de verdad por tipo de informacion |
| Perdida de decisiones | Registrar decisiones en `decisions/decision_log.md` dentro del proyecto activo |
| Mezcla de teoria y runtime | `THEORY/` explica; `OPERACION/` gobierna ejecucion |
| Dependencia de una herramienta | Cline o Codex pueden ser agente principal, pero el sistema no depende de uno |
| Research disperso | NotebookLM y Obsidian son satelite; lo canonico vuelve al repo |
| Onboarding lento | `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y Graphify orientan lectura |

## 4. Que No Es

Este framework no es:

- un catalogo de prompts,
- una coleccion de herramientas de moda,
- un sistema multiagente inflado,
- un reemplazo del criterio tecnico,
- una base de conocimiento externa al repo,
- una invitacion a cargar todo el proyecto en cada tarea.

## 5. Decisiones Oficiales

### 5.1 Un agente principal por proyecto

Cada proyecto instanciado debe elegir un agente principal: Cline o Codex. No se usan ambos como cerebro principal del mismo proyecto.

La razon es gobernanza: si dos agentes intentan dirigir contexto, memoria y decisiones a la vez, la autoridad se vuelve ambigua.

### 5.2 Cuatro agentes base

Los agentes base oficiales son:

- Manager,
- Coder,
- Reviewer,
- Debugger.

Si una necesidad puede resolverse con skill, workflow o checklist, no debe convertirse en agente nuevo.

### 5.3 Contexto minimo por defecto

La ruta normal empieza con:

- `PROJECT_GUIDE.md`,
- `CONTEXT_INDEX.md`,
- `tasks/current/active_task.md`.

Dentro de este repo framework, cuando no hay proyecto instanciado, el fallback es:

- `README.md`,
- `AGENTS.md` raiz si hay instrucciones locales de tooling,
- `OPERACION/CONTEXT_ROUTER.md`,
- `PROJECT_BLUEPRINT/` para entender la estructura documental,
- `PROJECT_TEMPLATE/` como molde, no como verdad operativa.

### 5.4 Una fuente de verdad por tipo de informacion

En un proyecto activo:

| Informacion | Fuente canonica |
|---|---|
| Identidad y alcance | `PROJECT_GUIDE.md` |
| Ruta de consulta | `CONTEXT_INDEX.md` |
| Trabajo actual | `tasks/current/active_task.md` |
| Plan actual | `tasks/current/implementation_plan.md` |
| Preguntas abiertas | `tasks/current/open_questions.md` |
| Decisiones | `decisions/decision_log.md` |
| Hechos vigentes | `memory/project_facts.md` |
| Restricciones | `memory/constraints.md` |
| Problemas conocidos | `memory/known_issues.md` |
| Patrones | `memory/patterns.md` |
| Glosario | `memory/glossary.md` |
| Spec funcional | `docs/product/spec.md` |
| Diseno tecnico | `docs/architecture/sdd.md` |
| Mapa derivado | `graphify-out/*` |

### 5.5 `PROJECT_TEMPLATE/` no es un proyecto activo

> [!WARNING]
> `PROJECT_TEMPLATE/` no debe confundirse con memoria, decisiones ni tarea activa reales.

Los archivos dentro de `PROJECT_TEMPLATE/` son ejemplos estructurales. No contienen tarea activa real, decisiones reales ni memoria real. Solo se vuelven canonicos cuando se copian o adaptan dentro de un repo de proyecto.

## 6. Criterio de Exito

El framework esta sano si:

- el usuario puede retomar un proyecto sin reconstruir contexto desde cero,
- los agentes leen menos pero mejor,
- las decisiones importantes quedan registradas,
- `THEORY/` no se usa como instruccion de runtime,
- `PROJECT_TEMPLATE/` no se confunde con proyecto activo,
- Graphify orienta navegacion sin reemplazar fuentes canonicas,
- Obsidian y NotebookLM no gobiernan el repo,
- el stack crece por necesidad real, no por moda.

## 7. Regla Final

No se debe construir un proyecto donde la IA tenga que adivinar el sistema. Se debe construir un sistema donde la IA solo tenga que ejecutar bien.
