# VALIDATION_GUIDE.md

> Guia practica para validar la mini app y el valor de Graphify dentro de este ejemplo pedagogico.

## Proposito

Comprobar que `SAMPLE_PROJECT/` funciona como mesa interna de soporte operativo pequena, que sigue alineado con el framework y que Graphify ayuda como contexto derivado sin reemplazar fuentes canonicas.

## Validacion Funcional

Desde `SAMPLE_PROJECT/`:

```bash
python -m unittest discover -s tests
python app.py demo
python app.py create --title "Acceso VPN" --description "Alta para equipo operaciones" --area "Operaciones" --type acceso
python app.py list
python app.py close --id <id> --note "Resuelto con alta manual"
```

Verifica:

- `data/requests.json` cambia al crear o cerrar solicitudes.
- Una solicitud de tipo `seguridad` parte con prioridad `alta`.
- El cierre sin nota falla.
- Cerrar un id inexistente falla con mensaje claro.

## Validacion Documental

Revisa:

- `CONTEXT_INDEX.md` apunta a fuentes canonicas, codigo y Graphify con roles distintos.
- `docs/product/spec.md` gobierna reglas funcionales.
- `docs/architecture/sdd.md` describe la automatizacion minima y sus limites.
- `decisions/` explica que primero se documentan reglas y luego se automatiza lo minimo.
- `memory/` mantiene hechos, restricciones, patrones y problemas vigentes.
- La estructura documental sigue alineada con `PROJECT_TEMPLATE/`, sin convertir el template en app.

## Validacion Graphify

Desde `SAMPLE_PROJECT/`, ejecuta el comando publico:

```bash
graphify update .
```

El output esperado vive en:

```text
graphify-out/
```

Si Graphify no esta instalado o falla, conserva `graphify-out/.gitkeep` y registra la verificacion como pendiente. No uses `_rebuild_code(...)` como instruccion principal; solo puede servir como fallback tecnico justificado.

## Prueba Comparativa

Usa esta prueba para decidir si Graphify aporta valor real:

1. Sin Graphify, responde: "Si cambia la regla de prioridad de seguridad, que archivos debo revisar?"
2. Registra que archivos abriste manualmente y cuanto contexto necesitaste.
3. Ejecuta `graphify update .`.
4. Abre `graphify-out/GRAPH_REPORT.md` y repite la pregunta.
5. Compara si el reporte redujo exploracion, aclaro relaciones entre codigo/docs o no aporto suficiente valor.

Resultado esperado: Graphify debe orientar navegacion e impacto, pero la decision final debe validarse contra `docs/product/spec.md`, `docs/architecture/sdd.md`, `decisions/` y `memory/`.
