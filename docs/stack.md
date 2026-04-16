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

Prerequisitos:

- Git.
- Editor de Markdown, por ejemplo VS Code.

Comandos:

```bash
git clone <url-del-repo>
cd arquitectura-ia
```

Lectura inicial:

```text
README.md
docs/openspec.md
PROJECT_BLUEPRINT/README.md
PROJECT_TEMPLATE/README.md
```

No necesitas instalar Graphify, MarkItDown ni un entorno Python solo para entender el framework.

## Instalacion Completa

Usa esta instalacion si quieres trabajar con todas las capacidades opcionales.

```bash
git clone <url-del-repo>
cd arquitectura-ia
```

Python para scripts o herramientas Python:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Node/npm para OpenSpec CLI:

```bash
node --version
npm --version
npm install -g @fission-ai/openspec@latest
openspec --version
```

Herramientas Python opcionales:

```bash
python -m pip install "markitdown[all]"
```

Graphify, Obsidian y Codex dependen del entorno del usuario. Instalarlos solo si se usaran.

## Segun Tu Caso

### Solo Quiero Leer y Aprender

Instala:

- Git.
- Un editor de Markdown.

Comandos:

```bash
git clone <url-del-repo>
cd arquitectura-ia
```

No hace falta instalar Python, Node/npm, Graphify, MarkItDown, Obsidian ni Codex. Lee `README.md`, `docs/openspec.md` y `PROJECT_BLUEPRINT/README.md`.

### Quiero Adaptar un Proyecto Existente

Instala:

- Git.
- Editor de Markdown.
- El stack que tu proyecto ya use para ejecutar y validar codigo.

Comandos sugeridos desde el repo del framework:

```bash
cp -r PROJECT_TEMPLATE ../mi-proyecto-base
```

En Windows puedes copiar la carpeta desde el explorador o usar PowerShell:

```powershell
Copy-Item -Recurse PROJECT_TEMPLATE ..\mi-proyecto-base
```

No hace falta instalar Graphify ni OpenSpec CLI al inicio. Primero completa `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, una spec vigente y `docs/architecture/system.md`. Luego decide si necesitas CLI, grafo o herramientas de conversion.

### Quiero Usar OpenSpec CLI

Instala:

- Node.js 20.19.0 o superior.
- npm, pnpm, yarn o bun.
- Paquete `@fission-ai/openspec`.

Comandos:

```bash
npm install -g @fission-ai/openspec@latest
openspec --version
openspec list
openspec validate <change-id> --strict
```

No hace falta Python salvo que tu proyecto lo use. La estructura Markdown de OpenSpec puede usarse sin CLI, pero el CLI ayuda a validar y operar cambios.

### Quiero Usar Graphify

Instala Graphify segun tu entorno. Si esta disponible como comando:

```bash
graphify update .
```

No lo pongas en `requirements.txt` salvo que la aplicacion lo importe o ejecute en runtime. Si solo lo usas para analizar el repo, tratalo como herramienta auxiliar y documentalo en setup o `requirements-tools.txt` cuando aplique.

Graphify es opcional. Ayuda a navegar impacto; no reemplaza OpenSpec, arquitectura ni decisiones.

### Quiero Usar MarkItDown

Instala Python 3.10 o superior y la herramienta:

```bash
python -m pip install "markitdown[all]"
markitdown entrada.pdf -o salida.md
```

No hace falta Node/npm. Si el proyecto controla herramientas auxiliares, agrega MarkItDown a `requirements-tools.txt`, no a `requirements.txt`, salvo que la aplicacion lo necesite para ejecutarse.

### Quiero Usar Obsidian

Instala Obsidian manualmente como aplicacion de escritorio. No hay comando obligatorio del repo.

No hace falta Python ni Node/npm para usar Obsidian como lector o mapa personal. Tampoco debes mover la autoridad a Obsidian: si una nota se vuelve relevante, resumirla en OpenSpec, arquitectura, decisiones o memoria.

### Quiero Trabajar con Codex

Instala o abre Codex desde su entorno propio. No va en `requirements.txt`, `requirements-dev.txt` ni `requirements-tools.txt`.

Antes de pedir cambios, asegurate de que el proyecto tenga:

- `AGENTS.md` con reglas locales;
- `PROJECT_GUIDE.md` con identidad y alcance;
- `CONTEXT_INDEX.md` con fuentes oficiales;
- OpenSpec suficiente para el comportamiento que se quiere tocar.

Codex puede redactar specs, proponer tareas e implementar, pero necesita fuentes claras para no inventar autoridad.

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

Si agregas herramientas auxiliares:

```bash
python -m pip install -r requirements-tools.txt
```

Distribucion recomendada:

| Archivo | Va aqui | No va aqui |
|---|---|---|
| `requirements.txt` | Dependencias necesarias para ejecutar la aplicacion. | Linters, Graphify, MarkItDown, herramientas de docs. |
| `requirements-dev.txt` | Tests, linters, type checkers, utilidades de desarrollo. | Dependencias runtime que produccion necesita. |
| `requirements-tools.txt` | Conversores, generadores, analizadores documentales. | Paquetes que la app importa en runtime. |
| Node/npm | OpenSpec CLI u otras herramientas JS. | Paquetes Python. |
| Instalacion manual | Obsidian, Codex, apps de escritorio. | Dependencias versionables de la app. |

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

Guia operativa del framework: `docs/openspec.md`.

## Graphify

Graphify es opcional y derivado. Sirve para generar `graphify-out/` y ayudar a navegar proyectos grandes o ambiguos.

Uso esperado cuando este disponible:

```bash
graphify update .
```

Si Graphify no esta instalado, el proyecto sigue siendo usable. Solo pierdes el mapa derivado; no pierdes autoridad documental. Nunca poner Graphify como requisito runtime de una aplicacion salvo que la aplicacion realmente lo ejecute.

Despues de generar salida, leer `graphify-out/GRAPH_REPORT.md` como mapa, no como fuente de verdad.

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

Codex puede proponer specs, cambios, disenos y tareas, pero debe dejar claro cuando una decision requiere aprobacion humana.

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
