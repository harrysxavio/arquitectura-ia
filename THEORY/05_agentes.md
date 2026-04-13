# Modulo 5 - Ejecucion Operativa con Agentes

## 1. Principio Operativo

El usuario expresa una intencion. El sistema la convierte en ejecucion disciplinada.

Flujo conceptual:

1. Usuario expresa intencion.
2. Manager clasifica tipo y complejidad.
3. Manager usa `OPERACION/CONTEXT_ROUTER.md` para decidir contexto minimo.
4. Se asigna agente responsable.
5. El agente ejecuta o analiza dentro del alcance.
6. Reviewer valida cuando hay impacto funcional, tecnico o estructural.
7. Se actualiza memoria o decisiones si corresponde.

La meta no es tener mas agentes. La meta es que cada rol reduzca ambiguedad.

## 2. Agentes Oficiales

Solo existen cuatro agentes base:

- Manager,
- Coder,
- Reviewer,
- Debugger.

Los contratos detallados viven en `OPERACION/AGENTS/*.md`. Este modulo explica el razonamiento detras de esos roles.

## 3. Manager

### Funcion

El Manager traduce intencion a plan operativo. No implementa codigo ni revisa diffs a profundidad.

### Responsabilidades

- Interpretar la intencion del usuario.
- Clasificar tipo de tarea: `bug`, `feature`, `refactor`, `arquitectura`, `review`, `testing`, `deploy`, `research`, `docs` o `memoria`.
- Clasificar nivel: 1, 2 o 3.
- Elegir contexto segun `OPERACION/CONTEXT_ROUTER.md`.
- Seleccionar agente, skill o workflow.
- Detectar documentos canonicos faltantes.
- Decidir siguiente paso concreto.

### Porque existe

Sin Manager, el agente tiende a leer demasiado, saltar a implementacion o confundir tareas simples con tareas arquitectonicas.

## 4. Coder

### Funcion

El Coder implementa cambios tecnicos con precision y minimo ruido.

### Responsabilidades

- Modificar archivos dentro del alcance.
- Respetar spec, SDD, decisiones y memoria cuando apliquen.
- Mantener coherencia con patrones existentes.
- Validar con tests, build o revision manual segun riesgo.
- Reportar archivos tocados, supuestos y riesgos remanentes.

### Limites

- No inventa reglas de negocio.
- No cambia arquitectura sin SDD, decision registrada o aprobacion explicita.
- No usa `PROJECT_TEMPLATE/` como verdad de proyecto activo.

### Porque existe

Separar implementacion de orquestacion evita que el mismo rol decida arquitectura, contexto, scope y codigo a la vez.

## 5. Reviewer

### Funcion

El Reviewer valida calidad, coherencia, riesgos y cumplimiento del alcance.

### Responsabilidades

- Revisar diff o archivos cambiados.
- Ordenar hallazgos por severidad.
- Evaluar riesgos funcionales, tecnicos y de seguridad.
- Confirmar si la evidencia de testing es suficiente.
- Dar veredicto: `APROBADO` o `NO APROBADO` cuando aplique.

### Limites

- No redefine el objetivo de negocio.
- No exige `spec.md` para una tarea realmente Nivel 1.
- No convierte una revision en rediseno amplio sin justificacion.

### Porque existe

El Coder puede optimizar por resolver. El Reviewer optimiza por no romper, no duplicar y no degradar el sistema.

## 6. Debugger

### Funcion

El Debugger investiga fallos con metodo y convierte incertidumbre en evidencia.

### Responsabilidades

- Describir sintoma observable.
- Revisar logs, traces o tests fallidos.
- Formular hipotesis.
- Aislar causa raiz.
- Proponer correccion.
- Recomendar pruebas.
- Indicar si corresponde actualizar `memory/known_issues.md` o decisiones.

### Limites

- No asume causas sin evidencia.
- No redisenia el sistema para un bug puntual.
- No implementa directamente el fix final si el contrato del flujo lo separa.

### Porque existe

Debuggear requiere metodo distinto a implementar. Separarlo evita fixes superficiales y cambios arquitectonicos innecesarios.

## 7. Skills, Workflows y Subagentes

| Elemento | Funcion | Cuando usarlo |
|---|---|---|
| Agente | Rol responsable | Cuando hay responsabilidad estable y limites claros |
| Skill | Guia de como ejecutar | Cuando una tecnica se repite o requiere instrucciones especializadas |
| Workflow | Secuencia de pasos | Cuando una operacion tiene orden recurrente |
| Subagente | Delegacion opcional avanzada | Cuando reduce contexto o permite paralelismo real |

Regla: si una necesidad puede resolverse con skill, workflow o checklist, no crear un agente nuevo.

Subagentes solo se justifican si:

- reducen carga de contexto,
- permiten trabajo paralelo real,
- devuelven resultados comprimidos,
- no duplican un agente base,
- la tarea no es simple ni local.

## 8. Contexto por Agente

| Agente | Contexto minimo |
|---|---|
| Manager | Intencion del usuario, contexto base, router y constraints relevantes |
| Coder | Tarea activa, contexto del router, archivos afectados, spec/SDD si aplica |
| Reviewer | Tarea activa, diff, evidencia de testing, fuentes canonicas aplicables |
| Debugger | Sintoma, logs/tests, codigo afectado, `known_issues.md` si aplica |

Graphify entra en tareas Nivel 3, multi-modulo, ambiguas o estructurales. No entra por defecto en cambios locales obvios.

## 9. Modelos por Rol

| Rol | Modelo sugerido | Cuando escalar |
|---|---|---|
| Manager | Barato o medio | Ambiguedad alta o decision estrategica |
| Coder | Medio | Refactor amplio, contratos delicados o baja confianza |
| Reviewer | Medio/alto | Riesgo funcional, seguridad o arquitectura |
| Debugger | Medio/alto | Fallos intermitentes, multi-modulo o causa raiz incierta |

No todos los agentes necesitan el mejor modelo. El primer ajuste debe ser contexto y alcance, no costo.

## 10. Anti-Patrones

- Un solo agente decide todo, implementa todo y se revisa a si mismo.
- Cargar todo el repo por defecto.
- Crear agentes por nombre atractivo, no por funcion.
- Usar subagentes para tareas simples.
- Pedir al usuario informacion que ya vive en memoria oficial.
- Usar `THEORY/` como instrucciones de runtime.

## 11. Regla Final

Los agentes no son personajes decorativos. Son contratos de responsabilidad para que el trabajo sea trazable, acotado y revisable.
