# Módulo 6 — Delivery, Deploy y Operación

## 1. Principio Rector

> No todo lo que construyes debe desplegarse. Pero todo lo que se usa repetidamente debe automatizarse.

## 2. Tipos de Delivery

| Tipo | Ejemplo | Complejidad |
|------|---------|-------------|
| Script local | Automatización Excel / scraping | Baja |
| Bot automatizado | n8n + API + Gmail | Media |
| API / backend | FastAPI + DB | Media-alta |
| SaaS completo | Web + backend + auth | Alta |

## 3. Estrategia de Deployment

**Regla clave**: Empieza siempre con el nivel mínimo que permita validar valor real.

Antes de desplegar, responde:
1. ¿Se ejecuta una sola vez o varias? → Una vez = local. Varias = automatizar.
2. ¿Necesita acceso externo? → No = local. Sí = API/servicio.
3. ¿Tiene lógica reutilizable? → No = script. Sí = backend.
4. ¿Debe escalar? → No = simple. Sí = arquitectura deployada.

> Primero demuestra que funciona. Luego demuestra que se usa. Recién después despliegas en serio.

## 4. Niveles de Deployment

### Nivel 1: Local (inicio obligatorio)
VS Code, Python, Playwright, scripts. Costo cero, control total, debug fácil.

### Nivel 2: Automatización (n8n)
Flujos automáticos, integración con Gmail/Sheets/APIs. La forma más rápida de generar impacto sin backend complejo.

### Nivel 3: Backend/API
FastAPI + PostgreSQL (Supabase). Para lógica reutilizable e integraciones externas.

### Nivel 4: SaaS
Next.js (frontend) + FastAPI (backend) + Supabase (DB/auth) + Vercel (hosting frontend) + Railway/Render (hosting backend).

## 5. Plataformas de Deploy

| Plataforma | Uso ideal | Costo |
|-----------|-----------|-------|
| Vercel | Frontend Next.js | Bajo |
| Railway | Backend simple | Bajo-medio |
| Render | Backend estable | Medio |
| Supabase | DB + Auth + Storage | Bajo |
| Hostinger VPS | Control total | Bajo |

## 6. Docker: Cuándo Sí / Cuándo No

**Sí**: portabilidad, producción, múltiples servicios, consistencia entre entornos.
**No**: scripts simples, aprendizaje, prototipos rápidos, automatización local.

## 7. n8n como Pieza Clave

n8n es el **orquestador externo** del framework. Conecta APIs, scripts Python, Google Sheets, Gmail, webhooks e IA. Reduce necesidad de backend, código y aumenta velocidad de entrega.

## 8. Playwright vs Stagehand

- **Playwright**: flujos claros y estables, selectores identificables, procesos repetitivos. Preciso y controlable.
- **Stagehand**: UI cambiante, flujos complejos, elementos difíciles de identificar. Más resiliente a cambios.
- **Regla**: Empezar siempre con Playwright. Solo escalar a Stagehand si el flujo se rompe.

## 9. CI/CD con GitHub Actions

Flujo: Push → Test → Build → Deploy. Automatiza validación y despliegue.

## 10. Seguridad Básica

- No subir API keys.
- Usar `.env` y variables de entorno.
- Control de accesos.
- `.gitignore` para excluir `.env`, credenciales y archivos sensibles.

## 11. Anti-Patrones Críticos

- ❌ Desplegar demasiado pronto → pérdida de tiempo.
- ❌ Usar microservicios sin necesidad → sobreingeniería.
- ❌ No automatizar → pierdes valor del framework.
- ❌ Depender solo de scripts manuales → no escalable.
