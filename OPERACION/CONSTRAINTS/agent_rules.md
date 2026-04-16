# RESTRICCIONES: Reglas de Agentes

Estas reglas definen el comportamiento minimo esperado de cualquier agente que trabaje con este framework.

## Proposito

Un agente puede escribir codigo, editar documentos o investigar fallas, pero siempre debe respetar el mapa de autoridad del proyecto. Estas restricciones evitan que la autonomia del agente se convierta en cambios amplios, contexto excesivo o reglas escondidas.

## Reglas

- Respetar el router de contexto antes de cargar fuentes amplias.
- Preferir el menor contexto suficiente para decidir.
- Tratar OpenSpec como autoridad funcional.
- Tratar Graphify solo como navegacion derivada.
- Preservar cambios del usuario y evitar refactors no relacionados.
- Explicar que fuente gobierna cuando el cambio afecta comportamiento.
- Validar o declarar claramente que validacion no pudo ejecutarse.

## Malas Interpretaciones

No significa que el agente deba pedir permiso para cada paso pequeño. Significa que debe actuar con fuentes correctas y alcance claro. Tampoco significa que Graphify este prohibido; significa que no puede mandar sobre OpenSpec, arquitectura o decisiones.

## Regla Breve

Autonomia sin autoridad clara produce ruido. El agente debe saber que documento manda antes de cambiar algo importante.
