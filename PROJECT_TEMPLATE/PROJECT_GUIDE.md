# PROJECT_GUIDE.md

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

Describe identidad del proyecto, usuarios, alcance, estructura, stack y restricciones importantes.

Este archivo es la puerta de entrada del proyecto activo. Debe permitir que una persona o agente entienda que problema existe, para quien se resuelve y que limites no deben cruzarse.

No define comportamiento funcional detallado. Para eso esta OpenSpec. Tampoco reemplaza arquitectura tecnica. Su funcion es orientar.

## Que Contiene

Identidad, usuarios, problema, alcance, estructura, stack y restricciones generales. Debe leerse antes que OpenSpec porque da contexto humano, pero no reemplaza las specs.

## Orden de Uso

Completar primero este archivo, luego `CONTEXT_INDEX.md`, despues la primera spec OpenSpec y finalmente arquitectura, memoria y decisiones segun necesidad.

## Relacion con Otros Documentos

- `CONTEXT_INDEX.md` apunta a las fuentes oficiales.
- OpenSpec contiene comportamiento funcional.
- `docs/architecture/system.md` contiene estructura tecnica.
- `memory/constraints.md` contiene limites vigentes detallados.

## Identidad

- Nombre:
- Usuario principal:
- Problema que resuelve:

Escribir el problema en lenguaje humano, no como lista de features. Una buena descripcion permite distinguir que pertenece al proyecto y que es expansion de alcance.

## Alcance

- Incluido:
- Fuera de alcance:

El alcance evita que el proyecto crezca por inercia. "Fuera de alcance" es tan importante como "incluido" porque protege decisiones futuras.

## Estructura

- `openspec/`: verdad funcional y cambios activos.
- `docs/architecture/system.md`: arquitectura estable.
- `decisions/`: indice de decisiones y ADRs.
- `memory/`: hechos, restricciones, patrones, glosario y problemas conocidos compactos.
- `graphify-out/`: contexto derivado.

Esta seccion debe explicar las carpetas propias del proyecto si hay particularidades. Si la estructura es estandar, mantenerla breve y enlazar a `CONTEXT_INDEX.md`.

## Stack

- Backend:
- Frontend:
- Data:
- Hosting:

Usar nombres concretos cuando existan. Si algo no aplica, escribir "No aplica" en vez de dejarlo ambiguo.

## Restricciones

- Tecnicas:
- Negocio:
- Seguridad:

Registrar solo restricciones de alto nivel que una persona debe conocer antes de actuar. Las restricciones detalladas y vigentes viven en `memory/constraints.md`.

## Regla

No poner reglas funcionales aqui. Enlazar a OpenSpec en su lugar.

## Ejemplo Minimo

```markdown
## Identidad

- Nombre: Portal Interno de Solicitudes.
- Usuario principal: equipos internos que piden soporte operativo.
- Problema que resuelve: centralizar solicitudes internas y dar trazabilidad a su estado.

## Alcance

- Incluido: crear solicitudes, consultar estado, asignar responsables.
- Fuera de alcance: portal publico, facturacion, integraciones externas.

## Stack

- Backend: Python.
- Frontend: No aplica en la primera version.
- Data: SQLite local.
- Hosting: No definido.
```

## Checklist de Calidad

- Una persona nueva puede explicar que problema resuelve el proyecto.
- Queda claro que esta fuera de alcance.
- Las rutas clave apuntan a documentos existentes.
- No hay reglas funcionales duplicadas desde OpenSpec.
