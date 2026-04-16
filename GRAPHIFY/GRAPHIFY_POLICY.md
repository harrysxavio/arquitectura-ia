# Politica Oficial de Graphify

## Rol

Graphify es contexto estructural derivado. Ayuda con navegacion, incorporacion tecnica, analisis de impacto y refactors amplios.

## Que Hace

Graphify toma codigo, documentos u otros insumos y construye una representacion navegable: nodos, relaciones, comunidades, reportes y, segun la configuracion, visualizaciones. Su valor esta en mostrar donde mirar cuando el proyecto ya no cabe comodamente en la cabeza.

Para una persona no tecnica, Graphify funciona como mapa de territorio. Para una persona tecnica, ayuda a ubicar componentes, dependencias, zonas centrales y posibles impactos antes de abrir muchos archivos.

## Autoridad

Graphify nunca es canonico. No reemplaza:

- specs OpenSpec
- cambios OpenSpec
- arquitectura estable
- decisiones
- memoria compacta

La razon es simple: Graphify procesa fuentes y puede inferir relaciones. Una inferencia puede ser util como hipotesis, pero no es una decision del proyecto ni una regla funcional.

## Cuando Usarlo

Usa Graphify para:

- preguntas amplias de arquitectura;
- propiedad poco clara;
- impacto entre multiples modulos;
- incorporacion tecnica;
- refactors donde el costo de navegacion es alto.

No usarlo por defecto para ediciones locales, typos o cambios obvios de un solo archivo.

## Cuando No Conviene

No conviene usarlo cuando la fuente canonica ya indica exactamente que revisar, cuando el cambio es local y evidente, o cuando el costo de validar inferencias seria mayor que abrir el archivo afectado.

Tampoco debe usarse para decidir comportamiento de producto. Si una regla funcional falta o es ambigua, el camino correcto es OpenSpec, no Graphify.

## Gobernanza

Si Graphify revela una relacion que debe gobernar el proyecto, validala contra archivos fuente y luego registrala en OpenSpec, arquitectura, decisiones o memoria.

## Integracion con el Flujo

1. Usar el router de contexto para decidir si Graphify aporta.
2. Leer `graphify-out/GRAPH_REPORT.md` como mapa inicial.
3. Abrir archivos fuente antes de tomar decisiones.
4. Si aparece conocimiento durable, registrarlo en la fuente canonica adecuada.
5. Mantener claro que `graphify-out/*` es salida derivada.

## Regla Breve

Graphify orienta la exploracion; las fuentes canonicas gobiernan el proyecto.
