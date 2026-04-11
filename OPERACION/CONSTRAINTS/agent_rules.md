# CONSTRAINTS: Agentes

## Agentes Oficiales

Solo existen cuatro agentes base:

- Manager
- Coder
- Reviewer
- Debugger

No crear agentes nuevos sin decision documentada. Si una necesidad puede resolverse con skill, workflow o checklist, no debe convertirse en agente.

## Subagentes

Los subagentes son opcionales y avanzados. Usarlos solo si:

- reducen carga de contexto,
- permiten trabajo paralelo real,
- devuelven resultados comprimidos,
- no duplican un agente base.

No usarlos para tareas simples o trabajo local evidente.

## Separacion de Rol

- Manager: clasifica, enruta contexto y decide siguiente paso.
- Coder: implementa cambios dentro del alcance.
- Reviewer: valida riesgos, coherencia, calidad y testing.
- Debugger: investiga causa raiz y propone correccion.

Los detalles de cada rol viven en `OPERACION/AGENTS/*.md`.

## Reglas Generales

- Todo agente trabaja dentro del alcance declarado.
- Todo agente respeta las fuentes canonicas y decisiones registradas.
- Todo agente evita pedir al usuario informacion que ya exista en memoria oficial.
- Todo agente debe explicar el contexto adicional que necesita antes de escalar lectura.
