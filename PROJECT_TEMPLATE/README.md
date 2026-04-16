# PROJECT_TEMPLATE

Molde reusable para crear un proyecto con arquitectura OpenSpec-first. No es documentacion final: es un punto de partida que debe completarse con identidad, reglas y decisiones reales del proyecto.

## Proposito

Esta carpeta existe para que un proyecto nuevo no empiece desde cero. Entrega los documentos minimos para separar comportamiento, arquitectura, decisiones, memoria y contexto derivado desde el primer dia.

Para una persona no tecnica, la plantilla muestra que cada pregunta tiene un lugar. Para una persona tecnica, muestra que archivos copiar, en que orden completarlos y que no debe duplicarse.

## Estructura

```text
PROJECT_TEMPLATE/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- openspec/
|   |-- specs/example-capability/spec.md
|   |-- changes/.gitkeep
|   `-- archive/.gitkeep
|-- docs/architecture/system.md
|-- decisions/decision_log.md
|-- decisions/adr/ADR_TEMPLATE.md
|-- memory/facts.md
|-- memory/constraints.md
|-- memory/patterns.md
|-- memory/glossary.md
`-- graphify-out/
```

## Uso

1. Copiar o adaptar la plantilla en un proyecto real.
2. Completar `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
3. Crear specs por capability en `openspec/specs/`.
4. Usar `openspec/changes/` para cambios activos.
5. Mantener memoria compacta y Graphify derivado.

## Orden Recomendado

Primero completa `PROJECT_GUIDE.md`: nombre, usuarios, problema y alcance. Luego completa `CONTEXT_INDEX.md` para que humanos y agentes sepan donde mirar. Despues crea la primera spec funcional en `openspec/specs/`.

No empieces llenando memoria, decisiones o Graphify. Esas piezas sirven cuando ya hay hechos, decisiones o estructura que vale recordar o navegar.

## Que Debe Adaptarse

- Reglas locales de agentes en `AGENTS.md`.
- Identidad y alcance en `PROJECT_GUIDE.md`.
- Fuentes oficiales en `CONTEXT_INDEX.md`.
- Specs reales en `openspec/specs/`.
- Arquitectura concreta en `docs/architecture/system.md`.
- Restricciones del dominio en `memory/constraints.md`.

## Que No Debe Hacerse

- Dejar placeholders como si fueran contenido final.
- Poner reglas funcionales en `PROJECT_GUIDE.md` o arquitectura.
- Usar `tasks/current/` como sistema principal de trabajo activo.
- Tratar `graphify-out/` como fuente canonica.

## Regla Breve

La plantilla no manda sobre el proyecto: se vuelve util cuando el proyecto la completa con fuentes reales.
