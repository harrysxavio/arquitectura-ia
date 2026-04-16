# Uso de OpenSpec en Este Framework

Esta guia explica como usar OpenSpec de forma practica dentro de la arquitectura del repositorio. No reemplaza la documentacion oficial de OpenSpec; adapta su flujo al reparto de autoridad de este framework.

## Idea Central

OpenSpec-first significa que el comportamiento funcional se acuerda antes de implementarse. La regla no nace en el codigo ni en una conversacion: nace como spec vigente o como cambio propuesto.

En la practica:

- `openspec/specs/*/spec.md` describe el comportamiento aprobado actual.
- `openspec/changes/*` describe cambios propuestos o en curso.
- El codigo implementa OpenSpec; no lo reemplaza.
- Arquitectura, decisiones y memoria explican contexto, no gobiernan comportamiento funcional.

## Que Vive en Cada Archivo

| Archivo | Que contiene | Quien lo completa |
|---|---|---|
| `openspec/specs/<capability>/spec.md` | Requirements y scenarios del comportamiento vigente. | Humano o agente, con revision humana. |
| `openspec/changes/<change-id>/proposal.md` | Por que se propone el cambio, alcance y no alcance. | Idealmente humano; el agente puede proponer borrador. |
| `openspec/changes/<change-id>/design.md` | Diseno tecnico del cambio cuando afecta arquitectura, datos, integraciones o contratos. | Humano tecnico o agente con revision. |
| `openspec/changes/<change-id>/tasks.md` | Lista verificable de implementacion y validacion. | Agente puede generar y actualizar; humano revisa. |
| `openspec/changes/<change-id>/specs/<capability>/spec.md` | Delta funcional: requirements agregados, modificados o removidos. | Humano o agente; debe revisarse antes de implementar. |

## Persona y Agente

| Momento | Que hace la persona | Que puede hacer el agente |
|---|---|---|
| Antes del cambio | Explica el problema, prioridad, alcance y limites. | Ordena la solicitud, detecta preguntas abiertas y propone estructura. |
| Al crear OpenSpec | Aprueba intencion, alcance y comportamiento esperado. | Redacta `proposal.md`, deltas de spec y primeros escenarios. |
| Durante diseno | Decide restricciones, riesgos aceptables y alternativas relevantes. | Propone `design.md`, impacto tecnico y tareas verificables. |
| Durante implementacion | Revisa que no se haya cambiado el alcance. | Implementa segun `tasks.md`, actualiza checkboxes y reporta desvio. |
| Al cerrar | Acepta el resultado funcional. | Ayuda a validar, archivar el cambio y actualizar docs derivadas. |

La persona no tiene que escribir todo a mano, pero si debe aportar criterio. El agente puede acelerar redaccion y ejecucion; no debe decidir solo una regla de negocio, una excepcion de seguridad o un cambio de alcance.

## Que Completa la Persona

La persona debe aportar intencion, prioridades, limites y aceptacion. En particular:

- definir el problema real;
- decidir alcance y no alcance;
- aprobar cambios funcionales;
- resolver ambiguedades de negocio;
- aceptar o rechazar decisiones tecnicas durables.

El agente puede redactar, estructurar y proponer, pero no debe inventar autoridad cuando hay ambiguedad.

## Que Puede Completar el Agente

El agente puede:

- convertir una solicitud en `proposal.md`;
- proponer deltas OpenSpec;
- sugerir `design.md` si detecta impacto tecnico;
- descomponer trabajo en `tasks.md`;
- actualizar checkboxes al implementar;
- detectar inconsistencias entre spec, arquitectura y codigo.

El agente debe pedir o dejar explicita una decision humana cuando el cambio afecta alcance, prioridad, riesgo, seguridad o costo.

## Flujo Operativo Manual

Usa este flujo aunque no instales el CLI oficial:

1. Leer `AGENTS.md`, `PROJECT_GUIDE.md` y `CONTEXT_INDEX.md`.
2. Ubicar la spec vigente en `openspec/specs/*/spec.md`.
3. Crear una carpeta de cambio: `openspec/changes/<change-id>/`.
4. Escribir `proposal.md` con intencion, alcance y no alcance.
5. Agregar delta funcional bajo `openspec/changes/<change-id>/specs/`.
6. Agregar `design.md` si cambia arquitectura, datos o contratos.
7. Crear `tasks.md` con pasos verificables.
8. Implementar siguiendo `tasks.md`.
9. Validar con tests o revision documental.
10. Al aprobarse, consolidar el comportamiento en `openspec/specs/*`.

## Adaptar un Proyecto Existente

Si ya tienes un proyecto con codigo, no empieces moviendo archivos ni pidiendo un refactor grande. Primero crea gobierno documental alrededor de lo que ya existe.

Pasos recomendados:

1. Copiar o adaptar `PROJECT_TEMPLATE/` dentro del proyecto existente.
2. Completar `PROJECT_GUIDE.md` con proposito, usuarios, alcance, stack real y limites.
3. Completar `CONTEXT_INDEX.md` apuntando a codigo, docs, specs y decisiones reales.
4. Identificar una o dos capacidades principales que el sistema ya ofrece.
5. Crear `openspec/specs/<capability>/spec.md` para describir comportamiento vigente, no comportamiento deseado.
6. Completar `docs/architecture/system.md` con componentes, datos, integraciones y flujos reales.
7. Registrar decisiones ya vigentes en `decisions/decision_log.md` solo si afectan trabajo futuro.
8. Registrar en `memory/` solo hechos confirmados, restricciones y patrones que conviene recordar.
9. Crear el primer `openspec/changes/<change-id>/` solo para el proximo cambio real.
10. Usar Graphify si el proyecto es grande y no esta claro donde viven las capacidades.

El objetivo de esta adaptacion no es documentar todo el pasado. Es crear suficientes fuentes confiables para que el siguiente cambio ya no dependa de memoria informal.

## Cuando Pedir Refactor al Agente

Pide refactor al agente cuando ya exista una base minima de autoridad:

- la capacidad afectada esta descrita en `openspec/specs/*/spec.md` o en un cambio activo;
- `docs/architecture/system.md` explica los componentes que se tocaran;
- las restricciones relevantes estan en `memory/constraints.md` o decisiones;
- el alcance del cambio esta escrito en `proposal.md`;
- hay una forma de validar, aunque sea revision manual guiada por `tasks.md`.

Todavia no conviene pedir refactor cuando:

- no sabes si el cambio es funcional, tecnico o ambos;
- el comportamiento vigente no esta escrito en ningun lugar;
- el agente tendria que inferir reglas de negocio desde codigo ambiguo;
- no hay acuerdo sobre alcance, riesgos o compatibilidad;
- el repositorio es grande y nadie sabe que areas toca el cambio.

En esos casos, pide primero investigacion, mapa de impacto o borrador de OpenSpec. El refactor viene despues de fijar el marco de verdad.

## Cuando Usar Solo la Estructura OpenSpec

Usa solo la estructura de carpetas y Markdown cuando:

- el proyecto esta empezando;
- no quieres instalar herramientas;
- el equipo prefiere revisar cambios manualmente;
- el cambio es pequeno y basta con estructura clara;
- tu agente no necesita slash commands.

El framework sigue funcionando porque la autoridad esta en los archivos, no en el CLI.

## Cuando Usar OpenSpec CLI

Usa el CLI oficial cuando quieres:

- inicializar estructura OpenSpec automaticamente;
- validar formato de cambios;
- listar cambios activos;
- mostrar detalles de un cambio;
- archivar cambios completados;
- generar integraciones con asistentes compatibles.

El CLI ayuda a operar la estructura; no cambia el reparto de autoridad del framework.

## Instalacion del CLI

Requisitos habituales:

- Node.js 20.19.0 o superior.
- npm, pnpm, yarn o bun.

Instalacion con npm:

```bash
npm install -g @fission-ai/openspec@latest
openspec --version
```

Inicializar en un proyecto:

```bash
cd mi-proyecto
openspec init
```

## Comandos Tipicos

```bash
openspec list
openspec show <change-id>
openspec validate <change-id> --strict
openspec archive <change-id> --yes
openspec update
```

Uso esperado:

- `openspec list`: ver cambios activos.
- `openspec show <change-id>`: revisar un cambio.
- `openspec validate <change-id> --strict`: validar estructura antes de implementar o cerrar.
- `openspec archive <change-id> --yes`: archivar un cambio completado y consolidar specs.
- `openspec update`: refrescar instrucciones/integraciones de agentes si cambia la configuracion.

## Ejemplo Breve

Cambio: agregar exportacion CSV.

1. Persona define: "usuarios internos necesitan exportar solicitudes filtradas".
2. Agente propone `openspec/changes/add-csv-export/proposal.md`.
3. Agente agrega delta en `specs/requests/spec.md`:
   - `Requirement: Exportar solicitudes filtradas`
   - `Scenario: Exportacion con filtros activos`
4. Si requiere nuevo endpoint o job, se agrega `design.md`.
5. `tasks.md` lista implementacion, tests y docs.
6. Se valida:

```bash
openspec validate add-csv-export --strict
```

7. Tras implementar y aprobar:

```bash
openspec archive add-csv-export --yes
```

## Relacion con Otros Documentos

- `PROJECT_GUIDE.md`: explica identidad y alcance general.
- `CONTEXT_INDEX.md`: dice que spec o cambio leer.
- `docs/architecture/system.md`: explica como se implementa tecnicamente.
- `decisions/`: registra decisiones durables que exceden el cambio.
- `memory/`: guarda hechos, restricciones y patrones que afectan trabajo futuro.
- `graphify-out/*`: ayuda a navegar impacto, pero no decide comportamiento.

## Regla Breve

OpenSpec define que debe cambiar. Arquitectura explica como se sostiene. El agente puede redactar y ejecutar, pero la autoridad funcional debe quedar en specs y cambios revisables.
