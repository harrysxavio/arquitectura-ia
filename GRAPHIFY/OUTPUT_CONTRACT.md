# Contrato de Outputs Graphify

## Ubicacion Esperada

> [!NOTE]
> Estos outputs viven en el proyecto instanciado, no como fuente canonica del framework global.

En un proyecto instanciado, los outputs de Graphify deben vivir en:

```text
graphify-out/
├── GRAPH_REPORT.md
├── graph.json
└── graph.html
```

## Rol de Cada Output

| Archivo | Uso | Fuente de verdad |
|---|---|---|
| `GRAPH_REPORT.md` | Resumen humano/agentico de estructura, modulos e impacto | No |
| `graph.json` | Grafo consultable por herramientas o agentes | No |
| `graph.html` | Visualizacion humana | No |

## Reglas de Consumo

> [!TIP]
> Lee `GRAPH_REPORT.md` antes de abrir muchos archivos cuando la tarea sea Nivel 3.

- Leer `GRAPH_REPORT.md` antes de abrir muchos archivos en tareas Nivel 3.
- Usar `graph.json` cuando se necesite consulta estructurada.
- Usar `graph.html` para navegacion humana o Obsidian.
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
