# SAMPLE_PROJECT - Mesa Interna de Soporte Operativo

Proyecto ejemplo que muestra la arquitectura OpenSpec-first en uso con una mini app CLI.

## Que es

Una app pedagogica para crear, listar y cerrar solicitudes internas de soporte operativo. Sirve para aprender como conviven OpenSpec, arquitectura estable, decisiones, memoria compacta, codigo, tests y Graphify.

## Autoridades Activas

| Necesidad | Fuente |
|---|---|
| Verdad funcional | `openspec/specs/support-requests/spec.md` |
| Cambio activo de ejemplo | `openspec/changes/add-security-priority/` |
| Arquitectura estable | `docs/architecture/system.md` |
| Decisiones vigentes | `decisions/decision_log.md` |
| Memoria compacta | `memory/facts.md`, `memory/constraints.md`, `memory/patterns.md` |
| Contexto derivado | `graphify-out/` |

## Ejecutar

```bash
python -B -m unittest discover -s tests
python -B app.py demo
python -B app.py create --title "Acceso VPN" --description "Alta para equipo operaciones" --area "Operaciones" --type acceso
python -B app.py list
```

`data/requests.json` es ejecucion local, no fuente de verdad.

## Como Leer

1. `PROJECT_GUIDE.md` para identidad y alcance.
2. `CONTEXT_INDEX.md` para elegir fuentes.
3. `openspec/specs/support-requests/spec.md` para comportamiento aprobado.
4. `openspec/changes/add-security-priority/` para ver el flujo de cambio.
5. `docs/architecture/system.md` para diseno estable.
6. `decisions/` y `memory/` solo si la tarea lo necesita.
7. `graphify-out/` solo como mapa derivado.

## Que no es

No es plantilla de produccion, API real, sistema desplegable ni reemplazo de `PROJECT_TEMPLATE/`.
