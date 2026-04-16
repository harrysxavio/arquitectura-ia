# Estructura Ejemplo de Proyecto OpenSpec-First

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

## Adopcion

1. Completar identidad e indice.
2. Crear specs por capability.
3. Usar changes para trabajo activo.
4. Mantener memoria breve.
5. Consultar Graphify solo cuando reduzca exploracion.
