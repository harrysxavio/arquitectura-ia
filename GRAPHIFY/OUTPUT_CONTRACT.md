# Contrato de Salida de Graphify

Las salidas de Graphify son artefactos derivados. Pueden incluir reportes, grafos JSON o visualizaciones.

## Proposito

Este contrato define que puede esperarse de `graphify-out/` y como debe interpretarse. La carpeta puede ser muy util para navegar, pero no debe confundirse con documentacion canonica.

## Salidas Esperadas

- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/graph.json`
- salida visual opcional si la herramienta la genera

## Como Leerlas

`GRAPH_REPORT.md` resume nodos relevantes, comunidades, conexiones e indicios de impacto. `graph.json` conserva una forma estructurada que herramientas pueden procesar. Una visualizacion ayuda a explorar, pero sigue siendo una vista derivada.

Las relaciones pueden venir de señales directas o inferencias. Mientras mas inferida sea una relacion, mas importante es validar contra el archivo fuente.

## Reglas

- Las salidas pueden quedar desactualizadas.
- Las salidas solo guian la navegacion.
- La informacion canonica debe vivir en OpenSpec, arquitectura, decisiones o memoria.

## Uso Correcto

Usa una salida de Graphify para formular mejores preguntas: que archivo revisar, que modulo podria verse afectado, que componente parece central. No la uses para afirmar que una regla funcional existe ni para justificar un cambio sin revisar la fuente.

## Regla Breve

Una salida de Graphify es una pista estructural, no una sentencia de autoridad.
