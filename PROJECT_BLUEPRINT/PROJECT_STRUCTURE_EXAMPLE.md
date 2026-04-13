# Estructura Ejemplo de Proyecto

> Blueprint estructural. Este documento muestra como deberia verse un proyecto real despues de adoptar el framework.

## Arbol recomendado

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- tasks/
|   `-- current/
|       |-- active_task.md
|       |-- implementation_plan.md
|       `-- open_questions.md
|-- decisions/
|   |-- decision_log.md
|   `-- adr/
|       `-- ADR_TEMPLATE.md
|-- memory/
|   |-- project_facts.md
|   |-- constraints.md
|   |-- known_issues.md
|   |-- patterns.md
|   `-- glossary.md
|-- docs/
|   |-- product/
|   |   `-- spec.md
|   `-- architecture/
|       `-- sdd.md
`-- graphify-out/
    |-- GRAPH_REPORT.md
    |-- graph.json
    `-- graph.html
```

## Justificacion

La raiz contiene los documentos que un humano o agente debe consultar primero: identidad del proyecto, indice de contexto y reglas locales de agentes.

`tasks/current/` queda separado porque describe el trabajo activo. No debe mezclarse con decisiones historicas ni memoria vigente.

`decisions/` contiene decisiones aprobadas. El log sirve para decisiones breves; las ADRs sirven cuando hay contexto, alternativas e impacto arquitectonico.

`memory/` contiene conocimiento vigente y comprimido. No es backlog, no es diario de trabajo y no reemplaza specs.

`docs/product/` contiene verdad funcional. `docs/architecture/` contiene diseno tecnico.

`graphify-out/` contiene outputs derivados. Debe estar disponible para tareas estructurales, pero no debe gobernar el proyecto.

## Flujo de adopcion

1. Copiar o adaptar `PROJECT_TEMPLATE/` dentro del proyecto real.
2. Completar `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y `tasks/current/active_task.md`.
3. Completar solo los documentos necesarios para el estado actual del proyecto.
4. Registrar decisiones reales en `decisions/decision_log.md` o `decisions/adr/`.
5. Mantener `memory/` como conocimiento vigente, no como archivo historico.
6. Generar `graphify-out/` solo cuando aporte valor estructural.

## Nota

Esta estructura es una base disciplinada, no una obligacion de llenar todo desde el dia uno. Un documento vacio que nadie consulta agrega ruido; un documento minimo pero vigente reduce contexto innecesario.
