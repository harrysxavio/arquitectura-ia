# Politica Oficial de NotebookLM

## Rol

NotebookLM sirve para research sobre fuentes externas: PDFs, documentacion de terceros, papers, links y material largo que no debe cargarse completo al agente en cada tarea.

## Flujo Correcto

1. Definir preguntas de investigacion.
2. Cargar fuentes externas en NotebookLM.
3. Generar sintesis accionable.
4. Llevar el resultado al repo como artefacto comprimido.
5. Registrar decisiones o restricciones si la investigacion cambia el proyecto.

## Limites

- No es memoria viva del repo.
- No es fuente oficial del proyecto.
- No reemplaza `decision_log.md`, `project_facts.md`, `spec.md` ni `sdd.md`.
- No debe contener tareas activas oficiales.

## Salida Esperada

El conocimiento util debe volver al repo como:

- nota de integracion,
- resumen de investigacion,
- decision documentada,
- restriccion,
- patron aprobado.
