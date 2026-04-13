# CONSTRAINTS: Flujo y Ejecucion

## Flujo Base

1. El usuario expresa una intencion.
2. El Manager clasifica tipo y complejidad.
3. El Manager usa `OPERACION/CONTEXT_ROUTER.md` para definir el contexto minimo suficiente.
4. El agente responsable ejecuta o analiza.
5. Reviewer valida cuando hay impacto funcional, tecnico o estructural.
6. Se actualiza memoria o decisiones si corresponde.

## Micro-Specs

> [!NOTE]
> El nivel de la tarea define cuanta especificacion y validacion se exige.

- Nivel 1: requiere tarea clara y archivo afectado. No requiere `spec.md`.
- Nivel 2: requiere `docs/product/spec.md` cuando hay regla funcional, usuario, contrato o criterio de aceptacion.
- Nivel 3: requiere `docs/architecture/sdd.md`, decisiones relevantes y Graphify vigente si existe.

## Skills y Workflows

- Skills y workflows son recomendados para tareas repetibles.
- No bloquean el arranque de un proyecto si aun no existen.
- Si una operacion se repite tres veces, debe evaluarse convertirla en skill o workflow.
- Si una skill puede resolver la necesidad, no crear un agente nuevo.

## Reglas de Ejecucion

> [!WARNING]
> No iniciar cambios fuera del alcance declarado ni cambiar arquitectura sin SDD, decision o aprobacion explicita.

- Registrar decisiones relevantes en `decisions/decision_log.md`.
- En tareas Nivel 2 o 3, no cerrar sin validacion suficiente.
- No usar `PROJECT_TEMPLATE/` como fuente de verdad del proyecto activo.

## Validacion

El cierre debe indicar:

- que se cambio o decidio,
- como se valido,
- que documentos canonicos deben actualizarse,
- que riesgos quedan abiertos.
