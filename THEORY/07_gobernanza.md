# Modulo 7 - Gobernanza, Mantenimiento y Evolucion del Framework

## 1. Principio Rector

El problema no es construir el sistema. El problema es evitar que se degrade.

Gobernanza es el conjunto de reglas que mantiene usable el framework cuando crecen los proyectos, las herramientas, los agentes y la documentacion.

## 2. Que Gobierna el Framework

La gobernanza cubre:

- estructura del repo,
- separacion entre framework y proyecto activo,
- control de fuentes canonicas,
- uso de contexto,
- memoria persistente,
- decisiones,
- agentes,
- herramientas,
- delivery,
- conocimiento satelite.

## 3. Autoridad Documental

| Tipo de informacion | Fuente oficial |
|---|---|
| Como navegar este framework | `README.md` |
| Que contexto cargar | `OPERACION/CONTEXT_ROUTER.md` |
| Reglas ejecutables | `OPERACION/CONSTRAINTS/*.md` |
| Roles de agentes | `OPERACION/AGENTS/*.md` |
| Explicacion pedagogica | `THEORY/*.md` |
| Politica Graphify | `GRAPHIFY/GRAPHIFY_POLICY.md` |
| Contrato Graphify | `GRAPHIFY/OUTPUT_CONTRACT.md` |
| Politica Obsidian | `SATELLITE/OBSIDIAN_POLICY.md` |
| Politica NotebookLM | `SATELLITE/NOTEBOOKLM_POLICY.md` |
| Molde de proyecto | `PROJECT_TEMPLATE/` |
| Proyecto activo real | Repo instanciado desde `PROJECT_TEMPLATE/` |

En un proyecto activo, la autoridad pasa a sus documentos canonicos: `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `tasks/`, `decisions/`, `memory/`, `docs/` y `graphify-out/` como derivado.

## 4. Reglas de No Degradacion

### 4.1 No duplicar fuentes

Una idea debe vivir en un solo lugar canonico. Si se copia en varios documentos, tarde o temprano se contradice.

Ejemplos:

- Una decision vive en `decisions/decision_log.md`.
- Un hecho vigente vive en `memory/project_facts.md`.
- Una restriccion vive en `memory/constraints.md`.
- Una regla operativa del framework vive en `OPERACION/CONSTRAINTS/`.

### 4.2 No confundir plantilla con proyecto

`PROJECT_TEMPLATE/` no contiene verdad operativa. Si un agente lo trata como proyecto activo, puede inventar tareas, decisiones o memoria falsas.

### 4.3 No convertir teoria en runtime

`THEORY/` explica el sistema. Para ejecucion tecnica, gana `OPERACION/CONTEXT_ROUTER.md` y los constraints.

### 4.4 No dejar conocimiento util fuera del repo

Si una nota de Obsidian o sintesis de NotebookLM cambia una decision, restriccion o patron, debe volver al repo en el archivo canonico correspondiente.

### 4.5 No usar outputs derivados como autoridad

Graphify ayuda a leer, pero no reemplaza spec, SDD, decision log ni memoria. Si esta stale, se verifica o regenera antes de usarlo para decisiones estructurales.

## 5. Mantenimiento

Mantener el sistema cuando:

- se cierra una tarea importante,
- el agente empieza a responder con ambiguedad,
- aparecen documentos duplicados,
- el repo cambia de estructura,
- se agrega una herramienta,
- se detecta un patron repetido,
- Graphify queda desactualizado,
- el proyecto crece de Nivel 1 a Nivel 2 o 3.

Checklist:

- Esta actualizado `CONTEXT_INDEX.md`?
- La tarea activa sigue reflejando el trabajo real?
- Las decisiones importantes estan registradas?
- Hay hechos nuevos para `project_facts.md`?
- Hay restricciones nuevas para `constraints.md`?
- Hay problemas que deban ir a `known_issues.md`?
- Hay patrones repetidos para `patterns.md`?
- Graphify sigue vigente?
- Hay docs que nadie usa?
- Hay contenido en Obsidian o NotebookLM que debe volver al repo?

## 6. Evolucion del Stack

Agregar herramientas solo mediante problema real:

1. Identificar friccion o necesidad concreta.
2. Confirmar que no se resuelve con una herramienta existente.
3. Probar en pequeno.
4. Documentar que reemplaza o complementa.
5. Registrar decision si afecta al proyecto.
6. Actualizar `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, SDD o constraints segun corresponda.

No incorporar herramientas por tendencia, curiosidad o promesa abstracta.

## 7. Evolucion de Agentes, Skills y Workflows

Crear un agente nuevo es excepcional. Antes de hacerlo, preguntar:

- Tiene responsabilidad estable?
- Tiene limites claros?
- No duplica Manager, Coder, Reviewer o Debugger?
- No basta con una skill?
- No basta con un workflow?
- Reduce errores reales?

Regla practica: si una operacion se repite tres veces, evaluar convertirla en skill o workflow antes de crear un agente.

## 8. Gestion de Deuda Tecnica

La deuda tecnica no debe esconderse en conversaciones. Debe registrarse como:

- decision con tradeoff en `decisions/decision_log.md`,
- problema conocido en `memory/known_issues.md`,
- restriccion en `memory/constraints.md`,
- patron a corregir en `memory/patterns.md`,
- item de tarea si requiere accion inmediata.

Una deuda aceptada puede ser valida. Una deuda no registrada se convierte en confusion.

## 9. Metricas de Salud

El framework esta sano si:

- la informacion se encuentra rapido,
- los agentes no necesitan prompts largos,
- el contexto cargado es pequeno y suficiente,
- no hay duplicacion documental,
- las decisiones son trazables,
- el stack tiene justificacion,
- Graphify se usa para impacto estructural y no para microcambios,
- Obsidian y NotebookLM ayudan sin gobernar,
- el proyecto puede retomarse despues de una pausa.

## 10. Anti-Patrones

- Cambiar toda la estructura de golpe.
- Agregar documentos sin funcion de consulta.
- Mantener duplicados por respeto historico.
- Usar `PROJECT_TEMPLATE/` como proyecto activo.
- Tratar `THEORY/` como constraint operativo.
- Crear agentes innecesarios.
- Escalar modelo cuando el problema es contexto.
- Desplegar antes de validar uso.
- Dejar decisiones importantes en chat.

## 11. Regla Final

La gobernanza no existe para hacer el sistema pesado. Existe para que el sistema siga siendo liviano cuando el trabajo crece.
