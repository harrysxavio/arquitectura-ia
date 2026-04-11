# Módulo 1 — Principios Rectores y Marco de Decisión

## 1. Propósito del Framework

Este framework resuelve un problema concreto: trabajar con múltiples herramientas de IA sin estructura produce desorden, gasto innecesario, prompts pobres, duplicación documental y resultados inconsistentes.

El propósito no es "tener más herramientas". Es construir un sistema donde el usuario pueda trabajar con claridad, bajo desperdicio de contexto, buena trazabilidad y una ruta de crecimiento realista.

El framework permite:
- Programar con apoyo de IA sin improvisación constante.
- Entender repositorios grandes con menos fricción.
- Ejecutar cambios con criterio.
- Automatizar tareas repetitivas.
- Investigar documentación extensa.
- Desplegar aplicaciones y servicios.
- Mantener memoria útil del proyecto.
- Cambiar de herramienta o proveedor sin romper la lógica del sistema.

## 2. Principio Rector Oficial

> La calidad del resultado no debe depender del modelo. Debe depender del sistema.

Un modelo menos potente rinde bien si:
- Recibe una tarea bien acotada.
- Accede solo al contexto que necesita.
- Trabaja bajo reglas explícitas.
- No necesita adivinar la organización del proyecto.
- Existe una fuente de verdad clara.
- Las decisiones previas ya están registradas.

Incluso un modelo premium rinde mal si el proyecto está desordenado y la documentación se contradice.

## 3. Problemas que Resuelve

| Problema | Solución del framework |
|----------|----------------------|
| Exceso de contexto | Cargar contexto por necesidad, no por disponibilidad |
| Prompts pobres | El sistema traduce intención a ejecución |
| Caos documental | Documentación separada por función, sin duplicación |
| Pérdida de memoria | Decisiones registradas en `decision_log.md` |
| Uso arbitrario de herramientas | Toda incorporación debe justificarse |
| Dificultad para retomar proyectos | El sistema permite retomar sin reconstruir contexto |
| Dependencia del usuario experto | Principiantes pueden operar con orden creciente |

## 4. Qué NO Es Este Framework

- No es una colección de herramientas de moda.
- No depende de un proveedor específico.
- No es un catálogo de prompts sueltos.
- No es un sistema multiagente inflado.
- No es un reemplazo de criterio técnico.
- No intenta meter todo lo "potencialmente útil" desde el inicio.

## 5. Decisiones Oficiales de Simplificación

### 5.1 Un solo agente principal por proyecto
Se permite Cline o Codex, pero no ambos gobernando el mismo proyecto simultáneamente.

### 5.2 Pocos agentes reales
Solo 4 agentes base: Manager, Coder, Reviewer, Debugger. Todo lo demás se resuelve con skills o workflows.

### 5.3 Contexto mínimo por defecto
El sistema trabaja primero con guía, índice y tarea activa. Cargar más contexto es una decisión, no una costumbre.

### 5.4 Una sola fuente de verdad por tipo de información
- Lo activo → `tasks/`
- Las decisiones → `decisions/`
- Los hechos → `memory/`
- La guía estructural → `PROJECT_GUIDE.md`
- La ruta de consulta → `CONTEXT_INDEX.md`

### 5.5 Subagentes como capacidad opcional avanzada
Los subagentes no son base obligatoria. Solo se justifican si reducen carga mental real, evitan leer contexto innecesario y devuelven resultados comprimidos. Si una necesidad se resuelve con skill o workflow, no debe crearse un subagente.

## 6. Criterio de Éxito

El framework está bien implementado si:
- El usuario no necesita recordar todo para retomar un proyecto.
- El sistema no depende de un solo proveedor.
- El contexto cargado es pequeño pero suficiente.
- Las decisiones ya no se pierden.
- El trabajo diario es más rápido y menos caótico.
- El costo del razonamiento baja.
- El sistema puede crecer sin rehacerse entero.

## 7. Cierre

> No se debe construir un proyecto donde la IA tenga que adivinar el sistema. Se debe construir un sistema donde la IA solo tenga que ejecutar bien.
