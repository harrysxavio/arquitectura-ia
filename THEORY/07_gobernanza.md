# Gobernanza

Gobernanza no significa burocracia. En este framework significa proteger la claridad del proyecto cuando muchas personas, agentes y herramientas pueden escribir documentos.

## Proposito

Este documento explica como evitar que el sistema se degrade. Un repo OpenSpec-first puede empezar ordenado y volverse confuso si cada cambio agrega una fuente nueva, duplica reglas o convierte una salida derivada en autoridad.

## Que Gobierna Cada Fuente

| Fuente | Gobierna | No debe gobernar |
|---|---|---|
| OpenSpec | Comportamiento funcional y cambios activos. | Estructura tecnica estable completa. |
| Arquitectura | Componentes, limites, datos, integraciones. | Reglas funcionales detalladas. |
| Decisiones | Direcciones aprobadas y su razon. | Backlog o tareas pendientes. |
| Memoria | Hechos, restricciones y patrones vigentes. | Historia completa del proyecto. |
| Graphify | Navegacion derivada e impacto probable. | Verdad funcional o decisiones. |
| README | Entrada y orientacion. | Reglas funcionales profundas. |

## Politica de No Duplicacion

Duplicar parece util al principio, pero crea deuda documental. Si una regla esta en dos lugares, tarde o temprano uno queda viejo. La gobernanza exige que los documentos secundarios enlacen, resuman o expliquen sin competir.

## Cuando Crear o Actualizar Documentos

Crear un documento nuevo tiene costo. Debe resolver una necesidad clara: separar una autoridad, explicar una pieza estable o reducir confusion recurrente. Si el contenido solo repite otra fuente, debe enlazarla en vez de duplicarla.

Actualizar memoria o decisiones requiere que el conocimiento sea durable. Una observacion de una sesion no basta si no afectara trabajo futuro.

## Señales de Degradacion

- Nadie sabe si manda README, memoria o OpenSpec.
- Los agentes cargan carpetas completas por costumbre.
- Las decisiones importantes solo existen en chats.
- `memory/` contiene listas de tareas viejas.
- Graphify se usa para justificar comportamiento sin revisar specs.

## Regla Breve

Gobernar el proyecto es impedir que la informacion util se convierta en ruido.
