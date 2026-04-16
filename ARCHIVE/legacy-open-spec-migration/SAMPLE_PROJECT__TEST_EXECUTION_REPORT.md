# TEST_EXECUTION_REPORT.md

> Evidencia de ejecucion real para `SAMPLE_PROJECT/`.

## Resumen

| Campo | Valor |
|---|---|
| Fecha de ejecucion | 2026-04-13 22:34:57 -04:00 |
| Entorno | Windows PowerShell, repo local `arquitectura-ia`, directorio `SAMPLE_PROJECT/` |
| Objetivo | Validar mini app, tests, persistencia runtime y Graphify |
| Estado final | Validado |

## Comandos Ejecutados

| Paso | Comando | Resultado | Salida relevante |
|---|---|---|---|
| 1 | `python -B -m unittest discover -s tests` | Paso | `Ran 11 tests in 0.048s`; `OK` |
| 2 | `python -B app.py demo` | Paso | Creo una solicitud `acceso` cerrada y una `seguridad` en triage con prioridad `alta` |
| 3 | `python -B app.py create --title "Acceso VPN" --description "Alta para equipo operaciones" --area "Operaciones" --type acceso` | Paso | Creo `req-d0ee6e6b` con prioridad `media` y estado `en triage` |
| 4 | `python -B app.py list` | Paso | Listo 3 solicitudes: demo acceso cerrada, demo seguridad en triage, acceso VPN en triage |
| 5 | `python -B app.py close --id req-d0ee6e6b --note "Resuelto con alta manual"` | Paso | Cerro `req-d0ee6e6b` con nota `Resuelto con alta manual` |
| 6 | `graphify update .` | Paso | `Rebuilt: 72 nodes, 130 edges, 9 communities`; actualizo `graph.json` y `GRAPH_REPORT.md` |
| 7 | Reset runtime | Paso | `data/requests.json` quedo en `[]` |
| 8 | `graphify update .` despues de crear este reporte y `TRACE_LOG.md` | Paso | `GRAPH_REPORT.md` quedo actualizado; ver valor de corpus en el reporte generado |

## Salidas Resumidas

### Tests

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.048s

OK
```

### Demo

```text
Demo ejecutado.

Solicitud cerrada:
id: req-bee8fb56
title: Revisar acceso a VPN
type: acceso
priority: media
status: cerrada

Solicitud de seguridad en triage:
id: req-92569ca3
title: Alerta de credenciales
type: seguridad
priority: alta
status: en triage
```

### Create/List/Close

```text
id: req-d0ee6e6b
title: Acceso VPN
type: acceso
priority: media
status: en triage
```

`list` mostro las tres solicitudes esperadas despues de `demo` y `create`.

```text
id: req-d0ee6e6b
title: Acceso VPN
type: acceso
priority: media
status: cerrada
closing_note: Resuelto con alta manual
```

### Graphify

```text
Re-extracting code files in . (no LLM needed)...
[graphify watch] Rebuilt: 72 nodes, 130 edges, 9 communities
[graphify watch] graph.json and GRAPH_REPORT.md updated in graphify-out
Code graph updated. For doc/paper/image changes run /graphify --update in your AI assistant.
```

## Pruebas Pasadas

- Tests unitarios de triage, servicio y storage.
- Flujo CLI `demo`.
- Flujo CLI `create`.
- Flujo CLI `list`.
- Flujo CLI `close`.
- Regla observada: solicitud de `seguridad` parte con prioridad `alta`.
- Persistencia runtime observada: `data/requests.json` cambia durante la prueba.
- Limpieza final: `data/requests.json` vuelve a `[]`.
- Regeneracion Graphify con comando publico desde `SAMPLE_PROJECT/`.
- Regeneracion Graphify repetida despues de agregar evidencia auditable.

## Pruebas Fallidas

No hubo fallos en los comandos ejecutados en esta ronda.

No se ejecutaron comandos negativos directos para cierre sin nota o id inexistente en CLI. Esa cobertura se observo por tests unitarios: `test_close_request_requires_note` y `test_close_request_requires_existing_id`.

## Correcciones Necesarias

- Se reseteo `data/requests.json` a `[]` despues de validar la CLI, porque es persistencia runtime y no fuente canonica.
- No fue necesario cambiar codigo de la mini app.

## Estado Final

- `SAMPLE_PROJECT/` queda funcional y documentado como laboratorio pedagogico.
- `graphify-out/GRAPH_REPORT.md` y `graphify-out/graph.json` existen como contexto derivado.
- `GRAPH_REPORT.md` reporta 72 nodos, 130 edges y 9 comunidades sobre el corpus actualizado.
- `graph.html` no fue generado por `graphify update .`; esto es coherente con el contrato actualizado, donde `graph.html` es opcional.
- Las nuevas evidencias viven en `TEST_EXECUTION_REPORT.md` y `TRACE_LOG.md`.
