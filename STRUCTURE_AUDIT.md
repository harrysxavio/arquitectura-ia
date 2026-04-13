# Auditoria Estructural del Repositorio

## Veredicto

La arquitectura actual es valida y debe evolucionar sin crear un framework paralelo. Las capas principales ya tienen una intencion clara: `OPERACION/` gobierna la ejecucion, `THEORY/` explica los fundamentos, `GRAPHIFY/` regula contexto estructural derivado, `PROJECT_TEMPLATE/` funciona como molde reusable, `SATELLITE/` delimita conocimiento externo al nucleo, `EXAMPLES/` muestra casos de uso y `ARCHIVE/` conserva fuentes historicas no canonicas.

El problema principal no es la ausencia de arquitectura, sino la ambiguedad entre tres niveles documentales:

- explicacion conceptual del framework;
- plano operativo de un proyecto real;
- archivos copiables o reutilizables.

La estructura final recomendada agrega `PROJECT_BLUEPRINT/` como capa explicativa intermedia y renombra `TEMPLATES/` a `DOC_TEMPLATES/` para distinguir plantillas documentales sueltas del molde integral `PROJECT_TEMPLATE/`.

## Diagnostico estructural

| Area | Hallazgo | Riesgo | Recomendacion |
|---|---|---|---|
| `PROJECT_TEMPLATE/` | Ya representa un proyecto instanciable, pero sus archivos eran demasiado minimos. | El usuario o agente copia una plantilla sin suficiente guia de llenado. | Fortalecer cada `.md` con proposito, instruccion, ejemplo minimo y nota de uso. |
| `TEMPLATES/` | Contenia plantillas documentales sueltas que se parecen a archivos dentro de `PROJECT_TEMPLATE/`. | Confusion entre molde integral y formatos auxiliares. | Renombrar a `DOC_TEMPLATES/` y documentar que es biblioteca auxiliar, no proyecto completo. |
| Capa explicativa | No habia una capa dedicada a explicar la anatomia documental de un proyecto real. | `THEORY/` podia terminar absorbiendo guias operativas de adopcion. | Crear `PROJECT_BLUEPRINT/`. |
| `README.md` | Funcionaba como entrada inicial, pero no como mapa maestro completo. | Humanos y agentes no ven con suficiente rapidez que gobierna, que explica y que solo sirve de referencia. | Fortalecerlo como mapa de capas, autoridad y ruta de lectura. |
| `AGENTS.md` raiz | No existe en la raiz; si existen `OPERACION/AGENTS/*.md` y `PROJECT_TEMPLATE/AGENTS.md`. | Crear un `AGENTS.md` raiz podria duplicar autoridad. | No crearlo por defecto; solo crear un indice minimo si se aprueba despues. |
| `documentacion/` | Existe localmente vacia y no aparece como capa trackeada. | Puede convertirse en una arquitectura paralela accidental. | No adoptarla como capa oficial. |

## Estructura final recomendada

```text
/
|-- README.md
|-- STRUCTURE_AUDIT.md
|-- OPERACION/
|-- GRAPHIFY/
|-- THEORY/
|-- PROJECT_BLUEPRINT/
|   |-- PROJECT_DOCUMENTS.md
|   `-- PROJECT_STRUCTURE_EXAMPLE.md
|-- PROJECT_TEMPLATE/
|-- DOC_TEMPLATES/
|-- SATELLITE/
|-- EXAMPLES/
`-- ARCHIVE/
```

## Justificacion por capa

| Capa | Funcion | Fuente de verdad |
|---|---|---|
| `README.md` | Mapa maestro del repositorio y ruta de lectura. | Si, para orientacion del framework. |
| `OPERACION/` | Router, constraints y contratos de agentes. | Si, para ejecucion. |
| `GRAPHIFY/` | Politica y contrato de contexto estructural derivado. | Politica si; outputs generados no. |
| `THEORY/` | Fundamentos, principios y explicacion pedagogica del framework. | No para runtime tecnico. |
| `PROJECT_BLUEPRINT/` | Plano explicativo de como debe organizarse un proyecto real. | Si, para la anatomia documental recomendada. |
| `PROJECT_TEMPLATE/` | Molde completo copiable para iniciar un proyecto. | No en este repo; se vuelve canonico al instanciarse. |
| `DOC_TEMPLATES/` | Plantillas documentales sueltas y auxiliares. | No; formato auxiliar. |
| `SATELLITE/` | Politicas para Obsidian, NotebookLM y conocimiento fuera del nucleo. | No gobierna el proyecto activo. |
| `EXAMPLES/` | Casos practicos de uso del framework. | No; referencia. |
| `ARCHIVE/` | Fuentes historicas o materiales no canonicos. | No. |

## Frontera entre THEORY y PROJECT_BLUEPRINT

`THEORY/` responde por que existe el framework: principios, gobernanza, contexto, agentes, herramientas y criterios conceptuales.

`PROJECT_BLUEPRINT/` responde como debe verse documentalmente un proyecto real: archivos requeridos, ubicacion, autoridad, ciclo de vida, consulta y relacion entre `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md`, `tasks/`, `decisions/`, `memory/`, `docs/` y `graphify-out/`.

Regla practica:

- Si explica principios generales, va en `THEORY/`.
- Si explica la anatomia documental de un proyecto instanciado, va en `PROJECT_BLUEPRINT/`.
- Si es copiable como molde, va en `PROJECT_TEMPLATE/`.
- Si enruta ejecucion diaria, va en `OPERACION/`.

## TEMPLATES vs PROJECT_TEMPLATE

La recomendacion final es no unificar ambas capas.

`PROJECT_TEMPLATE/` debe mantenerse como molde integral de proyecto. Incluye estructura, carpetas y archivos base que se copian o adaptan al crear un proyecto real.

`DOC_TEMPLATES/` debe existir como biblioteca auxiliar de plantillas documentales sueltas. Su contenido puede reutilizarse dentro o fuera de un proyecto instanciado, pero no representa una estructura completa ni una fuente de verdad.

El nombre `DOC_TEMPLATES/` es mas preciso que `SNIPPETS/` porque los archivos actuales son documentos completos o semi-completos, no fragmentos parciales.

## Fortalecimiento de PROJECT_TEMPLATE

Cada archivo Markdown de `PROJECT_TEMPLATE/` debe seguir una convencion comun:

```md
# Nombre del documento

> Plantilla. Se vuelve canonica solo dentro de un proyecto activo.

## Proposito

## Como llenarlo

## Ejemplo minimo

## Nota de uso
```

Esta convencion evita dos extremos: plantillas vacias que no guian y documentos tan pesados que dejan de ser molde reusable.

Mejoras aplicadas o esperadas:

- agregar instrucciones breves a `PROJECT_GUIDE.md`, `CONTEXT_INDEX.md` y `AGENTS.md`;
- completar `docs/product/spec.md` con casos de uso y dependencias;
- completar `docs/architecture/sdd.md` con decisiones, contratos y validacion;
- mejorar `tasks/current/*` para distinguir tarea, plan y preguntas abiertas;
- mejorar `memory/*` para separar hechos, restricciones, problemas, patrones y glosario;
- agregar `decisions/adr/ADR_TEMPLATE.md`;
- mantener `graphify-out/` como destino de outputs derivados, no canonicos.

## Fortalecimiento del README

El README principal debe operar como mapa maestro. Debe explicar:

- que capa gobierna ejecucion;
- que capa explica fundamentos;
- que capa explica la estructura documental de un proyecto real;
- que capa es molde copiable;
- que capa contiene plantillas auxiliares;
- que capa es satelite o historica;
- que no debe cargarse todo el repo por defecto;
- como leer el repositorio sin mezclar contexto canonico y derivado.

## Riesgos de sobreingenieria

- Crear mas capas si `PROJECT_BLUEPRINT/` ya resuelve la ambiguedad.
- Convertir `PROJECT_BLUEPRINT/` en teoria larga.
- Duplicar plantillas completas entre `PROJECT_TEMPLATE/` y `DOC_TEMPLATES/`.
- Crear `AGENTS.md` raiz sin funcion distinta a `OPERACION/AGENTS/`.
- Mezclar Obsidian o NotebookLM con memoria canonica.
- Usar Graphify como fuente de verdad en vez de contexto derivado.
- Hacer una reorganizacion masiva antes de validar los documentos nuevos.

## Plan de etapa 2

1. Mantener la nueva estructura con `PROJECT_BLUEPRINT/` y `DOC_TEMPLATES/`.
2. Actualizar referencias internas a `DOC_TEMPLATES/`.
3. Usar `PROJECT_BLUEPRINT/` como guia de adopcion y no como teoria.
4. Mantener `PROJECT_TEMPLATE/` como molde reusable completo.
5. No crear `AGENTS.md` raiz salvo decision explicita.
6. No adoptar `documentacion/` como capa oficial.
7. Revisar periodicamente si `DOC_TEMPLATES/` acumula documentos que deberian integrarse al molde completo.

## Checklist de validacion

- La diferencia entre plantilla integral y plantillas documentales sueltas queda explicita.
- La capa explicativa intermedia existe y no compite con `THEORY/`.
- `SATELLITE/` se mantiene.
- `PROJECT_TEMPLATE/` queda fortalecido.
- `README.md` queda orientado como mapa maestro.
- La propuesta facilita el paso framework -> blueprint -> template -> proyecto real.
- No se crea una arquitectura paralela.
