# Arquitectura del Sistema

> Arquitectura tecnica estable para la plantilla de proyecto. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Describe la forma tecnica estable del proyecto: componentes, limites, datos, integraciones y estrategia de validacion.

Este documento responde "como esta construido el sistema?". Debe ser suficientemente claro para que una persona tecnica entienda componentes, responsabilidades y limites sin leer todo el codigo.

No debe duplicar reglas funcionales. Si una regla describe comportamiento aprobado, enlazar a OpenSpec.

## Que Contiene

Componentes, limites, contratos, datos, integraciones y validacion tecnica. Debe explicar decisiones tecnicas vigentes, no tareas futuras.

## Orden de Uso

Completar despues de `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y la primera spec funcional. Actualizar cuando cambian componentes, datos, integraciones o contratos.

## Relacion con Otros Documentos

OpenSpec define comportamiento; este documento define estructura. ADRs explican decisiones estructurales durables. Memoria guarda restricciones y patrones compactos.

## Fuentes Estables

- Comportamiento funcional: `openspec/specs/*/spec.md`
- Cambios activos: `openspec/changes/*`
- Decisiones: `decisions/decision_log.md` y ADRs
- Memoria compacta: `memory/facts.md`, `memory/constraints.md`, `memory/patterns.md`

## Componentes

| Componente | Rol |
|---|---|
| Aplicacion | Por definir |
| Datos | Por definir |
| Tests | Por definir |
| Herramientas | Por definir |

Completar la tabla con componentes reales. Cada fila debe explicar responsabilidad, no solo repetir el nombre de una carpeta.

## Ejemplo Minimo de Componentes

```markdown
| Componente | Rol |
|---|---|
| `api/` | Expone endpoints internos para solicitudes. |
| `domain/requests.py` | Contiene reglas de dominio implementadas desde OpenSpec. |
| `storage/` | Persiste solicitudes en SQLite. |
| `tests/` | Valida comportamiento y contratos principales. |
```

## Limites y Contratos

Describir que responsabilidades pertenecen a cada componente y que contratos los conectan. Un contrato puede ser una interfaz, un formato de datos, un endpoint, una cola, un archivo o una convencion de llamada.

Si un contrato define comportamiento de usuario, enlazar a OpenSpec.

## Datos y Estado de Ejecucion

Documentar datos de ejecucion aqui solo cuando sean arquitectura estable. Los datos de ejecucion no son automaticamente canonicos.

Indicar que datos son persistentes, temporales, derivados o solo de ejemplo. Esta distincion evita que una muestra local se convierta en autoridad accidental.

## Integraciones

Listar integraciones externas cuando existan: APIs, colas, servicios, proveedores, herramientas de automatizacion o almacenamiento. Si no hay integraciones, decirlo explicitamente.

## Validacion

Listar los comandos o revisiones que prueban que la arquitectura sigue funcionando.

La validacion puede incluir tests, lint, chequeos de contratos, ejecuciones manuales o revision documental. Debe ser proporcional al riesgo del proyecto.

## Regla

No duplicar requirements funcionales aqui. Enlazar a OpenSpec en su lugar.

## Ejemplo Minimo de Validacion

```bash
python -m pytest
python -m mypy src
```

```markdown
La arquitectura se considera valida si pasan tests unitarios, los contratos principales no cambian sin ADR y la spec OpenSpec relevante sigue enlazada desde los componentes de dominio.
```

## Checklist de Calidad

- Los componentes tienen responsabilidades claras.
- Los limites entre componentes se entienden.
- Los datos y estado de ejecucion no se confunden con autoridad funcional.
- La validacion esta descrita con comandos o criterios concretos.
