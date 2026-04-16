# Hechos

> Hechos confirmados y compactos para el ejemplo de mesa de soporte de SAMPLE_PROJECT.

## Proyecto

- El ejemplo es una app CLI pedagogica, no una plantilla productiva.
- Usa solo la biblioteca estandar de Python.
- No tiene frontend, base de datos productiva, hosting ni integraciones externas.
- GitHub y Markdown son la base aprobada de documentacion/versionado.

## Datos de Ejecucion

- `data/requests.json` es solo persistencia de ejecucion local.
- `src/` contiene la automatizacion minima alineada con OpenSpec.
- `graphify-out/` contiene contexto estructural derivado.

## Problemas Vigentes

| Problema | Impacto | Mitigacion |
|---|---|---|
| Graphify puede no estar instalado localmente. | El contexto derivado puede quedar desactualizado. | Regenerar cuando este disponible; si no, tratar la salida como desactualizada. |
| El ejemplo puede confundirse con una base productiva. | Expansion de alcance. | Revisar `PROJECT_GUIDE.md` y `docs/architecture/system.md` antes de expandir. |
| Las prioridades manuales pueden variar. | Operacion inconsistente. | Mantener politica funcional en OpenSpec y patrones en memoria. |
