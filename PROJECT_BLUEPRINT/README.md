# PROJECT_BLUEPRINT

`PROJECT_BLUEPRINT/` explica la anatomia documental de un proyecto real que adopta este framework.

## Que problema resuelve

Evita que `THEORY/` tenga que explicar estructura operativa y evita que `PROJECT_TEMPLATE/` cargue explicaciones largas. Esta carpeta responde que documentos debe tener un proyecto instanciado, donde viven y como se relacionan.

## Documentos

| Documento | Uso |
|---|---|
| `README.md` | Entrada breve a esta carpeta y sus limites. |
| `PROJECT_DOCUMENTS.md` | Rol, autoridad y momento de consulta de cada documento de un proyecto instanciado. |
| `PROJECT_STRUCTURE_EXAMPLE.md` | Estructura minima y estructura estandar de adopcion. |

## Diferencia con THEORY

`THEORY/` explica principios, criterios y fundamentos del framework.

`PROJECT_BLUEPRINT/` explica la forma documental de un proyecto real. No justifica toda la filosofia del sistema.

## Diferencia con PROJECT_TEMPLATE

`PROJECT_TEMPLATE/` contiene archivos copiables.

`PROJECT_BLUEPRINT/` contiene explicacion estructural. No se copia completo dentro de un proyecto activo.

## Como leer esta carpeta

1. Leer `PROJECT_DOCUMENTS.md` para entender autoridad y uso de cada documento.
2. Leer `PROJECT_STRUCTURE_EXAMPLE.md` para elegir entre adopcion minima y estandar.
3. Usar `PROJECT_TEMPLATE/` solo despues, como molde real de archivos.

## Que NO es

- No es teoria general.
- No es una biblioteca de plantillas sueltas.
- No es fuente de verdad de un proyecto activo.
- No reemplaza `OPERACION/CONTEXT_ROUTER.md`.
