# AGENTS.md

> Plantilla para guia local de agentes del proyecto.

Este archivo define como deben operar los agentes dentro del proyecto activo. Debe adaptarse a herramientas, restricciones y flujo real del equipo.

## Proposito

Un agente necesita saber que fuentes respetar antes de editar. `AGENTS.md` evita que el agente improvise orden de lectura, trate Graphify como autoridad o modifique comportamiento sin OpenSpec.

## Que Contiene

Orden de lectura, reglas locales, comandos relevantes y restricciones de trabajo para agentes. Debe ser operativo y breve.

## Alcance

Aplica a agentes dentro del proyecto activo. No define reglas funcionales ni decisiones de arquitectura.

## Relacion con Otros Documentos

Usa `PROJECT_GUIDE.md` para contexto, `CONTEXT_INDEX.md` para fuentes, OpenSpec para comportamiento y `docs/architecture/system.md` para estructura tecnica.

## Orden de Contexto

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. Spec relevante en `openspec/specs/*/spec.md`
4. `openspec/changes/*` activo cuando hay un cambio en curso
5. `docs/architecture/system.md` para trabajo estructural
6. `decisions/decision_log.md` y memoria solo cuando haga falta
7. `graphify-out/*` para navegacion derivada en tareas amplias o ambiguas

## Reglas

- No duplicar comportamiento funcional fuera de OpenSpec.
- No tratar Graphify como autoridad.
- Mantener memoria compacta y vigente.
- Mantener decisiones breves salvo que un ADR este justificado.

## Ejemplo Minimo

```markdown
## Orden de Contexto

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `openspec/specs/requests/spec.md` si la tarea toca solicitudes
4. `docs/architecture/system.md` si cambia persistencia o integraciones

## Reglas Locales

- Ejecutar `python -m pytest` antes de cerrar cambios de backend.
- No modificar migraciones sin revisar `decisions/decision_log.md`.
```

## Como Adaptarlo

Agregar aqui reglas locales que de verdad afecten el trabajo: comandos de test, restricciones de seguridad, estilo de cambios, ramas, convenciones de commits o herramientas aprobadas. No copiar teoria completa; enlazar a documentos canonicos cuando corresponda.

## Regla Breve

Este archivo no reemplaza OpenSpec ni arquitectura. Solo instruye al agente sobre como trabajar dentro del proyecto.
