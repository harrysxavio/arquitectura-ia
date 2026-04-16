# Spec de Ejemplo: Solicitudes Internas

> Ejemplo de spec vigente para una capacidad funcional. Al usarla en un proyecto real, renombra `example-capability` y reemplaza solicitudes internas por una capacidad de tu dominio.

## Proposito

Este archivo muestra como describir comportamiento aprobado en `openspec/specs/*/spec.md`.

La idea es que una persona o un agente pueda entender que debe hacer el sistema sin leer codigo primero.

## Como Adaptar Esta Plantilla

1. Cambia el nombre de la carpeta `example-capability` por el nombre real de la capacidad, por ejemplo `requests`, `auth` o `billing`.
2. Cambia el titulo por el nombre de la capacidad.
3. Reemplaza las reglas de ejemplo por reglas reales del proyecto.
4. Escribe escenarios verificables para casos exitosos y casos rechazados.
5. Mueve detalles tecnicos a `docs/architecture/system.md` o al `design.md` de un cambio activo.

## Requirements

### Requirement: Crear solicitud interna

El sistema SHALL permitir crear una solicitud interna con titulo, descripcion, area solicitante y tipo.

#### Scenario: Solicitud valida

- WHEN una persona envia titulo, descripcion, area solicitante y tipo validos
- THEN el sistema registra la solicitud
- AND asigna un identificador unico
- AND deja la solicitud en estado inicial `nueva`

#### Scenario: Solicitud incompleta

- WHEN una persona intenta crear una solicitud sin un dato obligatorio
- THEN el sistema rechaza la solicitud
- AND informa que dato falta

### Requirement: Consultar solicitud interna

El sistema SHALL permitir consultar una solicitud existente por su identificador.

#### Scenario: Solicitud existente

- WHEN una persona consulta una solicitud con un identificador existente
- THEN el sistema devuelve los datos de la solicitud
- AND muestra su estado actual

#### Scenario: Solicitud inexistente

- WHEN una persona consulta una solicitud con un identificador que no existe
- THEN el sistema informa que la solicitud no fue encontrada

## Que No Debe Ir Aqui

- Componentes internos, clases, tablas o librerias.
- Planes de implementacion.
- Decisiones de arquitectura.
- Notas temporales o preguntas abiertas.
- Reglas que aun no fueron aprobadas.

Para cambios propuestos usa `openspec/changes/<change-id>/`. Para arquitectura estable usa `docs/architecture/system.md`. Para decisiones durables usa `decisions/`.

## Checklist de Calidad

- La capacidad gobernada se entiende sin leer codigo.
- Cada requirement expresa una obligacion observable del sistema.
- Cada scenario tiene condicion y resultado.
- Los casos rechazados estan cubiertos cuando afectan al usuario.
- La spec no duplica arquitectura ni tareas.
