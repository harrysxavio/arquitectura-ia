# PROJECT_GUIDE.md

> Ejemplo rellenado. En un proyecto real, este archivo se vuelve canonico dentro del proyecto activo.

## Proposito

Describir la identidad, alcance, estructura, stack y restricciones principales de la Mesa Interna de Soporte Operativo.

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
  - ejemplo minimo de codigo para ilustrar el flujo.
- Fuera de alcance:
  - autenticacion real;
  - integracion con mesa de ayuda externa;
  - base de datos productiva;
  - notificaciones automaticas;
  - interfaz web completa.

## Estructura

- `README.md`: guia de onboarding para entender el ejemplo.
- `CONTEXT_INDEX.md`: mapa de fuentes oficiales del proyecto.
- `AGENTS.md`: ajustes locales para roles de agente.
- `tasks/current/`: tarea activa, plan y preguntas abiertas.
- `decisions/`: decisiones aprobadas y ADRs.
- `docs/product/`: verdad funcional del flujo de soporte.
- `docs/architecture/`: diseno tecnico vigente o propuesto.
- `memory/`: hechos, restricciones, patrones, problemas y glosario.
- `graphify-out/`: placeholders pedagogicos de outputs derivados.
- `src/`: codigo minimo ilustrativo, no obligatorio en el framework.

## Stack

- Backend: Python simple ilustrativo.
- Frontend: no aplica en este ejemplo.
- Base de datos: no aplica; el ejemplo asume almacenamiento futuro.
- Hosting: no aplica; no es una app desplegable.

## Restricciones

- Tecnicas:
  - no construir una aplicacion completa dentro de este ejemplo;
  - mantener el codigo en `src/` como apoyo pedagogico;
  - no tratar `graphify-out/*` como fuente canonica.
- Negocio:
  - cubrir solo solicitudes internas de operaciones;
  - no modelar procesos de soporte externo a clientes finales.
- Seguridad:
  - no incluir datos reales de personas, clientes ni tickets;
  - no guardar credenciales ni tokens en Markdown.

## Nota de uso

Si una regla funcional cambia, actualizar primero `docs/product/spec.md`. Si el cambio afecta diseno tecnico o contratos, actualizar tambien `docs/architecture/sdd.md` y registrar decision cuando corresponda.

