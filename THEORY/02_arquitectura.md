# Modulo 2 - Arquitectura Troncal del Framework

## 1. Vision General

La arquitectura actual separa framework global, proyecto instanciado, teoria, herramientas estructurales y conocimiento satelite.

La separacion evita que una nota pedagogica, un output derivado o una investigacion externa gobiernen una tarea tecnica.

| Nivel | Donde vive | Autoridad |
|---|---|---|
| Framework global reusable | Este repo | Canonico para definir el metodo |
| Operacion del framework | `OPERACION/` | Canonico para ejecucion, reglas y roles |
| Proyecto activo | Repo creado desde `PROJECT_TEMPLATE/` | Canonico para ese proyecto |
| Manual teorico | `THEORY/` | Explicativo, no runtime |
| Mapa estructural | `graphify-out/*` en proyecto instanciado | Derivado, no canonico |
| Conocimiento satelite | Obsidian, NotebookLM, `SATELLITE/` | Apoyo humano/research, no canonico |
| Historico | `ARCHIVE/` | Referencia historica, no canonica |

## 2. Estructura del Repo Framework

```text
/
|-- README.md
|-- OPERACION/
|   |-- CONTEXT_ROUTER.md
|   |-- AGENTS/
|   +-- CONSTRAINTS/
|-- GRAPHIFY/
|   |-- GRAPHIFY_POLICY.md
|   +-- OUTPUT_CONTRACT.md
|-- PROJECT_TEMPLATE/
|-- THEORY/
|-- TEMPLATES/
|-- EXAMPLES/
|-- SATELLITE/
+-- ARCHIVE/
```

### `README.md`

Es la puerta de entrada humana. Explica como esta organizado el framework y que fuente consultar primero.

### `OPERACION/`

Contiene lo que gobierna ejecucion:

- `CONTEXT_ROUTER.md`: matriz oficial para decidir que leer.
- `CONSTRAINTS/*.md`: reglas ejecutables de arquitectura, contexto, memoria, herramientas, agentes y proceso.
- `AGENTS/*.md`: contratos de Manager, Coder, Reviewer y Debugger.

No debe acumular teoria larga ni tutoriales.

### `GRAPHIFY/`

Define como usar Graphify:

- `GRAPHIFY_POLICY.md`: cuando usarlo y con que limites.
- `OUTPUT_CONTRACT.md`: ubicacion y rol esperado de `GRAPH_REPORT.md`, `graph.json` y `graph.html`.

Graphify ayuda a navegar y analizar impacto. No decide por encima de specs, SDD, decisiones o memoria.

### `PROJECT_TEMPLATE/`

Es el molde para crear proyectos reales. Tiene estructura canonica esperada, pero sus contenidos son placeholders.

### `THEORY/`

Explica el por que del framework. Sirve para onboarding, criterio y aprendizaje. No se carga durante una tarea tecnica rutinaria.

### `TEMPLATES/`

Contiene formatos reutilizables que pueden copiarse o adaptarse: tarea activa, decision, hechos del proyecto y spec.

### `EXAMPLES/`

Muestra casos de referencia para entender uso practico: bug backend, nuevo feature y research con NotebookLM.

### `SATELLITE/`

Define limites de herramientas externas:

- Obsidian ayuda a pensar y visualizar.
- NotebookLM ayuda a investigar fuentes externas.

Ninguno reemplaza el repo como fuente oficial.

## 3. Proyecto Instanciado

Un proyecto real debe nacer al copiar o adaptar `PROJECT_TEMPLATE/` dentro de un repo concreto.

Estructura minima recomendada:

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- tasks/
|   +-- current/
|       |-- active_task.md
|       |-- implementation_plan.md
|       +-- open_questions.md
|-- decisions/
|   |-- decision_log.md
|   +-- adr/
|-- memory/
|   |-- project_facts.md
|   |-- constraints.md
|   |-- known_issues.md
|   |-- patterns.md
|   +-- glossary.md
|-- docs/
|   |-- product/spec.md
|   +-- architecture/sdd.md
+-- graphify-out/
    |-- GRAPH_REPORT.md
    |-- graph.json
    +-- graph.html
```

## 4. Porque Esta Separacion Importa

La IA falla cuando todo parece igual de importante. Esta arquitectura marca autoridad:

- `OPERACION/` dice como actuar.
- `PROJECT_TEMPLATE/` dice que forma debe tener un proyecto.
- El proyecto instanciado dice que es verdad para su dominio.
- `THEORY/` explica el sistema.
- `GRAPHIFY/` define un mapa derivado.
- `SATELLITE/` limita herramientas externas.

Asi el agente puede resolver tareas sin transformar notas, ejemplos o outputs en reglas falsas.

## 5. Flujo de Instanciacion

1. Copiar o adaptar `PROJECT_TEMPLATE/` en el repo del proyecto.
2. Completar `PROJECT_GUIDE.md` con proposito, alcance, estructura, stack y restricciones.
3. Completar `CONTEXT_INDEX.md` con las fuentes oficiales reales.
4. Definir `tasks/current/active_task.md`.
5. Registrar decisiones iniciales en `decisions/decision_log.md`.
6. Completar memoria minima en `memory/project_facts.md` y `memory/constraints.md`.
7. Agregar `docs/product/spec.md` y `docs/architecture/sdd.md` cuando el proyecto lo justifique.
8. Generar o actualizar `graphify-out/*` para tareas estructurales, onboarding o impacto transversal.

## 6. Regla de Ubicacion

| Si el contenido... | Debe vivir en... |
|---|---|
| gobierna ejecucion diaria | `OPERACION/` |
| explica el framework | `THEORY/` |
| sirve como molde reusable | `PROJECT_TEMPLATE/` o `TEMPLATES/` |
| representa verdad del proyecto | proyecto instanciado |
| resume relaciones del repo | `graphify-out/*` |
| es research externo o nota personal | `SATELLITE/`, Obsidian o NotebookLM |
| es historico | `ARCHIVE/` |

## 7. Regla Final

Si un documento sera obedecido por un agente, debe estar en la capa operativa o canonica correcta. Si solo ayuda a entender, debe permanecer como teoria, ejemplo, plantilla, satelite o archivo historico.
