# Contrato de Outputs Graphify

## Ubicacion Esperada

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

Si esta stale, no debe usarse como base de decision sin regenerarse o verificarse contra archivos canonicos.
