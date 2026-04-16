# Architecture Migration Plan

> Plan ejecutable aprobado para migrar la arquitectura actual a OpenSpec-first.

## Objetivo

Aplicar la arquitectura definida en `ARCHITECTURE_REDESIGN_PROPOSAL.md` sin dejar dos fuentes funcionales activas ni dos flujos principales de cambio.

## Inventario Afectado

| Area | Rutas legacy | Destino |
|---|---|---|
| Verdad funcional | `docs/product/spec.md` | `openspec/specs/<capability>/spec.md` |
| Cambio activo | `tasks/current/*` | `openspec/changes/<change-id>/*` |
| Diseno tecnico | `docs/architecture/sdd.md` | `docs/architecture/system.md` + `openspec/changes/*/design.md` |
| Hechos | `memory/project_facts.md` | `memory/facts.md` |
| Problemas conocidos | `memory/known_issues.md` | `memory/facts.md` si sigue vigente, o archivo legacy |
| Router | `OPERACION/CONTEXT_ROUTER.md` | OpenSpec-first |
| Blueprint | `PROJECT_BLUEPRINT/*` | Guia compacta OpenSpec-first |
| Graphify | `GRAPHIFY/*`, `graphify-out/*` | Derivado, no canonico |

## Fase 1: Preparacion

1. Crear `ARCHITECTURE_REDESIGN_PROPOSAL.md`.
2. Crear este `ARCHITECTURE_MIGRATION_PLAN.md`.
3. Crear `ARCHIVE/legacy-open-spec-migration/`.
4. Copiar alli documentos legacy antes de retirarlos.
5. Hacer inventario de referencias legacy.

Validacion: la propuesta, el plan y el archivo legacy existen antes de retirar rutas activas.

## Fase 2: Migracion de Autoridad Funcional a OpenSpec

1. Crear `openspec/specs/example-capability/spec.md` en `PROJECT_TEMPLATE/`.
2. Crear `openspec/specs/support-requests/spec.md` en `SAMPLE_PROJECT/`.
3. Migrar reglas, casos de uso y criterios de aceptacion desde `docs/product/spec.md`.
4. Actualizar `CONTEXT_INDEX.md` para declarar OpenSpec como fuente funcional.
5. Retirar o archivar `docs/product/spec.md` como ruta activa.

Validacion: ninguna ruta activa presenta `docs/product/spec.md` como verdad funcional.

## Fase 3: Migracion del Flujo de Cambio a OpenSpec Changes

1. Crear `openspec/changes/` y `openspec/archive/`.
2. Crear un cambio ejemplo en `SAMPLE_PROJECT/openspec/changes/add-security-priority/`.
3. Migrar objetivo, alcance y no alcance a `proposal.md`.
4. Migrar pasos y validacion a `tasks.md`.
5. Migrar diseno de cambio a `design.md`.
6. Crear delta de spec en `specs/support-requests/spec.md`.
7. Retirar o archivar `tasks/current/*` como ruta activa.

Validacion: ninguna ruta activa usa `tasks/current/*` como flujo de cambio.

## Fase 4: Simplificacion Documental

1. Migrar `docs/architecture/sdd.md` a `docs/architecture/system.md`.
2. Compactar memoria en `facts.md`, `constraints.md`, `patterns.md` y `glossary.md` opcional.
3. Mantener `decision_log.md` como indice breve.
4. Mantener ADRs para decisiones estructurales.
5. Fusionar docs pedagogicos redundantes del sample en `VALIDATION_GUIDE.md` o archivarlos.

Validacion: `system.md` contiene arquitectura estable, no reglas funcionales.

## Fase 5: Actualizacion de Template y Sample

1. Alinear `PROJECT_TEMPLATE/` con la estructura OpenSpec-first.
2. Alinear `SAMPLE_PROJECT/` con la misma arquitectura y con codigo/tests conservados.
3. Redefinir `PROJECT_BLUEPRINT/` sin eliminarlo.
4. Actualizar `README.md`, `OPERACION/`, `GRAPHIFY/`, `EXAMPLES/`, `THEORY/` y `SATELLITE/`.

Validacion: template y sample ensenan el mismo modelo.

## Fase 6: Validacion Final y Limpieza

1. Ejecutar busquedas de referencias legacy:
   - `tasks/current`
   - `docs/product/spec.md`
   - `docs/architecture/sdd.md`
   - `project_facts.md`
   - `known_issues.md`
2. Corregir cualquier referencia activa indebida.
3. Ejecutar tests del sample.
4. Regenerar o marcar stale Graphify.
5. Crear `ARCHITECTURE_MIGRATION_REPORT.md`.

## Rollback y Correccion

- Si OpenSpec queda incompleto, no cerrar la fase y restaurar temporalmente el legacy desde `ARCHIVE/legacy-open-spec-migration/`.
- Si aparece duplicacion funcional, OpenSpec gana y la otra fuente se archiva o se vuelve referencia no canonica.
- Si `PROJECT_BLUEPRINT/` duplica demasiado, reducirlo, no eliminarlo.
- Si Graphify falla al regenerarse, marcarlo como derivado stale y no usarlo como validacion canonica.

## Criterios de Cierre

- `openspec/specs/*/spec.md` es la unica verdad funcional activa.
- `openspec/changes/*` reemplaza `tasks/current/*`.
- `docs/architecture/system.md` es arquitectura estable.
- `decision_log.md` es breve y vigente.
- `memory/` esta compacta pero separada.
- `PROJECT_BLUEPRINT/` sigue presente y redefinido.
- `PROJECT_TEMPLATE/` y `SAMPLE_PROJECT/` estan alineados.
- Graphify sigue derivado.
- No hay referencias legacy activas.
