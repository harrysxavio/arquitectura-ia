# Herramientas

Este framework no adopta herramientas por moda. Una herramienta entra cuando reduce ambiguedad, costo de contexto o riesgo operativo.

## Proposito

Este documento entrega el criterio para decidir si una herramienta ayuda al sistema o solo agrega ruido. Se complementa con `OPERACION/CONSTRAINTS/tooling_rules.md`, que contiene reglas operativas mas concretas.

## Criterio de Adopcion

Antes de incorporar una herramienta, debe poder responderse:

- Que problema real resuelve?
- Que reemplaza o complementa?
- Que complejidad agrega?
- Que complejidad reduce?
- Que fuente canonica alimenta o consulta?
- Que riesgo aparece si se la trata como autoridad?

Si no hay respuesta clara, la herramienta queda fuera.

## Herramientas en Este Modelo

OpenSpec define comportamiento y cambios. Git versiona el conocimiento. Markdown hace visible la documentacion. Graphify genera navegacion derivada. Obsidian o NotebookLM pueden servir como apoyo externo, pero no como fuente canonica.

La regla no es usar pocas herramientas por austeridad. La regla es que cada herramienta tenga un rol que no duplique ni contradiga otro.

## Herramientas Derivadas

Una herramienta derivada procesa fuentes existentes y produce una vista nueva: un grafo, un resumen, una visualizacion o una nota de investigacion. Eso puede ser muy util para explorar, pero no debe gobernar el proyecto.

Cuando una salida derivada revela algo valioso, el hallazgo se valida y se registra en la fuente canonica correspondiente.

## Error Comun

El error mas frecuente es confundir comodidad con autoridad. Que una herramienta encuentre una relacion no significa que esa relacion sea una regla del sistema. Que una nota externa sea buena no significa que deba mandar sobre OpenSpec o arquitectura.

## Regla Breve

Una herramienta se acepta cuando mejora el sistema de fuentes; se rechaza cuando intenta reemplazarlo.
