# SDD

Este archivo existe como puente para equipos que esperan encontrar un `sdd.md`. En la arquitectura OpenSpec-first, no debe ser la fuente principal de comportamiento ni de arquitectura.

## Proposito

Usarlo solo si el proyecto necesita un resumen narrativo de diseno para lectores humanos. La autoridad tecnica estable debe vivir en `docs/architecture/system.md`; el comportamiento funcional debe vivir en OpenSpec.

## Que Contiene

Un resumen narrativo opcional de diseno. Debe enlazar fuentes canonicas y no competir con ellas.

## Orden de Uso

Completar solo despues de tener arquitectura estable suficiente. Si no aporta claridad adicional, mantenerlo como puente breve.

## Relacion con Otros Documentos

`docs/architecture/system.md` manda para arquitectura. OpenSpec manda para comportamiento. ADRs explican decisiones durables.

## Uso Recomendado

- Resumir decisiones de diseno en lenguaje accesible.
- Enlazar a `docs/architecture/system.md` para detalles tecnicos.
- Enlazar a OpenSpec para reglas funcionales.
- Mantenerlo corto si no aporta algo distinto.

## Ejemplo Minimo

```markdown
Este proyecto usa una API interna y una base SQLite local. La arquitectura detallada vive en `docs/architecture/system.md`. Las reglas funcionales de solicitudes viven en `openspec/specs/requests/spec.md`.
```

## No Usar Para

- Reemplazar specs OpenSpec.
- Guardar decisiones durables que pertenecen a ADRs.
- Duplicar la arquitectura completa.
- Archivar historia antigua como si fuera vigente.

## Regla Breve

Si este archivo no aporta una lectura humana distinta, puede quedar minimo y enlazado a las fuentes canonicas.
