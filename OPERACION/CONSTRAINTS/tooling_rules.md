# CONSTRAINTS: Política de Herramientas y Modelos

## Regla maestra de adopción
- Ninguna herramienta entra al framework si no responde claramente:
  - Qué problema resuelve.
  - Qué reemplaza o complementa.
  - Qué complejidad agrega.
  - Qué complejidad reduce.
  - Si compite con otra ya aprobada.
- La herramienta se adapta al sistema, NO al revés.
- PROHIBIDO agregar herramientas por tendencia, curiosidad o sin caso de uso.

## Núcleo obligatorio
- VS Code, Git, GitHub, agente principal (Cline o Codex), Markdown versionado.
- Estos NO son negociables.

## Agente principal
- OBLIGATORIO elegir uno como principal por proyecto: Cline o Codex.
- PROHIBIDO usar ambos como cerebro principal del mismo proyecto.
- Cline: para frameworks con fuerte gobernanza documental y contexto persistente.
- Codex: para simplicidad operativa y productividad en ecosistema OpenAI.

## Política de modelos
- No todos los agentes usan el mismo modelo.
- Manager → modelo barato (GPT-4.1-mini / Qwen / DeepSeek). PROHIBIDO usar GPT-5 para clasificación.
- Coder → modelo medio (GPT-4.1 / DeepSeek). El 80% del código NO necesita modelo premium.
- Reviewer → modelo medio/alto (GPT-4.1 / Claude Sonnet). Donde más se justifica subir calidad.
- Debugger → modelo alto (Claude Sonnet / GPT-5). Debugging complejo es el caso más crítico.
- Escalar modelo SOLO si falla el resultado.
- Si estás pagando mucho → el problema es de contexto, no de modelo.

## Playwright vs Stagehand
- Playwright es la base. Stagehand es capa especializada.
- OBLIGATORIO empezar con Playwright.
- Solo escalar a Stagehand si el flujo se rompe o se vuelve inestable.
- PROHIBIDO usar Stagehand como reemplazo estándar de E2E.

## n8n
- Es el orquestador externo para automatización.
- NO usarlo como sustituto de backend.
- Mantener workflows pequeños y trazables.
- Guardar lógica compleja fuera y llamar scripts/servicios cuando haga falta.

## Docker
- Usar cuando: portabilidad, producción, múltiples servicios, consistencia entre entornos.
- NO usar en: scripts simples, aprendizaje, prototipos rápidos, automatización local.

## Herramientas fuera del núcleo
- NO entran al inicio: Kubernetes, microservicios, Airflow, múltiples clouds, auth enterprise compleja, RAG/embeddings por defecto.

## Gobernanza de herramientas
- La evolución del stack DEBE ser controlada.
- PROHIBIDO cambiar todo de golpe.
- PROHIBIDO reestructurar sin necesidad.
- PROHIBIDO introducir herramientas sin uso claro documentado.

---
> Para contexto filosófico, consulte `/THEORY/03_herramientas.md` y `/THEORY/07_gobernanza.md`.
