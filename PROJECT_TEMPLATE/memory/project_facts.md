# Hechos del Proyecto

Este archivo existe como puente para proyectos que ya usaban `project_facts.md`. En la arquitectura OpenSpec-first, la fuente recomendada es `memory/facts.md`.

## Proposito

Usarlo solo si se necesita compatibilidad temporal con herramientas o agentes que esperan esta ruta. El contenido canonico de hechos confirmados debe mantenerse en `memory/facts.md`.

## Que Contiene

Idealmente solo un enlace a `memory/facts.md`. No debe mantener hechos duplicados.

## Orden de Uso

Usarlo al migrar desde una estructura anterior o mientras una herramienta externa aun espera esta ruta. Retirarlo cuando ya no haga falta compatibilidad.

## Relacion con Otros Documentos

`memory/facts.md` es la fuente canonica. Este archivo es puente, no memoria paralela.

## Uso Recomendado

- Enlazar a `memory/facts.md`.
- Evitar duplicar hechos.
- Mantenerlo breve hasta retirar la compatibilidad.

## Ejemplo Minimo

```markdown
Los hechos canonicos del proyecto viven en `memory/facts.md`.
```

## Regla Breve

No mantener dos memorias paralelas. Si este archivo existe, debe apuntar a la memoria canonica.
