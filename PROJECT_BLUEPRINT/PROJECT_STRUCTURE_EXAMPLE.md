# Estructura Ejemplo de Proyecto

> Blueprint estructural. Este documento muestra como deberia verse un proyecto real despues de adoptar el framework.

## Proposito

Mostrar dos niveles de adopcion:

- estructura minima: base viable para operar sin ambiguedad;
- estructura estandar: version completa alineada con `PROJECT_TEMPLATE/`.

La estructura estandar lista los `.md` que deben existir como plantilla dentro de `PROJECT_TEMPLATE/`.

## Estructura minima

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- tasks/
|   `-- current/
|       `-- active_task.md
|-- decisions/
|   `-- decision_log.md
`-- memory/
    `-- project_facts.md
```

Esta base alcanza para iniciar operacion disciplinada: identidad, ruta de contexto, reglas locales de agentes, tarea activa, decisiones y hechos vigentes.

## Estructura estandar

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
    `-- graph.html  # opcional, si la herramienta lo genera
```

## Diferencia entre minimo y estandar

| Nivel | Uso | Regla |
|---|---|---|
| Minimo | Iniciar un proyecto sin sobrecargar documentacion. | Completar primero y mantener vigente. |
| Estandar | Operar proyectos con mas superficie, decisiones, specs, diseno tecnico y memoria. | Debe coincidir con los `.md` disponibles en `PROJECT_TEMPLATE/`. |

No todo debe llenarse desde el dia 1. Un proyecto puede partir con la estructura minima y avanzar hacia la estandar cuando la complejidad lo justifique.

## Justificacion de la estructura estandar

La raiz contiene los documentos que un humano o agente debe consultar primero: identidad del proyecto, indice de contexto y reglas locales de agentes.

`tasks/current/` queda separado porque describe el trabajo activo. No debe mezclarse con decisiones historicas ni memoria vigente.

`decisions/` contiene decisiones aprobadas. El log sirve para decisiones breves; las ADRs sirven cuando hay contexto, alternativas e impacto arquitectonico.

`memory/` contiene conocimiento vigente y comprimido. No es backlog, no es diario de trabajo y no reemplaza specs.

`docs/product/` contiene verdad funcional. `docs/architecture/` contiene diseno tecnico.

`graphify-out/` contiene outputs derivados. Debe estar disponible para tareas estructurales, pero no debe gobernar el proyecto. `GRAPH_REPORT.md` aparece en la estructura estandar porque es el punto de entrada humano para Graphify; en `PROJECT_TEMPLATE/` existe solo como placeholder, no como reporte real. El output minimo esperado es `GRAPH_REPORT.md` y `graph.json`; `graph.html` es opcional cuando la herramienta lo genera.

## Flujo de adopcion

1. Copiar o adaptar `PROJECT_TEMPLATE/` dentro del proyecto real.
2. Completar primero la estructura minima.
3. Activar documentos estandar solo cuando exista necesidad real.
4. Registrar decisiones reales en `decisions/decision_log.md` o `decisions/adr/`.
5. Mantener `memory/` como conocimiento vigente, no como archivo historico.
6. Generar `graphify-out/` solo cuando aporte valor estructural.
7. Verificar que cualquier `.md` nuevo marcado como estandar tambien exista como plantilla en `PROJECT_TEMPLATE/`.

## Nota

Esta estructura es una base disciplinada, no una obligacion de llenar todo desde el dia uno. Un documento vacio que nadie consulta agrega ruido; un documento minimo pero vigente reduce contexto innecesario.
