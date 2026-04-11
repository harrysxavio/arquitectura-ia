# Modulo 2 - Arquitectura Troncal del Framework

## 1. Vision General

El framework separa cuatro niveles para que teoria, operacion y conocimiento satelite convivan sin competir.

| Nivel | Rol | Fuente de verdad operativa |
|---|---|---|
| Framework global reusable | Reglas, agentes, router, plantillas, teoria y politicas | Si, para el framework |
| Nucleo operativo del proyecto | Documentos canonicos del proyecto activo | Si, despues de instanciarse |
| Capa teorica / manual | Explicacion y onboarding humano | No para runtime tecnico |
| Conocimiento satelite | Obsidian, NotebookLM, outputs visuales o historicos | No |

## 2. Framework Global Reusable

Este repo contiene el framework global. Su proposito es dar estructura reusable para trabajar con proyectos distintos sin mezclar tareas activas ni decisiones locales.

Incluye:

- `OPERACION/`: router, constraints y contratos de agentes.
- `GRAPHIFY/`: politica y contrato de outputs estructurales.
- `PROJECT_TEMPLATE/`: molde para crear proyectos individuales.
- `THEORY/`: manual teorico y pedagogico.
- `TEMPLATES/`: formatos reutilizables.
- `EXAMPLES/`: casos de uso.
- `SATELLITE/`: politicas para conocimiento fuera del nucleo.
- `ARCHIVE/`: fuentes historicas no canonicas.

## 3. Proyecto Individual Operativo

Un proyecto activo real no es `PROJECT_TEMPLATE/`. Nace cuando la plantilla se copia o adapta dentro de un repo concreto.

Debe contener:

```text
project/
├── AGENTS.md
├── PROJECT_GUIDE.md
├── CONTEXT_INDEX.md
├── tasks/current/
│   ├── active_task.md
│   ├── implementation_plan.md
│   └── open_questions.md
├── decisions/
│   ├── decision_log.md
│   └── adr/
├── memory/
│   ├── project_facts.md
│   ├── constraints.md
│   ├── known_issues.md
│   ├── patterns.md
│   └── glossary.md
├── docs/
│   ├── product/spec.md
│   └── architecture/sdd.md
└── graphify-out/
    ├── GRAPH_REPORT.md
    ├── graph.json
    └── graph.html
```

## 4. Rol de PROJECT_TEMPLATE

`PROJECT_TEMPLATE/` es solo una plantilla reusable.

No contiene:

- tarea activa real,
- decisiones reales,
- hechos reales,
- memoria oficial,
- documentacion tecnica aprobada.

Solo despues de instanciarse en un proyecto, sus archivos pasan a ser canonicos para ese proyecto.

## 5. Rol de OPERACION

`OPERACION/` contiene documentos para ejecutar:

- `CONTEXT_ROUTER.md`: autoridad unica de carga contextual.
- `CONSTRAINTS/*.md`: reglas ejecutables.
- `AGENTS/*.md`: contratos de rol.

No debe contener teoria larga ni ejemplos pedagogicos.

## 6. Rol de Graphify

Graphify actua como contexto estructural persistente derivado. En tareas estructurales entra despues del contexto base y del router, pero antes de exploracion amplia de documentacion o modulos.

No reemplaza `spec.md`, `sdd.md`, `decision_log.md`, `project_facts.md` ni `CONTEXT_INDEX.md`.

## 7. Rol de THEORY

`THEORY/` explica el sistema para humanos. Ayuda al onboarding, pero no se carga durante ejecucion tecnica rutinaria.

## 8. Regla Final

Si explica el sistema, va a `THEORY/`. Si guia ejecucion diaria, va a `OPERACION/`. Si es conocimiento humano no oficial, va a `SATELLITE/` o `ARCHIVE/`.
