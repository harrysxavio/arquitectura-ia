# CONTEXT_INDEX.md

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Mapear las fuentes oficiales del proyecto para que humanos y agentes carguen solo el contexto necesario.

## Como llenarlo

Agregar solo documentos con una funcion clara de consulta. No listar notas personales, archivos historicos ni outputs derivados como si fueran canonicos.

## Ejemplo minimo

```text
Necesidad: Diseno tecnico
Archivo: docs/architecture/sdd.md
Uso: Consultar antes de cambios estructurales.
```

## Fuentes Oficiales

| Necesidad | Archivo | Uso |
|---|---|---|
| Identidad del proyecto | `PROJECT_GUIDE.md` | Entrada base del proyecto. |
| Tarea actual | `tasks/current/active_task.md` | Alcance y estado del trabajo activo. |
| Plan actual | `tasks/current/implementation_plan.md` | Secuencia de ejecucion cuando aplica. |
| Preguntas abiertas | `tasks/current/open_questions.md` | Dudas que bloquean o cambian alcance. |
| Decisiones | `decisions/decision_log.md` | Decisiones aprobadas y su impacto. |
| ADRs | `decisions/adr/*.md` | Decisiones arquitectonicas extensas. |
| Hechos vigentes | `memory/project_facts.md` | Datos confirmados del proyecto. |
| Restricciones | `memory/constraints.md` | Limites tecnicos, negocio, seguridad y costo. |
| Problemas conocidos | `memory/known_issues.md` | Bugs, deuda o workarounds vigentes. |
| Patrones aprobados | `memory/patterns.md` | Formas aceptadas de implementar. |
| Glosario | `memory/glossary.md` | Terminos del dominio. |
| Spec funcional | `docs/product/spec.md` | Verdad funcional. |
| Diseno tecnico | `docs/architecture/sdd.md` | Diseno y contratos tecnicos. |
| Graphify | `graphify-out/GRAPH_REPORT.md` | Contexto estructural derivado. |

## Nota de uso

Graphify orienta navegacion, pero no reemplaza spec, SDD, decision log ni memoria canonica.
