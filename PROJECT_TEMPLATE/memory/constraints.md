# Restricciones

> Restricciones compactas para un proyecto instanciado desde esta plantilla.

Este archivo guarda limites vigentes que deben respetarse antes de decidir o implementar. Una restriccion puede ser tecnica, de negocio, seguridad, costo, compliance o equipo.

## Tecnicas

- Mantener comportamiento funcional en OpenSpec.
- Mantener arquitectura estable en `docs/architecture/system.md`.
- Mantener Graphify como derivado.

## Negocio

- Por definir

## Seguridad

- No almacenar secretos, credenciales ni tokens reales en Markdown.

## Costo

- Por definir

## Como Usarlo

Consultar antes de ampliar alcance, introducir herramientas, cambiar arquitectura o tocar datos sensibles. Si una restriccion bloquea un cambio, el cambio debe rediseñarse o abrir una decision explicita.

## Que No Va Aqui

No poner reglas funcionales completas, backlog ni preferencias personales. Si una restriccion se convierte en comportamiento observable, debe reflejarse en OpenSpec.

## Regla Breve

Una restriccion es un limite que cambia decisiones, no una recomendacion decorativa.
