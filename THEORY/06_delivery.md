# Modulo 6 - Delivery, Deploy y Operacion

## 1. Principio Rector

No todo lo que se construye debe desplegarse. Pero todo lo que se usa repetidamente debe automatizarse.

Delivery en este framework significa llevar una solucion desde intencion hasta uso real con el menor nivel de complejidad suficiente.

## 2. Preguntas Antes de Desplegar

Antes de elegir plataforma o stack, responder:

1. Se ejecuta una sola vez o muchas veces?
2. Necesita acceso externo?
3. Tiene logica reutilizable?
4. Necesita usuarios, auth o pagos?
5. Debe escalar?
6. Hay datos persistentes?
7. Hay requisitos de seguridad?
8. Hay tests o checks reproducibles?

Primero demostrar que funciona. Luego demostrar que se usa. Despues desplegar en serio.

## 3. Tipos de Delivery

| Tipo | Ejemplo | Stack sugerido | Complejidad |
|---|---|---|---|
| Script local | Limpieza de CSV, automatizacion puntual | Python, CLI, archivos locales | Baja |
| Automatizacion | Gmail, Sheets, webhooks, APIs | n8n + scripts/API | Media |
| Bot o scraping | Flujo web repetible | Python + Playwright, Stagehand si aplica | Media |
| API interna | Servicio reutilizable | FastAPI + Postgres/Supabase | Media-alta |
| App web | Producto con UI | Next.js + TypeScript + backend si aplica | Alta |
| SaaS | Usuarios, auth, pagos, observabilidad | Next.js, FastAPI, Supabase, Stripe, Sentry | Alta |

## 4. Niveles de Deployment

### Nivel 1: Local

Usar para scripts, prototipos, pruebas rapidas y tareas sin usuarios externos.

Stack comun:

- VS Code,
- Python o Node,
- Playwright si hay navegador,
- archivos locales o SQLite si basta.

### Nivel 2: Automatizacion externa

Usar cuando el flujo se repite y conecta sistemas.

Stack comun:

- n8n,
- webhooks,
- Gmail/Sheets/APIs,
- scripts pequenos o endpoint interno.

n8n orquesta. No debe cargar logica compleja que pertenezca a un backend.

### Nivel 3: Backend/API

Usar cuando hay logica reutilizable, integraciones externas o necesidad de servicio.

Stack recomendado:

- FastAPI,
- Postgres o Supabase,
- Docker si hay produccion o portabilidad,
- GitHub Actions para validacion,
- Sentry cuando haya fallos en uso real.

### Nivel 4: App web o SaaS

Usar cuando hay usuarios, UI, auth, persistencia y evolucion de producto.

Stack recomendado:

- Next.js + TypeScript,
- FastAPI si el backend merece separacion,
- Supabase para DB/auth/storage cuando simplifique,
- Vercel para frontend,
- Railway, Render o VPS para backend,
- Stripe solo si hay cobro real,
- Playwright para flujos criticos,
- GitHub Actions para CI/CD.

## 5. Plataformas

| Plataforma | Uso ideal |
|---|---|
| Vercel | Frontend Next.js |
| Railway | Backend simple o prototipo deployado |
| Render | Backend estable con bajo mantenimiento |
| Supabase | Postgres, auth y storage gestionados |
| Hostinger VPS | Control total con mas responsabilidad operativa |
| GitHub Actions | Tests, build, checks y despliegues automatizados |

## 6. Docker

Usar Docker cuando:

- se necesita portabilidad,
- hay produccion,
- hay multiples servicios,
- el entorno local y remoto deben coincidir,
- hay dependencias dificiles de reproducir.

Evitar Docker cuando:

- es un script simple,
- el proyecto esta en aprendizaje,
- el prototipo cambia demasiado,
- no hay despliegue real.

## 7. Playwright y Stagehand

Playwright es la herramienta base para E2E y automatizacion robusta.

Stagehand se usa cuando:

- la UI cambia con frecuencia,
- los selectores son fragiles,
- el flujo requiere interpretacion semantica,
- scraping o navegacion exploratoria son parte del trabajo.

Regla: empezar con Playwright. Escalar a Stagehand solo con evidencia.

## 8. CI/CD

Flujo minimo:

1. Push o pull request.
2. Instalar dependencias.
3. Ejecutar lint/tests si existen.
4. Build si aplica.
5. Deploy solo si los checks pasan.

No introducir CI/CD si no hay comandos reproducibles. Primero definir scripts locales, despues automatizarlos.

## 9. Seguridad Basica

- No subir API keys.
- Usar variables de entorno.
- Mantener `.env.example` con valores dummy cuando aplique.
- Excluir `.env`, `.env.*` y credenciales locales.
- No guardar secretos en Markdown, logs o decisiones.
- Registrar restricciones de seguridad en `memory/constraints.md`.

## 10. Documentacion Operativa

Cuando el proyecto ya esta desplegado, debe existir informacion suficiente para operar:

- como correr localmente,
- como testear,
- como desplegar,
- que variables de entorno requiere,
- donde mirar logs,
- que integraciones externas existen,
- que riesgos o incidentes conocidos hay.

Segun el proyecto, esto puede vivir en `PROJECT_GUIDE.md`, `docs/architecture/sdd.md`, `memory/known_issues.md` o un runbook listado en `CONTEXT_INDEX.md`.

## 11. Regla Final

El mejor delivery es el menor sistema que resuelve el problema real y deja una ruta clara para crecer sin reescribir todo.
