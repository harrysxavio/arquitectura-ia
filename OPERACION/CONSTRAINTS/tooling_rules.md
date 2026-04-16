# RESTRICCIONES: Politica de Herramientas y Modelos

Este documento evita que el framework se convierta en una coleccion de herramientas sin criterio. Las herramientas solo tienen sentido si mejoran el sistema de fuentes, contexto y validacion.

## Como Leer Este Documento

Para una persona no tecnica, la regla importante es que ninguna herramienta debe mandar sobre el proyecto solo porque parece poderosa. Para una persona tecnica o un agente, este archivo define criterios de adopcion, escalamiento y limites de uso.

## Regla maestra de adopcion

> [!IMPORTANT]
> La herramienta se adapta al sistema, NO al reves.

- Ninguna herramienta entra al framework si no responde claramente:
  - Que problema resuelve.
  - Que reemplaza o complementa.
  - Que complejidad agrega.
  - Que complejidad reduce.
  - Si compite con otra ya aprobada.
- PROHIBIDO agregar herramientas por tendencia, curiosidad o sin caso de uso.

## Nucleo obligatorio
- VS Code, Git, GitHub, agente principal (Cline o Codex), Markdown versionado.
- Estos NO son negociables.

## Agente principal

> [!WARNING]
> PROHIBIDO usar Cline y Codex como cerebro principal del mismo proyecto.

- OBLIGATORIO elegir uno como principal por proyecto: Cline o Codex.
- Cline: para frameworks con fuerte gobernanza documental y contexto persistente.
- Codex: para simplicidad operativa y productividad en ecosistema OpenAI.

## Politica de modelos
- No todos los agentes usan el mismo modelo.
- Manager -> modelo barato (GPT-4.1-mini / Qwen / DeepSeek). PROHIBIDO usar GPT-5 para clasificacion.
- Coder -> modelo medio (GPT-4.1 / DeepSeek). El 80% del codigo NO necesita modelo premium.
- Reviewer -> modelo medio/alto (GPT-4.1 / Claude Sonnet). Donde mas se justifica subir calidad.
- Debugger -> modelo alto (Claude Sonnet / GPT-5). Debugging complejo es el caso mas critico.
- Escalar modelo SOLO si falla el resultado.
- Si estas pagando mucho -> el problema es de contexto, no de modelo.

## Playwright vs Stagehand

> [!TIP]
> Empezar con Playwright y escalar a Stagehand solo si el flujo se rompe o se vuelve inestable.

- Playwright es la base. Stagehand es capa especializada.
- OBLIGATORIO empezar con Playwright.
- Solo escalar a Stagehand si el flujo se rompe o se vuelve inestable.
- PROHIBIDO usar Stagehand como reemplazo estandar de E2E.

## n8n
- Es el orquestador externo para automatizacion.
- NO usarlo como sustituto de backend.
- Mantener workflows pequenos y trazables.
- Guardar logica compleja fuera y llamar scripts/servicios cuando haga falta.

## Docker
- Usar cuando: portabilidad, produccion, multiples servicios, consistencia entre entornos.
- NO usar en: scripts simples, aprendizaje, prototipos rapidos, automatizacion local.

## Herramientas fuera del nucleo
- NO entran al inicio: Kubernetes, microservicios, Airflow, multiples clouds, auth enterprise compleja, RAG/embeddings por defecto.

## Gobernanza de herramientas
- La evolucion del stack DEBE ser controlada.
- PROHIBIDO cambiar todo de golpe.
- PROHIBIDO reestructurar sin necesidad.
- PROHIBIDO introducir herramientas sin uso claro documentado.

## Integracion con el Framework

Cuando una herramienta produce conocimiento, ese conocimiento debe ubicarse en una fuente correcta. Si define comportamiento, va a OpenSpec. Si describe estructura estable, va a arquitectura. Si registra una direccion aprobada, va a decisiones. Si solo ayuda a navegar, se mantiene como derivado.

La pregunta final no es "podemos usar esta herramienta?", sino "que parte del sistema mejora y que autoridad respeta?".

---
> [!NOTE]
> Para contexto filosofico, consulte `/THEORY/03_herramientas.md` y `/THEORY/07_gobernanza.md`.
