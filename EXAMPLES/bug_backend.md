# Ejemplo: Bug en Backend

> Caso prÃ¡ctico que muestra cÃ³mo el framework maneja un bug en un endpoint.

## SituaciÃ³n
"El endpoint de login dejÃ³ de funcionar despuÃ©s de mover una validaciÃ³n al backend."

## ClasificaciÃ³n por el Manager
- **Tipo**: Bug / Debugging.
- **Nivel**: 2 (requiere contexto dirigido).
- **Agente asignado**: Debugger â†’ Coder â†’ Reviewer.

## Contexto Cargado (segÃºn OPERACION/CONTEXT_ROUTER.md)

### Contexto mÃ­nimo (siempre)
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `active_task.md`

### Contexto dirigido (Nivel 2)
- `skills/debug-issue.md`
- `docs/engineering/error_handling.md`
- `memory/known_issues.md`
- Archivo del endpoint login.
- Archivo del servicio auth.

### QuÃ© NO se carga
- âŒ Toda la arquitectura.
- âŒ Todo el backlog.
- âŒ Todas las ADRs.
- âŒ Todo el repo.

## Flujo de EjecuciÃ³n

1. **Debugger** recopila logs y stack traces.
2. **Debugger** consulta `known_issues.md` â†’ no hay bug similar.
3. **Debugger** genera hipÃ³tesis: la validaciÃ³n movida impide el flujo de auth.
4. **Debugger** verifica: confirma que el middleware de validaciÃ³n ahora bloquea antes del login.
5. **Debugger** propone correcciÃ³n: reordenar middleware.
6. **Coder** implementa el fix.
7. **Reviewer** valida: el cambio es coherente, no afecta otros endpoints.

## Post-EjecuciÃ³n
- Se actualiza `memory/known_issues.md` con el patrÃ³n detectado.
- Se registra decisiÃ³n en `decision_log.md` si el reordenamiento de middleware es significativo.

