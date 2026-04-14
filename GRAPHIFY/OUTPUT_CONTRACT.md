# Contrato de Outputs Graphify

## Ubicacion Esperada

> [!NOTE]
> Estos outputs viven en el proyecto instanciado, no como fuente canonica del framework global.

En un proyecto instanciado, los outputs de Graphify deben vivir en `graphify-out/`.

El output minimo esperado es `GRAPH_REPORT.md` y `graph.json`. `graph.html` es opcional y solo debe esperarse cuando la herramienta lo genere.

## Rol de Cada Output

| Archivo | Uso | Fuente de verdad |
|---|---|---|
| `GRAPH_REPORT.md` | Resumen humano/agentico de estructura, modulos e impacto | No |
| `graph.json` | Grafo consultable por herramientas o agentes | No |
| `graph.html` | Visualizacion humana opcional cuando existe | No |

## Generacion

El comando publico recomendado desde el proyecto instanciado es:

```bash
graphify update .
```

Si `graph.html` no aparece, no debe tratarse como falla del proyecto salvo que la tarea requiera visualizacion HTML.

## Reglas de Consumo

> [!TIP]
> Lee `GRAPH_REPORT.md` antes de abrir muchos archivos cuando la tarea sea Nivel 3.

- Leer `GRAPH_REPORT.md` antes de abrir muchos archivos en tareas Nivel 3.
- Usar `graph.json` cuando se necesite consulta estructurada.
- Usar `graph.html` para navegacion humana u Obsidian solo si fue generado.
- No copiar conclusiones de Graphify a memoria canonica sin validarlas.

## Vigencia

Un output Graphify se considera potencialmente stale cuando:

- cambiaron carpetas o modulos principales,
- hubo refactor transversal,
- se agrego una integracion importante,
- cambio la arquitectura documentada,
- el agente detecta contradiccion con el repo.

> [!WARNING]
> No uses outputs stale como base de decision sin regenerarlos o verificarlos contra archivos canonicos.
