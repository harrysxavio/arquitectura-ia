# Delivery

Delivery en este framework no significa solo terminar codigo. Significa cerrar una unidad de trabajo con comportamiento, documentacion y validacion alineados.

## Proposito

Este documento define que debe estar claro antes de considerar una tarea terminada. Se conecta con `OPERACION/CONSTRAINTS/process_constraints.md` y con los `tasks.md` dentro de cambios OpenSpec.

## Cierre de una Tarea

Una tarea queda bien cerrada cuando se puede responder:

- Que fuente definia el comportamiento o alcance?
- Que archivos cambiaron y por que?
- Que validacion demuestra que el cambio funciona?
- Hay una decision durable que registrar?
- Hay memoria compacta que actualizar?
- Quedo alguna pregunta abierta en el lugar correcto?

No todas las tareas requieren todos los documentos. Pero toda tarea debe cerrar sin dejar reglas escondidas.

## Delivery Funcional

Si cambia comportamiento, el flujo natural es:

1. Cambio OpenSpec en `openspec/changes/*`.
2. Diseño si afecta arquitectura, datos o contratos.
3. Implementacion en codigo o docs.
4. Tests o validacion documental.
5. Actualizacion de spec aprobada cuando corresponda.

## Delivery Documental

Si el cambio es documental, tambien requiere autoridad. Un documento no debe inventar reglas funcionales fuera de OpenSpec. Debe explicar, enlazar o aclarar la fuente adecuada.

## Errores Comunes

- Cerrar una tarea porque "compila" sin revisar docs.
- Actualizar memoria con informacion transitoria.
- Crear decisiones largas para acuerdos menores.
- Dejar `tasks.md` desactualizado respecto del cambio real.
- Validar solo con lectura cuando existian tests claros.

## Regla Breve

Una entrega esta completa cuando el proximo humano o agente puede entender que cambio, por que cambio y como se valido.
