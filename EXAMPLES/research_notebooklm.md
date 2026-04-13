# Ejemplo: Research con NotebookLM

> [!NOTE]
> Caso practico que muestra como el framework maneja una investigacion documental.

## Situacion
"Necesito revisar varios PDFs y links sobre una API externa antes de integrarla."

## Clasificacion por el Manager
- **Tipo**: Research.
- **Nivel**: 2.
- **Herramienta**: NotebookLM (fuera del repo).
- **Agente**: Manager define objetivo -> Research externo -> Contexto comprimido al repo.

## Flujo de Ejecucion

### Fase 1: Research (fuera del repo)
1. Cargar fuentes en NotebookLM (PDFs, documentacion de la API, ejemplos).
2. Hacer preguntas especificas:
   - Cuales son los endpoints principales?
   - Que autenticacion requiere?
   - Cuales son las limitaciones de rate?
   - Hay SDKs oficiales?
3. Generar sintesis accionable.

### Fase 2: Compresion al repo
Crear `docs/architecture/integration-notes.md` con:
- Resumen de la API.
- Endpoints clave con metodo y payload.
- Tipo de autenticacion requerida.
- Limitaciones detectadas.
- Riesgos de integracion.
- Dudas abiertas que requieren confirmacion.

### Fase 3: Ejecucion
- El Coder usa `integration-notes.md` como contexto dirigido.
- NO necesita releer los PDFs originales.
- El modelo barato puede trabajar perfectamente con el contexto comprimido.

## Que NO debe pasar

> [!WARNING]
> NotebookLM no debe convertirse en fuente oficial ni reemplazar documentacion canonica del repo.

- Usar NotebookLM como fuente oficial del proyecto.
- Dejar el conocimiento solo en el notebook sin traerlo al repo.
- No documentar la integracion dentro del repo.
- Forzar al agente a releer las fuentes originales en cada tarea posterior.

## Post-Ejecucion
- `integration-notes.md` se agrega a `CONTEXT_INDEX.md` como ruta para tareas de integracion.
- Si se toman decisiones sobre la API, se registran en `decision_log.md`.
