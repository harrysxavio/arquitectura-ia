# Adopcion Practica del Framework en un Proyecto Real

Esta guia es un recorrido paso a paso para usar esta arquitectura en un proyecto propio. No explica la teoria del framework ni reemplaza `docs/openspec.md` o `docs/stack.md`; los aterriza en una secuencia practica.

Sirve para responder:

- que hacer primero;
- que instalar segun tu caso;
- que documentos llenar;
- que puede hacer un agente;
- cuando usar OpenSpec manualmente o con CLI;
- como validar que el proyecto quedo gobernado por fuentes claras.

## Resultado Esperado

Al terminar la adopcion, tu proyecto deberia tener:

- una guia del proyecto en `PROJECT_GUIDE.md`;
- un mapa de fuentes en `CONTEXT_INDEX.md`;
- reglas para agentes en `AGENTS.md`, si trabajaras con IA;
- comportamiento vigente en `openspec/specs/*/spec.md`;
- cambios activos separados en `openspec/changes/*`;
- arquitectura estable en `docs/architecture/system.md`;
- decisiones y memoria compactas solo cuando hagan falta;
- Graphify tratado como ayuda derivada, no como autoridad.

## Escenarios de Entrada

Esta guia tiene solo dos caminos. Elige uno y siguelo completo antes de pedir refactors grandes.

| Escenario | Cuando usarlo | Resultado minimo |
|---|---|---|
| Crear un proyecto nuevo | Todavia no tienes repo productivo o puedes iniciar desde una base limpia. | Proyecto creado con template, primera spec vigente y primer cambio OpenSpec. |
| Adaptar un proyecto existente | Ya tienes codigo, docs, reglas informales o usuarios reales. | Proyecto mapeado sin romperlo, fuentes de verdad creadas y primer cambio controlado. |

En ambos escenarios asumimos que trabajas con VS Code y Codex. VS Code sirve para abrir, editar y revisar el repo. Codex sirve para ayudarte a redactar, mapear, proponer cambios y eventualmente refactorizar, pero no reemplaza tu revision.

## Instalacion Paso a Paso

### Instalacion Minima

Para crear o adaptar un proyecto con esta arquitectura necesitas una base sencilla:

- Git, para versionar cambios.
- VS Code, para abrir carpetas, editar Markdown y revisar diffs.
- Codex, si quieres asistencia de agente.
- El stack real de tu proyecto, solo cuando necesites ejecutar codigo.

Para obtener este framework:

```bash
git clone <url-del-repo>
cd arquitectura-ia
```

Abre la carpeta en VS Code:

```bash
code .
```

Si `code .` no funciona, abre VS Code manualmente y usa `File > Open Folder`.

### Instalacion Recomendada Para un Proyecto Real

Ademas de Git, VS Code y Codex, instala solo lo necesario para tu proyecto. Si el proyecto es Python:

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

Separa dependencias:

```text
requirements.txt         runtime de la aplicacion
requirements-dev.txt     tests, linters, type checkers
requirements-tools.txt   conversores, analizadores y utilidades documentales
```

No pongas todo en `requirements.txt`. OpenSpec CLI usa Node/npm; Obsidian y Codex se instalan fuera del proyecto.

### Herramientas Opcionales

| Si quieres... | Instala | Comandos utiles | No hace falta |
|---|---|---|---|
| Usar OpenSpec CLI | Node.js 20.19+ y npm/pnpm/yarn/bun | `npm install -g @fission-ai/openspec@latest` | Python, salvo que tu proyecto lo use |
| Usar Graphify | Graphify segun tu entorno | `graphify update .` | Ponerlo como runtime si solo analiza docs/codigo |
| Usar MarkItDown | Python 3.10+ y paquete MarkItDown | `python -m pip install "markitdown[all]"` | Node/npm |
| Usar Obsidian | Aplicacion de escritorio | Sin comando del repo | Cambiar fuentes canonicas |
| Trabajar con Codex | Entorno Codex | Leer `AGENTS.md` antes de pedir cambios | Instalarlo en `requirements.txt` |

Para mas detalle por escenario, usa `docs/stack.md`.

## Escenario 1: Crear un Proyecto Nuevo

Usa este escenario si vas a empezar un proyecto desde cero o puedes crear una base limpia sin arrastrar documentos antiguos.

### 1. Crear la Carpeta del Proyecto

Desde una terminal:

```bash
mkdir mi-proyecto
cd mi-proyecto
git init
code .
```

En VS Code deberias ver una carpeta vacia. Esa carpeta sera tu proyecto real, no una copia completa de este framework.

### 2. Copiar el Template

Desde el repo del framework, copia el contenido de `PROJECT_TEMPLATE/` al proyecto nuevo.

En PowerShell:

```powershell
Copy-Item -Recurse PROJECT_TEMPLATE\* ..\mi-proyecto\
```

En macOS/Linux:

```bash
cp -r PROJECT_TEMPLATE/* ../mi-proyecto/
```

Despues abre `mi-proyecto` en VS Code. Deberias ver archivos como `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `AGENTS.md`, `openspec/`, `docs/architecture/`, `decisions/` y `memory/`.

### 3. Completar lo Minimo a Mano

Antes de pedirle a Codex que haga trabajo grande, completa tres archivos con informacion basica.

En `PROJECT_GUIDE.md`, escribe:

```text
Nombre del proyecto: Solicitudes internas
Usuarios: colaboradores de la empresa y equipo de operaciones
Problema: registrar y dar seguimiento a solicitudes internas
No alcance: mesa de ayuda para clientes externos
Stack inicial: Python, CLI, almacenamiento JSON local
```

En `CONTEXT_INDEX.md`, deja un mapa inicial:

```text
Comportamiento funcional: openspec/specs/requests/spec.md
Cambios activos: openspec/changes/
Arquitectura estable: docs/architecture/system.md
Decisiones: decisions/decision_log.md
Restricciones: memory/constraints.md
```

En `AGENTS.md`, indica como debe trabajar Codex:

```text
Antes de implementar, leer PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Si una tarea cambia comportamiento, revisar OpenSpec.
No inventar reglas de negocio.
No usar Graphify como fuente de verdad.
Pedir confirmacion antes de refactors amplios.
```

### 4. Crear la Primera Spec Vigente

Elige una capacidad pequeña. Para el ejemplo: solicitudes internas.

Crea o reemplaza:

```text
openspec/specs/requests/spec.md
```

Ejemplo inicial:

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
```

Esta spec no explica codigo. Explica comportamiento observable: que debe poder hacer el sistema.

### 5. Crear el Primer Cambio Activo

Ahora crea una mejora concreta. Por ejemplo: agregar prioridad urgente.

Estructura:

```text
openspec/changes/add-urgent-priority/
|-- proposal.md
|-- tasks.md
`-- specs/
    `-- requests/
        `-- spec.md
```

Agrega `design.md` solo si el cambio toca arquitectura, datos, integraciones o seguridad.

Contenido minimo de `proposal.md`:

```markdown
# Agregar prioridad urgente

## Problema
Las solicitudes de seguridad necesitan distinguirse de solicitudes normales.

## Alcance
- Agregar prioridad `urgente`.
- Permitir usarla en solicitudes de seguridad.

## Fuera de Alcance
- Cambiar todo el sistema de notificaciones.
- Cambiar roles o permisos.
```

Contenido minimo de `tasks.md`:

```markdown
# Tasks

- [ ] Actualizar delta OpenSpec de `requests`
- [ ] Implementar prioridad urgente
- [ ] Agregar validacion
- [ ] Agregar prueba o validacion manual
```

### 6. Version Manual

Si lo haces sin agente:

1. Completa los documentos en VS Code.
2. Revisa el diff de Git.
3. Confirma que cada regla funcional esta en OpenSpec.
4. Implementa codigo solo despues de tener `proposal.md`, delta de spec y `tasks.md`.
5. Ejecuta las pruebas del stack de tu proyecto.

Comandos utiles:

```bash
git status
git diff
```

Si usas OpenSpec CLI:

```bash
openspec validate add-urgent-priority --strict
```

### 7. Version con Codex

Usa Codex para acelerar, pero dale una tarea acotada.

Prompt recomendado para crear la base:

```text
Estoy creando un proyecto nuevo con este framework OpenSpec-first.
Asume que trabajo en VS Code.
Lee PROJECT_GUIDE.md, CONTEXT_INDEX.md y AGENTS.md.
Ayudame a completar la primera spec vigente para la capacidad `requests`.
No implementes codigo todavia.
No inventes reglas: si falta informacion, deja preguntas abiertas.
```

Prompt recomendado para el primer cambio:

```text
Necesito agregar prioridad urgente a solicitudes internas.
Crea o ajusta openspec/changes/add-urgent-priority/ con proposal.md,
tasks.md y delta de spec para requests.
Agrega design.md solo si explicas por que hace falta.
No implementes codigo hasta que yo apruebe el proposal.
```

Prompt recomendado para implementar despues de revisar:

```text
Ya revise y apruebo el cambio add-urgent-priority.
Implementa solo lo necesario para cumplir la spec y tasks.md.
Actualiza checkboxes completados.
Ejecuta o indica la validacion disponible.
No cambies arquitectura fuera del alcance.
```

### 8. Como Validar que Funciona

Valida en VS Code y terminal:

- `PROJECT_GUIDE.md` explica el proyecto sin depender de conversaciones.
- `CONTEXT_INDEX.md` dice donde esta cada fuente.
- `AGENTS.md` le dice a Codex como trabajar.
- Existe `openspec/specs/requests/spec.md`.
- Existe `openspec/changes/add-urgent-priority/`.
- El cambio tiene `proposal.md`, delta de spec y `tasks.md`.
- `design.md` solo existe si habia impacto tecnico real.
- `git diff` muestra cambios entendibles.
- Las pruebas del proyecto pasan, si ya hay codigo.

## Escenario 2: Adaptar un Proyecto Existente

Usa este escenario si ya tienes codigo, README, docs sueltas, reglas en conversaciones o una app que ya usan personas reales.

La regla principal: primero ordenar y documentar lo que existe; despues refactorizar.

### 1. Abrir el Proyecto en VS Code

En la carpeta del proyecto existente:

```bash
code .
git status
```

Si hay cambios sin guardar, no empieces la adopcion todavia. Primero confirma, guarda o separa esos cambios para no mezclar trabajo.

Crea una rama:

```bash
git checkout -b adopt-openspec-first
```

### 2. Hacer un Mapa Inicial

Antes de copiar archivos, responde en notas simples:

```text
Que hace hoy el sistema?
Quienes lo usan?
Donde esta el codigo principal?
Hay tests?
Hay README o docs actuales?
Que reglas conoce la persona pero no estan escritas?
Que partes no entiendo todavia?
```

Ejemplo:

```text
El sistema registra solicitudes internas.
Lo usan operaciones y soporte.
El codigo principal esta en src/.
Los datos se guardan en data/requests.json.
Hay tests en tests/.
La prioridad de seguridad existe como regla informal, no como codigo claro.
```

### 3. Copiar el Template sin Pisar el Proyecto

No reemplaces todo automaticamente. Copia solo las piezas que falten:

- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `AGENTS.md`
- `openspec/`
- `docs/architecture/`
- `decisions/`
- `memory/`

En PowerShell, desde el repo del framework hacia el proyecto:

```powershell
Copy-Item -Recurse PROJECT_TEMPLATE\openspec ..\mi-proyecto\openspec
Copy-Item PROJECT_TEMPLATE\PROJECT_GUIDE.md ..\mi-proyecto\PROJECT_GUIDE.md
Copy-Item PROJECT_TEMPLATE\CONTEXT_INDEX.md ..\mi-proyecto\CONTEXT_INDEX.md
Copy-Item PROJECT_TEMPLATE\AGENTS.md ..\mi-proyecto\AGENTS.md
```

Si el proyecto ya tiene carpetas parecidas, copia a una carpeta temporal y fusiona a mano.

### 4. Completar Fuentes Minimas

En `PROJECT_GUIDE.md`, describe el proyecto real, no el ideal:

```text
Nombre: Portal de solicitudes internas
Usuarios: empleados, operaciones, administradores
Problema: registrar, consultar y cerrar solicitudes internas
Stack: Python, Flask, SQLite
No alcance actual: atencion a clientes externos
Riesgos: datos internos y permisos por area
```

En `CONTEXT_INDEX.md`, apunta a fuentes reales:

```text
Codigo principal: src/
Tests: tests/
Datos: app.db
Comportamiento vigente: openspec/specs/requests/spec.md
Arquitectura estable: docs/architecture/system.md
Decisiones: decisions/decision_log.md
Restricciones: memory/constraints.md
```

En `docs/architecture/system.md`, resume como funciona hoy:

```text
La aplicacion Flask expone rutas para crear y consultar solicitudes.
SQLite guarda solicitudes y estados.
El modulo src/requests.py contiene la logica principal.
Los tests de requests viven en tests/test_requests.py.
```

### 5. Convertir Comportamiento Existente en Spec

No escribas deseos futuros. Escribe primero lo que el sistema ya hace o deberia hacer segun usuarios.

Crear:

```text
openspec/specs/requests/spec.md
```

Ejemplo:

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

Si no estas seguro de una regla, no la inventes. Agregala como pregunta abierta en el cambio o en una nota temporal, no como spec aprobada.

### 6. Pedir Ayuda a Codex para Mapear, no Refactorizar

Primer prompt recomendado:

```text
Estoy adaptando este proyecto existente a una arquitectura OpenSpec-first.
Trabajo en VS Code con Codex.
Lee AGENTS.md, PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Revisa la estructura del repo y dime:
1. que capacidades funcionales parecen existir,
2. que archivos implementan cada capacidad,
3. que tests o validaciones existen,
4. que preguntas quedan abiertas.
No modifiques codigo ni refactorices.
```

Segundo prompt recomendado:

```text
Con base en el mapa anterior, propone una spec vigente para la capacidad `requests`.
Debe describir comportamiento actual verificable.
No inventes reglas de negocio.
Si algo no esta claro, dejalo como pregunta abierta.
```

### 7. Crear el Primer Cambio Controlado

Cuando ya entiendes lo existente, crea un cambio pequeño. Ejemplo: agregar prioridad urgente.

```text
openspec/changes/add-urgent-priority/
|-- proposal.md
|-- design.md
|-- tasks.md
`-- specs/
    `-- requests/
        `-- spec.md
```

En un proyecto existente, `design.md` suele ser util si el cambio toca base de datos, permisos, integraciones o migraciones. Si solo agrega una validacion simple, puede no hacer falta.

Prompt recomendado:

```text
Necesito agregar prioridad urgente al proyecto existente.
Primero crea un cambio OpenSpec en openspec/changes/add-urgent-priority/.
Incluye proposal.md, delta de spec para requests y tasks.md.
Agrega design.md solo si hay impacto en datos, permisos o arquitectura.
No implementes codigo todavia.
Explica que archivos probablemente se tocarian.
```

### 8. Cuando Si Pedir Refactor al Agente

Pide refactor solo cuando ya tengas:

- `PROJECT_GUIDE.md` completado;
- `CONTEXT_INDEX.md` con fuentes reales;
- spec vigente de la capacidad;
- cambio activo con `proposal.md`, delta y `tasks.md`;
- arquitectura basica en `docs/architecture/system.md`;
- forma de validar con tests o revision manual.

Prompt recomendado:

```text
Ya existe spec vigente para requests y el cambio add-urgent-priority esta aprobado.
Refactoriza solo lo necesario para implementar ese cambio.
Respeta docs/architecture/system.md y memory/constraints.md.
No cambies comportamiento fuera de la spec.
Actualiza tasks.md y dime como validar.
```

No pidas refactor si el agente aun tendria que adivinar reglas desde codigo viejo, conversaciones o README ambiguos.

### 9. Como Validar que la Adaptacion Funciona

Valida antes y despues de Codex:

```bash
git status
git diff
```

Si hay tests:

```bash
python -m unittest
```

O usa el comando real de tu proyecto, por ejemplo `npm test`, `pytest` o el script que corresponda.

Checklist especifica para proyecto existente:

- El codigo viejo no fue reorganizado antes de crear fuentes de verdad.
- `PROJECT_GUIDE.md` describe el proyecto real.
- `CONTEXT_INDEX.md` apunta a archivos reales.
- OpenSpec describe comportamiento vigente, no deseos.
- El primer cambio esta separado en `openspec/changes/*`.
- `docs/architecture/system.md` explica la estructura actual.
- Las decisiones anteriores importantes estan resumidas.
- Codex no implemento refactor antes de aprobar alcance.
- Las pruebas o validaciones siguen pasando.

## Que Llena la Persona y Que Llena el Agente

| Elemento | Persona | Agente | Revision humana necesaria |
|---|---|---|---|
| Problema y objetivo | Define necesidad real, prioridad y limites. | Puede reformular y detectar ambiguedades. | Siempre. |
| `PROJECT_GUIDE.md` | Completa identidad, usuarios, alcance y stack. | Puede ordenar o mejorar redaccion. | Siempre. |
| `CONTEXT_INDEX.md` | Confirma fuentes oficiales. | Puede mapear archivos y proponer rutas. | Si. |
| `AGENTS.md` | Decide reglas, permisos y limites. | Puede proponer instrucciones operativas. | Siempre. |
| Spec vigente | Aprueba comportamiento actual. | Puede redactar requirements y scenarios. | Siempre. |
| `proposal.md` | Define alcance y no alcance. | Puede convertir una necesidad en borrador. | Siempre. |
| `design.md` | Decide alternativas y riesgos aceptables. | Puede proponer diseno tecnico. | Si hay impacto tecnico. |
| `tasks.md` | Revisa que el trabajo sea correcto. | Puede descomponer, ejecutar y actualizar checkboxes. | Si. |
| Decisiones | Aprueba direccion durable. | Puede redactar ADR o resumen. | Siempre. |
| Memoria | Confirma hechos y restricciones. | Puede compactar informacion. | Si. |
| Refactor | Define objetivo y limites. | Puede implementar una vez que existan fuentes claras. | Siempre antes de mergear. |

Pide ayuda al agente con instrucciones concretas:

```text
Lee AGENTS.md, PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Quiero adoptar OpenSpec-first para la capacidad de solicitudes internas.
Primero propone una spec vigente, no implementes codigo todavia.
Marca preguntas abiertas y no inventes reglas de negocio.
```

Para un cambio:

```text
Convierte esta necesidad en un cambio OpenSpec:
"Necesitamos prioridad urgente para solicitudes de seguridad".
Crea propuesta de proposal.md, delta de spec y tasks.md.
Agrega design.md solo si detectas impacto tecnico.
No implementes hasta que revise el alcance.
```

Todavia no pidas refactor si:

- no existe spec vigente;
- el alcance esta en conversacion;
- no sabes que archivos son autoridad;
- el agente tendria que inferir reglas desde codigo desordenado;
- no hay forma de validar el resultado.

En ese caso, pide investigacion, mapa de impacto o borrador documental.

## OpenSpec en la Practica

Usa OpenSpec manualmente cuando:

- estas empezando;
- no quieres instalar CLI;
- el equipo revisa Markdown en Git;
- el cambio es pequeno;
- necesitas claridad antes que automatizacion.

Usa OpenSpec CLI cuando:

- quieres validar formato;
- quieres listar cambios activos;
- quieres archivar cambios completados;
- quieres usar integraciones oficiales.

Comandos habituales:

```bash
npm install -g @fission-ai/openspec@latest
openspec list
openspec show <change-id>
openspec validate <change-id> --strict
openspec archive <change-id> --yes
```

Archivos obligatorios para un cambio real:

- `proposal.md`;
- delta bajo `openspec/changes/<change-id>/specs/<capability>/spec.md`;
- `tasks.md`.

Archivo condicional:

- `design.md`, solo si hay impacto tecnico relevante.

Como pasar de necesidad a OpenSpec:

1. Persona dice: "necesitamos exportar solicitudes filtradas a CSV".
2. Agente propone `proposal.md` con alcance y no alcance.
3. Agente propone delta de spec con requirement y scenarios.
4. Persona revisa si el comportamiento es correcto.
5. Agente crea `tasks.md`.
6. Se implementa solo despues de aprobar el marco.

Como pasar de regla vigente a spec:

1. Persona o agente identifica una regla que ya existe en el sistema.
2. Se confirma contra codigo, usuarios o documentacion vigente.
3. Se escribe en `openspec/specs/<capability>/spec.md`.
4. La persona aprueba que representa el comportamiento actual.
5. Cambios futuros ya se hacen mediante `openspec/changes/*`.

La persona usa OpenSpec para decidir y aprobar comportamiento. El agente usa OpenSpec para orientarse, redactar deltas, implementar tareas y verificar que no cambio el alcance.

Guia especifica: `docs/openspec.md`.

## Como Usar Agentes en Este Framework

Flujo real para pedir trabajo a un agente:

1. El agente lee `AGENTS.md` para conocer reglas locales, permisos y validacion.
2. El agente lee `PROJECT_GUIDE.md` para entender que es el proyecto y que no debe intentar resolver.
3. El agente usa `CONTEXT_INDEX.md` para saber que fuentes abrir, en vez de leer todo.
4. Si la tarea toca comportamiento, consulta `openspec/specs/*` o `openspec/changes/*`.
5. Si la tarea toca estructura tecnica, consulta `docs/architecture/system.md`.
6. Si hay decisiones previas, consulta `decisions/decision_log.md` y ADRs.
7. Si hay restricciones, patrones o terminos de dominio, consulta `memory/`.
8. Si el impacto es amplio o no se sabe donde mirar, usa Graphify como mapa derivado.
9. El agente propone o ejecuta cambios.
10. La persona revisa alcance, riesgos y resultado.

Graphify ayuda cuando:

- el repo es grande;
- hay muchas carpetas;
- no sabes que archivos implementan una capacidad;
- quieres estimar impacto antes de tocar codigo.

Graphify no ayuda a decidir:

- comportamiento funcional;
- reglas de negocio;
- decisiones de arquitectura;
- excepciones de seguridad.

El agente debe tratar Graphify como brujula, no como juez.

## Checklist de Validacion

Usa esta lista para saber si la adopcion quedo suficientemente bien:

- [ ] `PROJECT_GUIDE.md` explica identidad, usuarios, alcance y stack.
- [ ] `CONTEXT_INDEX.md` dice donde estan las fuentes oficiales.
- [ ] `AGENTS.md` existe si se trabajara con agentes.
- [ ] Hay al menos una verdad funcional clara en `openspec/specs/*/spec.md`.
- [ ] El cambio activo esta separado en `openspec/changes/<change-id>/`.
- [ ] `proposal.md` tiene problema, alcance y no alcance.
- [ ] El delta OpenSpec describe el comportamiento que cambia.
- [ ] `design.md` existe si hay impacto en arquitectura, datos o contratos.
- [ ] `tasks.md` permite validar trabajo terminado.
- [ ] `docs/architecture/system.md` explica estructura estable sin reemplazar OpenSpec.
- [ ] `decisions/decision_log.md` resume decisiones durables, si existen.
- [ ] `memory/` contiene hechos compactos, no backlog ni diario.
- [ ] Graphify, si existe, esta tratado como salida derivada.
- [ ] Un agente puede saber que leer primero sin abrir todo el repo.
- [ ] No hay secretos, tokens ni datos sensibles en Markdown.

Si varios puntos fallan, no pidas un refactor grande todavia. Primero completa fuentes de verdad minimas.

## Ejemplos Practicos

### Ejemplo 1: Crear Proyecto Nuevo de Solicitudes Internas

Situacion: quieres crear una herramienta interna para que colaboradores pidan ayuda a operaciones.

Hazlo tu primero:

1. Crea repo y abre VS Code:

```bash
mkdir solicitudes-internas
cd solicitudes-internas
git init
code .
```

2. Copia `PROJECT_TEMPLATE/`.
3. Llena `PROJECT_GUIDE.md`:

```text
Nombre: Solicitudes internas
Usuarios: colaboradores y equipo de operaciones
Problema: registrar solicitudes y ver su estado
No alcance: soporte a clientes externos
Stack inicial: Python y CLI
```

4. Llena `CONTEXT_INDEX.md`:

```text
Spec principal: openspec/specs/requests/spec.md
Cambios activos: openspec/changes/
Arquitectura: docs/architecture/system.md
Restricciones: memory/constraints.md
```

5. Crea `openspec/specs/requests/spec.md` con el comportamiento minimo de crear solicitud.

Luego pide a Codex:

```text
Estoy creando desde cero un proyecto de solicitudes internas.
Lee PROJECT_GUIDE.md, CONTEXT_INDEX.md y AGENTS.md.
Revisa la spec inicial de requests.
Mejora la redaccion de requirements y scenarios sin agregar reglas nuevas.
Despues propone un primer cambio OpenSpec para agregar prioridad urgente.
No implementes codigo todavia.
```

Valida:

- puedes explicar que hace el proyecto leyendo `PROJECT_GUIDE.md`;
- Codex sabe donde mirar leyendo `CONTEXT_INDEX.md`;
- la primera regla funcional vive en `openspec/specs/requests/spec.md`;
- el primer cambio vive en `openspec/changes/add-urgent-priority/`;
- no hay reglas funcionales escondidas solo en README o memoria.

### Ejemplo 2: Adaptar Proyecto Existente de Solicitudes Internas

Situacion: ya tienes una app que registra solicitudes internas. Hay codigo en `src/`, datos en SQLite y algunas reglas solo estan en conversaciones.

Hazlo tu primero:

1. Abre el proyecto en VS Code:

```bash
code .
git status
git checkout -b adopt-openspec-first
```

2. Copia las piezas del template que faltan.
3. Llena `PROJECT_GUIDE.md` con lo real:

```text
Nombre: Portal de solicitudes internas
Usuarios: colaboradores, operaciones y administradores
Problema: crear, consultar y cerrar solicitudes internas
Stack: Python, Flask, SQLite
Riesgo: algunas solicitudes tienen informacion sensible
```

4. Llena `CONTEXT_INDEX.md`:

```text
Codigo principal: src/
Tests: tests/
Base de datos: SQLite
Spec vigente: openspec/specs/requests/spec.md
Arquitectura: docs/architecture/system.md
```

5. Escribe una spec vigente basada en comportamiento actual, no en deseos futuros.

Pide a Codex primero investigacion, no refactor:

```text
Estoy adaptando un proyecto existente a OpenSpec-first.
Lee AGENTS.md, PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Mapea la capacidad de solicitudes internas:
1. archivos principales,
2. reglas funcionales visibles,
3. tests existentes,
4. preguntas abiertas.
No modifiques codigo.
No refactorices.
```

Despues pide la spec:

```text
Con base en el mapa, propone openspec/specs/requests/spec.md.
Debe representar comportamiento vigente.
No inventes reglas.
Marca como pregunta abierta cualquier comportamiento que no puedas confirmar.
```

Solo despues pide refactor:

```text
Ya revise la spec vigente de requests.
Crea un cambio OpenSpec para agregar prioridad urgente.
Cuando yo apruebe proposal.md y tasks.md, implementa solo ese cambio.
No reorganices modulos ni cambies comportamiento no pedido.
```

Valida:

- `git diff` no muestra refactors antes de tener spec y cambio activo;
- `openspec/specs/requests/spec.md` describe comportamiento actual;
- `openspec/changes/add-urgent-priority/` separa la mejora nueva;
- `docs/architecture/system.md` explica como funciona hoy la app;
- las pruebas existentes siguen pasando;
- Codex puede justificar que leyo las fuentes correctas.

## Regla Final

Adoptar el framework no significa escribir muchos documentos. Significa crear el minimo conjunto de fuentes claras para que el siguiente cambio sea entendible, revisable y seguro para humanos y agentes.
