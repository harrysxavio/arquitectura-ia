# Contexto

El contexto es un recurso limitado. Leer mas no siempre mejora una respuesta; muchas veces mezcla señales, aumenta costo y hace que el agente pierda la fuente correcta.

## Proposito

Este documento explica la filosofia de carga de contexto. La version operativa esta en `OPERACION/CONTEXT_ROUTER.md`.

## Idea Central

El contexto se carga por necesidad, no por disponibilidad. Que un archivo exista no significa que deba abrirse. Primero se identifica la tarea, luego se eligen fuentes.

Para una tarea funcional, OpenSpec suele ser la primera fuente. Para una tarea estructural, arquitectura puede entrar temprano. Para una tarea ambigua o transversal, Graphify puede ayudar a decidir donde mirar. Para una decision historica, se consulta `decisions/`.

## Escalamiento Sano

Un flujo sano se ve asi:

1. Entender identidad y alcance del proyecto.
2. Ubicar la fuente oficial en `CONTEXT_INDEX.md`.
3. Cargar la spec o cambio OpenSpec si hay comportamiento.
4. Agregar arquitectura si hay estructura tecnica.
5. Agregar memoria si hechos o restricciones afectan la tarea.
6. Agregar Graphify si el impacto es amplio o poco claro.

Cada paso agrega contexto por una razon especifica.

## Señales de Sobrecarga

- Se abre una carpeta completa sin saber que se busca.
- Se lee memoria antes de confirmar la regla funcional.
- Se usa Graphify para un cambio local obvio.
- Se mezclan documentos historicos con fuentes activas.
- El agente explica mucho contexto pero no puede decir que fuente manda.

## Regla Breve

Leer menos no significa entender menos. Significa leer la fuente correcta en el momento correcto.
