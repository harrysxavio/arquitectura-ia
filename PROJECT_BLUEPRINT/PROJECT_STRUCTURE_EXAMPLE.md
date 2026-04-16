# Estructura Ejemplo de Proyecto OpenSpec-First

Este documento muestra una estructura recomendada para proyectos que adoptan el framework. No exige usar todas las carpetas desde el primer dia; muestra que piezas conviene tener para que el conocimiento no se disperse.

## Como Elegir Estructura

Usa la estructura minima cuando el proyecto esta empezando, tiene pocas capacidades o solo necesita una fuente funcional clara. Usa la estructura estandar cuando ya hay cambios activos, decisiones durables, memoria compacta o necesidad de navegacion derivada.

## Estructura Minima

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- openspec/
|   |-- specs/<capability>/spec.md
|   `-- changes/
|-- docs/architecture/system.md
|-- decisions/decision_log.md
`-- memory/
    |-- facts.md
    |-- constraints.md
    `-- patterns.md
```

Esta estructura basta para operar con una fuente funcional clara, cambios trazables y memoria compacta.

La estructura minima ya permite trabajar OpenSpec-first: hay identidad, indice, specs, cambios, arquitectura, decisiones y memoria. Si una carpeta no tiene contenido real todavia, es mejor dejarla simple que llenarla con texto generico.

## Estructura Estandar

```text
project/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- openspec/
|   |-- specs/<capability>/spec.md
|   |-- changes/<change-id>/
|   |   |-- proposal.md
|   |   |-- design.md
|   |   |-- tasks.md
|   |   `-- specs/<capability>/spec.md
|   `-- archive/
|-- docs/architecture/system.md
|-- decisions/
|   |-- decision_log.md
|   `-- adr/
|-- memory/
|   |-- facts.md
|   |-- constraints.md
|   |-- patterns.md
|   `-- glossary.md
`-- graphify-out/
```

## Flujo de Adopcion

1. Completar `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
2. Crear specs por capability en `openspec/specs/`.
3. Crear changes para trabajo activo en `openspec/changes/`.
4. Mantener arquitectura estable en `docs/architecture/system.md`.
5. Registrar decisiones breves y usar ADRs solo cuando aporten.
6. Mantener memoria breve y separada.
7. Consultar Graphify solo si reduce exploracion o aclara impacto.

## Que Completar Primero

El orden recomendado no es accidental. `PROJECT_GUIDE.md` fija identidad y alcance. `CONTEXT_INDEX.md` evita busquedas ambiguas. OpenSpec define comportamiento. Arquitectura explica como se construye. Decisiones y memoria entran cuando ya existe conocimiento que vale conservar.

## Que No Hacer

- Crear ADRs antes de tener una decision real.
- Copiar placeholders y dejarlos como documentacion final.
- Crear specs sin actores, alcance ni escenarios entendibles.
- Usar Graphify como paso obligatorio para cada cambio.

## Cuando Usar Graphify

Usarlo para incorporacion tecnica, impacto multiarchivo, refactors y tareas ambiguas.

No usarlo como paso obligatorio en cambios locales, ajustes triviales o cuando el archivo afectado ya esta claro.

## Regla Breve

La estructura debe hacer mas facil encontrar autoridad, no aumentar la cantidad de archivos que leer.
