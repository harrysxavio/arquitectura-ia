# SDD - Mesa Interna de Soporte Operativo

> Ejemplo rellenado. Diseno tecnico minimo e ilustrativo.

## Contexto

Este ejemplo no busca entregar una aplicacion completa. La arquitectura prioriza documentacion canonica y trazabilidad antes de automatizacion.

`src/sample_flow.py` existe solo para mostrar como una regla funcional podria convivir con codigo minimo. No reemplaza `docs/product/spec.md`.

## Referencias

- Spec: `docs/product/spec.md`
- Decision: `decisions/decision_log.md`
- ADR: `decisions/adr/0001-documentar-triage-en-markdown.md`

## Decision Tecnica

Mantener el flujo principal en Markdown y usar codigo solo como demostracion de apoyo. No introducir API, base de datos ni frontend hasta que las reglas de triage esten estables.

## Arquitectura Propuesta

```text
SAMPLE_PROJECT/
|-- docs/product/spec.md        # verdad funcional
|-- docs/architecture/sdd.md    # diseno tecnico
|-- decisions/                  # decisiones aprobadas
|-- memory/                     # conocimiento vigente
|-- src/                        # codigo ilustrativo opcional
`-- graphify-out/               # contexto derivado, placeholder pedagogico
```

## Componentes Impactados

- Documentacion funcional: `docs/product/spec.md`.
- Memoria de patrones y restricciones: `memory/patterns.md`, `memory/constraints.md`.
- Codigo ilustrativo: `src/sample_flow.py`.
- Graphify: `graphify-out/*`, solo como placeholder de ejemplo.

## Contratos / Interfaces

El ejemplo conceptual usa una solicitud con estos campos:

| Campo | Descripcion |
|---|---|
| `title` | Titulo breve de la solicitud. |
| `request_type` | Tipo: soporte, acceso, datos, seguridad u otro. |
| `priority` | Prioridad: baja, media, alta o critica. |
| `status` | Estado del flujo. |
| `owner` | Responsable asignado, si existe. |
| `closing_note` | Nota requerida para cerrar. |

## Datos y Migraciones

No hay base de datos ni migraciones. Si el proyecto se vuelve funcional, crear una ADR nueva antes de elegir persistencia.

## Riesgos

- Confundir `src/` con una implementacion obligatoria.
- Usar el placeholder de Graphify como si fuera reporte real.
- Agregar automatizacion antes de estabilizar reglas funcionales.

## Validacion

- Revisar que reglas de negocio vivan en `docs/product/spec.md`.
- Revisar que decisiones duraderas vivan en `decisions/`.
- Revisar que hechos y patrones vigentes vivan en `memory/`.
- Mantener `src/` pequeno y claramente opcional.

## Nota de uso

Si el diseno se aprueba para produccion, registrar la decision en `decisions/decision_log.md` o una ADR nueva.

