# Módulo 3 — Herramientas Oficiales del Stack

## 1. Principio de Adopción

Una herramienta entra al framework solo si responde claramente:
- Qué problema resuelve.
- Qué reemplaza o complementa.
- Qué complejidad agrega.
- Qué complejidad reduce.
- Si duplica otra herramienta ya presente.
- Si mejora el retorno del sistema más de lo que aumenta su mantenimiento.

## 2. Clasificación Oficial

### A. Núcleo Obligatorio
| Herramienta | Función |
|-------------|---------|
| VS Code | Superficie visual principal (IDE) |
| Git | Control de versiones, trazabilidad |
| GitHub | Hosting de repos, PRs, CI/CD |
| Agente principal (Cline o Codex) | Cerebro de ejecución |
| Markdown versionado | Documentación dentro del repo |

### B. Núcleo Recomendado
| Herramienta | Función |
|-------------|---------|
| Aider | Edición quirúrgica con diffs limpios |
| NotebookLM | Research sobre fuentes externas |
| n8n | Automatización de flujos externos |

### C. Herramientas de Ejecución y Delivery
GitHub Actions, Playwright, Stagehand, Docker, FastAPI, Next.js, TypeScript, Postgres, Supabase, Vercel.

### D. Opcionales de Etapa 2
OpenCode, OpenRouter, Gemini CLI, Sentry, Clerk/Auth0/Stripe, Hostinger VPS, Cloudflare.

## 3. Decisión Cline vs Codex

El framework **no obliga** uno de los dos, pero **sí obliga a elegir uno como principal** por proyecto.

| Criterio | Cline | Codex |
|----------|-------|-------|
| Fortaleza | Gobernanza documental, Memory Bank, rules, subagents | Simplicidad operativa, integración OpenAI |
| Memoria | Muy fuerte (Memory Bank nativo) | Configuración compartida IDE/CLI |
| Mejor para | Frameworks con fuerte contexto persistente | Productividad rápida en ecosistema OpenAI |

**Regla**: No usar ambos como cerebro principal del mismo proyecto.

**Claude Code** y **OpenCode** no quedan excluidos por debilidad, sino para mantener dos rutas base simples y gobernables. Pueden incorporarse como herramientas complementarias o de etapa 2.

## 4. Roles Claros por Herramienta

- **VS Code**: la superficie.
- **Git + GitHub**: trazabilidad y colaboración.
- **Cline o Codex**: el agente principal.
- **Aider**: herramienta quirúrgica de cambios controlados.
- **NotebookLM**: capa de investigación.
- **n8n**: capa de automatización externa.

## 5. Stack Técnico Recomendado

### App Web Estándar
Next.js + TypeScript + Vercel + FastAPI + Postgres/Supabase + GitHub Actions + Playwright.

### SaaS Liviano/Mediano
Lo anterior + Docker (backend) + Sentry (posterior) + Stripe (si hay cobro).

### Bot o Automatización Web
Python + Playwright + Stagehand (si sitio cambiante) + Docker + n8n.

### API / Servicio Interno
FastAPI + Postgres + Docker + GitHub Actions + Sentry (posterior).

## 6. Secuencia Oficial de Adopción

1. VS Code → 2. Git → 3. GitHub → 4. Cline o Codex → 5. Aider → 6. NotebookLM → 7. n8n → 8. GitHub Actions → 9. FastAPI → 10. Next.js + TypeScript → 11. Postgres → 12. Supabase → 13. Vercel → 14. Docker → 15. Playwright → 16. Stagehand → 17. Sentry.

## 7. Política Playwright vs Stagehand

- **Playwright**: estándar base para testing E2E y automatización robusta.
- **Stagehand**: capa especializada para exploración web, scraping semántico y flujos frágiles.
- Stagehand **no reemplaza** Playwright. Empezar siempre con Playwright.

## 8. Política de Modelos

| Nivel | Uso | Ejemplos |
|-------|-----|----------|
| Baratos/locales | Clasificación, resumen, preprocesamiento | Qwen, DeepSeek, GPT-4.1-mini |
| Medios | Implementación, revisión, debugging moderado | GPT-4.1, Claude Sonnet |
| Premium | Arquitectura, refactors grandes, debugging difícil | GPT-5, Claude Opus |
