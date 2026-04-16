# VALIDATION_GUIDE.md

> Guia practica para validar `SAMPLE_PROJECT/` como ejemplo OpenSpec-first y para decidir si Graphify aporta valor real.

## Validacion Funcional

Desde `SAMPLE_PROJECT/`:

```bash
python -B -m unittest discover -s tests
python -B app.py demo
python -B app.py create --title "Acceso VPN" --description "Alta para equipo operaciones" --area "Operaciones" --type acceso
python -B app.py list
```

Comprobar:

- Los tests pasan.
- `demo` ejecuta un flujo pequeno completo.
- Las solicitudes de tipo `seguridad` parten con prioridad `alta`.
- El cierre sin nota falla con mensaje claro.
- `data/requests.json` se usa solo como persistencia de ejecucion.

## Validacion Documental

Comprobar:

- La verdad funcional vive en `openspec/specs/support-requests/spec.md`.
- El cambio activo de ejemplo vive en `openspec/changes/add-security-priority/`.
- La arquitectura estable vive en `docs/architecture/system.md`.
- `decisions/decision_log.md` es un indice breve de decisiones vigentes.
- `memory/` esta compacta y separada en `facts.md`, `constraints.md`, `patterns.md` y glosario si aporta.
- Graphify esta descrito como contexto derivado, no como fuente de verdad.

## Validacion de Arquitectura Total

La arquitectura funciona si una persona o agente puede responder estas preguntas sin abrir carpetas completas:

| Pregunta | Fuente esperada |
|---|---|
| Que problema resuelve el ejemplo? | `PROJECT_GUIDE.md` |
| Donde esta la regla funcional? | `openspec/specs/support-requests/spec.md` |
| Donde esta el cambio activo? | `openspec/changes/add-security-priority/` |
| Como esta construida la mini app? | `docs/architecture/system.md` |
| Que decisiones siguen vigentes? | `decisions/decision_log.md` |
| Que restricciones limitan cambios? | `memory/constraints.md` |
| Que mapa estructural derivado existe? | `graphify-out/GRAPH_REPORT.md` |

Senales de fallo:

- Hay que leer todo el repo para entender una tarea simple.
- Una regla funcional aparece como autoridad fuera de OpenSpec.
- Una salida derivada se usa para decidir comportamiento.
- La memoria se convierte en backlog o diario historico.

## Validacion de Graphify

Cuando Graphify este disponible, regenerar desde `SAMPLE_PROJECT/`:

```bash
graphify update .
```

Comprobar:

- `graphify-out/GRAPH_REPORT.md` menciona nodos reales del ejemplo.
- `graphify-out/graph.json` se actualiza.
- El reporte ayuda a ubicar componentes, no a reemplazar OpenSpec.
- Si el reporte esta desactualizado, se marca como derivado desactualizado y no se usa como base de decision.

## Sin Graphify vs Con Graphify

| Modo | Contexto inicial | Uso esperado | Riesgo |
|---|---|---|---|
| Sin Graphify | `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, OpenSpec relevante | Bueno para cambios locales o reglas claras. | Puede requerir mas exploracion si el impacto cruza modulos. |
| Con Graphify | Contexto inicial + `graphify-out/GRAPH_REPORT.md` | Bueno para incorporacion tecnica, impacto transversal o refactors. | Puede agregar ruido si la tarea ya era local y clara. |

Ejemplo practico: si cambia la prioridad de seguridad, primero consulta OpenSpec. Usa Graphify solo si necesitas ubicar que modulos y tests implementan esa regla.

## Criterios Para Decidir si Graphify Aporto Valor

Graphify aporto valor si:

- redujo la cantidad de archivos abiertos;
- mostro un modulo o test relevante que no era obvio;
- aclaro dependencias entre componentes;
- ayudo a estimar impacto transversal;
- mejoro la revision sin contradecir fuentes canonicas.

Graphify no aporto suficiente si:

- solo repitio nombres evidentes;
- obligo a validar muchas inferencias irrelevantes;
- no cambio la ruta de investigacion;
- agrego contexto para una tarea que ya era local;
- contradijo OpenSpec, arquitectura, decisiones o memoria.

## EXTRACTED vs INFERRED

| Tipo | Que significa | Como usarlo |
|---|---|---|
| `EXTRACTED` | Relacion detectada desde senales estructurales: imports, llamadas, clases, tests o rutas. | Tratar como pista fuerte, verificando si cambia codigo o docs canonicos. |
| `INFERRED` | Relacion deducida por nombres, texto o semantica. | Tratar como hipotesis; abrir los archivos citados antes de decidir. |

Regla practica: `EXTRACTED` orienta; `INFERRED` pregunta. Ninguno reemplaza OpenSpec.

## Plantilla de Registro de Prueba Real

Usar esta plantilla cuando se quiera comparar trabajo manual contra trabajo con Graphify sin crear archivos nuevos.

| Campo | Registro |
|---|---|
| Escenario |  |
| Prompt |  |
| Contexto minimo cargado |  |
| Contexto adicional cargado |  |
| Contexto evitado |  |
| Decision de usar o no Graphify |  |
| Archivos impactados |  |
| Resultado observado |  |
| Conclusion |  |

## Cierre Esperado

La validacion es satisfactoria cuando el ejemplo puede ejecutarse, las fuentes de autoridad son claras, Graphify se mantiene derivado y una persona puede explicar que leer para una tarea sin cargar el repo completo.
