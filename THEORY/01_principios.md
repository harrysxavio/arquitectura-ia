# Principios

Este documento explica las ideas que sostienen el framework. No es una lista decorativa: sirve para decidir que hacer cuando un documento, una herramienta o un agente parecen competir por autoridad.

## Proposito

El objetivo del sistema es que humanos y agentes trabajen con el mismo mapa. Para lograrlo, cada tipo de conocimiento tiene un lugar preferente y una funcion concreta.

Una persona no tecnica puede leer estos principios como reglas de orden. Una persona tecnica puede usarlos como criterios de diseño para mantener un proyecto entendible cuando crecen el codigo, las specs y la memoria.

## Principios Base

| Principio | Que significa en la practica |
|---|---|
| Una fuente de verdad por tipo de informacion | No poner la misma regla funcional en README, memoria y arquitectura. Elegir la fuente correcta. |
| OpenSpec gobierna comportamiento | Si algo define que debe hacer el sistema, vive en `openspec/specs/*` o empieza como cambio en `openspec/changes/*`. |
| Arquitectura explica estructura estable | Componentes, limites, datos e integraciones viven en `docs/architecture/system.md`, no en la spec funcional. |
| Decisiones explican por que | `decisions/decision_log.md` y ADRs evitan rediscutir una direccion ya aprobada. |
| Memoria es compacta y accionable | La memoria guarda hechos, restricciones y patrones que afectan trabajo futuro; no es diario ni backlog. |
| Graphify es derivado | Ayuda a navegar y estimar impacto, pero no reemplaza fuentes canonicas. |

## Por Que Importa

Un agente de IA no falla solo por falta de inteligencia. Falla cuando el sistema le entrega señales contradictorias: una regla en una spec, otra en un README, una decision vieja en memoria y un grafo derivado que parece autoridad. Este framework reduce esas contradicciones.

El beneficio para humanos tambien es directo: una persona nueva no necesita adivinar que documento manda. Puede seguir el reparto de autoridad y entender donde buscar cada respuesta.

## Errores Comunes

- Escribir reglas funcionales en arquitectura porque parece mas rapido.
- Usar `memory/facts.md` para tareas pendientes.
- Tratar `graphify-out/GRAPH_REPORT.md` como prueba de comportamiento.
- Crear ADRs para decisiones pequeñas que caben en `decision_log.md`.
- Copiar texto conceptual en todos los documentos en vez de enlazar la fuente adecuada.

## Regla Breve

Cuando dudes donde escribir algo, pregunta que tipo de verdad es: comportamiento, estructura, decision, memoria o navegacion. Esa respuesta define el documento.
