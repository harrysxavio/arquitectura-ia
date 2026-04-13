# Arquitectura Transversal para IA

Framework documental para trabajar con agentes de IA usando contexto minimo, fuentes de verdad claras y separacion limpia entre operacion, teoria y conocimiento satelite.

Principio rector:

> [!IMPORTANT]
> La calidad del resultado no debe depender del modelo. Debe depender del sistema.

## Como Esta Organizado

```text
/
|-- README.md                 # Puerta de entrada humana
|-- OPERACION/                # Documentos que guian la ejecucion diaria
|-- GRAPHIFY/                 # Politica de contexto estructural persistente
|-- PROJECT_TEMPLATE/         # Plantilla reusable, no proyecto activo
|-- THEORY/                   # Manual teorico y pedagogico
|-- TEMPLATES/                # Formatos reutilizables
|-- EXAMPLES/                 # Casos de uso de referencia
|-- SATELLITE/                # Politicas de conocimiento fuera del nucleo
+-- ARCHIVE/                  # Fuentes historicas no canonicas
```

## Capas Principales

| Capa | Proposito | Es fuente operativa |
|---|---|---|
| `OPERACION/` | Router, constraints y roles de agentes para ejecucion diaria | Si |
| `PROJECT_TEMPLATE/` | Molde para crear un proyecto individual operativo | No, hasta instanciarse |
| `THEORY/` | Explica el framework, sus principios y su uso | No para runtime tecnico |
| `GRAPHIFY/` | Define como usar el grafo estructural del repo | Politica si; outputs derivados no |
| `SATELLITE/` | Define limites de Obsidian y NotebookLM | No |

## Advertencia Sobre PROJECT_TEMPLATE

> [!WARNING]
> `PROJECT_TEMPLATE/` no representa el proyecto actual.

Sus archivos son ejemplos estructurales:

- `PROJECT_TEMPLATE/tasks/current/active_task.md` no es una tarea activa real.
- `PROJECT_TEMPLATE/decisions/decision_log.md` no contiene decisiones reales.
- `PROJECT_TEMPLATE/memory/project_facts.md` no contiene hechos reales.

Solo cuando esta plantilla se copia o adapta dentro de un repo de proyecto, esos archivos pasan a ser canonicos para ese proyecto.

## Fuentes de Autoridad

| Informacion | Fuente oficial |
|---|---|
| Como navegar este framework | `README.md` |
| Que contexto cargar | `OPERACION/CONTEXT_ROUTER.md` |
| Reglas de ejecucion | `OPERACION/CONSTRAINTS/*.md` |
| Rol de cada agente | `OPERACION/AGENTS/*.md` |
| Explicacion pedagogica | `THEORY/*.md` |
| Politica Graphify | `GRAPHIFY/GRAPHIFY_POLICY.md` |
| Contrato de outputs Graphify | `GRAPHIFY/OUTPUT_CONTRACT.md` |
| Rol de Obsidian | `SATELLITE/OBSIDIAN_POLICY.md` |
| Molde de proyecto | `PROJECT_TEMPLATE/` |
| Proyecto activo real | Repo instanciado desde `PROJECT_TEMPLATE/` |

## Ruta de Lectura Humana

1. `README.md`
2. `THEORY/01_principios.md`
3. `THEORY/02_arquitectura.md`
4. `THEORY/04_contexto.md`
5. `THEORY/05_agentes.md`
6. `OPERACION/CONTEXT_ROUTER.md`
7. `GRAPHIFY/GRAPHIFY_POLICY.md`
8. `SATELLITE/OBSIDIAN_POLICY.md`
9. `PROJECT_TEMPLATE/`
10. `EXAMPLES/`

## Regla de Uso Diario

> [!TIP]
> No cargues todo el repo por defecto. Empieza por el contexto minimo del proyecto activo y escala solo cuando la tarea lo justifique.
