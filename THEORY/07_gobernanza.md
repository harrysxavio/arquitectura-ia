# Módulo 7 — Gobernanza, Mantenimiento y Evolución del Framework

## 1. Principio Rector

> El problema no es construir el sistema. El problema es evitar que se degrade.

## 2. Qué es Gobernanza

Gobernanza = reglas que aseguran que el sistema siga siendo usable. Incluye:
- Orden del proyecto.
- Control de documentación.
- Uso correcto de agentes.
- Uso eficiente de contexto.
- Registro de decisiones.
- Disciplina en ejecución.

## 3. Componentes de Gobernanza

### 3.1 Fuente de Verdad Única
Todo lo operativo vive en el repo. Nada crítico queda fuera.

### 3.2 Estructura Obligatoria
Siempre deben existir: `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `active_task.md`, `decision_log.md`, `project_facts.md`. Si falta uno, el sistema empieza a fallar.

### 3.3 Regla de No Duplicación
Una idea → un solo lugar. Duplicación produce confusión, decisiones contradictorias y pérdida de coherencia.

### 3.4 Registro de Decisiones
Toda decisión relevante debe registrarse: qué se decidió, por qué, e impacto.

## 4. Mantenimiento del Sistema

### Cuándo Mantener
- Al cerrar una tarea importante.
- Cuando el sistema se siente confuso.
- Cuando el agente responde mal.
- Cuando hay duplicación.
- Cuando el repo crece.

### Checklist de Mantenimiento
- ¿Hay duplicados?
- ¿Hay archivos obsoletos?
- ¿El CONTEXT_INDEX está actualizado?
- ¿Las decisiones están registradas?
- ¿Hay contexto comprimido donde debería?
- ¿Las tareas activas están claras?

## 5. Gestión de Documentación

La documentación debe **ayudar a ejecutar**, no solo explicar. Errores comunes: documentar demasiado, sin estructura, o sin uso real.

## 6. Gestión de Agentes

No crear agentes innecesarios. Solo crear uno si tiene función clara, no duplica otro, reduce errores reales y aporta eficiencia. No crearlo por comodidad, moda o porque "suena bien".

## 7. Gestión de Skills y Workflows

- Skills: actualizar cuando hay errores repetidos o se detecta mejor forma de trabajar.
- Workflows: revisar cuando el proceso cambia o hay inconsistencias.
- **Regla**: Si algo se repite 3 veces → convertirlo en skill o workflow.

## 8. Evolución del Framework

**Regla clave**: Evolucionar sin romper lo existente.

Proceso: Identificar problema real → Probar solución pequeña → Validar impacto → Integrar → Documentar.

**No hacer**: Cambiar todo de golpe, reestructurar sin necesidad, introducir herramientas sin uso claro.

## 9. Gestión de Modelos de IA

- No usar siempre el mejor modelo.
- Tareas simples → modelos baratos. Tareas complejas → modelos premium.
- Escalar solo si falla el resultado.
- Si estás pagando mucho → el problema es de contexto, no de modelo.

## 10. Manejo de Deuda Técnica

Decisiones que funcionan hoy pero generan problemas mañana. Registrar en `decisions/`, no ignorarla, planificar refactor.

## 11. Métricas de Salud del Framework

El sistema está sano si:
- Encuentras rápido la información.
- Los agentes responden bien.
- No necesitas prompts largos.
- No hay duplicación.
- Las decisiones están claras.
- El trabajo fluye sin fricción.

## 12. Anti-Patrones Críticos

- ❌ Sistema crece sin orden → gobernanza estricta.
- ❌ Demasiados documentos → consolidar.
- ❌ Demasiados agentes → simplificar.
- ❌ Dependencia de prompts largos → mejorar contexto.
- ❌ No registrar decisiones → disciplina.
