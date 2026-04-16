# Plantilla ADR

Un ADR registra una decision arquitectonica durable. Debe explicar contexto, decision y consecuencias sin convertirse en ensayo largo.

## Proposito

Guardar el razonamiento de una decision estructural para que no dependa de memoria oral o chats.

## Que Contiene

Estado, contexto, decision, consecuencias y referencias. Puede incluir alternativas si ayudan a entender la compensacion.

## Orden de Uso

Crear un ADR despues de identificar una decision durable y antes de implementar cambios amplios que dependan de ella.

## Relacion con Otros Documentos

`decision_log.md` indexa el ADR. OpenSpec contiene comportamiento; arquitectura refleja la decision tecnica resultante.

## Estado

Propuesta | Aceptada | Reemplazada

## Contexto

Que problema, restriccion o compensacion requiere una decision arquitectonica durable?

## Decision

Que se aprobo?

## Consecuencias

Que cambia para implementacion, operacion, costo, riesgo o decisiones futuras?

## Referencias

- Cambio OpenSpec:
- Specs relacionadas:

## Ejemplo Minimo

```markdown
# ADR 0001 - Usar SQLite inicialmente

## Estado

Aceptada

## Contexto

El proyecto necesita persistencia local simple antes de definir infraestructura productiva.

## Decision

Usar SQLite para la primera version.

## Consecuencias

- Menor costo operativo inicial.
- Migracion futura posible si crecen concurrencia o integraciones.
- La arquitectura debe aislar acceso a datos en un modulo propio.

## Referencias

- Cambio OpenSpec: `openspec/changes/add-request-storage/`
- Specs relacionadas: `openspec/specs/requests/spec.md`
```

## Guia de Escritura

Usar un ADR cuando una decision afecta estructura, costo, seguridad, integraciones, datos o forma de operar. No usarlo para tareas de implementacion pequenas ni para reglas funcionales que pertenecen a OpenSpec.

El texto debe responder:

- Que problema obligo a decidir?
- Que alternativas existian?
- Por que se eligio esta opcion?
- Que costo o riesgo aceptamos?
- Que documentos quedan afectados?

## Regla Breve

Un ADR debe ayudar a no olvidar por que una decision parecia correcta.
