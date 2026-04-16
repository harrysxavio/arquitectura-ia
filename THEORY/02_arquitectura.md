# Arquitectura

La arquitectura OpenSpec-first no es una estructura de carpetas por estetica. Es un reparto de responsabilidades para que el proyecto conserve claridad aunque cambien personas, agentes y herramientas.

## Proposito

Este documento explica como se conectan las piezas principales del framework. Sirve para entender por que existen `PROJECT_BLUEPRINT/`, `PROJECT_TEMPLATE/`, `OPERACION/`, `GRAPHIFY/` y las fuentes canonicas de un proyecto activo.

## Modelo Mental

Un proyecto activo necesita responder cinco preguntas:

| Pregunta | Documento que debe responder |
|---|---|
| Que debe hacer el sistema? | OpenSpec |
| Como esta construido? | Arquitectura estable |
| Por que se eligio esta direccion? | Decisiones y ADRs |
| Que hechos conviene recordar? | Memoria compacta |
| Donde conviene mirar primero? | Graphify como contexto derivado |

La arquitectura consiste en mantener esas respuestas separadas, conectadas y sin competencia.

## Flujo OpenSpec-First

OpenSpec ocupa dos lugares:

- `openspec/specs/*/spec.md`: comportamiento aprobado.
- `openspec/changes/*`: cambios propuestos o en curso.

Esto evita que un cambio funcional empiece directamente en codigo o en memoria. Primero se expresa la intencion, luego se diseña, se implementa y se valida.

## Capas del Repositorio

`THEORY/` explica los fundamentos. `OPERACION/` dice como trabajar con contexto y agentes. `PROJECT_BLUEPRINT/` enseña como adoptar el modelo. `PROJECT_TEMPLATE/` ofrece un molde inicial. `GRAPHIFY/` define el uso de grafo derivado. Un proyecto activo toma esas ideas y las convierte en sus propias fuentes canonicas.

## Que No Es Arquitectura

No todo documento con una lista de archivos es arquitectura. Arquitectura es la explicacion estable de componentes, limites, contratos, datos e integraciones. Si un documento solo repite reglas funcionales, esta compitiendo con OpenSpec. Si solo lista archivos sin explicar responsabilidades, no ayuda a operar.

## Regla Breve

La arquitectura estable responde como esta construido el sistema; OpenSpec responde que debe hacer.
