# Ejemplo: Research con NotebookLM

> Caso práctico que muestra cómo el framework maneja una investigación documental.

## Situación
"Necesito revisar varios PDFs y links sobre una API externa antes de integrarla."

## Clasificación por el Manager
- **Tipo**: Research.
- **Nivel**: 2.
- **Herramienta**: NotebookLM (fuera del repo).
- **Agente**: Manager define objetivo → Research externo → Contexto comprimido al repo.

## Flujo de Ejecución

### Fase 1: Research (fuera del repo)
1. Cargar fuentes en NotebookLM (PDFs, documentación de la API, ejemplos).
2. Hacer preguntas específicas:
   - ¿Cuáles son los endpoints principales?
   - ¿Qué autenticación requiere?
   - ¿Cuáles son las limitaciones de rate?
   - ¿Hay SDKs oficiales?
3. Generar síntesis accionable.

### Fase 2: Compresión al repo
Crear `docs/architecture/integration-notes.md` con:
- Resumen de la API.
- Endpoints clave con método y payload.
- Tipo de autenticación requerida.
- Limitaciones detectadas.
- Riesgos de integración.
- Dudas abiertas que requieren confirmación.

### Fase 3: Ejecución
- El Coder usa `integration-notes.md` como contexto dirigido.
- NO necesita releer los PDFs originales.
- El modelo barato puede trabajar perfectamente con el contexto comprimido.

## Qué NO debe pasar
- ❌ Usar NotebookLM como fuente oficial del proyecto.
- ❌ Dejar el conocimiento solo en el notebook sin traerlo al repo.
- ❌ No documentar la integración dentro del repo.
- ❌ Forzar al agente a releer las fuentes originales en cada tarea posterior.

## Post-Ejecución
- `integration-notes.md` se agrega a `CONTEXT_INDEX.md` como ruta para tareas de integración.
- Si se toman decisiones sobre la API, se registran en `decision_log.md`.
