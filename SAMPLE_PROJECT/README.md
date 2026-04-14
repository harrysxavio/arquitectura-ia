# SAMPLE_PROJECT - Mesa Interna de Soporte Operativo

Este proyecto ejemplo muestra como se ve una instancia ya rellenada de `PROJECT_TEMPLATE/` con una mini app funcional.

Es una aplicacion pequena, ejecutable y pedagogica para aprender a usar la arquitectura con un caso realista: una mesa interna que recibe solicitudes operativas, las clasifica, prioriza, lista y cierra con persistencia JSON local.

No es una plantilla de produccion ni una base recomendada para sistemas productivos. El objetivo es validar el framework y Graphify sobre un proyecto simple con codigo, documentacion, memoria, decisiones y contexto derivado.

## Que es

`SAMPLE_PROJECT/` sirve para ver el framework en uso:

- documentos canonicos ya completados;
- una tarea activa realista;
- una decision corta y una ADR;
- memoria breve del proyecto;
- una spec funcional y un SDD tecnico;
- una adaptacion local de agentes;
- mini app CLI en Python estandar;
- tests basicos;
- persistencia runtime local en `data/requests.json`;
- outputs Graphify derivados dentro de `graphify-out/`.

## Que no es

No reemplaza `PROJECT_TEMPLATE/`, no compite con `PROJECT_BLUEPRINT/` y no agrega una autoridad nueva al framework.

La relacion correcta es:

| Carpeta | Rol |
|---|---|
| `THEORY/` | Explica fundamentos y principios. |
| `PROJECT_BLUEPRINT/` | Explica como debe verse un proyecto instanciado. |
| `PROJECT_TEMPLATE/` | Da el molde reusable y vacio. |
| `SAMPLE_PROJECT/` | Muestra ese molde ya instanciado y guiado. |
| `EXAMPLES/` | Guarda casos o escenarios sueltos. |

## Si no sabes por donde empezar

Haz esto:

1. Lee este `README.md`.
2. Abre `PROJECT_GUIDE.md` para entender que es el proyecto.
3. Abre `CONTEXT_INDEX.md` para saber donde vive cada fuente.
4. Abre `tasks/current/active_task.md` para ver la tarea activa.
5. Lee `docs/product/spec.md` solo si necesitas comportamiento funcional.
6. Lee `docs/architecture/sdd.md` solo si necesitas diseno tecnico.
7. Consulta `decisions/` y `memory/` cuando necesites contexto duradero.
8. Ejecuta `python app.py demo` para ver el flujo funcional.
9. Consulta `graphify-out/GRAPH_REPORT.md` solo para orientacion estructural cuando exista.

Primer paso concreto: imagina que quieres cambiar la regla de prioridad de solicitudes urgentes. Antes de editar codigo, carga `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `tasks/current/active_task.md` y `docs/product/spec.md`. Si el cambio afecta componentes o datos, agrega `docs/architecture/sdd.md`.

## Ejecutar la mini app

Desde `SAMPLE_PROJECT/`:

```bash
python -m unittest discover -s tests
python app.py demo
python app.py create --title "Acceso VPN" --description "Alta para equipo operaciones" --area "Operaciones" --type acceso
python app.py list
python app.py close --id <id> --note "Resuelto con alta manual"
```

`data/requests.json` guarda datos runtime del ejemplo. No es fuente canonica. Las reglas viven en `docs/product/spec.md`, el diseno en `docs/architecture/sdd.md`, las decisiones en `decisions/` y la memoria en `memory/`.

## Documentos minimos y estandar

Un proyecto puede empezar con pocos documentos y crecer despues.

| Nivel | Archivos | Uso |
|---|---|---|
| Minimo | `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `AGENTS.md`, `tasks/current/active_task.md`, `decisions/decision_log.md`, `memory/project_facts.md` | Base para operar sin perder identidad, contexto, tarea activa, decisiones y hechos. |
| Estandar | Todo lo anterior mas `implementation_plan.md`, `open_questions.md`, ADRs, `docs/product/spec.md`, `docs/architecture/sdd.md`, `memory/constraints.md`, `memory/known_issues.md`, `memory/patterns.md`, `memory/glossary.md`, `VALIDATION_GUIDE.md` y `graphify-out/` | Version completa alineada con `PROJECT_TEMPLATE/`. |

En este ejemplo se incluye la estructura estandar para que puedas ver como conversa todo. En un proyecto real no tienes que llenar todo desde el dia uno.

## Orden recomendado de lectura

1. `PROJECT_GUIDE.md`: identidad, alcance, stack y restricciones principales.
2. `CONTEXT_INDEX.md`: mapa para cargar solo el contexto necesario.
3. `tasks/current/active_task.md`: que se esta haciendo ahora.
4. `tasks/current/implementation_plan.md`: pasos si la tarea lo requiere.
5. `tasks/current/open_questions.md`: dudas que cambian alcance o bloquean.
6. `docs/product/spec.md`: comportamiento esperado por usuarios.
7. `docs/architecture/sdd.md`: diseno tecnico cuando hay impacto estructural.
8. `decisions/decision_log.md`: decisiones aprobadas en formato breve.
9. `decisions/adr/`: decisiones arquitectonicas con contexto.
10. `memory/`: hechos, restricciones, problemas, patrones y glosario.
11. `VALIDATION_GUIDE.md`: pruebas funcionales, documentales y comparativa Graphify.
12. `graphify-out/GRAPH_REPORT.md`: mapa derivado para orientacion.

## Que se llena primero

Al crear tu propio proyecto desde `PROJECT_TEMPLATE/`, llena primero:

1. `PROJECT_GUIDE.md`: que es el proyecto y que problema resuelve.
2. `CONTEXT_INDEX.md`: que documentos son fuente oficial.
3. `tasks/current/active_task.md`: la tarea activa principal.
4. `memory/project_facts.md`: hechos confirmados del proyecto.

Despues llena lo que la tarea realmente necesite:

- `docs/product/spec.md` si hay reglas de negocio o comportamiento de usuario.
- `docs/architecture/sdd.md` si hay diseno tecnico o contratos.
- `decisions/decision_log.md` para decisiones aprobadas.
- `decisions/adr/*.md` para decisiones con alternativas e impacto.
- `memory/constraints.md` si una decision limita el futuro.
- `memory/patterns.md` si aparece una forma aprobada de implementar.
- `memory/known_issues.md` si un problema conocido afecta tareas futuras.
- `memory/glossary.md` si hay terminos ambiguos.

## Primer ejercicio sugerido

Usa este ejercicio para practicar el flujo con una app pequena sin convertirla en producto:

1. Abre `tasks/current/active_task.md`.
2. Lee el objetivo de documentar el flujo de triage.
3. Consulta `docs/product/spec.md` para ver las reglas.
4. Consulta `decisions/decision_log.md` para entender por que el flujo vive en Markdown.
5. Ejecuta `python app.py demo`.
6. Propone una regla nueva: "solicitudes de seguridad siempre son prioridad alta".
7. Decide donde debe documentarse:
   - regla funcional: `docs/product/spec.md`;
   - impacto tecnico: `docs/architecture/sdd.md`;
   - decision duradera: `decisions/decision_log.md`;
   - restriccion futura: `memory/constraints.md`.

La idea es practicar leer menos, pero leer mejor.

## Como conversan los documentos

Ejemplo: llega una solicitud para agregar prioridad automatica por area.

1. `PROJECT_GUIDE.md` dice que el sistema solo cubre solicitudes internas de operaciones.
2. `CONTEXT_INDEX.md` indica que la verdad funcional vive en `docs/product/spec.md`.
3. `active_task.md` dice si el cambio entra en la tarea actual.
4. `spec.md` define la regla funcional de prioridad.
5. `sdd.md` explica si el calculo vive en `src/triage.py`, `src/service.py` u otro componente futuro.
6. `decision_log.md` registra la decision si cambia el criterio oficial.
7. `memory/patterns.md` conserva el patron para tareas posteriores.
8. `graphify-out/GRAPH_REPORT.md` puede orientar que archivos revisar, pero no decide por si mismo.

Este flujo mejora la eficiencia de contexto porque el agente no tiene que cargar todo el repo. Carga primero identidad, indice y tarea; despues escala segun la necesidad.

## Agentes en este ejemplo

`SAMPLE_PROJECT/AGENTS.md` es la adaptacion local del proyecto ejemplo. Sirve para decir como se aplican aqui los roles base.

`OPERACION/AGENTS/*.md` son los contratos globales del framework. Si hay conflicto, gana el contrato global salvo decision documentada.

Uso aplicado:

| Rol | Como se usa aqui |
|---|---|
| Manager | Clasifica la tarea, decide nivel de contexto y elige que documentos cargar. |
| Coder | Edita documentos o codigo minimo dentro del alcance definido. |
| Reviewer | Revisa que el cambio respete spec, SDD, decisiones y memoria. |
| Debugger | Investiga fallos o contradicciones entre documentacion, tarea y codigo. |

Para evitar cargar contexto de mas, empieza siempre por `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y `tasks/current/active_task.md`. Usa Graphify solo si la tarea es estructural, transversal o ambigua.

## Graphify

`graphify-out/` contiene contexto estructural derivado. Ayuda a navegar relaciones, detectar nodos importantes y orientar tareas amplias.

En este ejemplo, Graphify debe enfocarse operativamente en `SAMPLE_PROJECT/`, no en la raiz del framework. La capa `GRAPHIFY/` de la raiz sigue definiendo politica y contrato.

Graphify ayuda cuando:

- el cambio cruza varias carpetas;
- una persona nueva necesita orientacion rapida;
- se investiga impacto estructural;
- se revisa una refactorizacion amplia.

Graphify no ayuda tanto cuando:

- el cambio afecta un solo archivo claro;
- solo estas corrigiendo texto;
- ya sabes que documento canonico consultar.

Regla clave: Graphify no es fuente de verdad. Si Graphify contradice `PROJECT_GUIDE.md`, `spec.md`, `sdd.md`, `decision_log.md` o `memory/*`, gana la fuente canonica.

Uso basico esperado desde `SAMPLE_PROJECT/`:

```bash
graphify update .
```

Para mas detalle, consulta `GRAPHIFY/GRAPHIFY_POLICY.md` y `GRAPHIFY/OUTPUT_CONTRACT.md` en la raiz del framework.

## MarkItDown

MarkItDown ayuda a convertir insumos externos a Markdown: PDFs, DOCX, HTML u otros documentos que conviene traer al repo como texto legible.

Usalo cuando:

- recibes un documento externo que explica reglas del negocio;
- quieres convertir una minuta o especificacion a Markdown;
- necesitas que un agente lea mejor una fuente antes de resumirla en `spec.md`, `sdd.md`, `decisions/` o `memory/`.

No hace falta cuando:

- la informacion ya esta escrita en Markdown;
- el insumo externo no aporta a la tarea;
- el resultado quedaria como una copia sin revisar.

Instalacion basica:

```bash
pip install markitdown
```

Uso ilustrativo:

```bash
markitdown input.docx > docs/product/source-notes.md
```

Despues de convertir, revisa el Markdown y resume lo que sea canonico en el archivo correcto. El archivo convertido no se vuelve fuente oficial automaticamente.

## Markdown en la arquitectura

Markdown permite que el proyecto tenga memoria versionada cerca del trabajo. Es util porque:

- se revisa en pull requests;
- se puede citar en conversaciones con agentes;
- se mantiene junto al codigo;
- funciona bien para specs, decisiones, memoria y guias.

Mantener Markdown breve y factual suele ser mejor que crear documentos largos que nadie consulta.

## Que copiar, que adaptar y que es ilustrativo

| Tipo | Elementos |
|---|---|
| Puedes copiar | Estructura documental, orden de lectura, estilo de `active_task.md`, formato de decision/ADR, memoria breve y `CONTEXT_INDEX.md` como mapa. |
| Debes adaptar | Dominio, alcance, reglas de negocio, stack, restricciones, agentes locales, rutas del `CONTEXT_INDEX.md` y contenido de memoria. |
| Solo ilustrativo | Dominio, datos runtime de `data/requests.json` y la escala de la automatizacion. |

`src/`, `app.py`, `tests/` y `.env.example` no son parte obligatoria del nucleo del framework. Estan aqui para mostrar como una estructura documental puede convivir con una mini app funcional.

## Donde buscar mas documentacion

Desde la raiz del framework:

- `README.md`: mapa general.
- `PROJECT_BLUEPRINT/PROJECT_DOCUMENTS.md`: rol y autoridad de documentos.
- `PROJECT_BLUEPRINT/PROJECT_STRUCTURE_EXAMPLE.md`: estructura minima y estandar.
- `PROJECT_TEMPLATE/`: molde reusable.
- `OPERACION/CONTEXT_ROUTER.md`: que contexto cargar segun tarea.
- `OPERACION/AGENTS/*.md`: contratos globales de agentes.
- `GRAPHIFY/`: politica y contrato de outputs Graphify.
- `THEORY/`: fundamentos conceptuales.
