# Stack y Setup

Esta guia explica que herramientas necesita el framework, cuales son opcionales y como instalarlas sin mezclarlo todo en un unico `requirements.txt`.

## Lectura Rapida

Para empezar a leer y aplicar el modelo solo necesitas Git, un editor de Markdown y acceso al repositorio. Para ejecutar proyectos concretos puedes necesitar Python, Node/npm u otras herramientas segun el stack del proyecto activo.

OpenSpec, Graphify, MarkItDown, Obsidian y Codex cumplen roles distintos. No todos son obligatorios y no todos se instalan con Python.

## Capas del Stack

| Herramienta | Rol en el framework | Obligatoria? | Instalacion tipica |
|---|---|---|---|
| Markdown | Formato base de documentacion versionada. | Si | Editor de texto o VS Code. |
| Git | Versiona docs, specs, decisiones y codigo. | Si | Instalador de Git o gestor del sistema. |
| Python | Ejecuta scripts, ejemplos o proyectos Python. | Segun proyecto | Instalador oficial, `pyenv`, `uv` o gestor del sistema. |
| OpenSpec | Fuente de verdad funcional y flujo de cambios. | Si como modelo; CLI opcional | Node.js y npm/pnpm/yarn/bun si se usa CLI. |
| Graphify | Grafo derivado para navegacion e impacto. | Opcional | Segun distribucion de Graphify; puede ser Python o CLI externa. |
| MarkItDown | Convierte insumos externos a Markdown. | Opcional | Paquete Python o herramienta CLI, segun uso. |
| Obsidian | Notas personales y mapas de pensamiento. | Opcional | Instalacion manual de escritorio. |
| Codex | Agente de trabajo sobre el repo. | Opcional | Herramienta/entorno de agente, no dependencia del proyecto. |

## Instalacion Minima

Usa esta instalacion si quieres aprender el framework, leer la documentacion o copiar `PROJECT_TEMPLATE/` a un proyecto nuevo.

1. Instala Git.
2. Instala un editor que lea Markdown, por ejemplo VS Code.
3. Clona el repositorio.
4. Lee `README.md`, `PROJECT_BLUEPRINT/README.md` y `PROJECT_TEMPLATE/README.md`.

No necesitas instalar Graphify, MarkItDown ni un entorno Python solo para entender el framework.

## Instalacion Para un Proyecto Python

Si el proyecto activo tiene codigo Python, separa dependencias por proposito:

```text
requirements.txt         dependencias runtime del proyecto
requirements-dev.txt     tests, linters y herramientas de desarrollo
requirements-tools.txt   herramientas auxiliares de documentacion o analisis
```

No todo debe ir en `requirements.txt`. Ese archivo deberia contener solo lo que la aplicacion necesita para ejecutarse. Herramientas como MarkItDown, linters, generadores o utilidades de analisis suelen pertenecer a `requirements-dev.txt` o `requirements-tools.txt`.

Ejemplo:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

En macOS/Linux, la activacion suele ser:

```bash
source .venv/bin/activate
```

## OpenSpec y Node/npm

OpenSpec es parte del modelo de autoridad aunque no siempre necesites su CLI. Si usas herramientas oficiales o comandos de OpenSpec, revisa su instalacion vigente y separala del stack Python.

Requisitos habituales del CLI:

- Node.js 20.19.0 o superior.
- npm, pnpm, yarn o bun.

Instalacion global con npm:

```bash
npm install -g @fission-ai/openspec@latest
openspec --version
```

Si un proyecto usa OpenSpec CLI de forma estable, documentar los comandos exactos en el README del proyecto activo o en `AGENTS.md`. Si no usa CLI, mantener OpenSpec como estructura documental bajo `openspec/`.

## Graphify

Graphify es opcional y derivado. Sirve para generar `graphify-out/` y ayudar a navegar proyectos grandes o ambiguos.

Uso esperado cuando este disponible:

```bash
graphify update .
```

Si Graphify no esta instalado, el proyecto sigue siendo usable. Solo pierdes el mapa derivado; no pierdes autoridad documental. Nunca poner Graphify como requisito runtime de una aplicacion salvo que la aplicacion realmente lo ejecute.

## MarkItDown

MarkItDown puede convertir PDFs, documentos u otros insumos a Markdown antes de resumirlos o incorporarlos al repo. Es herramienta auxiliar, no fuente canonica.

MarkItDown requiere Python 3.10 o superior. Si se usa en un proyecto, conviene instalarla como herramienta:

```bash
python -m pip install "markitdown[all]"
```

Para proyectos que quieran controlar formatos y dependencias, registrar MarkItDown en `requirements-tools.txt` y usar grupos opcionales cuando corresponda, por ejemplo:

```text
markitdown[pdf,docx,pptx]
```

Luego documentar el comando concreto de conversion en el proyecto activo:

```bash
markitdown entrada.pdf -o salida.md
```

## Obsidian

Obsidian es opcional. Puede ayudar a pensar, mapear ideas o llevar notas personales, pero no gobierna el proyecto. Si una nota se vuelve importante, se resume y se registra en OpenSpec, arquitectura, decisiones o memoria.

Instalacion: manual, desde el sitio de Obsidian o gestor de escritorio correspondiente.

## Codex

Codex es un agente que puede operar sobre este repo. No es una dependencia que se instale en `requirements.txt`. Su uso depende del entorno del usuario.

Cuando Codex trabaja en un proyecto activo, debe empezar por:

1. `AGENTS.md`
2. `PROJECT_GUIDE.md`
3. `CONTEXT_INDEX.md`
4. OpenSpec relevante
5. Arquitectura, decisiones, memoria o Graphify solo si la tarea lo requiere

## Archivos Clave del Framework

| Archivo | Rol |
|---|---|
| `AGENTS.md` | Reglas locales para agentes. |
| `OPERACION/CONTEXT_ROUTER.md` | Decide que contexto cargar segun tarea y riesgo. |
| `PROJECT_GUIDE.md` | Identidad, alcance y stack del proyecto activo. |
| `CONTEXT_INDEX.md` | Mapa de fuentes oficiales del proyecto activo. |
| `openspec/specs/*/spec.md` | Comportamiento funcional aprobado. |
| `docs/architecture/system.md` | Arquitectura tecnica estable. |
| `graphify-out/*` | Contexto derivado para navegacion. |

## Setup Completo Recomendado

Para trabajar con todas las capacidades del framework:

1. Git y editor Markdown.
2. Python para proyectos, scripts o herramientas Python.
3. Node/npm si usaras OpenSpec CLI.
4. Graphify si necesitas grafo de conocimiento.
5. MarkItDown si procesaras fuentes externas.
6. Obsidian si quieres notas personales fuera del canon.
7. Codex u otro agente si trabajaras con asistencia IA.

## Regla Breve

Instala lo minimo para tu tarea. Documenta por separado runtime, desarrollo y herramientas. Ninguna herramienta opcional debe convertirse en autoridad del proyecto.
