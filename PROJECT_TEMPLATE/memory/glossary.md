# Glosario

> Opcional. Usar solo cuando el dominio tenga terminos ambiguos.

El glosario evita discusiones repetidas sobre palabras del dominio. No debe convertirse en diccionario general ni duplicar specs.

## Que Contiene

Terminos del dominio que pueden ser ambiguos para humanos o agentes.

## Orden de Uso

Completar solo cuando aparezca ambiguedad real. Consultar antes de nombrar capacidades, escenarios o conceptos de dominio.

## Relacion con Otros Documentos

OpenSpec usa estos terminos en requirements y scenarios. `PROJECT_GUIDE.md` puede usar terminos generales, pero el significado preciso vive aqui si hay ambiguedad.

| Termino | Significado |
|---|---|
| Capability | Area coherente de comportamiento visible para usuarios descrita por una spec OpenSpec. |
| Change | Modificacion propuesta bajo `openspec/changes/*`. |
| Contexto derivado | Ayuda de navegacion generada, como salida de Graphify, sin autoridad. |

## Ejemplo Minimo

```markdown
| Termino | Significado |
|---|---|
| Solicitud | Pedido interno registrado por un usuario. |
| Triage | Revision inicial para clasificar prioridad y responsable. |
| Cierre | Estado final cuando la solicitud tiene resolucion documentada. |
```

## Como Mantenerlo

Agregar terminos solo cuando la ambiguedad pueda afectar decisiones, implementacion o comunicacion. Si un termino es evidente para el equipo, no necesita entrada.

## Regla Breve

El glosario reduce ambiguedad real; no colecciona vocabulario por completitud.
