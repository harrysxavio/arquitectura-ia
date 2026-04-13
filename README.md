# Arquitectura Transversal para IA

Framework documental para trabajar con agentes de IA usando contexto minimo, fuentes de verdad claras y separacion limpia entre operacion, teoria, blueprint de proyecto, plantillas y conocimiento satelite.

Principio rector:

> La calidad del resultado no debe depender del modelo. Debe depender del sistema.

## Como Esta Organizado

```text
/
|-- README.md                 # Mapa maestro del framework
|-- STRUCTURE_AUDIT.md        # Auditoria estructural vigente
|-- OPERACION/                # Router, constraints y contratos de agentes
|-- GRAPHIFY/                 # Politica de contexto estructural derivado
|-- THEORY/                   # Fundamentos y explicacion conceptual
|-- PROJECT_BLUEPRINT/        # Plano documental de un proyecto real
|-- PROJECT_TEMPLATE/         # Molde reusable, no proyecto activo
|-- DOC_TEMPLATES/            # Plantillas documentales sueltas
|-- EXAMPLES/                 # Casos de uso de referencia
|-- SATELLITE/                # Politicas de conocimiento fuera del nucleo
`-- ARCHIVE/                  # Fuentes historicas no canonicas
```

## Capas Principales

| Capa | Proposito | Autoridad |
|---|---|---|
| `README.md` | Mapa maestro y ruta de lectura. | Si, para orientacion del framework. |
| `OPERACION/` | Router, constraints y roles de agentes para ejecucion diaria. | Si, para ejecucion. |
| `GRAPHIFY/` | Politica y contrato del contexto estructural derivado. | Politica si; outputs derivados no. |
| `THEORY/` | Fundamentos, principios y explicacion pedagogica. | No para runtime tecnico. |
| `PROJECT_BLUEPRINT/` | Anatomia documental de un proyecto instanciado. | Si, para explicar estructura de proyecto. |
| `PROJECT_TEMPLATE/` | Molde completo para crear un proyecto individual operativo. | No, hasta instanciarse. |
| `DOC_TEMPLATES/` | Plantillas documentales sueltas. | No; formato auxiliar. |
| `SATELLITE/` | Politicas para Obsidian y NotebookLM. | No; conocimiento fuera del nucleo. |
| `EXAMPLES/` | Casos practicos de referencia. | No. |
| `ARCHIVE/` | Fuentes historicas no canonicas. | No. |

## Como Leer la Arquitectura

La ruta mental correcta es:

```text
framework -> blueprint -> template -> proyecto activo
```

- `THEORY/` explica por que existe el framework y que principios lo sostienen.
- `PROJECT_BLUEPRINT/` explica como debe organizarse documentalmente un proyecto real.
- `PROJECT_TEMPLATE/` contiene archivos copiables para crear ese proyecto.
- `DOC_TEMPLATES/` contiene plantillas documentales sueltas, no una estructura completa.
- `OPERACION/` gobierna la ejecucion diaria y la carga de contexto.

## Advertencia Sobre PROJECT_TEMPLATE

`PROJECT_TEMPLATE/` no representa el proyecto actual.

Sus archivos son ejemplos estructurales:

- `PROJECT_TEMPLATE/tasks/current/active_task.md` no es una tarea activa real.
- `PROJECT_TEMPLATE/decisions/decision_log.md` no contiene decisiones reales.
- `PROJECT_TEMPLATE/memory/project_facts.md` no contiene hechos reales.

Solo cuando esta plantilla se copia o adapta dentro de un repo de proyecto, esos archivos pasan a ser canonicos para ese proyecto.

## Advertencia Sobre PROJECT_BLUEPRINT

`PROJECT_BLUEPRINT/` no es teoria larga ni plantilla copiable. Su funcion es explicar el plano documental de un proyecto real:

- que archivos `.md` debe tener,
- donde vive cada archivo,
- cuando se consulta,
- cuando se vuelve canonico,
- como se relacionan `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `tasks/`, `decisions/`, `memory/`, `docs/` y `graphify-out/`.

Regla de frontera:

- Si explica principios generales, va en `THEORY/`.
- Si explica anatomia documental de un proyecto real, va en `PROJECT_BLUEPRINT/`.
- Si es copiable como molde, va en `PROJECT_TEMPLATE/`.
- Si enruta ejecucion diaria, va en `OPERACION/`.

## Fuentes de Autoridad

| Informacion | Fuente oficial |
|---|---|
| Como navegar este framework | `README.md` |
| Que contexto cargar | `OPERACION/CONTEXT_ROUTER.md` |
| Reglas de ejecucion | `OPERACION/CONSTRAINTS/*.md` |
| Rol de cada agente | `OPERACION/AGENTS/*.md` |
| Explicacion pedagogica | `THEORY/*.md` |
| Plano de proyecto instanciado | `PROJECT_BLUEPRINT/*.md` |
| Politica Graphify | `GRAPHIFY/GRAPHIFY_POLICY.md` |
| Contrato de outputs Graphify | `GRAPHIFY/OUTPUT_CONTRACT.md` |
| Rol de Obsidian | `SATELLITE/OBSIDIAN_POLICY.md` |
| Molde de proyecto | `PROJECT_TEMPLATE/` |
| Plantillas documentales sueltas | `DOC_TEMPLATES/` |
| Proyecto activo real | Repo instanciado desde `PROJECT_TEMPLATE/` |

## Ruta de Lectura Humana

1. `README.md`
2. `THEORY/01_principios.md`
3. `THEORY/02_arquitectura.md`
4. `PROJECT_BLUEPRINT/PROJECT_DOCUMENTS.md`
5. `PROJECT_BLUEPRINT/PROJECT_STRUCTURE_EXAMPLE.md`
6. `THEORY/04_contexto.md`
7. `THEORY/05_agentes.md`
8. `OPERACION/CONTEXT_ROUTER.md`
9. `GRAPHIFY/GRAPHIFY_POLICY.md`
10. `SATELLITE/OBSIDIAN_POLICY.md`
11. `PROJECT_TEMPLATE/`
12. `DOC_TEMPLATES/`
13. `EXAMPLES/`

## Regla de Uso Diario

No cargues todo el repo por defecto. Empieza por el contexto minimo del proyecto activo y escala solo cuando la tarea lo justifique.
