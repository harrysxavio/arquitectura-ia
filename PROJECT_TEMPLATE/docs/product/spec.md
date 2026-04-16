# Spec de Producto

Este archivo existe como puente para equipos que esperan encontrar una spec de producto tradicional. En este framework, la autoridad funcional detallada vive en OpenSpec.

## Proposito

Puede usarse como resumen de producto: problema, usuarios, objetivos y enlaces a capacidades OpenSpec. No debe contener reglas funcionales detalladas que compitan con `openspec/specs/*/spec.md`.

## Que Contiene

Una narrativa breve de producto y enlaces a fuentes canonicas. No contiene scenarios ni reglas funcionales detalladas.

## Orden de Uso

Completar solo si el proyecto necesita una lectura de producto separada de `PROJECT_GUIDE.md`. Si no, enlazar a `PROJECT_GUIDE.md` y OpenSpec.

## Relacion con Otros Documentos

`PROJECT_GUIDE.md` define identidad y alcance. OpenSpec gobierna comportamiento. `docs/architecture/system.md` gobierna estructura tecnica.

## Uso Recomendado

- Explicar el problema de producto en lenguaje humano.
- Enlazar a `PROJECT_GUIDE.md` para identidad y alcance.
- Enlazar a specs OpenSpec para comportamiento aprobado.
- Registrar preguntas de producto solo si luego se convierten en cambios OpenSpec o decisiones.

## Ejemplo Minimo

```markdown
El producto ayuda a equipos internos a registrar solicitudes y seguir su estado. El alcance vigente esta en `PROJECT_GUIDE.md`. El comportamiento aprobado de solicitudes vive en `openspec/specs/requests/spec.md`.
```

## No Usar Para

- Definir escenarios funcionales fuera de OpenSpec.
- Mantener backlog.
- Guardar decisiones tecnicas.
- Documentar arquitectura.

## Regla Breve

La spec de producto orienta; OpenSpec gobierna comportamiento.
