# Agentes

Los agentes no son solo modelos ejecutando instrucciones. En este framework son roles operativos que deben respetar fuentes de autoridad, cargar contexto minimo y dejar trazabilidad suficiente.

## Proposito

Este documento explica como pensar el trabajo con agentes. Las instrucciones concretas viven en `OPERACION/AGENTS/` y en el `AGENTS.md` de cada proyecto activo.

## Roles Base

| Rol | Responsabilidad principal | Riesgo que debe evitar |
|---|---|---|
| Manager | Clasificar la tarea y elegir contexto. | Cargar demasiado o elegir la fuente equivocada. |
| Coder | Implementar dentro de limites aprobados. | Cambiar arquitectura o comportamiento sin fuente canonica. |
| Reviewer | Detectar riesgos, inconsistencias y falta de validacion. | Revisar estilo y olvidar autoridad funcional. |
| Debugger | Investigar fallas con hipotesis verificables. | Saltar a refactors amplios sin reproducir el problema. |

Estos roles pueden vivir en agentes separados o en una sola sesion. Lo importante es que la responsabilidad sea explicita.

## Relacion con OpenSpec

Cuando el agente toca comportamiento, OpenSpec manda. El agente puede descubrir que la spec esta incompleta, pero no debe resolverlo escondiendo la regla en codigo o memoria. Debe proponer o actualizar el cambio OpenSpec correspondiente.

## Relacion con Memoria y Graphify

La memoria ayuda cuando contiene hechos, restricciones o patrones vigentes. Graphify ayuda a navegar impacto. Ninguno reemplaza la lectura de la fuente canonica.

## Buen Comportamiento de Agente

Un agente saludable puede explicar:

- que tarea esta resolviendo;
- que fuentes cargo y por que;
- que fuente gobierna la decision;
- que validacion ejecuto o no pudo ejecutar;
- que conocimiento durable debe quedar registrado.

## Regla Breve

Un buen agente no solo produce cambios; tambien respeta el mapa de autoridad del proyecto.
