# Adopcion Practica del Framework en un Proyecto Real

Esta guia es para una persona que quiere usar esta arquitectura en su propio proyecto y necesita pasos concretos. No intenta explicar toda la teoria del framework. Para teoria usa `THEORY/`; para detalle de OpenSpec usa `docs/openspec.md`; para instalacion por herramienta usa `docs/stack.md`.

Aqui se asume que trabajas con:

- VS Code para abrir carpetas, editar Markdown y revisar cambios.
- Codex como agente para ayudarte a escribir, mapear, implementar o refactorizar.
- Git para guardar cambios y revisar diferencias.

La guia tiene solo dos escenarios:

1. crear un proyecto nuevo;
2. adaptar un proyecto existente.

Elige el escenario que corresponde a tu caso y siguelo de principio a fin. No empieces con refactors grandes: primero crea fuentes claras para que humanos y Codex sepan que es verdad, donde mirar y como validar.

## Antes de Empezar

### Que Debes Tener Instalado

Para cualquiera de los dos escenarios necesitas:

- Git.
- VS Code.
- Codex, si quieres trabajar con agente.
- El stack real de tu proyecto, por ejemplo Python, Node, Java, .NET u otro.

Para clonar este framework:

```bash
git clone <url-del-repo>
cd arquitectura-ia
code .
```

Si `code .` no funciona, abre VS Code manualmente y usa `File > Open Folder`.

### Herramientas Opcionales

No instales todo de una vez. Usa esta tabla para decidir:

| Herramienta | Cuando la necesitas | Comando o instalacion | Donde no va |
|---|---|---|---|
| OpenSpec CLI | Cuando quieres validar, listar o archivar cambios OpenSpec con comandos. | `npm install -g @fission-ai/openspec@latest` | No va en `requirements.txt`. Usa Node/npm. |
| Graphify | Cuando el repo es grande y no sabes que archivos tocar. | `graphify update .` | No es fuente de verdad. No debe ser runtime salvo que tu app lo use. |
| MarkItDown | Cuando necesitas convertir PDFs, DOCX u otros insumos a Markdown. | `python -m pip install "markitdown[all]"` | No va en runtime si solo es herramienta documental. |
| Obsidian | Cuando quieres notas personales o mapa visual. | Instalacion manual. | No reemplaza OpenSpec, arquitectura ni decisiones. |
| Codex | Cuando quieres ayuda de agente. | Entorno propio de Codex. | No va en `requirements.txt`. |

Si tu proyecto es Python, separa dependencias asi:

```text
requirements.txt         dependencias necesarias para ejecutar la aplicacion
requirements-dev.txt     tests, linters y herramientas de desarrollo
requirements-tools.txt   conversores, analizadores y herramientas documentales
```

Ejemplo para un proyecto Python:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

En macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## Escenario 1: Crear un Proyecto Nuevo

Usa este camino si vas a empezar desde cero o si puedes crear una base limpia sin arrastrar documentos antiguos.

Ejemplo que puedes replicar: quieres crear `solicitudes-internas`, una herramienta para que personas de una empresa creen solicitudes para operaciones.

Puedes cambiar estos nombres por los tuyos:

| En el ejemplo | Cambialo por |
|---|---|
| `solicitudes-internas` | nombre de tu proyecto |
| `requests` | capacidad principal de tu proyecto |
| Solicitudes internas | nombre humano de la capacidad |
| Python y CLI | stack real de tu proyecto |
| Operaciones | equipo o usuario real |

### 1. Crear la Carpeta del Proyecto

Abre una terminal y ejecuta:

```bash
mkdir solicitudes-internas
cd solicitudes-internas
git init
code .
```

Que debe pasar:

- VS Code abre una carpeta vacia.
- Git empieza a controlar cambios.
- Este sera tu proyecto real, no una copia completa del framework.

### 2. Copiar el Template

Desde el repo del framework, copia `PROJECT_TEMPLATE/` hacia tu proyecto.

En PowerShell:

```powershell
Copy-Item -Recurse PROJECT_TEMPLATE\* ..\solicitudes-internas\
```

En macOS/Linux:

```bash
cp -r PROJECT_TEMPLATE/* ../solicitudes-internas/
```

Ahora en VS Code deberias ver, como minimo:

```text
AGENTS.md
PROJECT_GUIDE.md
CONTEXT_INDEX.md
openspec/
docs/architecture/
decisions/
memory/
```

Si no ves esos archivos, revisa que copiaste el contenido de `PROJECT_TEMPLATE/`, no solo la carpeta vacia.

### 3. Completar `PROJECT_GUIDE.md`

Este archivo responde: que es el proyecto y que no es.

Ejemplo:

```text
Nombre del proyecto: Solicitudes internas
Usuarios principales: colaboradores de la empresa y equipo de operaciones
Problema que resuelve: registrar solicitudes internas y dar seguimiento a su estado
No intenta resolver: soporte a clientes externos ni mesa de ayuda completa
Stack inicial: Python, CLI, almacenamiento JSON local
Riesgos o limites: no guardar datos sensibles innecesarios
```

Hazlo tu mismo al inicio. Codex puede mejorar redaccion, pero tu debes definir el proposito y el alcance. Si eso lo inventa el agente, el proyecto nace torcido.

### 4. Completar `CONTEXT_INDEX.md`

Este archivo responde: donde debe mirar una persona o agente para cada tipo de pregunta.

Ejemplo:

```text
Comportamiento vigente: openspec/specs/requests/spec.md
Cambios activos: openspec/changes/
Arquitectura estable: docs/architecture/system.md
Decisiones: decisions/decision_log.md
Restricciones: memory/constraints.md
Patrones: memory/patterns.md
```

Piensalo como un mapa. Si Codex recibe una tarea, este archivo evita que lea todo el repo sin necesidad.

### 5. Completar `AGENTS.md`

Este archivo le dice a Codex como debe trabajar en tu proyecto.

Ejemplo simple:

```text
Antes de implementar, leer PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Si una tarea cambia comportamiento, revisar OpenSpec.
No inventar reglas de negocio.
No usar Graphify como fuente de verdad.
Pedir confirmacion antes de refactors amplios.
Ejecutar tests o explicar por que no se pudieron ejecutar.
```

No pongas aqui reglas funcionales del producto. Las reglas funcionales viven en OpenSpec.

### 6. Crear la Primera Spec Vigente

Una spec vigente describe lo que el sistema debe hacer. No describe codigo ni tareas.

Crea una carpeta para tu primera capacidad:

```text
openspec/specs/requests/spec.md
```

Ejemplo para solicitudes internas:

```markdown
# Solicitudes Internas

## Requirements

### Requirement: Crear solicitud
El sistema SHALL permitir crear una solicitud con titulo, descripcion, area solicitante y tipo.

#### Scenario: Solicitud valida
- WHEN una persona envia titulo, descripcion, area solicitante y tipo validos
- THEN el sistema registra la solicitud
- AND asigna un identificador unico
- AND deja la solicitud en estado inicial `nueva`

#### Scenario: Solicitud incompleta
- WHEN una persona intenta crear una solicitud sin titulo
- THEN el sistema rechaza la solicitud
- AND informa que dato falta
```

Como adaptarlo:

- cambia `Solicitudes Internas` por tu capacidad;
- cambia `Crear solicitud` por una accion real de tu sistema;
- cambia los datos obligatorios por los datos reales;
- agrega escenarios rechazados cuando haya errores importantes para usuarios.

### 7. Crear el Primer Cambio Activo

La spec vigente dice que ya esta aprobado. Un cambio activo dice que quieres modificar o agregar algo.

Ejemplo: agregar prioridad urgente.

Crea esta estructura:

```text
openspec/changes/add-urgent-priority/
|-- proposal.md
|-- tasks.md
`-- specs/
    `-- requests/
        `-- spec.md
```

Agrega `design.md` solo si el cambio toca arquitectura, base de datos, permisos, integraciones o contratos.

Ejemplo de `proposal.md`:

```markdown
# Agregar prioridad urgente

## Problema
Las solicitudes relacionadas con seguridad necesitan distinguirse de solicitudes normales.

## Alcance
- Agregar prioridad `urgente`.
- Permitir usarla en solicitudes de seguridad.

## Fuera de Alcance
- Cambiar todo el sistema de notificaciones.
- Cambiar roles o permisos.
```

Ejemplo de `tasks.md`:

```markdown
# Tasks

- [ ] Actualizar delta OpenSpec de `requests`
- [ ] Implementar prioridad urgente
- [ ] Agregar validacion
- [ ] Agregar prueba o validacion manual
```

### 8. Version Manual: Hacerlo Tu Mismo

Sigue este orden:

1. Completa `PROJECT_GUIDE.md`.
2. Completa `CONTEXT_INDEX.md`.
3. Completa `AGENTS.md` si usaras Codex.
4. Crea `openspec/specs/requests/spec.md`.
5. Crea `openspec/changes/add-urgent-priority/`.
6. Revisa el diff.
7. Implementa codigo solo despues de tener spec y cambio activo.

Comandos utiles:

```bash
git status
git diff
```

Si instalaste OpenSpec CLI:

```bash
openspec validate add-urgent-priority --strict
```

Si todavia no tienes codigo, valida leyendo: deberias poder explicar que hace el proyecto solo con `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y la spec.

### 9. Version con Codex: Pedir Ayuda sin Perder Control

Primero pide ayuda documental, no codigo.

Prompt para completar la base:

```text
Estoy creando un proyecto nuevo llamado solicitudes-internas.
Trabajo en VS Code con Codex.
Lee PROJECT_GUIDE.md, CONTEXT_INDEX.md y AGENTS.md.
Ayudame a revisar si la estructura inicial del framework esta bien aplicada.
No implementes codigo todavia.
Si falta informacion, haz preguntas concretas.
```

Prompt para mejorar la primera spec:

```text
Revisa openspec/specs/requests/spec.md.
Quiero que sea clara para una capacidad de solicitudes internas.
Mejora requirements y scenarios sin inventar reglas nuevas.
Mantiene la spec enfocada en comportamiento observable, no en arquitectura.
```

Prompt para crear el primer cambio:

```text
Necesito agregar prioridad urgente a solicitudes internas.
Crea openspec/changes/add-urgent-priority/ con proposal.md, tasks.md y delta de spec para requests.
Agrega design.md solo si justificas impacto tecnico.
No implementes codigo hasta que yo apruebe el proposal.
```

Prompt para implementar despues de aprobar:

```text
Ya revise y apruebo el cambio add-urgent-priority.
Implementa solo lo necesario para cumplir la spec y tasks.md.
Actualiza checkboxes completados.
Ejecuta la validacion disponible o explica por que no se puede ejecutar.
No cambies arquitectura fuera del alcance.
```

En un proyecto nuevo, no pidas "refactoriza todo". Todavia no hay suficiente historia. Pide cambios pequenos guiados por OpenSpec.

### 10. Validar que el Proyecto Nuevo Quedo Bien

Checklist:

- [ ] `PROJECT_GUIDE.md` explica nombre, usuarios, problema, no alcance y stack.
- [ ] `CONTEXT_INDEX.md` apunta a OpenSpec, arquitectura, decisiones y memoria.
- [ ] `AGENTS.md` indica como debe trabajar Codex.
- [ ] Existe `openspec/specs/requests/spec.md` o la capacidad que corresponda.
- [ ] Existe un primer cambio en `openspec/changes/<change-id>/`.
- [ ] `proposal.md` explica problema, alcance y fuera de alcance.
- [ ] `tasks.md` tiene pasos verificables.
- [ ] `design.md` existe solo si habia impacto tecnico real.
- [ ] `git diff` muestra cambios entendibles.
- [ ] Codex no implemento codigo antes de que aprobaras la spec o el cambio.

## Escenario 2: Adaptar un Proyecto Existente

Usa este camino si ya tienes codigo, README, reglas informales, tests, usuarios o una aplicacion funcionando.

Ejemplo que puedes replicar: ya tienes un proyecto `portal-solicitudes` con codigo en `src/`, tests en `tests/` y una base de datos SQLite. Quieres ordenarlo con OpenSpec-first sin romper lo que ya funciona.

Puedes cambiar estos nombres por los tuyos:

| En el ejemplo | Cambialo por |
|---|---|
| `portal-solicitudes` | nombre de tu proyecto existente |
| `src/` | carpeta real de codigo |
| `tests/` | carpeta real de pruebas |
| `requests` | capacidad principal que vas a documentar primero |
| SQLite | almacenamiento real de tu proyecto |

### 1. Abrir el Proyecto en VS Code

Desde la carpeta de tu proyecto existente:

```bash
code .
git status
```

Si `git status` muestra cambios sin guardar, no empieces todavia. Primero decide si esos cambios se guardan, se terminan o se separan. Adoptar el framework encima de cambios mezclados vuelve dificil saber que paso.

Crea una rama:

```bash
git checkout -b adopt-openspec-first
```

### 2. Mapear lo que ya Existe

Antes de copiar archivos, escribe respuestas simples. Puedes hacerlo en una nota temporal o directamente en `PROJECT_GUIDE.md` despues.

Preguntas:

```text
Que hace hoy el sistema?
Quienes lo usan?
Donde esta el codigo principal?
Donde estan los tests?
Donde estan los datos o configuraciones?
Que reglas solo viven en conversaciones?
Que partes del sistema no entiendo todavia?
```

Ejemplo:

```text
El sistema registra solicitudes internas.
Lo usan operaciones y soporte.
El codigo principal esta en src/.
Los tests estan en tests/.
Los datos se guardan en SQLite.
La prioridad de seguridad existe como regla informal.
No esta claro donde se valida el area solicitante.
```

### 3. Copiar el Template sin Pisar tu Proyecto

No copies encima de archivos importantes sin revisar. Si tu proyecto ya tiene docs, conserva lo que sirve y agrega la estructura del framework de forma controlada.

Piezas que normalmente necesitas:

```text
PROJECT_GUIDE.md
CONTEXT_INDEX.md
AGENTS.md
openspec/
docs/architecture/
decisions/
memory/
```

Desde el repo del framework, en PowerShell:

```powershell
Copy-Item PROJECT_TEMPLATE\PROJECT_GUIDE.md ..\portal-solicitudes\PROJECT_GUIDE.md
Copy-Item PROJECT_TEMPLATE\CONTEXT_INDEX.md ..\portal-solicitudes\CONTEXT_INDEX.md
Copy-Item PROJECT_TEMPLATE\AGENTS.md ..\portal-solicitudes\AGENTS.md
Copy-Item -Recurse PROJECT_TEMPLATE\openspec ..\portal-solicitudes\openspec
Copy-Item -Recurse PROJECT_TEMPLATE\docs\architecture ..\portal-solicitudes\docs\architecture
Copy-Item -Recurse PROJECT_TEMPLATE\decisions ..\portal-solicitudes\decisions
Copy-Item -Recurse PROJECT_TEMPLATE\memory ..\portal-solicitudes\memory
```

Si una carpeta ya existe, copia primero a una carpeta temporal y fusiona a mano en VS Code.

### 4. Completar `PROJECT_GUIDE.md` con la Realidad Actual

No escribas el proyecto ideal. Escribe lo que existe hoy.

Ejemplo:

```text
Nombre: Portal de solicitudes internas
Usuarios: colaboradores, operaciones y administradores
Problema: crear, consultar y cerrar solicitudes internas
Stack: Python, Flask, SQLite
No alcance actual: atencion a clientes externos
Riesgos: algunas solicitudes pueden contener informacion sensible
Estado actual: app funcionando con tests parciales
```

Esto ayuda a Codex a no proponer una arquitectura imaginaria.

### 5. Completar `CONTEXT_INDEX.md` con Rutas Reales

Ejemplo:

```text
Codigo principal: src/
Tests: tests/
Base de datos: SQLite
Comportamiento vigente: openspec/specs/requests/spec.md
Cambios activos: openspec/changes/
Arquitectura estable: docs/architecture/system.md
Decisiones: decisions/decision_log.md
Restricciones: memory/constraints.md
```

Si no sabes una ruta, escribe `por confirmar`. Es mejor reconocer un hueco que inventar una fuente falsa.

### 6. Crear Arquitectura Basica

Completa `docs/architecture/system.md` con una descripcion corta de como funciona hoy.

Ejemplo:

```text
La aplicacion Flask expone rutas para crear, consultar y cerrar solicitudes.
SQLite guarda solicitudes, estado, area solicitante y fecha de creacion.
El modulo src/requests.py contiene la logica principal.
Los tests de solicitudes viven en tests/test_requests.py.
```

No pongas aqui todas las reglas funcionales. Si una regla dice que debe hacer el sistema, va en OpenSpec.

### 7. Convertir Comportamiento Existente en Spec

Elige una capacidad real y pequena. En el ejemplo: `requests`.

Crea:

```text
openspec/specs/requests/spec.md
```

Ejemplo basado en comportamiento actual:

```markdown
# Solicitudes Internas

## Requirements

### Requirement: Crear solicitud
El sistema SHALL permitir crear una solicitud interna con titulo, descripcion y area.

#### Scenario: Solicitud valida
- WHEN una persona envia titulo, descripcion y area validos
- THEN el sistema registra la solicitud
- AND devuelve su identificador

#### Scenario: Solicitud sin titulo
- WHEN una persona intenta crear una solicitud sin titulo
- THEN el sistema rechaza la solicitud
```

Importante: no escribas deseos futuros como si ya estuvieran aprobados. Si quieres agregar algo nuevo, crea un cambio en `openspec/changes/*`.

### 8. Version Manual: Adaptarlo Tu Mismo

Sigue este orden:

1. Crea rama `adopt-openspec-first`.
2. Copia piezas del template sin pisar docs existentes.
3. Completa `PROJECT_GUIDE.md`.
4. Completa `CONTEXT_INDEX.md`.
5. Escribe arquitectura basica en `docs/architecture/system.md`.
6. Crea una spec vigente para una capacidad real.
7. Registra restricciones confirmadas en `memory/constraints.md`.
8. Registra decisiones durables en `decisions/decision_log.md` solo si existen.
9. Revisa `git diff`.
10. Ejecuta tests actuales.

Comandos utiles:

```bash
git status
git diff
```

Segun tu stack:

```bash
python -m unittest
```

O:

```bash
pytest
npm test
```

Usa el comando real de tu proyecto. Si no hay tests, documenta una validacion manual en `tasks.md`.

### 9. Version con Codex: Primero Mapear, Luego Cambiar

En un proyecto existente, Codex no debe empezar refactorizando. Primero debe mapear.

Prompt para mapa inicial:

```text
Estoy adaptando este proyecto existente a una arquitectura OpenSpec-first.
Trabajo en VS Code con Codex.
Lee AGENTS.md, PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Revisa la estructura del repo y dime:
1. que capacidades funcionales parecen existir,
2. que archivos implementan cada capacidad,
3. que tests o validaciones existen,
4. que reglas parecen no estar documentadas,
5. que preguntas quedan abiertas.
No modifiques archivos.
No refactorices.
```

Prompt para crear spec vigente:

```text
Con base en el mapa anterior, propone openspec/specs/requests/spec.md.
Debe describir comportamiento actual verificable.
No inventes reglas de negocio.
Si algo no esta claro, dejalo como pregunta abierta y no como requirement aprobado.
No implementes codigo.
```

Prompt para crear primer cambio:

```text
Necesito agregar prioridad urgente al proyecto existente.
Primero crea un cambio OpenSpec en openspec/changes/add-urgent-priority/.
Incluye proposal.md, delta de spec para requests y tasks.md.
Agrega design.md solo si hay impacto en datos, permisos, arquitectura o migracion.
No implementes codigo todavia.
Explica que archivos probablemente se tocarian.
```

### 10. Cuando Pedir Refactor a Codex

Pide refactor solo cuando ya tengas:

- `PROJECT_GUIDE.md` completado;
- `CONTEXT_INDEX.md` con rutas reales;
- `docs/architecture/system.md` con arquitectura basica;
- spec vigente de la capacidad;
- cambio activo con `proposal.md`, delta y `tasks.md`;
- forma de validar con tests o revision manual.

Prompt para refactor controlado:

```text
Ya existe spec vigente para requests y el cambio add-urgent-priority esta aprobado.
Refactoriza solo lo necesario para implementar ese cambio.
Respeta docs/architecture/system.md y memory/constraints.md.
No cambies comportamiento fuera de la spec.
No reorganices modulos salvo que tasks.md lo pida explicitamente.
Actualiza tasks.md y dime como validar.
Ejecuta los tests disponibles.
```

No pidas refactor si:

- el comportamiento vigente no esta escrito;
- Codex tendria que adivinar reglas desde codigo viejo;
- no sabes que tests ejecutar;
- hay cambios sin guardar mezclados;
- el alcance todavia esta en conversacion.

En esos casos, pide investigacion, mapa de impacto o borrador documental.

### 11. Validar que la Adaptacion Funciona

Checklist:

- [ ] La rama `adopt-openspec-first` existe o el trabajo esta aislado.
- [ ] `PROJECT_GUIDE.md` describe el proyecto real.
- [ ] `CONTEXT_INDEX.md` apunta a rutas reales.
- [ ] `AGENTS.md` le dice a Codex como trabajar.
- [ ] `docs/architecture/system.md` explica la arquitectura actual sin duplicar OpenSpec.
- [ ] Existe al menos una spec vigente en `openspec/specs/*/spec.md`.
- [ ] El primer cambio nuevo vive en `openspec/changes/<change-id>/`.
- [ ] Las decisiones importantes estan resumidas en `decisions/` si existen.
- [ ] `memory/` contiene restricciones o hechos confirmados, no backlog.
- [ ] Codex no hizo refactor antes de que aprobaras spec y cambio.
- [ ] `git diff` muestra cambios que puedes explicar.
- [ ] Las pruebas existentes pasan o hay una validacion manual documentada.

## Como Saber si Vas Bien

Vas bien si puedes responder estas preguntas sin abrir todo el repo:

```text
Que hace el proyecto?
Donde esta la regla funcional vigente?
Que cambio esta activo ahora?
Donde esta la arquitectura estable?
Que debe leer Codex antes de tocar codigo?
Como valido que el cambio funciona?
```

Si no puedes responder alguna, completa primero `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, OpenSpec o arquitectura. Esa es la gracia del framework: no avanzar por intuicion cuando falta una fuente clara.

## Regla Final

Para un proyecto nuevo: crea una base pequena, clara y validable antes de implementar mucho codigo.

Para un proyecto existente: documenta y separa fuentes de verdad antes de refactorizar.

En ambos casos, Codex ayuda mucho cuando le das contexto y limites. Sin `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y OpenSpec, el agente adivina. Con esas fuentes, colabora.
