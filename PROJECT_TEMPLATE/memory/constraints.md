# Restricciones

> Restricciones compactas para un proyecto instanciado desde esta plantilla.

Este archivo guarda limites vigentes que deben respetarse antes de decidir o implementar. Una restriccion puede ser tecnica, de negocio, seguridad, costo, compliance o equipo.

## Que Contiene

Restricciones tecnicas, de negocio, seguridad y costo que cambian decisiones. Deben ser concretas y verificables.

## Orden de Uso

Consultar antes de ampliar alcance, cambiar arquitectura, instalar herramientas o tocar datos sensibles. Actualizar cuando una decision durable agrega o retira un limite.

## Relacion con Otros Documentos

OpenSpec define comportamiento; restricciones define limites. ADRs explican decisiones que crean restricciones durables.

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

## Ejemplo Minimo

```markdown
## Tecnicas

- Mantener comportamiento funcional en OpenSpec.
- No introducir servicios externos sin ADR.

## Seguridad

- No almacenar tokens en Markdown.
- Toda exportacion debe excluir datos personales.

## Costo

- No agregar servicios pagos en la primera version.
```

## Como Usarlo

Consultar antes de ampliar alcance, introducir herramientas, cambiar arquitectura o tocar datos sensibles. Si una restriccion bloquea un cambio, el cambio debe rediseñarse o abrir una decision explicita.

## Que No Va Aqui

No poner reglas funcionales completas, backlog ni preferencias personales. Si una restriccion se convierte en comportamiento observable, debe reflejarse en OpenSpec.

## Regla Breve

Una restriccion es un limite que cambia decisiones, no una recomendacion decorativa.
