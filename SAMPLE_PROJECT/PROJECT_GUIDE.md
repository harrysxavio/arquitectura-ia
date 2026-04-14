# PROJECT_GUIDE.md

> Ejemplo rellenado. En un proyecto real, este archivo se vuelve canonico dentro del proyecto activo.

## Proposito

Describir la identidad, alcance, estructura, stack y restricciones principales de la Mesa Interna de Soporte Operativo como mini app funcional y pedagogica del framework.

## Identidad

- Nombre: Mesa Interna de Soporte Operativo.
- Usuario principal: coordinadores de operaciones y equipos internos que solicitan apoyo.
- Problema que resuelve: centralizar solicitudes internas, clasificarlas por prioridad y dejar trazabilidad de decisiones operativas.

## Alcance

- Incluido:
  - registro manual de solicitudes internas;
  - clasificacion por tipo, area solicitante y prioridad;
  - flujo basico de triage, asignacion y cierre;
  - documentacion de reglas y decisiones en Markdown;
  - automatizacion minima por CLI para crear, listar y cerrar solicitudes;
  - persistencia runtime local en JSON para probar el flujo.
- Fuera de alcance:
  - autenticacion real;
  - integracion con mesa de ayuda externa;
  - base de datos productiva;
  - notificaciones automaticas;
  - interfaz web completa;
  - plantilla de produccion para nuevos sistemas.

## Estructura

- `README.md`: guia de onboarding para entender el ejemplo.
- `CONTEXT_INDEX.md`: mapa de fuentes oficiales del proyecto.
- `AGENTS.md`: ajustes locales para roles de agente.
- `VALIDATION_GUIDE.md`: guia para validar app, docs y Graphify.
- `ARCHITECTURE_VALIDATION.md`: prueba de arquitectura total como sistema.
- `CHAT_SCENARIOS.md`: prompts y trazas para evaluar rutas de contexto.
- `TEST_EXECUTION_REPORT.md`: evidencia de comandos ejecutados y resultados.
- `TRACE_LOG.md`: trazas observadas de escenarios de chat y Graphify.
- `app.py`: CLI ejecutable del ejemplo.
- `requirements.txt`: declara que no hay dependencias runtime externas.
- `tasks/current/`: tarea activa, plan y preguntas abiertas.
- `decisions/`: decisiones aprobadas y ADRs.
- `docs/product/`: verdad funcional del flujo de soporte.
- `docs/architecture/`: diseno tecnico vigente o propuesto.
- `memory/`: hechos, restricciones, patrones, problemas y glosario.
- `src/`: modulos Python de la mini app.
- `tests/`: pruebas basicas con `unittest`.
- `data/requests.json`: persistencia runtime del ejemplo, no fuente canonica.
- `graphify-out/`: outputs derivados de Graphify para este proyecto instanciado.

`VALIDATION_GUIDE.md`, `ARCHITECTURE_VALIDATION.md`, `CHAT_SCENARIOS.md`, `TEST_EXECUTION_REPORT.md`, `TRACE_LOG.md`, `app.py`, `src/`, `tests/` y `data/` son extras pedagogicos del laboratorio. No son estandar obligatorio de `PROJECT_TEMPLATE/`.

## Stack

- Backend: Python simple con biblioteca estandar.
- Frontend: no aplica en este ejemplo.
- Base de datos: JSON local runtime en `data/requests.json`.
- Hosting: no aplica; no es una app desplegable.

## Restricciones

- Tecnicas:
  - mantener la app pequena y pedagogica;
  - no convertir `SAMPLE_PROJECT/` en plantilla de produccion;
  - tratar `data/requests.json` como dato runtime, no como fuente canonica;
  - no tratar `graphify-out/*` como fuente canonica.
- Negocio:
  - cubrir solo solicitudes internas de operaciones;
  - no modelar procesos de soporte externo a clientes finales.
- Seguridad:
  - no incluir datos reales de personas, clientes ni tickets;
  - no guardar credenciales ni tokens en Markdown.

## Nota de uso

Si una regla funcional cambia, actualizar primero `docs/product/spec.md`. Si el cambio afecta diseno tecnico o contratos, actualizar tambien `docs/architecture/sdd.md`, adaptar la automatizacion minima y registrar decision cuando corresponda.
