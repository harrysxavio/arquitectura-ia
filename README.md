# Arquitectura Transversal para IA

Framework documental para trabajar con agentes de IA usando contexto minimo, fuentes de verdad claras y separacion limpia entre operacion, teoria, blueprint de proyecto, plantilla integral y conocimiento satelite.

Principio rector:

> La calidad del resultado no debe depender del modelo. Debe depender del sistema.

## Como Esta Organizado

```text
/
|-- README.md                 # Mapa maestro del framework
|-- AGENTS.md                 # Instruccion local de tooling para este repo
|-- STRUCTURE_AUDIT.md        # Registro estructural de referencia
|-- OPERACION/                # Router, constraints y contratos de agentes
|-- GRAPHIFY/                 # Politica de contexto estructural derivado
|-- THEORY/                   # Fundamentos y explicacion conceptual
|-- PROJECT_BLUEPRINT/        # Plano documental de un proyecto real
|-- PROJECT_TEMPLATE/         # Molde integral reusable, no proyecto activo
|-- SAMPLE_PROJECT/           # Ejemplo completo ya instanciado y guiado
|-- EXAMPLES/                 # Casos de uso de referencia
|-- SATELLITE/                # Politicas de conocimiento fuera del nucleo
`-- ARCHIVE/                  # Fuentes historicas no canonicas
```

## Capas Principales

| Capa | Proposito | Autoridad |
|---|---|---|
| `README.md` | Mapa maestro y ruta de lectura. | Si, para orientacion del framework. |
| `AGENTS.md` raiz | Puente operativo minimo para Codex/Graphify en este repo-framework. | Si, solo para tooling local del repo. |
| `OPERACION/` | Router, constraints y roles de agentes para ejecucion diaria. | Si, para ejecucion. |
| `GRAPHIFY/` | Politica y contrato del contexto estructural derivado. | Politica si; outputs derivados no. |
| `THEORY/` | Fundamentos, principios y explicacion pedagogica. | No para runtime tecnico. |
| `PROJECT_BLUEPRINT/` | Anatomia documental de un proyecto instanciado. | Si, para explicar estructura de proyecto. |
| `PROJECT_TEMPLATE/` | Molde integral y unico para crear un proyecto individual operativo. | No, hasta instanciarse. |
| `SAMPLE_PROJECT/` | Ejemplo completo, rellenado y guiado de un proyecto instanciado. | No; demostracion practica. |
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
- `PROJECT_TEMPLATE/` contiene el molde integral y unico para crear ese proyecto.
- `SAMPLE_PROJECT/` muestra ese molde ya instanciado, rellenado y guiado para aprender en la practica.
- `OPERACION/` gobierna la ejecucion diaria y la carga de contexto.

## Rol del AGENTS.md raiz

El `AGENTS.md` de la raiz existe para instrucciones locales de tooling en este repo-framework, especialmente Codex y Graphify.

No es una autoridad paralela sobre roles de agentes:

| Archivo | Rol |
|---|---|
| `AGENTS.md` raiz | Puente operativo minimo para herramientas que leen instrucciones locales del repo. |
| `OPERACION/AGENTS/*.md` | Contratos globales de Manager, Coder, Reviewer y Debugger. |
| `PROJECT_TEMPLATE/AGENTS.md` | Plantilla para adaptar esos roles dentro de un proyecto instanciado. |

Si hay conflicto de rol, ganan los contratos de `OPERACION/AGENTS/*.md`, salvo decision documentada.

## Advertencia Sobre PROJECT_TEMPLATE

`PROJECT_TEMPLATE/` no representa el proyecto actual.

Sus archivos son ejemplos estructurales:

- `PROJECT_TEMPLATE/tasks/current/active_task.md` no es una tarea activa real.
- `PROJECT_TEMPLATE/decisions/decision_log.md` no contiene decisiones reales.
- `PROJECT_TEMPLATE/memory/project_facts.md` no contiene hechos reales.

Solo cuando esta plantilla se copia o adapta dentro de un repo de proyecto, esos archivos pasan a ser canonicos para ese proyecto.

`PROJECT_TEMPLATE/` tambien es la unica fuente de plantillas `.md` para la arquitectura propuesta. No hay una carpeta separada de plantillas documentales sueltas.

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
| Instrucciones locales de tooling en este repo | `AGENTS.md` raiz |
| Rol de cada agente | `OPERACION/AGENTS/*.md` |
| Explicacion pedagogica | `THEORY/*.md` |
| Plano de proyecto instanciado | `PROJECT_BLUEPRINT/*.md` |
| Politica Graphify | `GRAPHIFY/GRAPHIFY_POLICY.md` |
| Contrato de outputs Graphify | `GRAPHIFY/OUTPUT_CONTRACT.md` |
| Rol de Obsidian | `SATELLITE/OBSIDIAN_POLICY.md` |
| Molde de proyecto | `PROJECT_TEMPLATE/` |
| Ejemplo guiado de proyecto instanciado | `SAMPLE_PROJECT/` |
| Proyecto activo real | Repo instanciado desde `PROJECT_TEMPLATE/` |

## Ruta de Lectura Humana

1. `README.md`
2. `THEORY/01_principios.md`
3. `THEORY/02_arquitectura.md`
4. `PROJECT_BLUEPRINT/README.md`
5. `PROJECT_BLUEPRINT/PROJECT_DOCUMENTS.md`
6. `PROJECT_BLUEPRINT/PROJECT_STRUCTURE_EXAMPLE.md`
7. `THEORY/04_contexto.md`
8. `THEORY/05_agentes.md`
9. `OPERACION/CONTEXT_ROUTER.md`
10. `GRAPHIFY/GRAPHIFY_POLICY.md`
11. `SATELLITE/OBSIDIAN_POLICY.md`
12. `PROJECT_TEMPLATE/`
13. `SAMPLE_PROJECT/`
14. `EXAMPLES/`

## Regla de Uso Diario

No cargues todo el repo por defecto. Empieza por el contexto minimo del proyecto activo y escala solo cuando la tarea lo justifique.
