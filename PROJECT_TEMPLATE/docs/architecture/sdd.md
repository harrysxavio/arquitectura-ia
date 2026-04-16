# SDD

Este archivo existe como puente para equipos que esperan encontrar un `sdd.md`. En la arquitectura OpenSpec-first, no debe ser la fuente principal de comportamiento ni de arquitectura.

## Proposito

Usarlo solo si el proyecto necesita un resumen narrativo de diseño para lectores humanos. La autoridad tecnica estable debe vivir en `docs/architecture/system.md`; el comportamiento funcional debe vivir en OpenSpec.

## Uso Recomendado

- Resumir decisiones de diseño en lenguaje accesible.
- Enlazar a `docs/architecture/system.md` para detalles tecnicos.
- Enlazar a OpenSpec para reglas funcionales.
- Mantenerlo corto si no aporta algo distinto.

## No Usar Para

- Reemplazar specs OpenSpec.
- Guardar decisiones durables que pertenecen a ADRs.
- Duplicar la arquitectura completa.
- Archivar historia antigua como si fuera vigente.

## Regla Breve

Si este archivo no aporta una lectura humana distinta, puede quedar minimo y enlazado a las fuentes canonicas.
