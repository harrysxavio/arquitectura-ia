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
|-- README.md
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
|-- memory/known_issues.md
`-- graphify-out/GRAPH_REPORT.md
```

## Vista Maestra del Template

| Archivo | Para que sirve | Quien lo completa primero | Cuando se usa | Que no debe ponerse | Relacion principal |
|---|---|---|---|---|---|
| `README.md` | Entrada local del proyecto creado desde la plantilla. | Persona responsable del proyecto. | Cuando alguien abre el proyecto por primera vez. | Reglas funcionales detalladas o historial largo. | Enlaza a `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y OpenSpec. |
| `PROJECT_GUIDE.md` | Explica identidad, usuarios, problema, alcance y stack. | Persona responsable del proyecto. | Primero, antes de specs y arquitectura. | Reglas funcionales detalladas. | Da contexto a `CONTEXT_INDEX.md` y OpenSpec. |
| `CONTEXT_INDEX.md` | Mapa de fuentes oficiales. | Persona o agente con revision humana. | Despues de `PROJECT_GUIDE.md`; se actualiza con nuevas specs o fuentes. | Explicaciones largas o notas temporales. | Guia a humanos y agentes hacia OpenSpec, arquitectura, decisiones y memoria. |
| `AGENTS.md` | Reglas locales para agentes. | Persona tecnica o responsable de operacion. | Al preparar trabajo asistido por IA. | Teoria general o reglas funcionales. | Usa `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y el router de operacion. |
| `openspec/specs/*/spec.md` | Comportamiento funcional aprobado. | Persona define; agente puede redactar. | Antes de implementar o al consolidar cambios aprobados. | Detalles internos de implementacion. | Es la fuente funcional principal. |
| `openspec/changes/*/proposal.md` | Intencion, alcance y no alcance de un cambio. | Persona define; agente puede proponer borrador. | Al iniciar cambio funcional o significativo. | Implementacion detallada. | Se complementa con deltas, `design.md` y `tasks.md`. |
| `openspec/changes/*/design.md` | Diseno tecnico del cambio. | Persona tecnica o agente con revision. | Solo si cambia arquitectura, datos, contratos o integraciones. | Reglas funcionales completas. | Enlaza OpenSpec con `docs/architecture/system.md`. |
| `openspec/changes/*/tasks.md` | Lista verificable de ejecucion y validacion. | Agente puede proponer; persona revisa. | Durante implementacion del cambio. | Backlog general del proyecto. | Sigue `proposal.md`, `design.md` y deltas OpenSpec. |
| `docs/architecture/system.md` | Arquitectura tecnica estable. | Persona tecnica o agente desde codigo real. | Despues de definir primeras capacidades y estructura. | Requisitos funcionales detallados. | Explica como se implementa lo que OpenSpec gobierna. |
| `decisions/decision_log.md` | Indice breve de decisiones vigentes. | Persona responsable o tech lead. | Cuando se aprueba una direccion durable. | Tareas pendientes o debates largos. | Puede enlazar ADRs y cambios OpenSpec. |
| `decisions/adr/*.md` | Contexto y consecuencias de decisiones grandes. | Persona tecnica; agente puede redactar borrador. | Para decisiones estructurales o de alto impacto. | Cambios funcionales que pertenecen a OpenSpec. | Se indexa desde `decision_log.md`. |
| `memory/facts.md` | Hechos confirmados que conviene recordar. | Persona o agente con evidencia. | Cuando existan hechos reales y vigentes. | Hipotesis, backlog o historia larga. | Complementa contexto sin reemplazar fuentes. |
| `memory/constraints.md` | Limites tecnicos, negocio, seguridad y costo. | Persona responsable del dominio o tecnologia. | Antes de implementar restricciones relevantes. | Preferencias vagas. | Informa decisiones y cambios. |
| `memory/patterns.md` | Patrones aprobados y antipatrones. | Persona tecnica o agente tras repeticion validada. | Cuando una forma de trabajo ya esta validada. | Reglas funcionales. | Ayuda a consistencia de implementacion y revision. |
| `memory/glossary.md` | Terminos ambiguos del dominio. | Persona del dominio. | Solo cuando evita malentendidos reales. | Diccionario general. | Ayuda a specs, docs y agentes. |
| `memory/known_issues.md` | Problemas conocidos que afectan trabajo futuro. | Persona tecnica o agente con evidencia. | Cuando un problema existe y aun no se resuelve. | Backlog general o deseos futuros. | Puede alimentar cambios OpenSpec o tareas de mantenimiento. |
| `graphify-out/*` | Salida derivada para navegacion. | Herramienta; persona o agente la valida contra fuentes. | Cuando Graphify se use en el proyecto. | Autoridad funcional o tecnica. | Ayuda a encontrar archivos; no decide. |

## Uso

1. Copiar o adaptar la plantilla en un proyecto real.
2. Completar `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
3. Crear specs por capability en `openspec/specs/`.
4. Usar `openspec/changes/` para cambios activos.
5. Mantener memoria compacta y Graphify derivado.

## Como Llenarlo Sin Perder Autoridad

1. La persona define problema, alcance y prioridades en `PROJECT_GUIDE.md`.
2. La persona o agente arma `CONTEXT_INDEX.md` con fuentes reales.
3. La persona aprueba la primera capacidad y el agente puede redactar la spec inicial.
4. El agente puede proponer `proposal.md`, `design.md` y `tasks.md`, pero la persona revisa alcance, riesgos y decisiones.
5. Arquitectura se completa cuando hay componentes reales que explicar.
6. Memoria se completa cuando hay hechos o restricciones confirmadas, no antes.

Si un archivo aun no tiene contenido real, es mejor dejar una guia breve y ejemplo minimo que inventar informacion.

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
- Crear planes o tareas paralelas fuera de `openspec/changes/*`.
- Tratar `graphify-out/` como fuente canonica.

## Regla Breve

La plantilla no manda sobre el proyecto: se vuelve util cuando el proyecto la completa con fuentes reales.
