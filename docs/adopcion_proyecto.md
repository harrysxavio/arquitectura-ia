# Adopcion Practica del Framework en un Proyecto Real

Esta guia es para una persona que parte de cero, trabaja en VS Code y quiere usar este framework en un proyecto real sin perderse entre documentos.

La idea central es simple: el repo del framework no es tu aplicacion. El framework se clona una vez para copiar o adaptar `PROJECT_TEMPLATE/`. Tu proyecto real vive en otra carpeta, con su codigo, sus documentos y sus cambios Git.

## Antes de Empezar

**Que debes tener instalado**

- Git, para clonar repositorios y revisar cambios.
- VS Code, para abrir carpetas y editar Markdown/codigo.
- El stack real de tu proyecto, por ejemplo Python, Node, Java, .NET u otro.
- Codex en VS Code solo si quieres usar la ruta con agente.

**Dos carpetas distintas**

Usa dos carpetas separadas:

```text
proyectos/
|-- arquitectura-ia/          repo del framework
`-- mi-proyecto-real/         tu aplicacion real
```

El repo `arquitectura-ia/` contiene la plantilla y las guias. No debes desarrollar tu producto dentro de ese repo, salvo que estes modificando el framework mismo.

Tu proyecto real es la carpeta donde vivira tu aplicacion. Ahi copias o adaptas la plantilla.

**Clonar el framework**

Desde una terminal:

```bash
cd proyectos
git clone https://github.com/harrysxavio/arquitectura-ia.git arquitectura-ia
```

Si usas otra ubicacion, no hay problema. Lo importante es recordar donde quedo la carpeta del framework.

Para revisar el framework en VS Code:

```bash
cd arquitectura-ia
code .
```

**Estructura oficial vigente que se copia al proyecto real**

La plantilla actual es esta:

```text
PROJECT_TEMPLATE/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- README.md
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
|-- memory/known_issues.md
`-- graphify-out/GRAPH_REPORT.md
```

No tienes que llenar todo el primer dia. El orden recomendado es:

1. `PROJECT_GUIDE.md`: que es el proyecto, para quien existe, que problema resuelve y que queda fuera.
2. `CONTEXT_INDEX.md`: donde esta cada fuente oficial.
3. `AGENTS.md`: como debe trabajar Codex dentro de tu proyecto.
4. `openspec/specs/<capability>/spec.md`: primera capacidad funcional vigente.
5. `docs/architecture/system.md`: como esta construido o como se construira la primera version.
6. `memory/constraints.md`, `memory/facts.md`, `memory/patterns.md`, `memory/glossary.md` y `memory/known_issues.md`: solo cuando haya informacion confirmada que valga recordar.

OpenSpec va antes de implementar o refactorizar porque define comportamiento observable: que debe hacer el sistema, que escenarios acepta y que casos rechaza. Sin OpenSpec, Codex tiende a inferir reglas desde codigo, README o conversaciones. Con OpenSpec, una persona y el agente revisan la misma fuente antes de cambiar codigo.

## Escenario 1: Crear un Proyecto Nuevo

Usa este escenario si todavia no tienes una aplicacion o si puedes empezar con una carpeta limpia.

Ejemplo: quieres crear `solicitudes-internas`, una herramienta para registrar solicitudes de operaciones.

### Como Implementar en Tu Proyecto de Forma Manual

1. Crea la carpeta del proyecto real.

```bash
cd proyectos
mkdir solicitudes-internas
cd solicitudes-internas
git init
code .
```

Ahora VS Code debe estar abierto en `solicitudes-internas/`. Esa carpeta es tu proyecto real.

2. Copia la plantilla desde el framework.

En PowerShell, desde la carpeta `proyectos/`:

```powershell
Copy-Item -Recurse .\arquitectura-ia\PROJECT_TEMPLATE\* .\solicitudes-internas\
```

En macOS/Linux:

```bash
cp -r ./arquitectura-ia/PROJECT_TEMPLATE/* ./solicitudes-internas/
```

3. Revisa que tu proyecto real tenga esta base.

```text
solicitudes-internas/
|-- AGENTS.md
|-- PROJECT_GUIDE.md
|-- CONTEXT_INDEX.md
|-- README.md
|-- openspec/
|-- docs/architecture/system.md
|-- decisions/
|-- memory/
`-- graphify-out/
```

Si esa estructura aparecio dentro de `arquitectura-ia/`, copiaste en el lugar equivocado. La plantilla debe quedar dentro del proyecto real.

4. Completa primero `PROJECT_GUIDE.md`.

Escribe respuestas simples:

```text
Nombre: Solicitudes internas
Usuario principal: equipo de operaciones
Problema que resuelve: registrar solicitudes internas y saber en que estado estan
Incluido: crear solicitudes, consultar estado, cerrar solicitudes
Fuera de alcance: atencion a clientes externos, facturacion, portal publico
Stack inicial: Python, CLI, almacenamiento JSON local
Restricciones: no guardar secretos ni datos sensibles innecesarios
```

No busques perfeccion. Este archivo debe dejar claro que es el proyecto y que no es.

5. Completa `CONTEXT_INDEX.md`.

Ejemplo inicial:

```text
Identidad y alcance: PROJECT_GUIDE.md
Reglas para agentes: AGENTS.md
Comportamiento vigente: openspec/specs/requests/spec.md
Cambios activos: openspec/changes/
Arquitectura estable: docs/architecture/system.md
Decisiones: decisions/decision_log.md
Restricciones: memory/constraints.md
Problemas conocidos: memory/known_issues.md
```

Este indice ayuda a que una persona o Codex sepan donde mirar sin abrir todo el repo.

6. Ajusta `AGENTS.md`.

Ejemplo:

```text
Antes de implementar, leer PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Si la tarea cambia comportamiento, revisar o crear OpenSpec.
No inventar reglas de negocio.
No usar graphify-out como fuente de verdad.
Ejecutar tests disponibles antes de cerrar un cambio, o explicar por que no se pudieron ejecutar.
```

7. Crea la primera spec vigente.

Renombra o reemplaza `openspec/specs/example-capability/spec.md` por una capacidad real. Para el ejemplo:

```text
openspec/specs/requests/spec.md
```

Contenido inicial:

```markdown
# Solicitudes Internas

Requisitos

Requisito: Crear solicitud
El sistema debe permitir crear una solicitud con titulo, descripcion, area solicitante y tipo.

#### Escenario: Solicitud valida
- Cuando una persona envia titulo, descripcion, area solicitante y tipo validos
- Entonces el sistema registra la solicitud
- Y asigna un identificador unico
- Y deja la solicitud en estado inicial `nueva`

#### Escenario: Solicitud incompleta
- Cuando una persona intenta crear una solicitud sin titulo
- Entonces el sistema rechaza la solicitud
- Y explica que dato falta
```

8. Escribe arquitectura minima en `docs/architecture/system.md`.

Si todavia no hay codigo, basta con una version honesta:

```text
La primera version sera una CLI en Python.
La logica de solicitudes vivira en src/.
Los datos se guardaran en un archivo JSON local.
Los tests viviran en tests/.
```

Si algo no esta decidido, escribe `por definir`. No inventes estructura tecnica para que el documento parezca completo.

9. Usa memoria solo cuando haya informacion confirmada.

- `memory/facts.md`: hechos estables, por ejemplo entornos, integraciones o datos confirmados.
- `memory/constraints.md`: limites que cambian decisiones, por ejemplo seguridad, costo o compliance.
- `memory/patterns.md`: formas de trabajo aprobadas que se repetiran.
- `memory/glossary.md`: terminos ambiguos del dominio.
- `memory/known_issues.md`: problemas vigentes con impacto y mitigacion.

10. Revisa el resultado.

```bash
git status
git diff
```

Cuando la base documental este clara, recien ahi implementa la primera version de codigo o crea un cambio en `openspec/changes/<change-id>/`.

### Como Implementar en Tu Proyecto con Apoyo de un Agente como Codex en VS Code

1. Abre el proyecto real en VS Code.

No abras solo el framework. Codex debe trabajar dentro de `solicitudes-internas/` o el nombre real de tu aplicacion.

2. Pidele primero que mapee, no que implemente.

Prompt:

```text
Estoy creando un proyecto nuevo desde cero.
Este repo abierto en VS Code es mi proyecto real, no el repo del framework.
Quiero adoptar la arquitectura OpenSpec-first del framework arquitectura-ia.
Primero revisa la estructura actual y dime si la plantilla esta bien copiada.
Lee PROJECT_GUIDE.md, CONTEXT_INDEX.md y AGENTS.md si existen.
No implementes codigo todavia.
No refactorices.
Si falta informacion, haz preguntas concretas.
```

3. Pidele completar contexto base.

Antes de este prompt, escribe tu idea de proyecto en palabras simples. Por ejemplo: nombre, usuarios, problema, stack deseado y que queda fuera.

Prompt:

```text
Ayudame a completar la base documental del proyecto.
Usa esta informacion:
- Nombre: Solicitudes internas
- Usuarios: equipo de operaciones
- Problema: registrar solicitudes internas y seguir su estado
- Incluido: crear, consultar y cerrar solicitudes
- Fuera de alcance: clientes externos y facturacion
- Stack deseado: Python, CLI, JSON local

Completa o ajusta PROJECT_GUIDE.md, CONTEXT_INDEX.md y AGENTS.md.
Mantiene la estructura oficial del template actual.
No inventes reglas funcionales detalladas.
No implementes codigo.
```

4. Pidele crear o mejorar OpenSpec.

Prompt:

```text
Ahora crea la primera especificacion vigente en openspec/specs/requests/spec.md.
Debe describir comportamiento observable para solicitudes internas.
Incluye requisitos y escenarios claros.
No describas clases, tablas ni arquitectura interna.
Si falta una regla de negocio, dejala como pregunta abierta y no como requisito aprobado.
```

5. Pidele completar arquitectura minima.

Prompt:

```text
Con base en PROJECT_GUIDE.md y la spec OpenSpec de requests, completa docs/architecture/system.md con una arquitectura inicial minima.
Debe explicar componentes, datos, integraciones y validacion.
No dupliques requisitos funcionales de OpenSpec.
Si algo no esta decidido, escribelo como por definir.
```

6. Recien despues pide implementacion.

Prompt:

```text
La base documental ya esta revisada.
Implementa solo la primera version necesaria para cumplir openspec/specs/requests/spec.md.
Respeta docs/architecture/system.md y memory/constraints.md.
No agregues funcionalidades fuera de la spec.
Actualiza tests o agrega validacion manual clara.
Ejecuta los tests disponibles o explica por que no se pueden ejecutar.
```

7. Para un cambio nuevo, usa `openspec/changes/`.

Prompt:

```text
Quiero agregar prioridad urgente a solicitudes.
Antes de tocar codigo, crea openspec/changes/add-urgent-priority/ con proposal.md, tasks.md y delta de spec para requests.
Agrega design.md solo si hay impacto tecnico en datos, arquitectura, contratos o seguridad.
No implementes hasta que yo apruebe el cambio.
```

## Escenario 2: Adaptar un Proyecto Existente

Usa este escenario si ya tienes codigo, README, tests, usuarios o una aplicacion funcionando. La meta no es reescribir todo: es poner fuentes claras alrededor de lo que ya existe.

Ejemplo: ya tienes `portal-solicitudes/` con codigo en `src/`, tests en `tests/` y una base SQLite.

### Como Implementar en Tu Proyecto de Forma Manual

1. Clona el framework si todavia no lo tienes.

```bash
cd proyectos
git clone https://github.com/harrysxavio/arquitectura-ia.git arquitectura-ia
```

2. Abre tu proyecto real.

```bash
cd proyectos/portal-solicitudes
code .
git status
```

Si hay cambios sin guardar, decide primero si los vas a guardar, terminar o separar. Adoptar la plantilla sobre cambios mezclados vuelve dificil revisar que cambio corresponde a que.

3. Crea una rama de adopcion.

```bash
git checkout -b adopt-openspec-first
```

4. Mapea lo que existe antes de copiar.

Escribe respuestas breves:

```text
Que hace hoy el sistema?
Quienes lo usan?
Donde esta el codigo principal?
Donde estan los tests?
Donde estan los datos o configuraciones?
Que reglas importantes solo viven en conversaciones o README?
Que partes no entiendo todavia?
```

Ejemplo:

```text
El sistema registra solicitudes internas.
Lo usan operaciones y soporte.
El codigo principal esta en src/.
Los tests estan en tests/.
Los datos se guardan en SQLite.
No esta claro donde se valida el area solicitante.
```

5. Copia la plantilla con cuidado.

Si tu proyecto no tiene esos archivos, puedes copiar la base:

```powershell
Copy-Item .\..\arquitectura-ia\PROJECT_TEMPLATE\PROJECT_GUIDE.md .\PROJECT_GUIDE.md
Copy-Item .\..\arquitectura-ia\PROJECT_TEMPLATE\CONTEXT_INDEX.md .\CONTEXT_INDEX.md
Copy-Item .\..\arquitectura-ia\PROJECT_TEMPLATE\AGENTS.md .\AGENTS.md
Copy-Item -Recurse .\..\arquitectura-ia\PROJECT_TEMPLATE\openspec .\openspec
Copy-Item -Recurse .\..\arquitectura-ia\PROJECT_TEMPLATE\docs .\docs
Copy-Item -Recurse .\..\arquitectura-ia\PROJECT_TEMPLATE\decisions .\decisions
Copy-Item -Recurse .\..\arquitectura-ia\PROJECT_TEMPLATE\memory .\memory
Copy-Item -Recurse .\..\arquitectura-ia\PROJECT_TEMPLATE\graphify-out .\graphify-out
```

Si ya existen `docs/`, `decisions/`, `memory/` u `openspec/`, no copies encima a ciegas. Copia la plantilla a una carpeta temporal y fusiona manualmente:

```powershell
Copy-Item -Recurse .\..\arquitectura-ia\PROJECT_TEMPLATE .\_framework_template
```

Luego mueve o adapta solo lo que falte.

6. Completa `PROJECT_GUIDE.md` con la realidad actual.

Ejemplo:

```text
Nombre: Portal de solicitudes internas
Usuarios: colaboradores, operaciones y administradores
Problema: crear, consultar y cerrar solicitudes internas
Stack: Python, Flask, SQLite
Incluido hoy: creacion, consulta y cierre
Fuera de alcance actual: atencion a clientes externos
Riesgos: algunas solicitudes pueden contener informacion sensible
Estado actual: app funcionando con tests parciales
```

No escribas el proyecto ideal. Escribe el proyecto real.

7. Completa `CONTEXT_INDEX.md` con rutas reales.

Ejemplo:

```text
Codigo principal: src/
Tests: tests/
Comportamiento vigente: openspec/specs/requests/spec.md
Cambios activos: openspec/changes/
Arquitectura estable: docs/architecture/system.md
Decisiones: decisions/decision_log.md
Restricciones: memory/constraints.md
Problemas conocidos: memory/known_issues.md
```

Si no sabes una ruta, escribe `por confirmar`.

8. Escribe arquitectura actual en `docs/architecture/system.md`.

Ejemplo:

```text
La aplicacion Flask expone rutas para crear, consultar y cerrar solicitudes.
SQLite guarda solicitudes, estado, area solicitante y fecha de creacion.
El modulo src/requests.py contiene la logica principal.
Los tests de solicitudes viven en tests/test_requests.py.
```

No pongas reglas funcionales completas aqui. Las reglas funcionales van en OpenSpec.

9. Convierte comportamiento existente en OpenSpec.

Elige una capacidad pequena que ya exista. Para el ejemplo:

```text
openspec/specs/requests/spec.md
```

Contenido inicial:

```markdown
# Solicitudes Internas

Requisitos

Requisito: Crear solicitud
El sistema debe permitir crear una solicitud interna con titulo, descripcion y area.

#### Escenario: Solicitud valida
- Cuando una persona envia titulo, descripcion y area validos
- Entonces el sistema registra la solicitud
- Y devuelve su identificador

#### Escenario: Solicitud sin titulo
- Cuando una persona intenta crear una solicitud sin titulo
- Entonces el sistema rechaza la solicitud
```

Documenta lo que el sistema hace hoy. Si quieres agregar algo nuevo, crea un cambio en `openspec/changes/<change-id>/`.

10. Registra memoria solo si aporta decision futura.

- Restricciones confirmadas en `memory/constraints.md`.
- Hechos estables en `memory/facts.md`.
- Patrones repetibles en `memory/patterns.md`.
- Terminos ambiguos en `memory/glossary.md`.
- Problemas vigentes en `memory/known_issues.md`.

11. Revisa y valida.

```bash
git status
git diff
```

Ejecuta el comando real de tu proyecto:

```bash
pytest
```

O:

```bash
npm test
```

Si no hay tests, deja escrita una validacion manual concreta en el cambio OpenSpec cuando empieces a modificar comportamiento.

### Como Implementar en Tu Proyecto con Apoyo de un Agente como Codex en VS Code

1. Abre tu proyecto real en VS Code.

Codex debe ver el codigo real, no solo el framework. Si tambien necesita consultar el framework, dile donde esta clonado.

2. Pidele mapear antes de editar.

Prompt:

```text
Estoy adaptando este proyecto existente a una arquitectura OpenSpec-first.
Este repo abierto en VS Code es mi proyecto real.
El framework esta clonado en ../arquitectura-ia.

Primero mapea el proyecto sin modificar archivos:
1. que capacidades funcionales parecen existir,
2. que archivos implementan cada capacidad,
3. que tests o validaciones existen,
4. que documentos actuales aportan valor,
5. que documentos duplican autoridad o confunden,
6. que preguntas quedan abiertas.

No refactorices.
No implementes.
No borres documentos sin justificar funcion y reemplazo.
```

3. Pidele completar contexto base.

Prompt:

```text
Con base en el mapa anterior, adopta la estructura oficial vigente del framework en este proyecto real.
Usa PROJECT_TEMPLATE del framework solo como plantilla.
Completa o ajusta PROJECT_GUIDE.md, CONTEXT_INDEX.md, AGENTS.md y docs/architecture/system.md.
Respeta documentos existentes que aporten valor.
No introduzcas rutas legacy.
No dupliques reglas funcionales fuera de OpenSpec.
No implementes codigo todavia.
```

4. Pidele crear OpenSpec desde comportamiento existente.

Prompt:

```text
Ahora crea o ajusta openspec/specs/requests/spec.md para describir comportamiento actual verificable.
Usa el codigo y tests existentes como evidencia, pero no inventes reglas de negocio.
Si una regla no esta clara, registrala como pregunta abierta y no como requisito aprobado.
Mantiene escenarios claros y observables.
No implementes codigo.
```

5. Pidele preparar un cambio antes del refactor.

Prompt:

```text
Necesito refactorizar/completar la funcionalidad de solicitudes sin cambiar alcance.
Antes de tocar codigo, crea un cambio OpenSpec en openspec/changes/refactor-requests-flow/.
Incluye proposal.md, tasks.md y delta de spec solo si el comportamiento visible cambiara.
Agrega design.md si el refactor toca arquitectura, datos, contratos, seguridad o integraciones.
Explica que archivos probablemente se tocarian y como se validaria.
No implementes hasta que yo apruebe el cambio.
```

6. Recien despues pide implementacion o refactor.

Prompt:

```text
Apruebo el cambio openspec/changes/refactor-requests-flow/.
Implementa solo lo necesario para cumplir proposal.md, design.md si existe, tasks.md y la spec relacionada.
Respeta PROJECT_GUIDE.md, CONTEXT_INDEX.md, docs/architecture/system.md y memory/constraints.md.
No cambies comportamiento fuera de OpenSpec.
No reorganices modulos si no esta justificado en el cambio.
Actualiza tasks.md al completar pasos.
Ejecuta los tests disponibles y reporta el resultado.
```

7. Pidele consolidar documentos despues del cambio.

Prompt:

```text
Revisa la adopcion despues del cambio.
Actualiza solo documentos que hayan quedado desalineados:
- CONTEXT_INDEX.md si cambiaron rutas oficiales,
- docs/architecture/system.md si cambio estructura tecnica,
- memory/constraints.md si aparecio un limite vigente,
- memory/known_issues.md si queda un problema confirmado.

No agregues historia cerrada.
No dupliques comportamiento de OpenSpec.
No toques documentos sin razon concreta.
```

El orden con Codex debe ser siempre: mapear, completar contexto base, escribir o revisar OpenSpec, y recien despues implementar o refactorizar. Ese orden protege tu proyecto de cambios grandes basados en suposiciones.
