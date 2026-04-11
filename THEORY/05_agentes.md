# Módulo 5 — Ejecución Operativa con Agentes

## 1. Principio Operativo

> El usuario NO ejecuta tareas directamente. El sistema las traduce.

El usuario expresa intención → El sistema clasifica → El manager orquesta → El agente ejecuta → Se revisa → Se actualiza memoria si corresponde.

## 2. Flujo Oficial de Ejecución

1. Usuario expresa intención.
2. Manager interpreta y clasifica tipo de tarea.
3. Define contexto mínimo necesario.
4. Decide si necesita contexto dirigido.
5. Selecciona skill o workflow.
6. Asigna agente responsable.
7. Ejecuta.
8. Evalúa resultado.
9. Decide si actualizar memoria o decisiones.

## 3. Agentes Oficiales

### 3.1 Manager (Orquestador)
- Interpreta intención, clasifica tarea, selecciona contexto.
- Elige agente, activa skill o workflow, controla ejecución.
- Lee SIEMPRE: `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `active_task.md`.
- **No** implementa código, no debuggea directamente, no revisa en profundidad.

### 3.2 Coder (Ejecutor Técnico)
- Implementa código, modifica archivos, refactoriza, integra componentes.
- Lee: contexto mínimo + skill técnica + archivos específicos.
- **No** decide arquitectura, no redefine reglas, no interpreta intención global.

### 3.3 Reviewer (Control de Calidad)
- Valida código, detecta errores, evalúa impacto, revisa coherencia.
- Revisa: cambios del coder, integración con sistema, cumplimiento de reglas.
- **No** implementa cambios (solo sugiere), no redefine el plan.

### 3.4 Debugger (Analista de Fallos)
- Investiga errores, genera hipótesis, identifica causa raíz, propone soluciones.
- Usa: logs, código afectado, `known_issues.md`, contexto dirigido.
- **No** implementa directamente, no redefine arquitectura.

## 4. Regla Estructural

> Si algo puede resolverse con una skill o workflow, NO debe ser un agente.

## 5. Subagentes (Nivel Avanzado)

Los subagentes son **opcionales** y solo en etapa avanzada.

**Cuándo sí**: repos grandes, tareas paralelizables, research complejo, validaciones especializadas.

**Cuándo no**: tareas simples, trabajo diario, debugging básico, implementaciones directas.

**Riesgos**: sobreingeniería, mayor consumo de tokens, complejidad de coordinación, duplicación de funciones.

## 6. Relación Agentes ↔ Skills ↔ Workflows

| Elemento | Rol |
|----------|-----|
| Agente | Ejecuta |
| Skill | Guía cómo ejecutar |
| Workflow | Define secuencia |

**Ejemplo**: Tarea "crear endpoint" → Manager clasifica como desarrollo backend → Activa `skill/python-backend.md` + `workflow/implementation.md` → Asigna Coder.

## 7. Estrategia de Modelos por Agente

| Agente | Modelo base | Modelo premium | Observación |
|--------|------------|----------------|-------------|
| Manager | GPT-4.1-mini / Qwen | GPT-5 / Claude Opus | No necesita modelo caro si el contexto está bien estructurado |
| Coder | GPT-4.1 / DeepSeek | GPT-5 / Claude Sonnet | El 80% del código NO necesita modelo premium |
| Reviewer | GPT-4.1 / Claude Sonnet | Claude Opus / GPT-5 | Donde más se justifica subir calidad |
| Debugger | Claude Sonnet | GPT-5 / Claude Opus | Debugging complejo es el caso más caro pero más crítico |

## 8. Reglas de Optimización de Costos

1. No todos los agentes usan el mismo modelo.
2. Escalar modelo solo si falla el resultado.
3. El problema casi nunca es el modelo → **es el contexto**.

Impacto estimado: ↓ 40–70% costo en tokens, ↑ calidad promedio, ↓ retrabajo.

## 9. Anti-Patrones Críticos

- ❌ Usar un solo agente para todo → sobrecarga, peor calidad.
- ❌ Cargar todo el repo → alto costo, respuestas difusas.
- ❌ No usar workflows → inconsistencia, repetición de errores.
- ❌ Crear demasiados agentes → sistema inmanejable.
