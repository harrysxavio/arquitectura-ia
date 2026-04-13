# Modulo 3 - Herramientas Oficiales del Stack

## 1. Principio de Adopcion

Una herramienta entra al framework solo si resuelve un problema real y mejora el retorno del sistema mas de lo que aumenta su mantenimiento.

Antes de incorporarla, debe responder:

- que problema resuelve,
- que reemplaza o complementa,
- que complejidad agrega,
- que complejidad reduce,
- si duplica otra herramienta ya aprobada,
- como se documenta su uso,
- que agente o workflow la necesita.

La herramienta se adapta al sistema. El sistema no se reorganiza por moda.

## 2. Nucleo Obligatorio

| Herramienta | Funcion | Porque es obligatoria |
|---|---|---|
| VS Code | Superficie principal de trabajo | Permite operar repo, agente, terminal y documentos en un lugar |
| Git | Control de versiones | Da trazabilidad, rollback y comparacion de cambios |
| GitHub | Hosting, PRs, colaboracion y CI/CD | Centraliza repos, issues, pull requests y automatizacion |
| Agente principal | Ejecucion asistida por IA | Traduce intencion a cambios, analisis o documentacion |
| Markdown versionado | Documentacion dentro del repo | Mantiene reglas y memoria cerca del codigo |

El agente principal debe ser uno por proyecto: Cline o Codex.

## 3. Cline vs Codex

El framework permite ambos, pero obliga a elegir uno como cerebro principal del proyecto.

| Criterio | Cline | Codex |
|---|---|---|
| Fortaleza | Gobernanza documental, Memory Bank, reglas persistentes | Simplicidad operativa, integracion OpenAI, flujo CLI/IDE |
| Mejor uso | Proyectos con mucha memoria documental | Productividad rapida y cambios de codigo guiados |
| Riesgo | Sobrecargar estructura si no se controla | Depender demasiado del prompt si falta documentacion |

Regla: no usar Cline y Codex como directores simultaneos del mismo proyecto. Pueden coexistir solo si uno tiene rol principal y el otro rol auxiliar claramente documentado.

## 4. Herramientas Recomendadas

| Herramienta | Rol | Limite |
|---|---|---|
| Aider | Edicion quirurgica con diffs controlados | No reemplaza al agente principal ni la gobernanza |
| NotebookLM | Research sobre fuentes externas extensas | No es memoria oficial del repo |
| n8n | Automatizacion externa de flujos | No sustituye backend cuando hay logica compleja |
| GitHub Actions | Validacion y despliegue automatizado | No arregla ausencia de tests o scripts reproducibles |
| Playwright | Testing E2E y automatizacion web robusta | No debe reemplazarse por herramientas semanticas por defecto |
| Stagehand | Automatizacion web semantica en flujos fragiles | Solo despues de Playwright si el flujo lo justifica |
| Docker | Portabilidad y consistencia de entornos | No usar en scripts simples o prototipos locales sin necesidad |

## 5. Stack Tecnico Recomendado

### App web estandar

- Frontend: Next.js + TypeScript.
- Backend: FastAPI si la logica no cabe bien en el frontend.
- Base de datos: Postgres o Supabase.
- Hosting: Vercel para frontend; Railway, Render o VPS para backend.
- Validacion: GitHub Actions + Playwright.

### SaaS liviano o mediano

- Next.js + TypeScript.
- FastAPI o backend equivalente.
- Supabase para Postgres, auth y storage cuando simplifique.
- Stripe solo si hay cobro real.
- Sentry cuando ya hay usuarios o debugging recurrente.
- Docker cuando haya produccion, multiples servicios o necesidad de portabilidad.

### Bot o automatizacion

- Python para logica local o scripts.
- Playwright para flujos web estables.
- Stagehand si la UI cambia o los selectores son fragiles.
- n8n para orquestacion externa, webhooks, Gmail, Sheets o APIs.
- Docker si se ejecuta en servidor o necesita entorno reproducible.

### API o servicio interno

- FastAPI.
- Postgres o Supabase.
- Docker si se despliega como servicio.
- GitHub Actions para tests/build.
- Sentry cuando los fallos ya no se puedan investigar solo localmente.

## 6. Secuencia de Adopcion

1. VS Code.
2. Git.
3. GitHub.
4. Cline o Codex como agente principal.
5. Markdown canonico dentro del repo.
6. Aider si se necesitan diffs quirurgicos.
7. NotebookLM si hay research externo largo.
8. n8n si hay automatizacion repetible.
9. GitHub Actions cuando haya validacion automatizable.
10. FastAPI, Next.js, TypeScript, Postgres o Supabase segun producto.
11. Vercel, Railway, Render o VPS segun delivery.
12. Docker, Playwright, Stagehand y Sentry cuando el proyecto lo justifique.

## 7. Politica Playwright vs Stagehand

Playwright es la base. Es preciso, trazable y compatible con testing E2E.

Stagehand es una capa especializada para exploracion semantica, scraping o flujos donde la UI cambia y los selectores se rompen.

Regla: empezar con Playwright. Escalar a Stagehand solo si hay evidencia de fragilidad o necesidad semantica.

## 8. Politica de Modelos

| Nivel | Uso | Ejemplos |
|---|---|---|
| Barato/local | Clasificacion, resumen, preprocesamiento | Qwen, DeepSeek, modelos mini |
| Medio | Implementacion, revision moderada, debugging simple | GPT-4.1, Claude Sonnet, equivalentes |
| Premium | Arquitectura, refactors grandes, debugging dificil | GPT-5, Claude Opus, equivalentes |

El modelo se escala cuando falla el resultado o sube el riesgo. Si el costo sube demasiado, revisar primero contexto, fuentes y workflow antes de culpar al modelo.

## 9. Regla Final

El stack correcto es el minimo que permite entregar valor, validar calidad y mantener trazabilidad. Agregar herramientas sin caso de uso documentado degrada el framework.
