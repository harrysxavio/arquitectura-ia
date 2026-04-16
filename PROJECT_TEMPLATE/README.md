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

## Vista Maestra del Template

| Archivo | Para que sirve | Cuando se completa | Que no debe ponerse | Relacion principal |
|---|---|---|---|---|
| `PROJECT_GUIDE.md` | Explica identidad, usuarios, problema, alcance y stack. | Primero, antes de specs y arquitectura. | Reglas funcionales detalladas. | Da contexto a `CONTEXT_INDEX.md` y OpenSpec. |
| `CONTEXT_INDEX.md` | Mapa de fuentes oficiales. | Despues de `PROJECT_GUIDE.md`; se actualiza con nuevas specs o fuentes. | Explicaciones largas o notas temporales. | Guia a humanos y agentes hacia OpenSpec, arquitectura, decisiones y memoria. |
| `AGENTS.md` | Reglas locales para agentes. | Al preparar trabajo asistido por IA. | Teoria general o reglas funcionales. | Usa `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y el router de operacion. |
| `openspec/specs/*/spec.md` | Comportamiento funcional aprobado. | Antes de implementar o al consolidar cambios aprobados. | Detalles internos de implementacion. | Es la fuente funcional principal. |
| `openspec/changes/*/proposal.md` | Intencion, alcance y no alcance de un cambio. | Al iniciar cambio funcional o significativo. | Implementacion detallada. | Se complementa con deltas, `design.md` y `tasks.md`. |
| `openspec/changes/*/design.md` | Diseno tecnico del cambio. | Solo si cambia arquitectura, datos, contratos o integraciones. | Reglas funcionales completas. | Enlaza OpenSpec con `docs/architecture/system.md`. |
| `openspec/changes/*/tasks.md` | Lista verificable de ejecucion y validacion. | Durante implementacion del cambio. | Backlog general del proyecto. | Sigue `proposal.md`, `design.md` y deltas OpenSpec. |
| `docs/architecture/system.md` | Arquitectura tecnica estable. | Despues de definir primeras capacidades y estructura. | Requirements funcionales detallados. | Explica como se implementa lo que OpenSpec gobierna. |
| `docs/architecture/sdd.md` | Puente opcional de diseno narrativo. | Solo si ayuda a lectores humanos. | Arquitectura completa duplicada. | Enlaza a `system.md` y OpenSpec. |
| `docs/product/spec.md` | Puente opcional de lectura de producto. | Solo si hace falta una narrativa de producto separada. | Scenarios funcionales autoritativos. | Enlaza a `PROJECT_GUIDE.md` y OpenSpec. |
| `decisions/decision_log.md` | Indice breve de decisiones vigentes. | Cuando se aprueba una direccion durable. | Tareas pendientes o debates largos. | Puede enlazar ADRs y cambios OpenSpec. |
| `decisions/adr/*.md` | Contexto y consecuencias de decisiones grandes. | Para decisiones estructurales o de alto impacto. | Cambios funcionales que pertenecen a OpenSpec. | Se indexa desde `decision_log.md`. |
| `memory/facts.md` | Hechos confirmados que conviene recordar. | Cuando existan hechos reales y vigentes. | Hipotesis, backlog o historia larga. | Complementa contexto sin reemplazar fuentes. |
| `memory/constraints.md` | Limites tecnicos, negocio, seguridad y costo. | Antes de implementar restricciones relevantes. | Preferencias vagas. | Informa decisiones y cambios. |
| `memory/patterns.md` | Patrones aprobados y antipatrones. | Cuando una forma de trabajo ya esta validada. | Reglas funcionales. | Ayuda a consistencia de implementacion y revision. |
| `memory/glossary.md` | Terminos ambiguos del dominio. | Solo cuando evita malentendidos reales. | Diccionario general. | Ayuda a specs, docs y agentes. |
| `graphify-out/*` | Salida derivada para navegacion. | Cuando Graphify se use en el proyecto. | Autoridad funcional o tecnica. | Ayuda a encontrar archivos; no decide. |
| `tasks/current/*` | Puente de compatibilidad. | Solo si una herramienta espera esa ruta. | Trabajo activo real. | Debe enlazar a `openspec/changes/*`. |

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
- Usar `tasks/current/` como sistema principal de trabajo activo.
- Tratar `graphify-out/` como fuente canonica.

## Regla Breve

La plantilla no manda sobre el proyecto: se vuelve util cuando el proyecto la completa con fuentes reales.
