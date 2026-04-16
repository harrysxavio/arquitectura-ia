# Arquitectura Transversal para IA

Este repositorio es un framework documental para trabajar con agentes de IA sin depender de memoria informal, prompts gigantes ni carpetas leidas al azar. Su propuesta es simple: cada tipo de conocimiento debe tener un lugar claro, y los agentes deben cargar solo el contexto que la tarea necesita.

Principio rector:

> La calidad del resultado no debe depender del modelo. Debe depender del sistema.

Para una persona no tecnica, este proyecto es una forma de ordenar el conocimiento de un proyecto para que humanos y agentes entiendan lo mismo. Para una persona tecnica, es una arquitectura reusable de documentacion, contexto, specs, decisiones y memoria compacta.

## Para Quien Esta Pensado

- Personas no tecnicas que necesitan entender como se organiza el conocimiento de un proyecto con IA.
- Equipos tecnicos que quieren aplicar agentes sin perder control de contexto, reglas y decisiones.
- Agentes de IA que necesitan saber que leer primero y que fuente respetar.
- Proyectos que quieren separar comportamiento, arquitectura, decisiones, memoria y navegacion derivada.

## Que Problema Resuelve

Los proyectos con IA suelen fallar por razones poco visibles:

- la regla vigente esta repartida entre README, issues, chats y codigo;
- el agente lee demasiado contexto y pierde foco;
- la memoria se vuelve una mezcla de backlog, diario historico y hechos actuales;
- las decisiones se toman en conversaciones que luego nadie encuentra;
- una herramienta derivada, como un grafo o resumen, termina tratandose como autoridad.

Este framework corrige eso separando responsabilidades. OpenSpec gobierna comportamiento funcional y cambios. La arquitectura estable explica como esta construido el sistema. Las decisiones justifican direcciones durables. La memoria guarda hechos compactos que conviene recordar. Graphify ayuda a navegar, pero no decide.

## Que No Intenta Resolver

No es una metodologia pesada, una plantilla de empresa ni un reemplazo de criterio tecnico. Tampoco intenta convertir toda conversacion en documentacion. La idea no es escribir mas por escribir mas, sino escribir lo suficiente en el lugar correcto.

No reemplaza OpenSpec, Git, tests, revisiones humanas ni el entendimiento del dominio. Los ordena para que trabajen juntos.

## OpenSpec-First

Trabajar OpenSpec-first significa que el comportamiento aprobado vive en `openspec/specs/*/spec.md`, y los cambios funcionales empiezan en `openspec/changes/*`.

La consecuencia practica es importante: si una regla afecta lo que el sistema debe hacer, no se esconde en memoria, arquitectura ni un README. Se expresa como spec o cambio OpenSpec. Los demas documentos pueden orientar, enlazar o explicar, pero no competir como fuente funcional.

La guia operativa esta en `docs/openspec.md`. Este README explica el mapa general y el reparto de autoridad; `docs/openspec.md` muestra el flujo paso a paso: que archivo crear primero, que completa la persona, que puede proponer el agente, como adaptar un proyecto existente y cuando conviene usar el CLI oficial.

En un proyecto activo, la autoridad se reparte asi:

| Pregunta | Fuente principal |
|---|---|
| Que debe hacer el sistema? | `openspec/specs/*/spec.md` |
| Que cambio se esta proponiendo ahora? | `openspec/changes/*/proposal.md` |
| Como se disena tecnicamente ese cambio? | `openspec/changes/*/design.md` |
| Que falta ejecutar o validar? | `openspec/changes/*/tasks.md` |
| Como esta construido el sistema de forma estable? | `docs/architecture/system.md` |
| Por que se aprobo una direccion? | `decisions/decision_log.md` y `decisions/adr/*.md` |
| Que hechos o restricciones conviene recordar? | `memory/facts.md`, `memory/constraints.md`, `memory/patterns.md` |
| Donde conviene mirar primero en un sistema grande? | `graphify-out/*` como contexto derivado |

## Mapa del Repositorio

```text
/
|-- README.md                 entrada maestra al framework
|-- AGENTS.md                 reglas locales para agentes dentro de este repo
|-- docs/                     guias transversales de adopcion, setup y stack
|-- OPERACION/                reglas de ejecucion, contexto y roles de agentes
|-- GRAPHIFY/                 politica para contexto estructural derivado
|-- PROJECT_BLUEPRINT/        guia para adoptar el modelo en un proyecto real
|-- PROJECT_TEMPLATE/         molde reusable para iniciar un proyecto
|-- SAMPLE_PROJECT/           ejemplo ejecutable, no parte de esta lectura base
|-- EXAMPLES/                 flujos breves de uso
|-- SATELLITE/                politicas para herramientas externas de conocimiento
|-- THEORY/                   fundamentos conceptuales del sistema
`-- ARCHIVE/                  historia no canonica
```

## Capas del Framework

| Capa | Para que existe | Como se usa |
|---|---|---|
| `README.md` | Dar una vision completa y navegable. | Primera lectura para entender el sistema. |
| `docs/` | Explicar adopcion practica, setup y stack transversal. | Referencia antes de instalar herramientas o aplicar el framework. |
| `THEORY/` | Explicar los principios detras del modelo. | Lectura conceptual antes de adaptar el framework. |
| `OPERACION/` | Definir como un agente decide contexto, rol y validacion. | Referencia durante trabajo real con agentes. |
| `PROJECT_BLUEPRINT/` | Mostrar como pasar del framework a un proyecto concreto. | Guia de adopcion sin copiar todavia la plantilla. |
| `PROJECT_TEMPLATE/` | Proveer archivos iniciales para un proyecto nuevo. | Se copia o adapta, luego se completa con datos reales. |
| `GRAPHIFY/` | Definir cuando un grafo de conocimiento ayuda y cuando no. | Se consulta para navegacion, impacto y tareas amplias. |
| `SATELLITE/` | Poner limites a herramientas externas como Obsidian o NotebookLM. | Evita que notas externas se vuelvan autoridad accidental. |
| `EXAMPLES/` | Mostrar recorridos operativos cortos. | Ayuda a ejecutar bugs, features e investigacion sin improvisar. |

## Stack y Setup

El framework usa Markdown y Git como base. El resto del stack depende de lo que quieras hacer:

| Herramienta | Rol | Cuando la necesitas |
|---|---|---|
| Markdown | Escribir documentacion versionada y legible. | Siempre. |
| Git | Versionar docs, specs, decisiones y codigo. | Siempre. |
| Python | Ejecutar scripts, ejemplos o proyectos Python. | Solo si el proyecto activo lo usa. |
| OpenSpec | Gobernar comportamiento funcional y cambios. | Siempre como modelo; su CLI es opcional. |
| Node/npm | Instalar y ejecutar OpenSpec CLI cuando se usa la herramienta oficial. | Solo si tu flujo OpenSpec lo requiere. |
| Graphify | Generar grafo derivado para navegacion e impacto. | Opcional para proyectos amplios o ambiguos. |
| MarkItDown | Convertir insumos externos a Markdown antes de resumirlos. | Opcional para investigacion o migracion documental. |
| Obsidian | Notas personales y mapas de pensamiento. | Opcional; no es fuente canonica. |
| Codex | Agente para operar sobre el repo. | Opcional; no es dependencia del proyecto. |

No todo va en `requirements.txt`. Las dependencias runtime de una aplicacion Python van ahi; herramientas de desarrollo pueden ir en `requirements-dev.txt`; herramientas auxiliares como conversion documental o analisis pueden ir en `requirements-tools.txt`; OpenSpec CLI se instala con Node/npm; Obsidian y Codex se instalan fuera del proyecto.

La guia completa esta en `docs/stack.md`. Ve ahi si necesitas elegir entre instalacion minima, instalacion completa, OpenSpec CLI, Graphify, MarkItDown, Obsidian o Codex. Si tu duda es "que instalo para mi caso?", ese documento es la siguiente parada.

## Instalacion Rapida

Instalacion minima para aprender y usar la documentacion:

```bash
git clone <repo>
cd arquitectura-ia
```

Con eso basta para leer Markdown, revisar el blueprint y copiar `PROJECT_TEMPLATE/`.

Instalacion completa segun capacidades:

1. Instalar Python si el proyecto activo ejecuta scripts o codigo Python.
2. Instalar Node/npm si se usara OpenSpec mediante CLI.
3. Instalar Graphify solo si se necesita grafo derivado.
4. Instalar MarkItDown solo si se convertiran fuentes externas.
5. Instalar Obsidian manualmente solo si se quieren notas personales.
6. Usar Codex u otro agente desde su entorno propio, no como dependencia del repo.

No instales herramientas opcionales antes de necesitarlas. El framework funciona como sistema documental aun sin Graphify, MarkItDown u Obsidian.

Resumen rapido:

- Para leer y aprender: Git + editor Markdown.
- Para crear un proyecto: Git + Markdown + `PROJECT_TEMPLATE/`.
- Para usar OpenSpec CLI: Node/npm + `@fission-ai/openspec`.
- Para usar MarkItDown: Python 3.10+ y paquete `markitdown`.
- Para usar Graphify: instalar Graphify solo si necesitas grafo derivado.
- Para Obsidian y Codex: instalacion externa al proyecto.

## Como Leer Este Repositorio

Si solo quieres entender de que trata, lee en este orden:

1. `README.md`
2. `docs/stack.md`
3. `docs/openspec.md`
4. `THEORY/01_principios.md`
5. `PROJECT_BLUEPRINT/README.md`
6. `PROJECT_BLUEPRINT/PROJECT_DOCUMENTS.md`
7. `GRAPHIFY/GRAPHIFY_POLICY.md`

Si quieres aplicar el framework en un proyecto:

1. Lee `docs/adopcion_proyecto.md` como guia practica paso a paso.
2. Lee `PROJECT_BLUEPRINT/README.md`.
3. Revisa `PROJECT_BLUEPRINT/PROJECT_STRUCTURE_EXAMPLE.md`.
4. Copia o adapta `PROJECT_TEMPLATE/`.
5. Completa `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
6. Crea la primera spec en `openspec/specs/`.
7. Usa `openspec/changes/` para el primer cambio funcional.
8. Ajusta `AGENTS.md` para tus agentes y reglas locales.

Si eres un agente trabajando dentro de un proyecto activo:

1. Lee `AGENTS.md`.
2. Usa `CONTEXT_INDEX.md` para ubicar fuentes.
3. Carga OpenSpec antes de tocar comportamiento.
4. Carga arquitectura solo si hay impacto tecnico.
5. Usa memoria solo si afecta la tarea.
6. Usa Graphify solo si el trabajo es amplio, ambiguo o multiarchivo.

## Flujo Operativo

El flujo del framework empieza con orientacion y termina con validacion. Un agente o persona no deberia saltar directo al codigo si la tarea afecta comportamiento.

1. `AGENTS.md` define reglas locales de trabajo.
2. `PROJECT_GUIDE.md` explica identidad, alcance y stack del proyecto.
3. `CONTEXT_INDEX.md` indica que fuente oficial corresponde a la pregunta.
4. OpenSpec entra cuando hay comportamiento funcional o cambio activo.
5. `docs/architecture/system.md` entra cuando hay estructura tecnica, datos, integraciones o contratos.
6. Decisiones y memoria entran cuando hay historia aprobada, restricciones o patrones que cambian la decision.
7. Graphify entra solo si ayuda a navegar impacto amplio o propiedad poco clara.

Este orden reduce tokens porque evita leer carpetas completas. Tambien reduce errores porque separa fuentes activas, memoria y salidas derivadas.

## Ejemplos Concretos

### Cambio Funcional: Agregar Prioridad Urgente

Supongamos que un sistema debe agregar una nueva prioridad `urgente` para solicitudes de soporte.

1. Leer `AGENTS.md` para reglas locales.
2. Leer `PROJECT_GUIDE.md` para confirmar alcance del sistema.
3. Leer `CONTEXT_INDEX.md` para ubicar la spec de solicitudes.
4. Abrir `openspec/specs/<capability>/spec.md` para ver el comportamiento vigente.
5. Crear `openspec/changes/add-urgent-priority/proposal.md` con intencion, alcance y no alcance.
6. Agregar el delta funcional bajo `openspec/changes/add-urgent-priority/specs/<capability>/spec.md`.
7. Usar `design.md` solo si cambia arquitectura, datos o contratos.
8. Consultar `memory/constraints.md` si hay limites de negocio o seguridad sobre prioridades.
9. Consultar `decisions/decision_log.md` si ya hubo decisiones sobre triage o clasificacion.
10. Usar Graphify solo si no esta claro que modulos implementan prioridad o que tests se verian afectados.

OpenSpec entra al principio porque la regla es funcional. Arquitectura entra solo si el cambio modifica estructura tecnica. Graphify no hace falta si la spec y el codigo afectado son obvios.

### Cambio Tecnico: Cambiar Persistencia Local por Base de Datos

Supongamos que un proyecto quiere reemplazar un JSON local por una base de datos.

1. Leer `AGENTS.md`, `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
2. Abrir `docs/architecture/system.md` porque el cambio afecta datos, componentes y validacion tecnica.
3. Revisar `memory/constraints.md` para limites de seguridad, costo, hosting o compliance.
4. Revisar `decisions/decision_log.md` y ADRs por decisiones previas sobre persistencia.
5. Crear un ADR si la decision es durable y tiene alternativas relevantes.
6. Crear un cambio OpenSpec solo si la persistencia cambia comportamiento visible para usuarios.
7. Usar Graphify si el repositorio es grande y no esta claro que componentes leen o escriben datos.

Aqui arquitectura entra antes que OpenSpec porque el nucleo del cambio es tecnico. OpenSpec entra solo si cambia comportamiento observable. Memoria y decisiones son importantes porque persistencia suele tocar restricciones, costos y riesgos.

## Rol de Graphify

Graphify convierte codigo y documentos en un grafo de conocimiento. Sirve para navegar sistemas grandes, detectar comunidades, encontrar nodos centrales y estimar impacto. En este framework es util porque reduce exploracion cuando no esta claro donde mirar.

Pero Graphify es derivado. Puede estar desactualizado, puede inferir relaciones equivocadas y no reemplaza fuentes canonicas. Si Graphify revela algo importante, primero se valida contra archivos fuente y luego se registra en OpenSpec, arquitectura, decisiones o memoria.

Regla breve:

> Graphify ayuda a encontrar. OpenSpec, arquitectura, decisiones y memoria deciden.

## Por Que Mejora el Trabajo con IA

Los agentes funcionan mejor cuando el proyecto les dice donde mirar y que autoridad respetar. Este framework reduce tres costos:

- costo de busqueda: el agente no necesita abrir todo el repo;
- costo de ambiguedad: una regla funcional tiene un lugar oficial;
- costo de continuidad: hechos, decisiones y restricciones sobreviven a una sesion de chat.

La mejora no viene de tener mas documentos. Viene de que cada documento tenga una responsabilidad concreta y no compita con los demas.

## Reglas Que No Deben Romperse

- No duplicar reglas funcionales fuera de OpenSpec.
- No usar Graphify como fuente de verdad.
- No convertir memoria en backlog o diario historico.
- No guardar secretos, tokens ni datos sensibles en Markdown.
- No cargar carpetas amplias por defecto si una fuente especifica basta.
- No tratar `SAMPLE_PROJECT/` como plantilla productiva.
- No reintroducir material heredado como autoridad activa.

## Takeaway

Este framework propone una disciplina simple: poner cada verdad en su lugar, leer solo lo necesario y hacer que humanos y agentes compartan el mismo mapa. OpenSpec gobierna comportamiento; arquitectura explica estructura; decisiones explican por que; memoria recuerda lo durable; Graphify orienta sin mandar.
