# Ejemplo: Bug en Backend

> [!NOTE]
> Caso practico que muestra como el framework maneja un bug en un endpoint.

## Situacion

"El endpoint de login dejo de funcionar despues de mover una validacion al backend."

## Clasificacion por el Manager
- **Tipo**: Bug / Debugging.
- **Nivel**: 2 (requiere contexto dirigido).
- **Agente asignado**: Debugger -> Coder -> Reviewer.

## Contexto Cargado (segun OPERACION/CONTEXT_ROUTER.md)

### Contexto minimo (siempre)
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `active_task.md`

### Contexto dirigido (Nivel 2)
- `skills/debug-issue.md`
- `docs/engineering/error_handling.md`
- `memory/known_issues.md`
- Archivo del endpoint login.
- Archivo del servicio auth.

### Que NO se carga

> [!WARNING]
> No se carga contexto amplio por si acaso.

- Toda la arquitectura.
- Todo el backlog.
- Todas las ADRs.
- Todo el repo.

## Flujo de Ejecucion

1. **Debugger** recopila logs y stack traces.
2. **Debugger** consulta `known_issues.md` -> no hay bug similar.
3. **Debugger** genera hipotesis: la validacion movida impide el flujo de auth.
4. **Debugger** verifica: confirma que el middleware de validacion ahora bloquea antes del login.
5. **Debugger** propone correccion: reordenar middleware.
6. **Coder** implementa el fix.
7. **Reviewer** valida: el cambio es coherente, no afecta otros endpoints.

## Post-Ejecucion
- Se actualiza `memory/known_issues.md` con el patron detectado.
- Se registra decision en `decision_log.md` si el reordenamiento de middleware es significativo.
