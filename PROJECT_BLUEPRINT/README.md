# PROJECT_BLUEPRINT

`PROJECT_BLUEPRINT/` es la guia de adopcion del framework. Explica como convertir las ideas del repositorio en un proyecto real, sin copiar todavia archivos ni rellenar plantillas.

## Rol

El blueprint responde tres preguntas:

- que fuentes debe tener un proyecto OpenSpec-first;
- que autoridad tiene cada fuente;
- como empezar sin crear documentacion innecesaria.

No es una plantilla copiable completa y no reemplaza `PROJECT_TEMPLATE/`. Si `PROJECT_TEMPLATE/` es el molde, `PROJECT_BLUEPRINT/` es la explicacion para saber por que ese molde existe y como adaptarlo con criterio.

## Para Quien Es

Una persona no tecnica puede usarlo para entender como se ordena el conocimiento del proyecto. Una persona tecnica puede usarlo para decidir que archivos crear primero, que contenido poner en cada uno y que errores evitar al adoptar el framework.

## Ruta de Adopcion

```text
framework -> PROJECT_BLUEPRINT -> PROJECT_TEMPLATE -> SAMPLE_PROJECT -> proyecto activo
```

- `framework`: define reglas, capas y politica general.
- `PROJECT_BLUEPRINT/`: explica como se reparte la autoridad documental.
- `PROJECT_TEMPLATE/`: entrega el molde reusable para iniciar un proyecto.
- `SAMPLE_PROJECT/`: muestra el molde aplicado en un caso ejecutable.
- `proyecto activo`: adapta la plantilla y se gobierna por sus propias fuentes canonicas.

## Como Usarlo

1. Leer `PROJECT_DOCUMENTS.md` para entender que documento responde que pregunta.
2. Revisar `PROJECT_STRUCTURE_EXAMPLE.md` para elegir estructura minima o estandar.
3. Revisar `../docs/stack.md` para distinguir instalacion minima, herramientas opcionales y dependencias del proyecto activo.
4. Copiar o adaptar `PROJECT_TEMPLATE/` solo despues de entender el reparto de autoridad.
5. Completar primero identidad, contexto y primera spec funcional.
6. Agregar memoria, decisiones o Graphify cuando haya una razon real.

## Flujo de Trabajo Recomendado

Una adopcion sana empieza pequeña:

1. Definir identidad y alcance en `PROJECT_GUIDE.md`.
2. Crear `CONTEXT_INDEX.md` con las fuentes que realmente existen.
3. Escribir la primera spec OpenSpec para la capacidad principal.
4. Documentar arquitectura estable solo en el nivel necesario.
5. Registrar decisiones cuando haya una direccion durable.
6. Agregar memoria compacta cuando existan hechos o restricciones vigentes.

Este orden evita dos extremos: proyectos sin fuentes de autoridad y proyectos llenos de archivos vacios.

## Autoridad Documental

| Tipo de informacion | Fuente |
|---|---|
| Comportamiento funcional vigente | `openspec/specs/*/spec.md` |
| Cambio activo | `openspec/changes/*` |
| Arquitectura estable | `docs/architecture/system.md` |
| Decisiones vigentes | `decisions/decision_log.md` y ADRs |
| Memoria compacta | `memory/facts.md`, `memory/constraints.md`, `memory/patterns.md` |
| Navegacion derivada | `graphify-out/*` |

## Graphify

Graphify entra cuando reduce exploracion: incorporacion tecnica, impacto transversal, refactors amplios o tareas ambiguas.

Graphify no entra por defecto en cambios locales, typos, ajustes claros o cuando OpenSpec ya indica exactamente que revisar.

## Stack y Herramientas

El blueprint no exige instalar todo. Markdown y Git bastan para adoptar el modelo documental. Python, Node/npm, OpenSpec CLI, Graphify, MarkItDown, Obsidian o Codex entran segun la necesidad del proyecto. La regla completa esta en `../docs/stack.md`: separar runtime, desarrollo y herramientas auxiliares.

## Errores Comunes

- Copiar toda la plantilla y dejar placeholders sin completar.
- Crear muchos documentos antes de tener una primera spec funcional.
- Usar memoria para guardar tareas pendientes.
- Escribir reglas funcionales en arquitectura porque parece mas visible.
- Tratar el blueprint como autoridad del proyecto activo. Una vez creado el proyecto, mandan sus propias fuentes.

## Regla

Blueprint orienta; la plantilla moldea; el ejemplo demuestra; el proyecto activo decide con sus fuentes canonicas.
