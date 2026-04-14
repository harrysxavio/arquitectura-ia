<!-- converted from arquitectura-IA-source.docx -->

Propuesta optimizada en marco general

La propuesta general más sólida para convertir esto en una guía completa es organizar todo en 7 módulos de manual, en este orden.


# CAPITULO 0
## Módulo 1. Principios rectores y marco de decisión
Aquí se define:
qué problema resuelve el framework
qué entra al núcleo y qué no
cómo evaluar una herramienta nueva
cómo decidir si algo debe ser agente, skill, workflow o simple documentación
cómo evitar sobreingeniería
Este módulo será la “constitución” de toda la guía.
## Módulo 2. Arquitectura troncal del framework
Aquí se define el marco operativo oficial:
framework global personal
plantilla de proyecto
capas del sistema
separación entre contexto estable, operativo y decisiones
flujo estándar del trabajo con IA
Este módulo responde: cómo está estructurado el sistema completo.

## Módulo 3. Herramientas oficiales del stack
Aquí entran, una por una:

En este módulo iremos herramienta por herramienta con:
Qué es
Para qué sirve
Cuándo usarla
Cuándo no usarla
Costo si aplica
Dónde obtenerla
Configuración base
Relación con el framework

## Módulo 4. Sistema de contexto, memoria y documentación
Aquí se explica:
AGENTS.md
PROJECT_GUIDE.md
CONTEXT_INDEX.md
decision_log.md
project_facts.md
skills
workflows
memoria reusable
cómo comprimir contexto
cómo evitar leer todo el proyecto
Este módulo será crítico, porque aquí está el ahorro real de tokens y la calidad del trabajo.

## Módulo 5. Ejecución operativa con agentes
Aquí definimos:
manager
coder
reviewer
debugger
Y resolvemos de forma limpia:
Qué hacen
Qué leen primero
Qué no deben leer
Cuándo se activan
Cómo se relacionan con skills y workflows
Cómo se evita la duplicación de contexto

## Módulo 6. Delivery, deploy y operación
Aquí se explica:
GitHub flow
branches
PR
CI/CD
Docker
Vercel
Supabase
variables de entorno
testing
observabilidad
Sentry
despliegue mínimo viable
cómo pasar de proyecto local a app usable

## Módulo 7. Roadmaps por nivel
Aquí recién lo aterrizamos para distintos perfiles:
Principiante total
Técnico intermedio
Creador de bots y automatizaciones
Constructor de apps/SaaS
Framework avanzado
Este módulo evita que la guía quede solo como referencia técnica y la vuelve utilizable.

# CAPITULO 1: Marco general optimizado oficial

## Documento maestro de la guía
Este documento establece el marco oficial para construir, operar y evolucionar un sistema de trabajo con IA orientado a desarrollo, automatización, análisis técnico y creación de productos digitales. Su objetivo es servir como base estable para personas principiantes, perfiles intermedios y usuarios avanzados, manteniendo una misma lógica operativa, aunque cambien las herramientas, los modelos o el tipo de proyecto.
La base conceptual de este marco retoma y depura los principios ya levantados en tu documento: la calidad debe depender del sistema y del contexto, no del modelo más caro; debe existir una gobernanza clara; y el framework debe separar la capa global personal de la plantilla de cada proyecto.

## 1. Propósito del framework
Este framework existe para resolver un problema muy concreto: hoy es posible trabajar con muchas herramientas de IA, muchos modelos y muchas plataformas, pero sin una estructura clara eso produce desorden, gasto innecesario, prompts pobres, duplicación documental y resultados inconsistentes. El propósito de este marco no es “tener más herramientas”, sino construir un sistema donde el usuario pueda trabajar con claridad, con bajo desperdicio de contexto, con buena trazabilidad y con una ruta de crecimiento realista.
El framework debe permitir:
Programar con apoyo de IA sin depender de improvisación constante
Entender repositorios grandes con menos fricción
Ejecutar cambios con criterio
Automatizar tareas repetitivas
Investigar documentación extensa
Desplegar aplicaciones y servicios cuando haga falta
Mantener memoria útil del proyecto
Cambiar de herramienta o proveedor sin romper la lógica del sistema

## 2. Principio rector oficial
La regla principal de este framework es la siguiente:
La calidad del resultado no debe depender del modelo. Debe depender del sistema.
Eso significa que un modelo menos potente o más barato puede rendir bien si:
Recibe una tarea bien acotada
Accede solo al contexto que necesita
Trabaja bajo reglas explícitas
No necesita adivinar cómo está organizado el proyecto
Existe una fuente de verdad clara
Las decisiones previas ya están registradas
El sistema lo obliga a operar con disciplina
Este principio también implica lo contrario: incluso un modelo muy potente puede rendir mal si el proyecto está desordenado, la documentación se contradice, no hay criterio de contexto y nadie sabe qué archivo consultar primero.

## 3. Qué problema resuelve este marco
Este framework está diseñado para resolver estos problemas estructurales:
### 3.1 Exceso de contexto
Evita cargar documentos por disponibilidad. El sistema debe cargar contexto por necesidad.
### 3.2 Prompts pobres o inconsistentes
El usuario no debería depender de escribir prompts complejos en cada tarea. El sistema debe traducir intención a ejecución.
### 3.3 Caos documental
La documentación debe estar separada por función y no duplicar información.
### 3.4 Pérdida de memoria del proyecto
Las decisiones importantes no deben quedar enterradas en chats o mensajes dispersos.
### 3.5 Uso arbitrario de herramientas
No toda herramienta popular mejora el framework. Toda incorporación debe justificarse.
### 3.6 Dificultad para retomar proyectos
El sistema debe permitir retomar un proyecto sin reconstruir el contexto desde cero.
### 3.7 Dependencia excesiva del usuario experto
El framework debe ayudar a que una persona principiante o intermedia pueda operar con orden creciente y no solo a quien ya sabe “cómo pedirle bien” a la IA.

## 4. Objetivo operativo oficial
El objetivo operativo del framework es que el usuario piense principalmente en qué necesita lograr, mientras el sistema se encarga de:
Interpretar la intención
Clasificar el tipo de tarea
Elegir el contexto mínimo
Decidir qué herramienta usar
Decidir qué modelo conviene
Ejecutar con un flujo repetible
Revisar si hace falta
Actualizar memoria o decisiones cuando corresponda
En términos prácticos, el framework debe producir estos resultados:
Menos consumo inútil de tokens
Menos retrabajo
Más consistencia entre código, documentación y decisiones
Mejor capacidad de escalar a varios proyectos
Mejor capacidad de cambiar entre herramientas
Mejor ruta de aprendizaje y operación real

## 5. Alcance oficial del framework
Este marco cubre cinco ámbitos:
### 5.1 Trabajo técnico diario
Incluye programación, refactorización, debugging, lectura de repos y documentación técnica.
### 5.2 Automatización
Incluye bots, flujos programados, integraciones, automatización web y procesos repetitivos.
### 5.3 Research y análisis
Incluye lectura de documentación extensa, compresión de información, comparación de fuentes y preparación de contexto.
### 5.4 Construcción de aplicaciones y SaaS (Software as a service)
Incluye estructura base para Frontend, Backend, base de datos, Auth, testing, observabilidad y despliegue.
### 5.5 Gobierno del sistema
Incluye reglas, memoria, decisiones, skills, workflows y criterios de adopción de herramientas.

## 6. Qué no es este framework
Este framework no es:
Una colección de herramientas de moda
Un sistema que dependa de un proveedor específico
Un catálogo de prompts sueltos
Una arquitectura pensada para impresionarte con complejidad
Un sistema multiagente inflado
Un reemplazo de criterio técnico
Un intento de meter desde el inicio todo lo que “podría ser útil algún día”

## 7. Decisiones oficiales de simplificación
Para mantener este marco usable en la práctica, se adoptan estas decisiones oficiales:
### 7.1 Un solo agente principal por proyecto
El framework permite Cline o Codex, pero no se asume que ambos deben gobernar el mismo proyecto al mismo tiempo. El documento comparativo incluido en el adjunto ya separa bien sus roles: Codex como opción muy equilibrada si quieres un solo núcleo y ya trabajas en OpenAI; Claude Code/Cline como opción más fuerte cuando importa más la estructura y el razonamiento profundo; y OpenCode como capa opcional de flexibilidad, no como martillo obligatorio inicial.
### 7.2 Pocos agentes reales
Los agentes oficiales del sistema serán pocos y claros:
Manager
Coder
Reviewer
Debugger
Todo lo demás debe resolverse, en la mayoría de los casos, con skills o workflows.
Nota, los subagentes deben existir como capacidad opcional de nivel 2, no como estructura obligatoria del marco general. Los subagentes pueden incorporarse como capacidad opcional de nivel avanzado cuando exista una necesidad clara de especialización o paralelización, especialmente en:
Análisis de repos grandes
Research técnico
Exploración de módulos
Revisiones separadas por dominio
Tareas multiárea de alto impacto
Los subagentes no deben crearse por defecto. Antes de crear uno, debe evaluarse si la necesidad se resuelve mejor con:
Una skill
Un workflow
Una mejora en la política de contexto.
Un subagente solo se justifica si:
Reduce carga mental real
Evita leer contexto innecesario
Devuelve un resultado comprimido y útil
No duplica el rol de otro agente
Mejora el flujo más de lo que aumenta la complejidad

Por qué no deben ser base obligatoria
Porque en un framework que busca ser:
Usable por principiantes
Sostenible
Barato en contexto
Claro en gobernanza

Meter subagentes desde el marco troncal genera varios riesgos:
1. Aumenta complejidad demasiado pronto
Un principiante todavía está tratando de entender:
Qué hace el manager
Qué hace el coder
Cómo se usa una skill
Cómo se carga contexto
Si además agregas 6 subagentes especialistas, el marco deja de ser pedagógico y pasa a ser confuso.
2. Duplica responsabilidades
Muchas veces lo que se llama “subagente especialista” en realidad debería ser:
Una skill
Un workflow
Una regla de contexto.
Ejemplo:
“subagente de testing”
“subagente de documentación”
“subagente de deploy”
En muchos casos eso no necesita ser un subagente. Basta con:
Un workflow de testing
Una skill de documentación
Una skill de deploy
3. Puede inflar el contexto en vez de reducirlo
En teoría, un subagente reduce carga porque toma una parte del trabajo.
En práctica, si está mal diseñado:
Lee demasiadas cosas
Devuelve reportes demasiado largos
Hace que el manager tenga que coordinar más de la cuenta
Terminas gastando más tokens, no menos.
4. Complica gobernanza
Cada subagente adicional exige definir:
Activación
Inputs
Límites
Outputs
Fallback
Relación con skills,
Relación con decisiones previas
Política de modelo
Eso es correcto si el retorno existe. Si no, es sobreingeniería.

Cuando sí tienen valor real:
Sí hay escenarios donde los subagentes mejoran mucho el flujo.
1. Repositorios grandes
Cuando tienes que revisar:
Varios módulos
Dependencias cruzadas
Rutas de ejecución largas
Zonas de alto impacto
un subagente explorador sí puede servir para:
Mapear módulos
Detectar hotspots
Resumir dependencias
Comparar dos implementaciones
2. Tareas paralelizables
Ejemplo:
Uno revisa Backend
Otro revisa Frontend
Otro revisa test
luego el manager consolida
Aquí sí hay ganancia real.
3. Research técnico previo
Un subagente puede investigar:
Documentación
Repo externo
Patrón de arquitectura
Librería nueva
y devolver un resumen comprimido al manager o al coder.
4. Validaciones separadas
En cambios importantes, puede tener sentido que haya un subagente que haga solo:
Revisión de diff
Revisión de seguridad
Revisión de compatibilidad
Pero aquí hay que tener cuidado: muchas veces eso puede seguir siendo un reviewer con una skill especializada, no necesariamente otro subagente fijo.

### 7.3 Contexto mínimo por defecto
El sistema debe trabajar primero con guía, índice y tarea activa. Cargar más contexto debe ser una decisión, no una costumbre.
### 7.4 Una sola fuente de verdad por tipo de información
Lo activo vive en tasks/
Las decisiones viven en decisions/
Los hechos del proyecto viven en memory/
La guía estructural vive en PROJECT_GUIDE.md
La ruta de consulta vive en CONTEXT_INDEX.md
### 7.5 El framework global no debe confundirse con cada proyecto
Debe existir una capa global reusable y una capa local por proyecto. Esa distinción ya aparece bien encaminada en este documento y aquí queda oficializada.

## 8. Arquitectura oficial del sistema
La arquitectura oficial queda dividida en dos grandes niveles.
### 8.1 Nivel A: framework global personal
Es tu sistema operativo de trabajo con IA.
Su función es almacenar:
Reglas globales
Política de modelos
Política de herramientas
Skills reutilizables
Workflows reutilizables
Plantillas
Memoria personal reusable
Scripts de bootstrap y auditoría

No debe contener:
Tareas activas de un proyecto
Bugs de un proyecto específico
Decisiones locales de un repositorio

### 8.2 Nivel B: proyecto individual
Es la implementación concreta de un producto, bot, scraper, app, API o automatización.
Su función es almacenar:
La guía del proyecto
El índice de contexto
La tarea activa
Las decisiones del proyecto
La memoria local
El código
Los tests
La infraestructura y el delivery
Esta separación es obligatoria porque permite mantener estabilidad global sin contaminarla con ruido operativo local.

## 9. Capas oficiales del framework
La guía final trabajará sobre estas capas oficiales, simplificadas respecto del material original pero manteniendo su lógica correcta.
### 9.1 Capa de gobernanza
Define el orden, las reglas, la jerarquía documental y la política de adopción de herramientas.
### 9.2 Capa de contexto estable
Define la identidad técnica y funcional del proyecto:
Propósito
Alcance
Restricciones
Overview
Integraciones
Estándares
### 9.3 Capa de contexto operativo
Define lo que se está haciendo ahora:
Tarea activa
Plan,
Preguntas abiertas
Backlog si aplica
### 9.4 Capa de decisiones
Registra lo ya decidido para no rediscutirlo ni romperlo sin advertencia.
### 9.5 Capa de ejecución
Es donde entran agentes, skills, workflows y la lógica de trabajo asistido.
### 9.6 Capa de delivery e infraestructura
Incluye testing, CI/CD, Docker, despliegue, auth, backend, hosting y observabilidad.

## 10. Reglas oficiales de contexto
Estas reglas quedan adoptadas como norma central del framework.
Cuando hablamos de contexto, no estamos hablando solo de “texto que le pasas a la IA”.
En este marco, contexto es el conjunto de información que el sistema decide mostrarle al agente o al modelo para que pueda resolver una tarea correctamente.
Eso incluye, por ejemplo:
- Qué proyecto es
- Qué se está haciendo ahora
- Qué reglas técnicas debe respetar
- Qué decisiones ya fueron tomadas
- Qué archivos son relevantes
- Qué no debe tocar
- Cuál es el resultado esperado
O sea, el contexto no es “todo lo que existe”. Es solo lo que hace falta para resolver bien una tarea específica.
### 10.1 Regla de oro
No cargar contexto por disponibilidad. Cargar contexto por necesidad.
Porque el problema más común al trabajar con IA en proyectos técnicos es este:
O le das muy poco contexto, y responde genérico o se equivoca
O le das demasiado contexto, y responde peor, más lento, más caro y con más ruido
Entonces, el objetivo del framework no es “meter más contexto”. El objetivo es dar el contexto correcto, en la cantidad correcta, en el momento correcto. Esa es la diferencia entre un sistema serio y una conversación improvisada.

### 10.2 Orden base de lectura
Por defecto, todo trabajo debe partir leyendo:
PROJECT_GUIDE.md (Qué es el proyecto)
CONTEXT_INDEX.md (Cómo está organizado)
tasks/current/active_task.md (Qué se está haciendo ahora)
Luego, solo si hace falta:
- Una skill
- Un workflow
- Uno o dos documentos técnicos concretos
- Una decisión previa relevante
Ejemplos:
Una skill de backend
Una guía de testing
Un archivo técnico puntual
Una decisión previa relevante
Aquí el contexto sigue siendo pequeño, pero ya está orientado a una necesidad concreta.
Ejemplo:
si la tarea es “corregir un endpoint FastAPI”, además del contexto mínimo podría entrar:
skills/python-backend.md
docs/engineering/coding-standards.md
apps/api/app/api/routes/...

### Qué papel cumple CONTEXT_INDEX.md
Este archivo es muy importante porque actúa como mapa de acceso al contexto.
No explica todo el proyecto.
Lo que hace es decir:
Si la tarea es arquitectura, lee esto
Si es debugging, lee esto
Si es backend, lee esto
Si es deploy, lee esto
Si es testing, lee esto
Eso evita dos problemas:
Que el usuario tenga que recordar dónde estaba cada cosa
Que el agente “adivine” qué debería leer
O sea, CONTEXT_INDEX.md convierte un repo grande en un sistema navegable.
Qué pasa si no controlas el contexto
Si el contexto no está gobernado, pasan estas cosas:
- El agente toca cosas que no debía tocar, porque no tenía claro el alcance.
- Propone soluciones incompatibles, porque no leyó decisiones previas o restricciones.
- Gasta demasiado, porque siempre relee mucho más de lo necesario.
- El usuario termina compensando a mano, y vuelve a escribir Prompts largos explicando todo cada vez.
- Los modelos baratos rinden mal, no porque sean necesariamente malos, sino porque les estás dando un problema demasiado abierto y ruidoso.

### 10.3 Escalado de contexto
Se define una política de tres niveles:
Nivel mínimo: guía, índice, tarea activa
Nivel dirigido: skill + workflow + archivo técnico puntual
Nivel ampliado: varios documentos solo si la tarea es transversal, riesgosa o arquitectónica
### 10.4 Regla de compresión
Cuando una investigación o análisis largo ya produjo un entendimiento útil, debe convertirse en un artefacto comprimido reutilizable en vez de obligar al sistema a releer todo el material original.

## 11. Sistema oficial de ejecución
La ejecución oficial del framework sigue este flujo:
El usuario expresa una intención
El sistema clasifica el tipo de tarea
El manager decide el contexto mínimo
Se elige la skill o workflow adecuado
Se ejecuta con el agente o herramienta correspondiente
Se revisa si hace falta
Se actualiza memoria o decisiones si el trabajo cambió algo estructural

Eso significa que la interacción correcta no es “pedirle al agente que revise todo el repo” como hábito, sino darle una intención concreta y dejar que el sistema la traduzca con disciplina. Esa idea aparece con fuerza en tu documento y aquí queda oficializada como regla del marco.

## 12. Sistema oficial de agentes
El marco general adopta este conjunto oficial de agentes:
### 12.1 Manager
Es el orquestador. Interpreta intención, clasifica tarea, elige contexto, decide skill o workflow, propone modelo y deriva ejecución.
### 12.2 Coder
Implementa código, modifica archivos, refactoriza y aplica reglas técnicas.
### 12.3 Reviewer
Evalúa calidad, coherencia, riesgos, mantenibilidad y posibles efectos colaterales.
### 12.4 Debugger
Investiga fallos, ordena evidencia, construye hipótesis y busca causa raíz.
### 12.5 Regla de diseño
Cualquier nuevo agente debe demostrar que reduce fricción real y no solo que “suena bien”. Si una función puede resolverse mejor como skill o workflow, no debe convertirse en agente.

## 13. Sistema oficial de skills
Una skill es una guía operativa reutilizable para un tipo de trabajo. No es teoría general ni documentación ornamental.
Las skills oficiales mínimas del marco son:
Clasificación de tarea
Desarrollo backend
Revisión de cambios
Debugging
Resumen documental
Despliegue
Testing con playwright
Automatización con stagehand
Organización del proyecto
Mantenimiento del framework
Cada skill debe contener:
Objetivo
Cuándo usarla
Cuándo no
Entradas esperadas
Reglas
Checklist
Errores comunes
Formato de salida esperado

## 14. Sistema oficial de workflows
Un workflow es una secuencia repetible de pasos. Debe existir para procesos que se repiten y que conviene ejecutar siempre con el mismo criterio.
Los workflows base oficiales son:
Spec
Implementation
Debugging
Research
Documentation-update
Memory-update
Deploy
PR-Review
E2E-validation
Su función es transformar intención difusa en ejecución consistente.

## 15. Política oficial de herramientas
### 15.1 Regla maestra
Ninguna herramienta entra al framework si no responde claramente:
Qué problema resuelve
Qué reemplaza o complementa
Qué complejidad agrega
Qué complejidad reduce
Si compite con otra ya aprobada
Y si mejora realmente el retorno del sistema. Esta lógica ya estaba muy bien planteada en tu documento y se adopta aquí como política oficial.
### 15.2 Herramientas núcleo aprobadas
El núcleo general del framework queda compuesto por:
Vs code
Git
Github
Un agente principal
Markdown versionado
Python
Sql/postgres
Docker básico
### 15.3 Herramientas recomendadas
Según tu documento consolidado, el stack recomendado para desarrollos futuros queda bien definido así:
FastAPI para backend
React + Next.js + TypeScript para frontend
Supabase + Postgres para backend/data/auth liviano
Vercel para frontend
GitHub Actions para CI/CD
NotebookLM para research
n8n para automatización
Playwright como base de web automation/testing
Stagehand como capa especializada encima o al lado de Playwright
### 15.4 Herramientas opcionales de etapa 2
OpenCode
OpenRouter
Gemini CLI
Firebase
Cloudflare
Hostinger VPS
Sentry
Clerk/Auth0/Stripe, según producto
### 15.5 Herramientas fuera del núcleo
No entran al núcleo inicial:
Antigravity
ECC completo
Kubernetes
Airflow
RAG/embeddings por defecto
Obsidian como fuente de verdad
microservicios tempranos
múltiples clouds sin necesidad

### 16. Política oficial de apps, SaaS y deploy
La ruta principal recomendada para apps y SaaS queda oficialmente así:
Frontend: Next.js + React + TypeScript
Backend: FastAPI
Base de datos: Postgres
Plataforma de soporte: Supabase
Despliegue frontend: Vercel
Empaquetado/portabilidad: Docker
CI/CD: GitHub Actions
Observabilidad: Sentry en etapa posterior
Billing: Stripe si el producto cobra

La regla oficial es:
no empezar con microservicios
No empezar con kubernetes
No meter auth compleja ni múltiples clouds antes de validar flujo y producto.

## 17. Política oficial sobre Playwright y Stagehand
Esta decisión queda formalmente fijada así:
Playwright es el estándar base para testing E2E y automatización robusta.
Stagehand es una capa especializada para exploración web, scraping semántico y flows más frágiles o cambiantes.
Stagehand no reemplaza Playwright.
Playwright no tiene por qué resolver solo todos los casos de navegación incierta.
Esta combinación ya estaba bien razonada en el documento y se convierte aquí en política oficial del framework.

## 18. Política oficial sobre modelos
La guía final deberá trabajar con una política de tres niveles:
### 18.1 Modelos baratos o locales
Para:
Clasificación
Resumen
Extracción de estructura
Preprocesamiento
Primer borrador
### 18.2 Modelos medios
Para:
Implementación normal
Revisión de cambios
Debugging moderado
### 18.3 Modelos premium
Para:
Arquitectura
Refactors grandes
Debugging difícil
Decisiones delicadas
Análisis transversal complejo
La conclusión estratégica del documento también apunta en esa dirección: no conviene perseguir el “modelo perfecto” como si eso sustituyera el sistema.

## 19. Política oficial de crecimiento
El framework debe crecer por etapas.
### Fase 1. Fundaciones
Estructura
Guía
Índice
Tarea activa
Decision log
Memoria básica
Skills mínimas
Workflows mínimo
### Fase 2. Ejecución operativa
Agente principal
Reviewer
Debugging
Uso real diario del sistema
### Fase 3. Automatización y delivery
GitHub Actions
Docker
deploy
n8n
testing E2E
Stagehand cuando se justifique
### Fase 4. Escala
observabilidad
auth más sofisticada
SaaS completo
modelos locales mejor integrados
tooling opcional de etapa 2

## 20. Criterio oficial de éxito del framework
El framework se considerará bien implementado si logra esto:
el usuario no necesita recordar todo para retomar un proyecto,
el sistema no depende de un solo proveedor,
el contexto cargado es pequeño pero suficiente,
las decisiones ya no se pierden,
el trabajo diario es más rápido y menos caótico,
el código, la documentación y la memoria quedan alineados,
el costo del razonamiento baja,
y el sistema puede crecer sin rehacerse entero.

## 21. Cierre oficial
La conclusión oficial del marco es esta:
No se debe construir un proyecto donde la IA tenga que adivinar el sistema. Se debe construir un sistema donde la IA solo tenga que ejecutar bien.
Ese principio resume correctamente tanto el espíritu de tu documento como la versión optimizada que conviene convertir en guía.

# Capítulo 2: Herramientas núcleo oficiales del framework

Este capítulo define las herramientas base del framework y fija qué función cumple cada una, cuándo entra, cuándo no, qué costo puede tener y cómo se conecta con el resto del sistema.
La lógica sigue el marco general ya aprobado: el framework no se diseña para “tener muchas herramientas”, sino para que cada pieza cumpla una función clara dentro de una arquitectura estable.

## 2.1 Principio de adopción de herramientas
Una herramienta entra al framework solo si responde bien estas preguntas:
Qué problema resuelve
Qué reemplaza o complementa
Qué complejidad agrega
Qué complejidad reduce
Si duplica otra herramienta ya presente
Y si mejora el retorno del sistema más de lo que aumenta su mantenimiento
Por eso este capítulo no presenta un catálogo de opciones “interesantes”, sino un Stack oficial con prioridades claras.

## 2.2 Clasificación oficial de herramientas
El framework divide las herramientas en 4 grupos.
### A. Núcleo obligatorio
Sin estas piezas, el framework pierde orden o no puede operar bien.
VS Code
Git
GitHub
Agente principal (Cline, Codex, etc)
Markdown versionado dentro del repo
### B. Núcleo recomendado
No son estrictamente obligatorias el día 1, pero sí forman parte del camino oficial del framework.
Aider
NotebookLM
n8n
### C. Herramientas de ejecución y delivery
Entran cuando ya estás construyendo software, automatizaciones o apps de forma seria.
GitHub Actions
Playwright
Stagehand
Docker
FastAPI
Next.js
TypeScript
Postgres
Supabase
Vercel
### D. Herramientas opcionales de etapa 2
Se usan si existe un caso concreto.
OpenCode
OpenRouter
Gemini CLI
Sentry
Clerk / Auth0 / Stripe
Hostinger VPS
Cloudflare
### Tabla rápida de decisión (herramientas núcleo)


## 2.3 VS Code
Qué es
Es la superficie visual principal del framework (IDE). VS Code integra edición de código, terminal, extensiones y control de código fuente. Su documentación oficial muestra que incluye vista de Source Control, staging, commits, revisión de cambios, resolución de conflictos y flujo integrado con Git/GitHub.
Para qué está definido
Su función oficial dentro del framework es ser el centro operativo diario:
Editar código
Abrir documentación del proyecto
Revisar diffs
Usar el terminal
Ejecutar scripts
Trabajar con agentes
Y mantener el repo ordenado en una sola superficie
Cuándo usarlo
Siempre. Es la base visual del sistema.
Cuándo no usarlo
No hay una alternativa mejor como núcleo para este framework en esta etapa. Podrás sumar otras superficies luego, pero no reemplazarlo al inicio.
Costo
VS Code se distribuye sin costo de licencia para uso general desde Microsoft.
Dónde obtenerlo
Desde el sitio oficial de Visual Studio Code.
Configuración base recomendada
Instalar Git antes o junto con VS Code
Activar terminal integrada
Trabajar siempre en repos Git
Usar extensiones solo cuando tengan función clara
Abrir siempre el proyecto desde la raíz del repo
Motivo de inclusión
Porque reduce fricción, centraliza herramientas y encaja muy bien con el enfoque documental y agentic del framework.

## 2.4 Git
Qué es
Es el sistema de control de versiones que permite seguir cambios, crear ramas, comparar versiones y revertir trabajo.
Para qué está definido
Dentro del framework, Git no es opcional. Su función es:
Preservar trazabilidad
Permitir revisión real
Hacer rollback
Sostener ramas de trabajo
Y servir de base para ci/cd, prs y colaboración
Cuándo usarlo
Siempre, desde el día 1 de cualquier proyecto.
Cuándo no usarlo
Nunca debería omitirse en un proyecto serio dentro de este framework.
Costo
Git es software libre y gratuito.
Motivo de inclusión
Sin Git, el framework no tiene memoria técnica confiable del código.

## 2.5 GitHub
Qué es
Es la plataforma principal de hosting de repositorios, colaboración, PRs, issues y automatización del framework.
Para qué está definido
Su función oficial es ser la columna vertebral colaborativa y operativa:
Repos remotos
Pull request
Issues
Templates
Workflows
CI/CD con GitHub Actions
Cuándo usarlo
Desde que el proyecto deja de ser un experimento aislado.
Cuándo no usarlo
Solo si existe una restricción corporativa que obligue a otro hosting. Aun así, el patrón de trabajo seguiría siendo equivalente.
Costo
GitHub tiene planes gratuitos y de pago, pero para la base del framework suele bastar iniciar con el plan gratuito para repos y flujo de trabajo básico.
Motivo de inclusión
Porque acelera el trabajo con issues, ramas, PRs y despliegue sin requerir infraestructura propia compleja.

## 2.6 Git worktree
Qué es
Es una capacidad de Git que permite tener varios working trees del mismo repositorio asociados a distintas ramas al mismo tiempo. La documentación oficial de Git lo describe como una forma de administrar múltiples working trees conectados al mismo repo.
Para qué está definido
Dentro del framework sirve para:
Trabajar en dos ramas a la vez
Aislar exploraciones
Revisar una versión estable mientras desarrollas otra
Evitar estar cambiando de rama dentro de la misma carpeta
Cuándo usarlo
Cuando el proyecto ya tiene al menos dos frentes de trabajo paralelos o cuando quieres revisar una rama sin alterar tu working tree principal.
Cuándo no usarlo
No hace falta para quien todavía está aprendiendo Git básico o trabaja en tareas muy lineales.
Costo
No tiene costo adicional; viene como parte de Git.
Motivo de inclusión
Porque mejora el flujo avanzado sin introducir otra herramienta externa.

## 2.7 Cline
Qué es
Es un agente de desarrollo orientado a IDE con capacidades como Memory Bank, reglas y subagents. La documentación pública y material asociado destacan precisamente Memory Bank y Subagents como capacidades relevantes, aunque estos últimos se consideran experimentales.
Para qué está definido
Cline entra como agente principal opcional A dentro del framework. Su función es:
Operar sobre el repo
Leer contexto persistente
Seguir reglas
Beneficiarse de una memoria estructurada
Y apoyar flujos más gobernados y modulares
Cuándo elegirlo
Elígelo si priorizas:
Memoria estructurada
Documentación viva
Reglas por proyecto
Y posibilidad futura de subagentes especializados
Cuándo no elegirlo
No lo elegiría como núcleo si tu prioridad absoluta es la simplicidad operativa y quieres menos decisiones de configuración.
Costo
El costo depende del modelo o proveedor que conectes detrás de Cline. La herramienta en sí no fija un único proveedor como costo base.
Dónde obtenerlo
Desde su ecosistema y documentación oficial de Cline.
Configuración base recomendada
Usarlo sobre un repo Git
Definir AGENTS.md
Mantener una carpeta de memoria o documentación equivalente
Empezar sin subagentes
Y usarlo solo después de tener PROJECT_GUIDE.md y CONTEXT_INDEX.md.
Motivo de inclusión
Porque encaja muy bien con un framework que quiere gobernanza documental y contexto persistente.

## 2.8 Codex
Qué es
Codex es el agente de desarrollo de OpenAI. La documentación oficial indica que puede leer, editar y ejecutar código, y que su extensión para VS Code permite usarlo dentro del IDE o delegar tareas a Codex Cloud. También indica que está incluido en planes ChatGPT Plus, Pro, Business, Edu y Enterprise.
Para qué está definido
Codex entra como agente principal opcional B. Su función dentro del framework es:
Trabajar directamente sobre el código
Avanzar tareas de desarrollo
Entender código ajeno
Y reducir fricción si ya operas dentro del ecosistema openai
Cuándo elegirlo
Elígelo si priorizas:
Simplicidad
Menor fricción
Integración con openai
Y rapidez de arranque
Cuándo no elegirlo
No lo tomaría como principal si tu prioridad absoluta es diseñar un framework más artesanal de reglas, memoria y orquestación documental.
Costo
Está incluido en varios planes pagados de ChatGPT, según la documentación oficial de OpenAI.
Dónde obtenerlo
Desde la documentación oficial de OpenAI Codex IDE extension.
Configuración base recomendada
Usarlo dentro de VS Code
Acotarlo a proyectos con buena estructura documental
No mezclarlo como “segundo cerebro principal” si ya definiste Cline como núcleo
Y operarlo sobre repos Git limpios
Motivo de inclusión
Porque es una de las mejores rutas para productividad práctica cuando ya estás dentro del stack OpenAI. El propio documento adjunto también lo deja bien posicionado como opción equilibrada si se busca una sola herramienta principal.

## 2.9 Cline vs Codex: decisión oficial
El framework no obliga uno de los dos, pero sí obliga a elegir uno como principal.
Elige Cline si:
Quieres memoria estructurada y persistente
Te importa más la gobernanza documental
Quieres una base más amigable para evolución agentic
Elige Codex si:
Ya usas OpenAI/ChatGPT
Quieres menos fricción
Quieres un camino más rápido a ejecución práctica
Regla oficial
No usar ambos como cerebro principal del mismo proyecto.
Puedes probar ambos en distintos proyectos o en laboratorio, pero el proyecto operativo debe tener una sola herramienta principal de agente.

Nota: No se descarta Claude Code ni OpenCode porque fueran peores, sino porque esta optimizado el framework para tener solo dos caminos base muy claros y fáciles de gobernar:
Cline como camino orientado a memoria, reglas, skills, workflows y contexto estructurado. Cline documenta explícitamente capacidades como Memory Bank, Rules, Skills, Workflows y Subagents.
Codex como camino orientado a simplicidad operativa, integración con OpenAI y ejecución directa dentro del IDE o vía Codex Cloud. OpenAI lo describe como un agente que puede leer, editar y ejecutar código, y que se usa desde la extensión del IDE o delegando tareas a la nube.
En ese marco:
Claude Code no queda fuera por falta de capacidad. De hecho, Anthropic lo presenta como una herramienta agentic que lee la base de código, edita archivos, ejecuta comandos e integra con terminal, IDE, app de escritorio y navegador, además de soportar skills, subagents y archivos de configuración jerárquicos como CLAUDE.md y .claude/settings.json. No se coloca en el núcleo inicial porque, para el manual, ya tiene cubierto ese carril “agente principal fuerte” con Codex como opción de simplicidad/productividad y con Cline como opción de gobernanza/contexto. Incluir Claude Code además de esos dos volvía el núcleo más confuso sin aumentar proporcionalmente el valor pedagógico del marco.
OpenCode tampoco queda fuera por debilidad. Al contrario, OpenCode soporta 75+ proveedores, modelos locales, AGENTS.md, agents, subagents, skills, commands, configuración por proyecto y permisos finos. No está como base principal porque su mayor valor está en la flexibilidad y soberanía técnica, no en ser la ruta más simple de arranque. Para un framework que quiere servir desde principiante hasta avanzado, OpenCode encaja mejor como capa opcional de etapa 2 o como laboratorio multi-provider, no como primera decisión obligatoria.
Dicho de forma directa:
Cline entró por su encaje natural con un framework documental y gobernado.
Codex entró por su encaje natural con un flujo simple y productivo dentro de OpenAI.
Claude Code es una alternativa real y fuerte, pero compite más con Codex que con Cline.
OpenCode es una plataforma flexible y poderosa, pero compite más como capa de orquestación abierta que como “martillo único” inicial.
El punto 2.9 no buscaba elegir “la mejor herramienta absoluta”
Buscaba definir dos rutas base simples para el framework:
Una ruta gobernada y documental → Cline
Una ruta simple y productiva → Codex
Eso hace el manual más enseñable y menos ambiguo.
framework prioriza claridad de adopción, el costo principal no es solo dinero. También es:
Complejidad mental
Tiempo de setup
Cantidad de decisiones
Duplicación de patrones

## 2.10 Aider
Qué es
Aider es una herramienta de pair programming por terminal que trabaja sobre el repo local. Su documentación oficial destaca que se usa para editar código dentro del repo Git y que ofrece comandos como /add, /model y modos como code, architect y ask. Además, su integración con Git confirma que, cuando edita archivos, hace commits descriptivos automáticamente para facilitar revisión y undo. También recomienda explícitamente no cargar demasiados archivos al chat y ser selectivo.
Para qué está definido
Aider no entra como cerebro principal del framework, sino como herramienta secundaria de edición controlada.
Su función es:
Hacer cambios puntuales
Trabajar con diffs limpios
Facilitar rollback
Editar pocos archivos de forma enfocada
Cuándo usarlo
Refactors pequeños o medianos
Cambios quirúrgicos
Trabajo donde quieras control claro del diff
Escenarios donde el agente principal sería demasiado pesado
Cuándo no usarlo
Si todavía no trabajas en Git
Si la tarea necesita más coordinación global del proyecto que edición puntual
Si intentas usarlo como reemplazo total del framework
Costo
Aider es abierto y el costo real depende del modelo o proveedor que conectes detrás.
Dónde obtenerlo
Desde la documentación oficial de Aider.
Configuración base recomendada
Repo Git limpio,
Pocos archivos cargados por tarea,
Usarlo como herramienta quirúrgica, no como sistema completo.
Motivo de inclusión
Porque añade una capa muy útil de edición enfocada y reversible.

## 2.11 NotebookLM
Qué es
NotebookLM es una herramienta de investigación de Google. Su sitio oficial la describe como una herramienta de investigación y “thinking partner” capaz de analizar tus fuentes y convertir complejidad en claridad. La versión pública también destaca que puede trabajar con varias clases de fuentes, incluidos PDFs, sitios web, videos de YouTube, audio y documentos de Google.
Para qué está definido
Dentro del framework, NotebookLM vive en la capa de research, no en la memoria viva del repo.
Su función es:
Resumir documentación extensa
Analizar corpus de investigación
Comparar fuentes
Preparar contexto comprimido antes de pasar al agente principal
Cuándo usarlo
Manuales largos
PDFs
Documentación externa
Análisis previos
Investigación de tema o mercado
Repos externos explicados en contenido documental
Cuándo no usarlo
Como fuente oficial del proyecto
Como reemplazo de PROJECT_GUIDE.md
Como sustituto de decision_log.md
Como bitácora operativa diaria
Costo
NotebookLM tiene versión pública accesible con cuenta Google. Existen planes ampliados asociados a Google One AI Premium y entornos empresariales/educativos, aunque el capítulo detallado de costos conviene consolidarlo cuando veamos herramientas ampliadas y opciones pagadas.
Dónde obtenerlo
Desde el sitio oficial de NotebookLM.
Configuración base recomendada
Separar notebooks por dominio
No mezclar un único notebook con todo
Exportar o resumir resultados clave al repo como contexto comprimido
Motivo de inclusión
Porque reduce drásticamente el costo cognitivo de research sin contaminar la memoria viva del proyecto.

Nota: Obsidian (app flexible para notas privadas, almacenadas localmente en archivos Markdown, con plugins, enlaces entre notas, grafo y opción de sincronización segura y publicación.) no forma parte del núcleo operativo del framework, pero puede incorporarse como herramienta satélite de conocimiento personal. Su rol se desarrolla en el capítulo de contexto, memoria y conocimiento satélite. Se excluye del núcleo operativo porque su rol correcto no es competir con la documentación oficial del proyecto. Obsidian se aprueba como herramienta satélite de conocimiento personal, aprendizaje e investigación transversal

## 2.12 n8n
Qué es
n8n es una plataforma de automatización. Su página oficial de precios indica que todos los planes cloud incluyen usuarios y workflows ilimitados, y que el cobro se basa en ejecuciones mensuales. La documentación de Community Edition muestra que existe edición comunitaria autohospedada y que puede registrarse para desbloquear funciones adicionales como folders, debug en editor y custom execution data.
Para qué está definido
Dentro del framework, n8n está definido como la capa de automatización externa.
Su función es:
Disparar flujos
Integrar sistemas
Automatizar procesos repetitivos
Ejecutar tareas programadas
Conectar correo, apis, hojas, bots y servicios
Cuándo usarlo
Procesos repetitivos
Integraciones entre herramientas
Bots de operación
Flujos programados
Sincronizaciones simples o medianas
Cuándo no usarlo
Lógica de negocio compleja que vive mejor en Python
Automatizaciones demasiado ambiguas
Cuando un simple script local resuelve mejor el problema
Costo
El pricing oficial cloud se basa en ejecuciones mensuales. La Community Edition existe y puede autohospedarse; la documentación oficial también detalla funciones adicionales que se desbloquean al registrar esa edición.
Dónde obtenerlo
Desde n8n oficial y su documentación.
Configuración base recomendada
No usarlo como sustituto de backend
Mantener workflows pequeños y trazables
Guardar lógica compleja fuera y llamar scripts/servicios cuando haga falta
Documentar cada flujo en el proyecto
Motivo de inclusión
Porque automatiza sin obligarte a construir una plataforma propia desde cero.

## 2.13 Relación entre estas herramientas
VS Code
Es la superficie.
Git + GitHub
Son la trazabilidad y la colaboración.
Cline o Codex
Son el agente principal.
Aider
Es la herramienta quirúrgica de cambios controlados.
NotebookLM
Es la capa de investigación.
n8n
Es la capa de automatización externa.
Esta separación es importante porque evita mezclar responsabilidades. El framework no quiere una única herramienta “que haga todo”, sino un sistema donde cada pieza tenga un rol claro.

## 2.14 Secuencia oficial de adopción
La secuencia recomendada de implementación de estas herramientas es:
VS Code
Git
GitHub
elegir Cline o Codex
Aider
NotebookLM
n8n
Ese orden mantiene bajo el costo de complejidad y evita instalar cosas antes de tener una base operativa.

## 2.15 Decisión oficial del capítulo 2
El capítulo 2 deja aprobadas como herramientas núcleo del framework:
VS Code como superficie visual,
Git + GitHub como base de control y colaboración,
Cline o Codex como agente principal,
Aider como herramienta secundaria de edición controlada,
NotebookLM como capa de research,
n8n como capa de automatización externa.
Y deja fijada esta regla:
el framework debe ser simple en el núcleo y especializado por capas, no una suma de herramientas que compiten entre sí.

# Capítulo 3: Herramientas de desarrollo, testing, backend y deploy

Este capítulo define el stack técnico oficial para construir software, automatizar navegación web, probar aplicaciones y desplegar entregables sin inflar la arquitectura. La regla central sigue siendo la misma del marco general: elegir herramientas por retorno operativo real, no por moda.

## 3.1 Objetivo del capítulo
Este capítulo existe para fijar qué herramientas usa el framework cuando deja de ser solo una estructura documental y pasa a construir:
Aplicaciones web
APIs
Bots
Automatizaciones
Scrapers
Flujos con interfaz
Productos tipo SaaS
Su objetivo no es listar “todo lo posible”, sino definir:
Qué herramienta cumple qué función
Cuándo entra
Cuándo no entra
Cómo se combina con el resto
Y cuál es el camino base recomendado

## 3.2 Principio oficial del stack técnico
La arquitectura oficial del stack sigue esta lógica:
Frontend simple, moderno y desplegable rápido
Backend claro, mantenible y amigable para Python
Testing fuerte y reproducible
Automatización web separada del testing
Deploy fácil al inicio
Portabilidad suficiente sin sobrediseño
Observabilidad cuando el producto ya merece monitoreo serio
Esto evita tres errores comunes:
Meter demasiadas piezas antes de validar valor,
Usar una herramienta compleja para resolver un problema simple,
O tratar Deploy, testing y automatización como si fueran lo mismo.

## 3.3 GitHub Actions
Qué es
GitHub Actions es la plataforma de automatización y CI/CD de GitHub. La documentación oficial la define como una plataforma de integración y entrega continuas que permite automatizar build, test y deployment directamente desde el repositorio.
Para qué está definido
Dentro del framework, GitHub Actions es la herramienta oficial para:
Correr test automáticamente
Validar Linting
Ejecutar pipelines al hacer Push o PR
Construir artefactos
Y desplegar cuando el proyecto ya tenga flujo de Release
Cuándo usarlo
Cuando el proyecto ya tiene repositorio estable
Cuando no quieres depender de correr todo manualmente
Cuando quieres bloquear errores antes del merging
Cuando empiezas a desplegar de forma repetible
Cuándo no usarlo
En prototipos de una tarde donde todavía no existe criterio mínimo de calidad,
Si aún ni siquiera tienes test o Build reproducible.
Costo
GitHub Actions tiene un modelo de uso incluido y escalable según plan y consumo, pero el detalle de cuotas depende del tipo de cuenta y runners. Para el marco base, lo importante es que es la opción nativa y más directa si ya usas GitHub.
Motivo de inclusión
Porque es la forma más simple de convertir el repositorio en un sistema que no solo guarda código, sino que también lo valida y lo mueve hacia producción.
https://github.com/features/actions

## 3.4 Playwright
Qué es
Playwright es un framework de automatización y testing end-to-end para aplicaciones web modernas. Su documentación oficial indica que soporta Chromium, WebKit y Firefox, que incluye runner, assertions, aislamiento, paralelización y tooling, y que está disponible para TypeScript, Python, Java y .NET.
Para qué está definido
Playwright es el estándar base oficial del framework para:
Pruebas E2E
Automatización web robusta
Scripts reproducibles
Validaciones en CI
Y verificación seria de interfaz
Cuándo usarlo
Cuando necesitas confiabilidad
Cuando el flujo debe ser repetible
Cuando quieres correr pruebas en CI
Cuando te importa control fino de selectores y eventos
Cuando la automatización es parte del producto o de la validación técnica
Cuándo no usarlo
Para una exploración muy abierta donde todavía ni siquiera entiendes bien la web
Cuando necesitas una capa más semántica y flexible para navegar sitios inestables
Buenas prácticas relevantes
Playwright recomienda usar locators porque tienen auto-waiting y retry-ability, y priorizar atributos de cara al usuario y contratos explícitos para que los tests sean más resilientes.
Costo
El framework es open source. El costo viene del entorno donde lo ejecutes, de la infraestructura de CI y de cualquier servicio externo de ejecución o almacenamiento de artefactos.
Motivo de inclusión
Porque da una base estable, reproducible y seria para testing y automatización web. Además, Playwright hoy ya se posiciona explícitamente también para scripting y workflows agentic, no solo para QA tradicional.
https://playwright.dev/

## 3.5 Stagehand
Qué es
Stagehand es un framework de automatización web con IA de Browserbase. La propia plataforma lo presenta como su framework open source más popular para automatización browser con IA, y su material reciente enfatiza que permite componer automatizaciones más resilientes con menos código manual y menos dependencia de selectores frágiles.
Para qué está definido
Dentro del framework, Stagehand está definido como una capa especializada de automatización semántica, no como reemplazo universal de Playwright.
Sirve para:
Scraping guiado por IA
Navegación semántica
Flujos donde el DOM cambia mucho
Automatizaciones más abiertas
Extracción o interacción cuando escribir selectores a mano sería demasiado costoso
Cuándo usarlo
Cuando la web es cambiante o frágil
Cuando el flujo es ambiguo
Cuando quieres acelerar prototipos de automatización web
Cuando necesitas extraer o actuar con menos rigidez
Cuándo no usarlo
Como base única de testing E2E
Cuando ya sabes exactamente qué elementos y flujos quieres validar
Cuando necesitas máxima reproducibilidad de CI
Costo
Stagehand como framework open source no impone por sí mismo el modelo de costo de Playwright. El costo real puede venir de servicios asociados, ejecución remota, sesiones browser y modelos utilizados según el tipo de implementación que montes. Browserbase además ofrece componentes de plataforma y runtime para despliegue browser-heavy, pero eso ya cae en una etapa más avanzada.
Motivo de inclusión
Porque resuelve bien el espacio donde Playwright puro puede volverse demasiado manual.
Política oficial:
Playwright = base
Stagehand = capa especializada
Esa decisión ya venía muy bien planteada en tu documento y aquí queda fijada oficialmente.
https://www.browserbase.com/stagehand

## 3.6 Docker
Qué es
Docker es la herramienta oficial de contenedorización del framework. Su documentación oficial explica que Docker Desktop permite construir imágenes, ejecutar contenedores y desarrollar con ellos; además, el material de introducción marca el camino para instalar, desarrollar y construir imágenes.
Para qué está definido
Dentro del framework, Docker se usa para:
Empaquetar aplicaciones
Estandarizar entornos
Facilitar despliegue
Evitar “en mi máquina funciona”
Levantar servicios locales coordinados
Y portar backend o stacks pequeños entre entornos
Cuándo usarlo
Cuando el proyecto ya tiene backend o varios servicios
Cuando quieres reproducibilidad
Cuando el deploy debe ser portable
Cuando hay diferencias entre entorno local y servidor
Cuándo no usarlo
En scripts muy pequeños que aún no necesitan entorno reproducible,
Cuando meter Docker desde el minuto uno solo complica una prueba de concepto simple
Costo
Docker Desktop tiene un punto importante: la documentación oficial indica que su uso comercial en empresas grandes, definidas como más de 250 empleados o más de 10 millones de USD de facturación anual, requiere suscripción paga.
Para usuarios individuales, aprendizaje y muchos casos pequeños, puede arrancarse sin esa fricción, pero esta consideración sí debe quedar explícita en la guía.
Motivo de inclusión
Porque Docker sí da retorno real cuando el proyecto empieza a crecer o a desplegarse. No lo pongo “para todo desde el día 1”, pero sí como estándar oficial de portabilidad.
https://www.docker.com/

## 3.7 FastAPI
Qué es
FastAPI es un framework web moderno y de alto rendimiento para construir APIs con Python, basado en type hints estándar de Python. Su documentación oficial lo presenta además como fácil de aprender, rápido para desarrollar y listo para producción.
Para qué está definido
FastAPI es el backend oficial en Python del framework para:
APIs
Servicios internos
Lógica de negocio expuesta por HTTP
Integraciones
Endpoints de automatización
Servicios de soporte para apps web o bots
Cuándo usarlo
Cuando el proyecto requiere Backend real
Cuando quieres mantenerte en Python
Cuando necesitas una api clara y bien estructurada
Cuando quieres buena ergonomía entre código, validación y documentación
Cuándo no usarlo
Cuando solo necesitas una función muy pequeña que vive mejor como script
Cuando todo el producto puede resolverse en Frontend con Backend ligero administrado.
Costo
El framework es open source. El costo viene del hosting y la operación, no del uso de FastAPI en sí.
Motivo de inclusión
Porque tiene muy buen equilibrio entre claridad, velocidad de desarrollo y seriedad operativa. Para tu perfil, además, encaja mejor que otras rutas backend más complejas o alejadas de Python.
https://fastapi.tiangolo.com/

## 3.8 Next.js
Qué es
Next.js es el framework web basado en React recomendado en este marco para construir frontend y, si hace falta, ciertas piezas full-stack ligeras. Su documentación y la de Vercel muestran que puede desplegarse como servidor Node.js, contenedor Docker o export estático, y que está especialmente bien alineado con Vercel.
Para qué está definido
Dentro del framework, Next.js está definido como:
Frontend principal para apps web
Capa UI para productos SaaS
Framework por defecto cuando quieres React con una ruta moderna y bien soportada
Cuándo usarlo
Cuando necesitas Frontend web serio
Cuando quieres SSR/SSG si aplica
Cuando vas a desplegar en Vercel
Cuando quieres una ruta con mucho soporte y documentación
Cuándo no usarlo
Cuando el proyecto no tiene interfaz web
Cuando la aplicación es tan pequeña que no necesita la estructura de un framework completo
O cuando la UI todavía ni siquiera es una prioridad.
Costo
Next.js es open source. El costo real viene del despliegue y de la infraestructura asociada.
Motivo de inclusión
Porque te da una ruta clara para frontend moderna sin abrir demasiadas alternativas paralelas.
https://nextjs.org/

## 3.9 TypeScript
Qué es
TypeScript es un lenguaje fuertemente tipado que se construye sobre JavaScript. El sitio oficial lo describe así y destaca que mejora el tooling a cualquier escala. También mantiene documentación muy accesible para principiantes y para programadores que vienen desde JavaScript.
Para qué está definido
Dentro del framework, TypeScript es el estándar para:
Frontend con Next.js/React
Funciones auxiliares en ecosistema JS/TS
Cualquier capa web donde convenga tener tipado y menos errores tontos
Cuándo usarlo
Siempre que desarrolles Frontend serio
Cuando tu proyecto crece y quieres contratos más claros
Cuando quieras reducir bugs por errores simples de estructura o llamadas
Cuándo no usarlo
No tiene mucho sentido evitarlo si ya estás en Next.js. La guía lo adopta como estándar para no fragmentar el stack
Costo
Es open source y se distribuye vía npm.
Motivo de inclusión
Porque reduce errores y mejora escalabilidad del Frontend con poco costo conceptual una vez que entra en la disciplina del proyecto.
https://www.typescriptlang.org/

## 3.10 Postgres
Qué es
Postgres es la base de datos relacional oficial del framework.
Para qué está definido
Se usa como:
Base de datos principal de apps y SaaS
Fuente de verdad transaccional
Almacenamiento estructurado
Base de Auth y datos de negocio si trabajas con supabase
Cuándo usarlo
Cuando el producto tiene datos reales
Cuando necesitas relaciones
Cuando necesitas consultar y modelar con SQL de forma seria
Cuando quieres una ruta sólida y portable
Cuándo no usarlo
Si el producto es puramente estático o experimental y aún no requiere Backend de datos.
Costo
Postgres como tecnología es open source. El costo depende del proveedor donde lo alojes.
Motivo de inclusión
Porque es una base seria, madura y además se alinea muy bien con Supabase y con una ruta de SaaS limpia.
https://www.postgresql.org/

## 3.11 Supabase
Qué es
Supabase se presenta oficialmente como una “Postgres development platform” y su propuesta actual incluye Postgres, Authentication, APIs instantáneas, Realtime, Edge Functions, Storage y vector embeddings. La documentación de Auth además aclara que Auth usa la base Postgres del proyecto por debajo y se integra con el resto del ecosistema.
Para qué está definido
Dentro del framework, Supabase es la plataforma preferida para:
Postgres administrado
Auth
Storage
APIs rápidas de soporte
Y aceleración de Backend para apps y SaaS pequeños o medianos
Cuándo usarlo
Cuando quieres lanzar rápido
Cuando no quieres administrar toda la base y Auth desde cero
Cuando el producto necesita Backend liviano pero serio
Cuando quieres concentrarte más en producto que en infraestructura
Cuándo no usarlo
Cuando el proyecto requiere una arquitectura Backend muy personalizada desde el inicio
Cuando una restricción corporativa obliga a otro proveedor.
Costo
Supabase tiene planes gratuitos y de pago; el costo escala según capacidad y uso. Lo importante para el marco es que su propuesta integrada reduce complejidad real frente a montar varias piezas separadas.
Riesgo relevante
Supabase también recuerda que es una plataforma real de operación y puede tener incidentes de servicio; eso refuerza que sigue siendo una plataforma conveniente, pero no “mágica” ni inmune a fallos.
Motivo de inclusión
Porque ofrece una relación muy buena entre velocidad, costo y capacidad para arrancar productos reales.
https://supabase.com/

## 3.12 Vercel
Qué es
Vercel es la plataforma oficial recomendada en este framework para desplegar Frontend y ciertos proyectos full-stack ligeros, especialmente con Next.js. La documentación oficial muestra despliegue vía CLI y documentación específica para Next.js sobre Vercel.
Para qué está definido
Dentro del framework, Vercel sirve para:
Desplegar Frontend rápidamente
Hospedar proyectos Next.js
Simplificar Preview Deployments
Acelerar la salida a producción de productos web
Cuándo usarlo
Cuando el proyecto tiene Frontend en Next.js,
Cuando quieres despliegues rápidos,
Cuando valoras simplicidad por encima de armar infraestructura propia.
Cuándo no usarlo
Cuando el Backend principal es Python pesado o necesita un entorno muy específico como servicio principal,
Cuando una política corporativa impide usar Vercel.
Costo
Vercel tiene un modelo con plan inicial y niveles más altos por uso y capacidades. El detalle exacto puede cambiar, pero el marco lo elige por su conveniencia operativa en Frontend, no por ser necesariamente la opción más barata en todos los escenarios.
Motivo de inclusión
Porque reduce muchísimo la fricción del deploy Frontend y encaja de forma natural con Next.js.
https://vercel.com/

## 3.13 Sentry
Qué es
Sentry es una plataforma de monitoreo de errores y observabilidad de aplicaciones.
Para qué está definido
Dentro del framework, Sentry no entra en el arranque mínimo, pero sí como herramienta recomendada de etapa posterior para:
Monitorear errores de Frontend y Backend
Capturar fallos en producción
Dar trazabilidad cuando el producto ya tiene usuarios o uso real
Cuándo usarlo
Cuando el proyecto ya se desplegó y tiene uso real
Cuando los errores en producción ya cuestan más que el esfuerzo de instrumentarlos
Cuándo no usarlo
En prototipos iniciales donde ni siquiera validaste el flujo principal
Motivo de inclusión
Porque la observabilidad sí da retorno cuando ya existe algo que vale la pena observar.
https://sentry.io/

## 3.14 Combinaciones oficiales recomendadas
### A. App web estándar
Next.js
TypeScript
Vercel
FastAPI si hace falta backend real
Postgres/Supabase
GitHub Actions
Playwright
### B. SaaS liviano/mediano
Next.js
TypeScript
FastAPI
Supabase + Postgres
Vercel para frontend
Docker para backend
GitHub Actions
Sentry después
Stripe si hay cobro
### C. Bot o automatización web
Python
Playwright
Stagehand si el sitio es cambiante o semántico
GitHub Actions si hay validación automática
Docker si debe correr fuera de tu máquina
n8n si forma parte de un flujo mayor
### D. API / servicio interno
FastAPI
Postgres
Docker
GitHub Actions
Sentry después

## 3.15 Qué no entra al camino base de este capítulo
No entran como base oficial inicial:
Kubernetes
microservicios
Airflow
múltiples clouds a la vez
Auth enterprise compleja
RAG/embeddings por defecto
Plataformas que no mejoran el retorno inmediato para tu perfil
Eso no significa que sean malas. Significa que aquí se prioriza una ruta usable, explicable y escalable sin rehacer todo.

## 3.16 Orden oficial de adopción del stack técnico
La secuencia recomendada es esta:
GitHub Actions
FastAPI
Next.js + TypeScript
Postgres
Supabase
Vercel
Docker
Playwright
Stagehand
Sentry
Este orden evita meter demasiadas piezas a la vez y respeta una progresión lógica:
Primero construyes
Luego automatizas validación
Luego despliegas
Luego fortaleces testing
Luego agregas observabilidad

## 3.17 Tabla rápida de decisión (ejecución y operación)


## 3.18 Decisión oficial del capítulo 3
El capítulo 3 deja aprobadas como herramientas oficiales de desarrollo, testing, backend y deploy:
GitHub Actions para CI/CD,
Playwright como base de testing y automatización reproducible,
Stagehand como capa especializada de browser automation con IA,
Docker como estándar de portabilidad,
FastAPI como backend Python,
Next.js + React + TypeScript como stack frontend,
Postgres como base de datos principal,
Supabase como plataforma preferida para acelerar backend/data/auth,
Vercel como plataforma preferida para frontend,
Sentry como recomendación de observabilidad de etapa posterior.
Y fija esta política:
el framework construye primero con un stack claro y compacto; la complejidad adicional entra solo cuando el producto ya la justifica.

# Capítulo 4: Sistema de contexto, memoria y conocimiento satélite

Este capítulo define cómo el framework selecciona, organiza, conserva y reutiliza la información para trabajar con precisión, bajo costo de contexto y alta coherencia operativa.
La lógica base que mantengo del documento que compartiste es esta: el ahorro real de tokens y buena parte de la calidad del trabajo no dependen del modelo, sino de cómo se gobierna el contexto, la memoria y la documentación del proyecto. También mantengo la distinción entre fuente de verdad operativa y conocimiento satélite, incluyendo el rol de Obsidian como herramienta complementaria y no como repositorio oficial del proyecto.

## 4.1 Objetivo del capítulo
Este capítulo existe para dejar resueltas estas preguntas:
Qué es contexto dentro del framework
Qué es memoria
Qué archivos son fuente de verdad
Qué archivos son operativos
Cómo evitar leer todo el proyecto
Cómo comprimir contexto
Cómo usar skills y workflows sin duplicar documentación
Cómo conviven NotebookLM y Obsidian sin competir con el repo

## 4.2 Principio oficial del contexto
La regla principal de este capítulo es:
El contexto no debe ser abundante. Debe ser preciso.
Y su consecuencia operativa es:
No cargar contexto por disponibilidad. Cargar contexto por necesidad.
Esto significa que el sistema no debe enviar al agente todo lo que existe en el proyecto.
Debe enviar solamente el paquete mínimo que permita resolver bien una tarea concreta.
Ese principio ya está claramente presente en tu documento y aquí queda consolidado como norma formal del capítulo.

## 4.3 Qué significa “contexto” en este framework
En este marco, contexto es el conjunto de información que el sistema decide mostrarle al agente o al modelo para que pueda resolver correctamente una tarea.
Eso puede incluir:
Qué proyecto es
Qué se está haciendo ahora
Qué reglas debe respetar
Qué decisiones previas existen
Qué archivos son relevantes
Qué restricciones aplican
Qué no debe tocar
Qué resultado se espera
Contexto no significa:
Todo el repo
Toda la documentación
Todo el histórico
Todas las decisiones
Todos los archivos “por si acaso”
Contexto significa:
La información correcta
En la cantidad correcta
En el momento correcto

## 4.4 Qué significa “memoria” en este framework
La memoria no es lo mismo que el contexto.
Contexto
Es lo que se carga para resolver una tarea puntual.
Memoria
Es lo que se guarda para no perder conocimiento útil entre tareas.
Ejemplos prácticos

Regla
La memoria no se carga completa siempre. Se consulta cuando hace falta.

## 4.5 Problemas que resuelve esta capa
Esta capa resuelve estos problemas operativos:
Exceso de contexto
Ruido documental
Respuestas genéricas
Duplicación de información
Pérdida de conocimiento
Baja calidad de modelos baratos por desorden del sistema
Dificultad para retomar proyectos
Dependencia de memoria informal del usuario

## 4.6 Política oficial de contexto
El framework adopta una política de tres niveles.
### Nivel 1: contexto mínimo
Es el punto de partida por defecto.
Incluye:
PROJECT_GUIDE.md
CONTEXT_INDEX.md
tasks/current/active_task.md
Con eso, el sistema ya entiende:
Qué es el proyecto
Cómo está organizado
Qué se está haciendo ahora
Este debe ser el modo base de trabajo.

### Nivel 2: contexto dirigido
Se agrega cuando la tarea necesita información más específica.
Puede incluir:
Una skill
Un workflow
Un archivo técnico puntual
Una decisión previa relevante
Uno o dos archivos de código concretos
Ejemplo:
Si la tarea es corregir un endpoint FastAPI, además del contexto mínimo podría entrar:
skills/python-backend.md
docs/engineering/coding-standards.md
apps/api/app/api/routes/...
Aquí el contexto sigue siendo pequeño, pero ya está orientado.

### Nivel 3: contexto ampliado
Solo debe usarse cuando el problema es transversal, riesgoso o arquitectónico.
Casos típicos:
Refactor grande
Cambio de arquitectura
Bug transversal
Integración entre frontend, backend y auth
Decisión de deploy con impacto en varias capas
Regla
Este nivel debe ser la excepción, no la forma normal de operar.

### 4.7 Orden oficial de lectura
El orden base de lectura queda fijado así:
PROJECT_GUIDE.md
CONTEXT_INDEX.md
tasks/current/active_task.md
Luego, solo si hace falta:
Una skill
Un workflow
Uno o dos documentos técnicos concretos
Una decisión previa relevante
Qué evita este orden
Tocar código sin entender el proyecto
Releer más de lo necesario
Empezar por documentación técnica cuando aún no se entiende la tarea
Resolver problemas fuera de alcance

## 4.8 Rol de CONTEXT_INDEX.md
CONTEXT_INDEX.md actúa como mapa de acceso al contexto. No explica todo el proyecto. Explica qué leer según la necesidad.
Debe responder cosas como:
Si la tarea es arquitectura, qué leer
Si la tarea es debugging, qué leer
Si la tarea es Backend, qué leer
Si la tarea es Deploy, qué leer
Si la tarea es testing, qué leer
Si la tarea es SaaS, qué leer
Valor real de este archivo
Tu documento ya lo posiciona correctamente como mapa de acceso al contexto, y mantengo esa definición.

## 4.9 Fuente de verdad por tipo de información
Para que la capa de contexto funcione, cada tipo de información debe tener una fuente principal.

Regla oficial
No debe haber dos fuentes equivalentes compitiendo por el mismo tipo de verdad.

## 4.10 Archivos troncales del sistema de contexto
### AGENTS.md
Función
Es la puerta de entrada para agentes y asistentes.
Debe contener
Propósito general del proyecto
Orden de lectura recomendado
Reglas locales
Alcance y límites
Qué no debe asumir el agente
Cómo decidir qué contexto cargar
No debe contener
Toda la documentación del proyecto
Historial largo
Decisiones completas
Duplicación de PROJECT_GUIDE.md

### PROJECT_GUIDE.md
Función
Es la constitución local del proyecto.
Debe contener
Propósito
Alcance
Límites
Estructura del repo
Reglas documentales
Reglas de actualización
Reglas de contexto
Reglas de consulta
Reglas de agentes
No debe contener
Tareas diarias detalladas
Historial operativo largo
Decisiones antiguas completas
Notas personales
Tu documento lo trata como artefacto estructural principal, y esa jerarquía se mantiene.

### CONTEXT_INDEX.md
Función
Es el mapa de acceso al contexto.
Debe contener
Qué leer si la tarea es arquitectura
Qué leer si es backend
Qué leer si es debugging
Qué leer si es testing
Qué leer si es deploy
Qué leer si es SaaS
Qué leer si requiere decisiones previas
No debe contener
Explicación completa del proyecto
Reglas duplicadas del PROJECT_GUIDE.md
Tareas activas
Debates o análisis largos

### decisions/decision_log.md
Función
Registrar decisiones relevantes de forma cronológica y breve.
Debe contener
Fecha
Decisión
Motivo
Impacto
Referencia a ADR si aplica
No debe contener
Ensayos largos
Discusiones sin cierre
Información operativa diaria

### memory/project_facts.md
Función
Conservar hechos estables y vigentes del proyecto.
Debe contener
Stack
Entornos
Proveedores aprobados
Base de datos
Auth
Hosting
Restricciones estructurales
Regla
- Solo hechos vigentes.
- No opiniones.
- No debates.
- No histórico.

## 4.11 Skills y workflows dentro de la capa de contexto
### Skills
- Las skills son contexto reusable especializado.
- No son teoría general.
- No son notas blandas.
- Son guías operativas para ejecutar un tipo de trabajo con calidad.
Ejemplos
Backend
Debugging
Review
Deploy
Playwright
Stagehand
Una skill debe contener
Objetivo
Cuándo usarla
Cuándo no usarla
Entradas esperadas
Reglas
Checklist
Errores comunes
Formato de salida esperado

### Workflows
Los workflows son secuencias repetibles. Sirven para ordenar el proceso completo.
Ejemplos
Spec
Implementation
Debugging
Research
Documentation-update
Memory-update
Deploy
PR-review
E2E-validation
Un workflow debe contener
Objetivo
Cuándo usarlo
Entradas requeridas
Pasos
Entregable esperado
Qué actualizar después
Tu documento ya fija bien este rol estructural de skills y workflows, y aquí lo dejo con formato más operativo.

## 4.12 Memoria reusable del proyecto
La memoria reusable debe vivir principalmente en memory/.
Archivos principales
project_facts.md
constraints.md
known_issues.md
glossary.md
patterns.md
Función de cada uno

## 4.13 Qué es contexto comprimido
El framework oficializa el uso de contexto comprimido.
Definición
Es un artefacto corto y reusable que resume algo largo o costoso de releer.
Ejemplos
repo-summary.md
incident-summary.md
integration-notes.md
module-map.md
decision-summary.md
Para qué sirve
Ahorrar tokens
Ahorrar tiempo
Estabilizar conocimiento
Reusar comprensión ya lograda
Permitir que modelos más modestos respondan mejor
Regla
Si una investigación o análisis largo ya generó comprensión útil, conviene convertirlo en un artefacto comprimido antes que forzar al sistema a revisar todo de nuevo.
Este diagrama muestra cómo el sistema decide qué leer antes de ejecutar una tarea.

Qué debe comunicar visualmente este diagrama
El usuario expresa una intención
El manager lee primero la base mínima
El sistema clasifica la tarea
Se evalúa si el contexto mínimo basta
Si no basta, se agrega contexto dirigido
Si la tarea es transversal o crítica, se agrega contexto ampliado justificado
Luego se ejecuta
Después se evalúa si corresponde actualizar memoria o decisiones

## 4.14 Qué pasa si no controlas bien el contexto
Si el sistema no gobierna bien el contexto, pasan estas cosas:
El agente toca cosas que no debía tocar
Propone soluciones incompatibles
Gasta más de lo necesario
El usuario compensa con prompts largos
La documentación pierde valor
Los modelos baratos parecen peores de lo que realmente son
El framework deja de ser un sistema y vuelve a ser una conversación improvisada

## 4.15 Conocimiento satélite
No todo conocimiento útil debe vivir dentro del repo.
El framework reconoce una capa llamada conocimiento satélite.
Función
Guardar conocimiento valioso que no debe competir con la fuente oficial del proyecto.
Ejemplos
Notas personales
Ideas en exploración
Comparativas de herramientas
Mapas mentales
Aprendizajes transversales
Glosarios entre proyectos
Conocimiento de largo plazo
Tu documento ya introduce esta idea como “conocimiento satélite opcional”, y aquí la dejo formalmente incorporada a la arquitectura del manual.

## 4.16 Regla de gobernanza
Regla obligatoria:
Cada concepto del framework debe existir en un único lugar como fuente principal.
Las menciones en otros capítulos deben ser referencias, no duplicaciones.
## 4.17 Obsidian dentro del framework
Obsidian no forma parte del núcleo operativo del proyecto, pero sí puede incorporarse como herramienta satélite oficial de conocimiento personal. Esa dirección también ya quedó incorporada en tu documento revisado.
Rol correcto de Obsidian
Obsidian debe usarse para:
Notas personales
Conocimiento transversal
Investigación personal
Mapas de arquitectura
Glosarios cruzados
Comparativas de herramientas
Aprendizaje
Ideas y exploración
Rol incorrecto de Obsidian
No debe usarse como:
Fuente de verdad operativa del proyecto
Ubicación oficial de tareas activas
Registro oficial de decisiones del proyecto
Reemplazo de PROJECT_GUIDE.md
Reemplazo de decision_log.md
Documentación que los agentes deban tomar como contrato primario
Regla oficial
El repo sigue siendo la fuente de verdad del proyecto. Obsidian funciona como cerebro extendido personal y capa satélite de conocimiento.

## 4.18 Relación entre NotebookLM y Obsidian
Estas herramientas no compiten si se ubican bien.

Regla de convivencia
NotebookLM entiende fuentes externas
Obsidian conserva y organiza conocimiento personal
El repo Git conserva la verdad operativa del proyecto

## 4.19 Diagrama de fuente de verdad vs conocimiento satélite
Este diagrama ayuda a mostrar qué vive en el repo y qué puede vivir fuera sin romper la gobernanza.

Qué debe comunicar visualmente
El repo contiene la fuente oficial del proyecto
PROJECT_GUIDE.md, CONTEXT_INDEX.md, tasks/, decisions/, memory/ y docs/ son la base operativa
NotebookLM y Obsidian viven fuera del núcleo operativo
Solo vuelve al repo lo que se convierte en contexto comprimido, decisión oficial o patrón reusable


## 4.20 Qué sí puede vivir fuera del proyecto
Sí puede vivir fuera del repo:
Comparativas entre herramientas
Notas de aprendizaje
Mapas de arquitectura personales
Conceptos reutilizables entre proyectos
Reglas personales de productividad
Investigación en progreso
Ideas todavía no aprobadas

## 4.21 Qué nunca debe salir del proyecto
No debe salir del repo:
Tarea activa oficial
Decisiones del proyecto
Restricciones del proyecto
Hechos vigentes del proyecto
Documentación técnica oficial
Guías que los agentes deben leer primero

## 4.22 Estructura recomendada del conocimiento satélite
Si usas Obsidian, la guía recomienda esta estructura base:
obsidian-vault/
├── 00_inbox/
├── 01_framework/
├── 02_tools/
├── 03_architecture/
├── 04_learning/
├── 05_project-notes/
├── 06_comparisons/
├── 07_patterns/
└── 99_archive/
Propósito de cada carpeta

## 4.23 Ejemplos prácticos de uso del sistema de contexto
### Ejemplo 1: bug en backend
Situación
“El endpoint de login dejó de funcionar después de mover una validación al backend.”
Qué debería cargar el sistema
Contexto mínimo
PROJECT_GUIDE.md
CONTEXT_INDEX.md
active_task.md
Contexto dirigido
skills/debug-issue.md
docs/engineering/error-handling.md
memory/known_issues.md
archivo del endpoint login
archivo del servicio auth
Qué no debería cargar
Toda la arquitectura
Todo el backlog
Todas las ADRs
Todo el repo
Qué debería producir
Hipótesis clara
Evidencia
Causa raíz probable
Corrección sugerida
Posible actualización de known_issues.md o decision_log.md

### Ejemplo 2: nuevo feature de backend
Situación
“Agregar validación para no permitir órdenes de clientes bloqueados.”
Qué debería cargar el sistema
Contexto mínimo
PROJECT_GUIDE.md
CONTEXT_INDEX.md
active_task.md
Contexto dirigido
workflows/spec.md
skills/python-backend.md
docs/product/requirements.md
docs/engineering/coding-standards.md
archivos afectados del caso de uso
Qué debería producir
Alcance del cambio
Plan de implementación
Regla de negocio
Cambio de código
Revisión de impacto
Posible actualización documental

### Ejemplo 3: research documental con NotebookLM
Situación
Necesitas revisar varios PDFs y links sobre una API externa antes de integrarla.
Qué debería pasar
Fuera del repo
Cargas fuentes en NotebookLM
Haces preguntas específicas
Generas una síntesis accionable
Lo que sí debería volver al repo
integration-notes.md
resumen de riesgos
endpoints clave
dudas abiertas
limitaciones detectadas
Qué no debería pasar
Usar NotebookLM como fuente oficial del proyecto
Dejar el conocimiento solo en el notebook
No documentar la integración dentro del repo

### Ejemplo 4: uso correcto de Obsidian
Situación
Estás comparando Cline, Codex, Claude Code y OpenCode para evolucionar tu framework.
Dónde debería vivir eso
En Obsidian
Qué sí va ahí
Comparativas entre herramientas
Reflexiones de arquitectura
Notas de aprendizaje
Pros y contras
Ideas de evolución futura
Patrones observados entre proyectos
Qué no debería ir ahí
active_task.md
decisiones oficiales del proyecto
restricciones vigentes del producto
flujo actual de implementación

### Ejemplo 5: contexto comprimido después de una investigación larga
Situación
Analizaste un repo grande y ya entendiste:
Módulos principales
Flujos críticos
Hotspots
Deuda técnica principal
Qué deberías hacer
Crear algo como:
repo-summary.md
module-map.md
hotspots.md
Qué efecto produce
La próxima vez el agente no necesita releer el repo completo para partir.




## 4.24 Diagrama resumen: las 4 decisiones del sistema de contexto
Este diagrama funciona bien como cierre visual del capítulo.

Qué resume
Qué debe leerse
Qué no debe leerse
Qué debe conservarse
Qué debe quedarse fuera del núcleo operativo



## 4.25 Política oficial de mantenimiento del contexto
El sistema de contexto debe revisarse periódicamente.
Cuándo revisarlo
Al cerrar una tarea importante
Al abrir una nueva etapa del proyecto
Al detectar duplicación
Cuando el agente no encuentra bien lo que necesita
Cuando el equipo ya no sabe qué archivo manda
Qué revisar
Duplicidades
Decisiones no registradas
Archivos obsoletos
CONTEXT_INDEX.md desactualizado
project_facts.md viejo
Memoria inflada
Falta de contexto comprimido

## 4.26 Tabla rápida de decisión para contexto y memoria

## 4.27 Decisión oficial del capítulo 4
El capítulo 4 deja formalmente establecido lo siguiente:
El contexto es un recurso estratégico
Debe cargarse por necesidad
La memoria no debe confundirse con contexto activo
El repo es la fuente de verdad operativa
AGENTS.md, PROJECT_GUIDE.md, CONTEXT_INDEX.md, decision_log.md y project_facts.md son artefactos troncales
Skills y workflows son parte estructural del sistema
El contexto comprimido es obligatorio cuando una comprensión larga ya fue lograda
Obsidian se aprueba como herramienta satélite de conocimiento personal
NotebookLM y Obsidian no compiten si se ubican bien
La política final de este capítulo se resume así:
El sistema debe saber qué leer, qué no leer, qué conservar, qué comprimir y qué dejar fuera del núcleo operativo.

# Capítulo 5: ejecución operativa con agentes

## 5.1 Objetivo del capítulo
Este capítulo define cómo se ejecuta realmente el trabajo dentro del framework.
Resuelve el problema más crítico:
Cómo pasar de intención → ejecución consistente sin depender de prompts improvisados.
Este capítulo establece:
Qué agentes existen
Qué hace cada uno
Cómo se activan
Qué leen
Qué NO deben leer
Cómo se coordinan
Cómo interactúan con skills y workflows
Cómo evitar duplicación de contexto
Cómo mantener bajo costo de tokens

## 5.2 Principio operativo de ejecución
La ejecución del framework se basa en una regla clave:
El usuario NO ejecuta tareas directamente. El sistema las traduce.
Esto implica:
El usuario expresa intención
El sistema clasifica la tarea
El manager decide cómo ejecutarla
Se usa el agente adecuado
Se carga el contexto mínimo necesario
Se ejecuta con disciplina

## 5.3 Flujo oficial de ejecución
El flujo operativo estándar es:
Usuario expresa intención
Manager interpreta intención
Clasifica tipo de tarea
Define contexto mínimo
Decide si necesita contexto dirigido
Selecciona skill o workflow
Asigna agente responsable
Ejecuta
Evalúa resultado
Decide si actualizar memoria o decisiones

## 5.4 Agentes oficiales del framework
El framework define 4 agentes base obligatorios:
1. Manager (orquestador)
2. Coder (ejecutor técnico)
3. Reviewer (control de calidad)
4. Debugger (análisis de fallos)

## 5.5 Rol detallado de cada agente

### 5.5.1 Manager
Qué es
El cerebro del sistema.
Responsabilidad
Interpretar intención
Clasificar tarea
Seleccionar contexto
Elegir agente
Activar skill o workflow
Controlar ejecución
Qué lee SIEMPRE
PROJECT_GUIDE.md
CONTEXT_INDEX.md
active_task.md
Qué decide
Qué agente ejecutar
Qué contexto agregar
Qué herramienta usar
Qué modelo usar
Qué NO hace
No implementa código
No debuggea directamente
No revisa en profundidad

### 5.5.2 Coder
Qué es
El ejecutor técnico.
Responsabilidad
Implementar código
Modificar archivos
Refactorizar
Crear funciones
Integrar componentes
Qué lee
Contexto mínimo
Skill técnica relevante
Archivos específicos
Qué NO hace
No decide arquitectura
No redefine reglas
No interpreta intención global

### 5.5.3 Reviewer
Qué es
El control de calidad.
Responsabilidad
Validar código
Detectar errores
Evaluar impacto
Revisar coherencia
Identificar riesgos
Qué revisa
Cambios del coder
Integración con sistema
Cumplimiento de reglas
Qué NO hace
No implementa cambios (solo sugiere)
No redefine el plan

### 5.5.4 Debugger
Qué es
El analista de fallos.
Responsabilidad
Investigar errores
Generar hipótesis
Identificar causa raíz
Proponer soluciones
Qué usa
Logs
Código afectado
known_issues.md
contexto dirigido
Qué NO hace
No implementa directamente
No redefine arquitectura

## 5.6 Regla estructural de agentes
Si algo puede resolverse con una skill o workflow, NO debe ser un agente.
Esto evita:
Inflar el sistema
Duplicar responsabilidades
Aumentar consumo de contexto

## 5.7 Subagentes (nivel avanzado)
Decisión oficial
Los subagentes:
NO son base del framework
SÍ son opcionales en etapa avanzada

Cuándo sí usarlos
Repos grandes
Tareas paralelizables
Research complejo
Validaciones especializadas

Ejemplo real
Subagente 1: analiza Backend
Subagente 2: analiza Frontend
Subagente 3: analiza testing
→ Manager consolida

Cuándo NO usarlos
Tareas simples
Trabajo diario
Debugging básico
Implementaciones directas

Riesgos
Sobreingeniería
Mayor consumo de tokens
Complejidad de coordinación
Duplicación de funciones

## 5.8 Relación entre agentes, skills y workflows
Este es el núcleo del sistema:

Ejemplo práctico
Tarea: “crear endpoint”
Manager:
clasifica → desarrollo backend
Activa:
skill/python-backend.md
workflow/implementation.md
Asigna:
Coder

## 5.9 Activación de agentes
El sistema define reglas claras:

## 5.10 Política de contexto en ejecución
Cada agente debe:
Leer solo lo necesario
Nivel mínimo:
PROJECT_GUIDE.md
CONTEXT_INDEX.md
active_task.md
Nivel dirigido:
skill
workflow
archivo puntual
Nivel ampliado:
solo si es crítico

## 5.11 Anti-patrones críticos

❌ Error 1: usar un solo agente para todo
Problema:
Sobrecarga mental
Peor calidad

❌ Error 2: cargar todo el repo
Problema:
Alto costo
Respuestas difusas

❌ Error 3: no usar workflows
Problema:
Inconsistencia
Repetición de errores

❌ Error 4: crear demasiados agentes
Problema:
Sistema inmanejable

## 5.12 Ejemplos operativos reales

### Caso 1: Bug en producción
Flujo:
Manager clasifica → debugging
Activa:
skill/debugging.md
Asigna:
Debugger
Debugger:
analiza causa raíz
Manager:
asigna Coder
Coder:
implementa fix
Reviewer:
valida

### Caso 2: Nuevo feature
Flujo:
Manager → clasificación
Workflow: implementation
Coder ejecuta
Reviewer valida
Manager actualiza memoria

### Caso 3: Refactor grande
Flujo:
Manager → tarea crítica
Contexto ampliado
Coder implementa
Reviewer evalúa impacto
Manager registra decisión

## 5.13 Relación con herramientas
### 5.13.1 Principio clave
- El agente define el rol.
- La herramienta define cómo opera.
- El modelo define la calidad/costo del razonamiento.
Error común:
- Elegir modelo sin considerar tipo de tarea
- Usar el mismo modelo para todo
- Sobredimensionar costo

### 5.13.2 Arquitectura real de ejecución
Cada ejecución tiene 3 capas:

### 5.13.3 Tabla maestra: Agentes vs herramientas vs modelos
(Optimizada para costo-beneficio real)

5.13.4 Benchmark simplificado por modelo (realista)

### 5.13.5 Estrategia óptima por agente (decisión ejecutiva)

Manager → eficiencia extrema
Modelo recomendado:
Base: GPT-4.1-mini / Qwen
Por qué:
No necesita profundidad
Solo clasifica y enruta
Error común:
Usar GPT-5 → desperdicio total

Coder → balance costo/calidad
Modelo recomendado:
Base: GPT-4.1 / DeepSeek
Escalado: GPT-5
Por qué:
Código requiere precisión, no siempre razonamiento profundo
Observación estratégica:
El 80% del código NO necesita modelo premium

Reviewer → calidad crítica
Modelo recomendado:
Base: GPT-4.1 / Claude Sonnet
Escalado: Claude Opus / GPT-5
Por qué:
Detecta errores invisibles al coder
Reduce bugs en producción

Debugger → razonamiento profundo
Modelo recomendado:
Base: Claude Sonnet
Escalado: GPT-5 / Claude Opus
Por qué:
Necesita análisis causal
Alta ambigüedad

### 5.13.6 Relación con herramientas (realista)

### 5.13.7 Estrategia de optimización de costos (clave del framework)

- Regla 1: No todos los agentes usan el mismo modelo
- Regla 2: Escalar modelo solo si falla el resultado
- Regla 3: El problema casi nunca es el modelo → es el contexto

Ejemplo real optimizado

### 5.13.8 Arquitectura híbrida recomendada

Modo eficiente (default)
Manager → modelo barato
Coder → modelo medio
Reviewer → modelo medio/alto
Debugger → modelo alto

Modo crítico
Todo escala a modelo premium

Modo ultra low cost
Manager + Coder → DeepSeek/Qwen
Reviewer → GPT-4.1
Debugger → Claude Sonnet

### 5.13.9 Conclusión operativa
Este punto es clave para todo el framework:
No optimizas usando el mejor modelo.
Optimizas usando el modelo correcto en el momento correcto.

Impacto real
Si aplicas esto bien:
↓ 40–70% costo en tokens
↑ calidad promedio
↓ retrabajo
↑ velocidad operativa

## 5.14 Impacto en costos
Este diseño permite:
Reducir tokens
Usar modelos más baratos
Evitar re-trabajo
Mejorar precisión

## 5.15 Resultado esperado del sistema
Un sistema bien implementado debe:
Ejecutar tareas sin caos
No depender de prompts largos
Mantener coherencia
Reducir errores
Escalar sin romperse

## 5.16 Decisión oficial del capítulo 5
Este capítulo establece que:
El sistema opera con 4 agentes base
El manager orquesta todo
Los agentes no deben duplicar funciones
Skills y workflows son obligatorios
El contexto es controlado
Subagentes son opcionales y avanzados
La ejecución debe ser disciplinada

Cierre estratégico
Este capítulo es el punto donde el framework deja de ser teoría.
Define cómo convertir:
Intención → acción
Caos → sistema
IA → productividad real


# Capítulo 6: delivery, deploy y operación

## 6.1 Objetivo del capítulo
Este capítulo define cómo el framework pasa de:
👉 código → producto
👉 ideas → automatización
👉 scripts → sistemas operativos reales
Y responde:
Cómo desplegar lo que construyes
Dónde ejecutar tus soluciones
Cómo automatizar tareas
Cómo escalar a SaaS
Cómo monitorear y mantener
Cómo evitar sobreingeniería desde el inicio

## 6.2 Principio rector
No todo lo que construyes debe desplegarse.
Pero todo lo que se usa repetidamente debe automatizarse.

## 6.3 Tipos de delivery dentro del framework
No todo se despliega igual. Hay 4 tipos de output:

## 6.4 Arquitectura base de ejecución
- Usuario / Evento
- Agente / Workflow
- Código / Script / API
- Entorno de ejecución
- Resultado
- Logs / Monitoreo

## 6.5 Estrategia de deployment (DECISIÓN CRÍTICA)
Regla clave
Empieza siempre con el nivel mínimo que permita validar valor real, y solo escala cuando haya uso, necesidad o riesgo operativo.

Cómo tomar la decisión correctamente
Antes de desplegar, responde estas preguntas:
¿Esto se ejecuta una sola vez o varias veces?
Una vez → mantener local
Varias veces → automatizar (n8n o script programado)
¿Necesita acceso externo (otros usuarios o sistemas)?
No → local
Sí → API o servicio deployado
¿Tiene lógica reutilizable?
No → script
Sí → backend/API
¿Debe escalar o crecer?
No → mantener simple
Sí → arquitectura deployada (backend + DB)

Decisión resumida

Error a evitar
Desplegar antes de validar uso real = pérdida de tiempo + sobreingeniería

Regla operativa final
- Primero demuestra que funciona.
- Luego demuestra que se usa.
- Recién después despliegas en serio.

## 6.6 Niveles de deployment

### Nivel 1: Local (inicio obligatorio)
Herramientas
VS Code
Python
Playwright
Scripts
Cuándo usarlo
Testing
Desarrollo
Automatizaciones simples
Scraping inicial
Ventajas
Costo cero
Control total
Debug fácil
Desventaja
No escalable
No accesible remotamente

### Nivel 2: Automatización (n8n)
Herramienta clave
n8n (self-hosted o cloud)
Qué permite
Flujos automáticos
Integración con Gmail, Sheets, APIs
Triggers (eventos)
Ejemplo real
Leer correos → procesar → actualizar Google Sheet
Cuándo usarlo
Tareas repetitivas
Integración entre sistemas
Workflows de negocio
Valor estratégico
Es la forma más rápida de generar impacto sin backend complejo

### Nivel 3: Backend/API
Stack recomendado
FastAPI
PostgreSQL (Supabase)
Cuándo usarlo
Lógica reutilizable
Integraciones externas
APIs internas
Ejemplo
API que procesa pedidos
API que analiza datos

### Nivel 4: SaaS / aplicación completa
Stack recomendado

## 6.7 Tabla comparativa de plataformas de deploy

## 6.8 Uso de Docker (CUÁNDO SÍ / CUÁNDO NO)

Usar Docker cuando
Quieres portabilidad
Vas a producción
Tienes múltiples servicios
Quieres consistencia entre entornos

NO usar Docker cuando
Estás aprendiendo
Script simple
Automatización local
Prototipo rápido

## 6.9 Automatización con n8n (pieza clave del framework)
Rol dentro del sistema
n8n es el orquestador externo del framework

Qué conecta
APIs
Scripts Python
Google Sheets
Gmail
Webhooks
IA

Ejemplo real
Trigger: correo recibido
↓
Filtrar contenido
↓
Enviar a modelo IA
↓
Generar resumen
↓
Guardar en Google Sheet
Por qué es crítico
Reduce necesidad de backend
Reduce código
Aumenta velocidad de entrega
Permite automatización inmediata

## 6.10 Playwright y Stagehand (automatización web)
Qué problema resuelven
Permiten automatizar sitios web cuando:
No existe API
La API es limitada
El flujo real ocurre en interfaz (UI)
Scrapping

### Playwright
Qué es
Automatización directa del navegador (control total del DOM).
Cuándo usarlo
Flujos claros y estables
Selectores identificables
Procesos repetitivos (login, formularios, scraping)
Ejemplo
Descargar reportes desde un portal
Completar formularios masivos (como Coupa)
Ventaja
Preciso, rápido y controlable
Limitación
Frágil ante cambios en la UI

### Stagehand
Qué es
Capa inteligente sobre automatización (menos dependiente de selectores rígidos).
Cuándo usarlo
UI cambiante o poco estructurada
Flujos complejos
Elementos difíciles de identificar
Ejemplo
Navegación en sistemas con layouts dinámicos
Scraping donde los selectores no son confiables
Ventaja
Más resiliente a cambios
Limitación
Menos control fino
Mayor complejidad


Decisión estratégica

Regla clave
- Empieza con Playwright.
- Solo escala a Stagehand si el flujo se rompe o se vuelve inestable.

Error a evitar
Usar Stagehand desde el inicio → innecesario, más complejo y difícil de controlar

## 6.11 Integración con agentes

Flujo real
Usuario
↓
Manager
↓
Coder crea script/API
↓
Deploy (local / cloud)
↓
n8n lo ejecuta
↓
Resultado
## 6.12 Monitoreo y observabilidad

Herramientas recomendadas

## 6.13 CI/CD (automatización de despliegue)

Herramienta base
GitHub Actions

Qué permite
Deploy automático
Tests automáticos
Validación

Flujo
Push → Test → Build → Deploy

## 6.14 Seguridad básica (mínimo necesario)

Reglas
No subir API keys
Usar .env
Variables de entorno
Control de accesos

## 6.15 Costos aproximados

## 6.16 Anti-patrones críticos

❌ Error 1: desplegar demasiado pronto
→ Pierdes tiempo

❌ Error 2: usar microservicios sin necesidad
→ Sobreingeniería

❌ Error 3: no automatizar
→ Pierdes valor del framework

❌ Error 4: depender solo de scripts manuales
→ No escalable

## 6.17 Flujo ideal del framework completo
Idea
↓
Manager
↓
Coder
↓
Reviewer
↓
Deploy
↓
n8n (automatización)
↓
Usuario final
## 6.18 Decisión oficial del capítulo 6
Este capítulo establece:
El deployment es progresivo
n8n es pieza clave
No todo requiere SaaS
Playwright cubre automatización web
Docker solo cuando agrega valor
Supabase + Vercel es stack base recomendado
GitHub Actions para CI/CD

Cierre estratégico
Este capítulo es donde el framework se vuelve:
Producto
Automatización real
Impacto en negocio

# CAPÍTULO 7: GOBERNANZA, MANTENIMIENTO Y EVOLUCIÓN DEL FRAMEWORK

## 7.1 Objetivo del capítulo
Este capítulo define cómo:
Mantener el framework ordenado en el tiempo
Evitar degradación del sistema
Controlar crecimiento sin caos
Asegurar calidad constante
Evolucionar sin rehacer todo

## 7.2 Principio rector
- El problema no es construir el sistema.
- El problema es evitar que se degrade.

## 7.3 Qué es gobernanza en este framework
Gobernanza = reglas que aseguran que el sistema siga siendo usable.
Incluye:
Orden del proyecto
Control de documentación
Uso correcto de agentes
Uso eficiente de contexto
Registro de decisiones
Disciplina en ejecución

## 7.4 Componentes de gobernanza

### 1. Fuente de verdad única
Regla:
Todo lo operativo vive en el repo
Nada crítico queda fuera

### 2. Estructura obligatoria
Siempre deben existir:
PROJECT_GUIDE.md
CONTEXT_INDEX.md
tasks/current/active_task.md
decisions/decision_log.md
memory/project_facts.md
Si falta uno → el sistema empieza a fallar

### 3. Regla de no duplicación
Una idea → un solo lugar
Problemas si no se cumple:
Confusión
Decisiones contradictorias
Pérdida de coherencia

### 4. Registro de decisiones
Toda decisión relevante debe registrarse:
Qué se decidió
Por qué
Impacto

## 7.5 Mantenimiento del sistema

Cuándo mantener
Al cerrar una tarea importante
Cuando el sistema se siente confuso
Cuando el agente responde mal
Cuando hay duplicación
Cuando el repo crece

Checklist de mantenimiento
¿Hay duplicados?
¿Hay archivos obsoletos?
¿El CONTEXT_INDEX está actualizado?
¿Las decisiones están registradas?
¿Hay contexto comprimido donde debería?
¿Las tareas activas están claras?

## 7.6 Gestión de documentación

Regla clave
La documentación debe ayudar a ejecutar, no solo explicar.

Tipos de documentos

Error común
Documentar demasiado
Documentar sin estructura
Documentar sin uso real

## 7.7 Gestión de agentes

Regla principal
No crear agentes innecesarios

Cuándo crear un nuevo agente
Solo si:
Tiene función clara
No duplica otro
Reduce errores reales
Aporta eficiencia

Cuándo NO crearlo
Por comodidad
Por moda
Porque “suena bien”

## 7.8 Gestión de skills y workflows

Skills
Se deben actualizar cuando:
Hay errores repetidos
Se detecta mejor forma de trabajar
Se quiere estandarizar

Workflows
Se deben revisar cuando:
El proceso cambia
Hay inconsistencias
Se agregan pasos innecesarios

Regla clave
Si algo se repite 3 veces → convertirlo en skill o workflow

## 7.9 Control del contexto (crítico)

Señales de problema
El agente responde mal
Usa información incorrecta
Mezcla conceptos
Se pierde

Causas reales
Demasiado contexto
Falta de estructura
CONTEXT_INDEX incorrecto
Falta de memoria clara

Solución
Reducir contexto
Mejorar índice
Crear contexto comprimido
Limpiar duplicados

## 7.10 Evolución del framework

Regla clave
Evolucionar sin romper lo existente

Cómo evolucionar
Identificar problema real
Probar solución pequeña
Validar impacto
Integrar al framework
Documentar

Qué NO hacer
Cambiar todo de golpe
Reestructurar sin necesidad
Introducir herramientas sin uso claro

## 7.11 Gestión de herramientas

Regla principal
La herramienta se adapta al sistema, no al revés

Cuándo agregar herramienta nueva
Solo si:
Resuelve un problema real
Reduce tiempo
Reduce errores
Se integra bien

Cuándo NO agregarla
Por tendencia
Por curiosidad
Sin caso de uso

## 7.12 Gestión de modelos de IA

Regla clave
No usar siempre el mejor modelo

Estrategia
Tareas simples → modelos baratos
Tareas complejas → modelos premium
Escalar solo si falla

Señal de problema
Estás pagando mucho → problema de contexto, no de modelo

## 7.13 Control de calidad

Dónde ocurre
Reviewer
Workflows
Testing

Qué se valida
Código
Coherencia
Impacto
Riesgos

## 7.14 Manejo de deuda técnica

Qué es
Decisiones que funcionan hoy pero generan problemas mañana

Cómo manejarla
Registrar en decisions/
No ignorarla
Planificar refactor

## 7.15 Anti-patrones críticos

❌ Sistema crece sin orden
→ Solución: gobernanza estricta

❌ Demasiados documentos
→ Solución: consolidar

❌ Demasiados agentes
→ Solución: simplificar

❌ Dependencia de prompts largos
→ Solución: mejorar contexto

❌ No registrar decisiones
→ Solución: disciplina

## 7.16 Métricas de salud del framework

El sistema está sano si:
Encuentras rápido la información
Los agentes responden bien
No necesitas prompts largos
No hay duplicación
Las decisiones están claras
El trabajo fluye sin fricción

## 7.17 Flujo de mantenimiento ideal
Trabajo → Resultado → Revisión → Actualización → Limpieza

## 7.18 Decisión oficial del capítulo 7
Este capítulo establece:
El sistema debe mantenerse activamente
La gobernanza es obligatoria
La simplicidad es prioritaria
La evolución debe ser controlada
Las herramientas no definen el sistema
El contexto es el activo más importante

Cierre estratégico
Este capítulo es el que convierte el framework en:
Sistema sostenible
Plataforma escalable
Activo profesional real




# CAPÍTULO EXTRA : ESTÁNDAR OFICIAL DE ARQUITECTURA EFICIENTE
Declaración operativa para crear cualquier proyecto dentro del framework

## 0. Propósito
Este capítulo define el estándar mínimo obligatorio que debe cumplir un proyecto para ser considerado compatible con la arquitectura eficiente del framework.
Su objetivo es que cualquier proyecto:
Sea entendible por humanos y agentes
Mantenga bajo consumo de contexto y tokens
Tenga fuentes de verdad claras
Permita ejecución disciplinada
Reduzca improvisación
Escale sin rehacerse
Pueda ser retomado sin reconstruir contexto desde cero

## 1. Principio fundamental
Un proyecto eficiente no le pide a la IA que adivine cómo funciona.
Le entrega una estructura clara para ejecutar bien.

## 2. Reglas maestras del estándar
Todo proyecto que cumpla esta arquitectura debe respetar estas reglas:
2.1 Una sola fuente de verdad por tipo de información
No debe existir duplicación de autoridad documental.
2.2 Contexto mínimo por defecto
Ningún agente debe cargar más de lo necesario.
2.3 SPEC y SDD son contexto dirigido
Son obligatorios, pero no forman parte del contexto mínimo por defecto.
2.4 Los secretos no se guardan en documentación
Las credenciales se referencian, no se escriben en texto plano.
2.5 Skills y workflows son obligatorios
Si no existen, el sistema termina dependiendo de prompts manuales.
2.6 Toda decisión importante debe quedar registrada
Nada crítico debe quedar solo en chat, memoria informal o intuición.
2.7 El proyecto debe poder ser retomado por otro agente o persona
Si solo tú entiendes el repo, el sistema está mal diseñado.

## 3. Estructura obligatoria del proyecto
Esta es la estructura mínima recomendada y obligatoria del estándar a modo ejemplo:
project/
│
├── AGENTS.md
├── agents/
│   └── manager.md
│   └──  coder.md
│   └──  reviewer.md
│   └── debugger.md
├── PROJECT_GUIDE.md
├── CONTEXT_INDEX.md
├── README.md
├── .env.example
├── .gitignore
│
├── tasks/
│   └── current/
│       ├── active_task.md
│       ├── implementation_plan.md
│       └── open_questions.md
│
├── decisions/
│   ├── decision_log.md
│   └── adr/
│       └── ADR-0001-template.md
│
├── memory/
│   ├── project_facts.md
│   ├── constraints.md
│   ├── known_issues.md
│   ├── patterns.md
│   └── glossary.md
│
├── docs/
│   ├── product/
│   │   ├── spec.md
│   │   ├── requirements.md
│   │   └── user_flows.md
│   │
│   ├── architecture/
│   │   ├── sdd.md
│   │   ├── system_overview.md
│   │   └── integrations.md
│   │
│   ├── engineering/
│   │   ├── coding_standards.md
│   │   ├── testing_strategy.md
│   │   └── error_handling.md
│   │
│   └── operations/
│       ├── runbook.md
│       ├── troubleshooting.md
│       └── deployment.md
│
├── skills/
│   ├── route-task.md
│   ├── project-organizer.md
│   ├── summarize-docs.md
│   ├── plan-change.md
│   ├── review-diff.md
│   ├── debug-issue.md
│   ├── memory-update.md
│   ├── framework-maintainer.md
│   ├── spec-writer.md
│   ├── architecture-review.md
│   ├── python-backend.md
│   ├── deploy-app.md
│   ├── playwright-testing.md
│   └── stagehand-automation.md
│
├── workflows/
│   ├── spec.md
│   ├── architecture.md
│   ├── implementation.md
│   ├── debugging.md
│   ├── documentation-update.md
│   ├── memory-update.md
│   ├── deploy.md
│   └── pr-review.md
│
├── config/
│   ├── env_map.md
│   ├── secrets_policy.md
│   ├── integrations_registry.md
│   └── access_matrix.md
│
├── apps/
├── tests/
├── scripts/
└── infra/
## 4. Qué hace cada documento obligatorio

### 4.1 Núcleo de gobierno
AGENTS.md
Contrato operativo para agentes.
Debe definir
Qué agentes existen
Qué leen primero
Qué no deben asumir
Cómo se enrutan tareas
Qué documentos tienen prioridad

PROJECT_GUIDE.md
Constitución del proyecto.
Debe definir
Propósito
Alcance
Límites
Estructura del repo
Reglas de trabajo
Reglas de contexto
Jerarquía documental

CONTEXT_INDEX.md
Mapa de acceso al contexto.
Debe responder
Si la tarea es feature, qué leer
Si es bug, qué leer
Si es arquitectura, qué leer
Si es deploy, qué leer
Si es integración, qué leer

### 4.2 Núcleo operativo
tasks/current/active_task.md
La verdad del presente.
Debe definir
Qué se está haciendo ahora
Objetivo inmediato
Alcance
Estado
Resultado esperado

implementation_plan.md
Plan detallado del trabajo actual.
open_questions.md
Incertidumbres activas.

### 4.3 Núcleo de memoria
project_facts.md
Hechos vigentes del proyecto.
constraints.md
Restricciones técnicas, negocio, acceso, costo.
known_issues.md
Problemas conocidos y workarounds.
patterns.md
Patrones aprobados.
glossary.md
Lenguaje del dominio.

### 4.4 Núcleo de decisiones
decision_log.md
Registro cronológico de decisiones.
ADR
Decisiones estructurales más grandes.

### 4.5 Núcleo funcional y técnico
docs/product/spec.md
Qué debe hacer el sistema.
docs/architecture/sdd.md
Cómo está diseñado el sistema.
docs/engineering/
Reglas de ingeniería.
docs/operations/
Cómo operar, desplegar y mantener.

## 5. SPEC y SDD: por qué sí deben existir
Sí, deben existir. Y deben ser obligatorios.
Pero la regla correcta es esta:
SPEC y SDD no son contexto mínimo. Son contexto dirigido.

### 5.1 SPEC
Rol
Define el problema y la solución esperada a nivel funcional.
Debe contener
Objetivo
Usuario o actor
Problema
Alcance
Casos de uso
Reglas de negocio
Criterios de aceptación
Riesgos funcionales

### 5.2 SDD
Rol
Define la solución técnica.
Debe contener
Arquitectura
Componentes
Flujo de datos
Integraciones
Riesgos técnicos
Restricciones
Decisiones de diseño
Dependencias

### 5.3 Cuándo se usan

## 6. Skills obligatorias del estándar
Aquí sí faltaba precisión. Si quieres eficiencia real de memoria, contexto e indexación, estas skills no son opcionales.
### 6.1 Skills mínimas obligatorias

### 6.2 Skills técnicas obligatorias según stack

## 7. Workflows obligatorios del estándar

## 8. Cómo se comunican agentes, skills y herramientas
Esto debe quedar explícito en el estándar.
### 8.1 Flujo general
Usuario
↓
Manager
↓
Lee PROJECT_GUIDE.md + CONTEXT_INDEX.md + active_task.md
↓
Clasifica tarea
↓
Activa workflow
↓
Activa skill
↓
Asigna agente responsable
↓
Ejecuta con herramienta adecuada
↓
Evalúa resultado
↓
Actualiza memoria / decisiones / docs
### 8.2 Relación real

## 9. Credenciales, secretos y configuración
Los secretos no se documentan con valores reales. Se documenta su existencia, propósito, ubicación y política de uso.

### 9.1 Qué sí debe existir
Dentro de config/:
env_map.md
Mapa de variables de entorno.
Debe indicar:
Nombre de variable
Qué servicio representa
Quién la usa
En qué entorno aplica
Si es obligatoria u opcional
secrets_policy.md
Política de manejo de secretos.
Debe indicar:
Nunca guardar secretos reales en Markdown
Nunca subir .env
Dónde vive cada secreto
Quién puede acceder
Cómo rotarlos
integrations_registry.md
Registro de integraciones.
Debe indicar:
Servicio externo
Tipo de autenticación
URL base
Entorno
Owner técnico
Riesgos
access_matrix.md
Matriz de accesos.
Debe indicar:
Rol
Recurso
Nivel de acceso

### 9.2 Qué NO debe existir
No debe existir nunca esto:
passwords.md
tokens.md
keys.txt
credenciales reales dentro de PROJECT_GUIDE.md
secretos copiados en decision_log.md

### 9.3 Archivos sí recomendados
.env.example
Debe existir siempre.
Debe contener:
nombres de variables
valores vacíos o dummy
comentarios de uso
.gitignore
Debe excluir:
.env
.env.*
credenciales locales
archivos temporales sensibles

## 10. Documento ejemplo mínimo
Te dejo un ejemplo breve de cómo debe verse uno de los documentos más importantes.
Ejemplo: docs/product/spec.md
# SPEC

## Objetivo
Permitir bloquear automáticamente la creación de órdenes para clientes marcados como bloqueados.

## Problema
Actualmente el sistema permite registrar órdenes para clientes con estado bloqueado, generando errores operativos posteriores.

## Alcance
Aplicar validación antes de confirmar la orden.

## No alcance
No modifica el proceso de desbloqueo de clientes.

## Regla de negocio
Si `customer.status = blocked`, entonces la orden no puede ser confirmada.

## Casos de uso
- Usuario intenta crear orden con cliente activo → permitido
- Usuario intenta crear orden con cliente bloqueado → rechazado con mensaje

## Criterios de aceptación
- No se crean órdenes de clientes bloqueados
- El mensaje de error es claro
- La validación queda cubierta por test
## 11. Política de indexación y eficiencia de tokens
Si quieres eficiencia real, el estándar debe incluir estas reglas:
### 11.1 Regla de indexación
Todo documento debe existir porque tiene una función clara en CONTEXT_INDEX.md.
### 11.2 Regla de compresión
Si algo se reutilizará, debe resumirse.
### 11.3 Regla de no ruido
No crear documentos “bonitos” que ningún agente usará.
### 11.4 Regla de prioridad documental
Los agentes leen en este orden:
PROJECT_GUIDE.md
CONTEXT_INDEX.md
tasks/current/active_task.md
skill / workflow
documento puntual
decisión previa
contexto ampliado solo si es necesario

## 12. Checklist de validación del estándar
Un proyecto cumple con esta arquitectura si:
Tiene núcleo documental completo
Tiene SPEC y SDD en ubicación correcta
Tiene skills mínimas obligatorias
Tiene workflows mínimos obligatorios
Tiene política de secretos
Tiene .env.example
No guarda credenciales reales en texto plano
Tiene una sola fuente de verdad por tipo
Puede ser entendido por otro agente sin prompts largos
El contexto puede cargarse en capas

## 13. Declaración final lista para copiar
Este proyecto cumple con el estándar oficial de arquitectura eficiente.

Todo proyecto debe:

1. Tener una sola fuente de verdad por tipo de información
2. Mantener PROJECT_GUIDE.md, CONTEXT_INDEX.md y active_task.md como núcleo mínimo
3. Tener SPEC para cambios funcionales y SDD para cambios técnicos
4. Usar skills y workflows obligatorios antes de improvisar
5. No cargar contexto innecesario
6. Comprimir contexto cuando el conocimiento ya fue obtenido
7. Registrar decisiones estructurales
8. Mantener memoria estable y consultable
9. Separar conocimiento operativo del conocimiento satélite
10. No guardar secretos reales en documentación
11. Usar .env.example y políticas de secretos para configuración
12. Permitir que agentes y personas entiendan el proyecto sin reconstruir el contexto desde cero

La eficiencia del proyecto depende de la claridad estructural, no del modelo más caro.


### Templates de plantillas operativas para la estructura:
Están diseñadas para que funcionen como base estándar de tu arquitectura eficiente, alineadas con todo el marco que construimos: contexto mínimo, SPEC + SDD como contexto dirigido, decisiones trazables, skills/workflows obligatorios y separación clara entre ejecución, memoria y documentación.
AGENTS.md
Define los roles de los agentes (Manager, Coder, Reviewer, Debugger), establece el orden obligatorio de lectura de los archivos y dicta las reglas de carga de contexto.
# AGENTS

## 1. Propósito de este archivo
Este archivo define cómo deben operar los agentes dentro de este proyecto.

Su función es:
- indicar el orden de lectura
- definir roles de agentes
- establecer reglas de contexto
- evitar suposiciones incorrectas
- asegurar ejecución eficiente y consistente

---

## 2. Regla principal
Ningún agente debe cargar más contexto del necesario para resolver correctamente la tarea solicitada.

---

## 3. Orden obligatorio de lectura
Antes de ejecutar cualquier tarea, los agentes deben leer en este orden:

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`

Luego, solo si la tarea lo requiere:

4. skill relevante
5. workflow relevante
6. documento técnico puntual
7. decisión previa relevante
8. contexto ampliado justificado

---

## 4. Agentes oficiales del proyecto

### 4.1 Manager
#### Rol
Orquestar la ejecución.

#### Responsabilidades
- interpretar intención del usuario
- clasificar tipo de tarea
- decidir qué contexto cargar
- elegir skill o workflow
- asignar agente responsable
- decidir si debe actualizarse memoria o decisiones

#### No debe
- implementar código directamente
- revisar diffs en profundidad
- debuggear a detalle salvo para enrutar

---

### 4.2 Coder
#### Rol
Implementar cambios técnicos.

#### Responsabilidades
- crear o modificar código
- refactorizar
- integrar componentes
- seguir estándares del proyecto

#### No debe
- redefinir arquitectura sin autorización
- inventar reglas no documentadas
- tocar áreas fuera del alcance de la tarea

---

### 4.3 Reviewer
#### Rol
Validar calidad y coherencia.

#### Responsabilidades
- revisar cambios
- detectar riesgos
- validar mantenibilidad
- verificar alineación con reglas y decisiones

#### No debe
- implementar cambios grandes directamente
- redefinir alcance del trabajo

---

### 4.4 Debugger
#### Rol
Investigar fallos.

#### Responsabilidades
- analizar errores
- generar hipótesis
- identificar causa raíz
- proponer corrección

#### No debe
- asumir causas sin evidencia
- rediseñar el sistema sin necesidad

---

## 5. Regla sobre subagentes
Los subagentes no son obligatorios.

Solo pueden usarse si:
- reducen carga mental real
- evitan leer contexto innecesario
- devuelven resultados comprimidos y útiles
- no duplican el rol de otro agente
- mejoran el flujo más de lo que aumentan la complejidad

Si una necesidad puede resolverse con una skill o workflow, no debe crearse un subagente.

---

## 6. Regla sobre SPEC y SDD
`docs/product/spec.md` y `docs/architecture/sdd.md` son obligatorios en el proyecto, pero no forman parte del contexto mínimo.

Se consideran contexto dirigido.

### Usar `spec.md` cuando
- se crea un nuevo feature
- cambia una regla de negocio
- se define alcance funcional

### Usar `sdd.md` cuando
- cambia arquitectura
- cambia integración
- se hace un refactor importante
- se modifica diseño técnico

---

## 7. Reglas de contexto

### Contexto mínimo por defecto
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `tasks/current/active_task.md`

### Contexto dirigido
Agregar solo si hace falta:
- skill relevante
- workflow relevante
- archivo técnico puntual
- uno o dos archivos de código afectados
- decisión previa relevante
- `spec.md` o `sdd.md` si aplica

### Contexto ampliado
Solo en tareas:
- transversales
- críticas
- arquitectónicas
- de alto impacto

---

## 8. Reglas de ejecución
Todo agente debe:

- trabajar dentro del alcance definido
- respetar decisiones ya registradas
- no asumir contexto no documentado
- producir resultados claros y verificables
- preferir cambios pequeños y trazables
- actualizar documentación si el cambio lo requiere

---

## 9. Reglas de documentación
Los agentes deben tratar estos archivos como fuente oficial por tipo de información:

- estructura del proyecto → `PROJECT_GUIDE.md`
- ruta de lectura → `CONTEXT_INDEX.md`
- trabajo actual → `tasks/current/active_task.md`
- decisiones → `decisions/decision_log.md`
- hechos vigentes → `memory/project_facts.md`
- restricciones → `memory/constraints.md`
- problemas conocidos → `memory/known_issues.md`

---

## 10. Reglas sobre secretos y configuración
Los agentes nunca deben escribir secretos reales en documentación.

### Secretos y credenciales
- no deben aparecer en archivos `.md`
- no deben copiarse en logs ni decisiones
- no deben incluirse en commits

### Referencias permitidas
Los agentes pueden consultar y actualizar:
- `config/env_map.md`
- `config/secrets_policy.md`
- `config/integrations_registry.md`
- `.env.example`

---

## 11. Qué hacer después de ejecutar
Si el trabajo genera conocimiento reusable, el agente responsable o el manager debe evaluar si corresponde:

- actualizar `memory/project_facts.md`
- actualizar `memory/known_issues.md`
- actualizar `memory/patterns.md`
- registrar decisión en `decisions/decision_log.md`
- actualizar `docs/product/spec.md`
- actualizar `docs/architecture/sdd.md`
- actualizar documentación técnica puntual

---

## 12. Regla final
La eficiencia del proyecto depende de la claridad estructural, no del modelo más caro.

Los agentes deben operar con disciplina, contexto mínimo y fuentes de verdad claras.

PROJECT_GUIDE.md
Actúa como la "constitución" del proyecto; contiene el propósito, alcance, límites y las reglas documentales y de actualización permanentes.
# PROJECT GUIDE

## 1. Propósito del proyecto
[Describir qué resuelve este proyecto, para quién existe y qué problema ataca.]

Ejemplo:
Este proyecto automatiza la creación y validación de órdenes de compra para reducir carga operativa manual, errores humanos y tiempos de gestión.

---

## 2. Alcance
[Definir qué sí cubre el proyecto.]

Ejemplo:
- automatización del flujo principal
- validación de reglas de negocio
- integración con sistema externo
- generación de logs y trazabilidad

---

## 3. No alcance
[Definir qué NO cubre el proyecto.]

Ejemplo:
- rediseño completo del sistema origen
- reemplazo del ERP
- analítica avanzada no operativa
- soporte a casos fuera del flujo definido

---

## 4. Regla principal del proyecto
Ningún agente, herramienta o persona debe cargar más contexto del necesario para resolver correctamente una tarea.

La claridad estructural tiene prioridad sobre la cantidad de documentación.

---

## 5. Estructura del repositorio
Este proyecto sigue una arquitectura documental y operativa separada por función.

### Núcleo de gobierno
- `AGENTS.md`
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`

### Núcleo operativo
- `tasks/current/active_task.md`
- `tasks/current/implementation_plan.md`
- `tasks/current/open_questions.md`

### Núcleo de decisiones
- `decisions/decision_log.md`
- `decisions/adr/*`

### Núcleo de memoria
- `memory/project_facts.md`
- `memory/constraints.md`
- `memory/known_issues.md`
- `memory/patterns.md`
- `memory/glossary.md`

### Núcleo funcional y técnico
- `docs/product/spec.md`
- `docs/product/requirements.md`
- `docs/product/user_flows.md`
- `docs/architecture/sdd.md`
- `docs/architecture/system_overview.md`
- `docs/architecture/integrations.md`
- `docs/engineering/*`
- `docs/operations/*`

### Ejecución reusable
- `skills/*`
- `workflows/*`

### Código e infraestructura
- `apps/*`
- `tests/*`
- `scripts/*`
- `infra/*`

### Configuración y seguridad
- `config/env_map.md`
- `config/secrets_policy.md`
- `config/integrations_registry.md`
- `config/access_matrix.md`
- `.env.example`

---

## 6. Fuentes de verdad por tipo
Este proyecto mantiene una sola fuente de verdad por categoría.

| Tipo | Archivo principal |
|---|---|
| Estructura del proyecto | `PROJECT_GUIDE.md` |
| Ruta de lectura | `CONTEXT_INDEX.md` |
| Tarea actual | `tasks/current/active_task.md` |
| Plan actual | `tasks/current/implementation_plan.md` |
| Dudas abiertas | `tasks/current/open_questions.md` |
| Decisiones | `decisions/decision_log.md` |
| Hechos vigentes | `memory/project_facts.md` |
| Restricciones | `memory/constraints.md` |
| Problemas conocidos | `memory/known_issues.md` |
| Patrones aprobados | `memory/patterns.md` |
| Especificación funcional | `docs/product/spec.md` |
| Diseño técnico | `docs/architecture/sdd.md` |

---

## 7. Regla sobre SPEC y SDD

### `docs/product/spec.md`
Define qué debe hacer el sistema.

Debe usarse cuando:
- se crea un feature
- cambia una regla de negocio
- cambia alcance funcional

### `docs/architecture/sdd.md`
Define cómo está resuelto técnicamente el sistema.

Debe usarse cuando:
- cambia arquitectura
- cambia integración
- cambia estructura técnica
- hay refactor importante

Ambos documentos son obligatorios, pero no forman parte del contexto mínimo por defecto.

---

## 8. Reglas de contexto

### Contexto mínimo
Todo trabajo empieza con:
1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`

### Contexto dirigido
Agregar solo si hace falta:
- skill relevante
- workflow relevante
- documento técnico puntual
- archivo(s) afectados
- decisión previa relevante
- `spec.md`
- `sdd.md`

### Contexto ampliado
Solo en tareas críticas o transversales:
- varios documentos relacionados
- decisiones múltiples
- documentación arquitectónica
- contexto comprimido

---

## 9. Reglas de documentación
Toda documentación debe tener una función clara.

### Está permitido
- crear documentos que resuelvan una necesidad operativa real
- resumir análisis largos en contexto comprimido
- registrar decisiones con impacto estructural

### No está permitido
- duplicar información
- crear documentos decorativos
- guardar ideas sueltas como si fueran reglas oficiales
- mezclar notas personales con documentación operativa

---

## 10. Reglas de configuración y secretos
Los secretos reales no deben almacenarse en Markdown ni en el repo.

### Documentación permitida
- mapa de variables de entorno
- política de secretos
- registro de integraciones
- matriz de accesos
- `.env.example`

### Prohibiciones
- no guardar tokens reales
- no guardar contraseñas reales
- no copiar secretos en documentos de arquitectura, tasks o decisiones

---

## 11. Reglas de agentes
Los agentes oficiales son:
- Manager
- Coder
- Reviewer
- Debugger

Deben operar según `AGENTS.md`.

No deben:
- asumir contexto no documentado
- tocar áreas fuera del alcance
- redefinir arquitectura sin registrar decisiones
- usar contexto ampliado sin justificación

---

## 12. Reglas de mantenimiento
Este proyecto debe mantenerse vivo.

Se debe revisar periódicamente:
- duplicidades
- documentos obsoletos
- `CONTEXT_INDEX.md`
- `active_task.md`
- decisiones faltantes
- memoria inflada
- falta de contexto comprimido

---

## 13. Criterio de calidad
El proyecto se considera bien estructurado si:

- puede ser retomado sin reconstruir contexto desde cero
- los agentes responden bien con contexto mínimo
- las decisiones son trazables
- no hay duplicación de verdad
- SPEC y SDD están vivos cuando corresponde
- la documentación ayuda a ejecutar

---

## 14. Regla final
Este proyecto debe funcionar como sistema, no como colección de archivos.

La arquitectura documental, el contexto y la ejecución deben permanecer alineados en todo momento.

CONTEXT_INDEX.md
Funciona como un mapa de acceso al contexto; indica qué archivos específicos deben leerse según el tipo de tarea (arquitectura, backend, deploy, etc.) para evitar el consumo innecesario de tokens
# CONTEXT INDEX

## 1. Propósito
Este archivo indica qué documentos consultar según el tipo de tarea.

No explica todo el proyecto.
Explica **qué leer según la necesidad**.

---

## 2. Orden base de lectura
Toda tarea debe comenzar leyendo:

1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`

Luego, agregar solo lo necesario.

---

## 3. Rutas de contexto por tipo de tarea

---

## 3.1 Si la tarea es de feature nuevo
Leer:

- `tasks/current/active_task.md`
- `tasks/current/implementation_plan.md`
- `docs/product/spec.md`
- `docs/product/requirements.md`
- skill relevante
- workflow `workflows/spec.md` o `workflows/implementation.md`

Agregar si hace falta:
- `docs/architecture/sdd.md`
- `decisions/decision_log.md`

---

## 3.2 Si la tarea es de cambio funcional
Leer:

- `tasks/current/active_task.md`
- `docs/product/spec.md`
- `docs/product/requirements.md`
- `decisions/decision_log.md`
- workflow `workflows/spec.md`

Agregar si hace falta:
- `docs/architecture/sdd.md`
- `memory/constraints.md`

---

## 3.3 Si la tarea es de arquitectura o diseño técnico
Leer:

- `docs/architecture/sdd.md`
- `docs/architecture/system_overview.md`
- `docs/architecture/integrations.md`
- `decisions/decision_log.md`
- `memory/project_facts.md`
- workflow `workflows/architecture.md`
- skill `skills/architecture-review.md`

Agregar si hace falta:
- `docs/product/spec.md`
- `memory/constraints.md`

---

## 3.4 Si la tarea es de backend Python
Leer:

- `tasks/current/active_task.md`
- `docs/engineering/coding_standards.md`
- skill `skills/python-backend.md`
- workflow `workflows/implementation.md`

Agregar si hace falta:
- `docs/product/spec.md`
- `docs/architecture/sdd.md`
- archivos afectados del código

---

## 3.5 Si la tarea es de debugging
Leer:

- `tasks/current/active_task.md`
- `docs/engineering/error_handling.md`
- `memory/known_issues.md`
- skill `skills/debug-issue.md`
- workflow `workflows/debugging.md`

Agregar si hace falta:
- `decisions/decision_log.md`
- archivos afectados
- logs
- `docs/architecture/sdd.md` si el fallo es estructural

---

## 3.6 Si la tarea es de revisión de cambios
Leer:

- `tasks/current/active_task.md`
- skill `skills/review-diff.md`
- workflow `workflows/pr-review.md`
- `docs/engineering/coding_standards.md`
- `decisions/decision_log.md`

Agregar si hace falta:
- `docs/architecture/sdd.md`
- `memory/patterns.md`

---

## 3.7 Si la tarea es de testing o validación E2E
Leer:

- `docs/engineering/testing_strategy.md`
- skill `skills/playwright-testing.md`
- workflow `workflows/pr-review.md` o `workflows/implementation.md`
- `tasks/current/active_task.md`

Agregar si hace falta:
- `docs/product/spec.md`
- `docs/architecture/sdd.md`

---

## 3.8 Si la tarea es de scraping o automatización semántica
Leer:

- `tasks/current/active_task.md`
- skill `skills/stagehand-automation.md`
- `docs/operations/runbook.md`
- `memory/constraints.md`

Agregar si hace falta:
- `docs/architecture/integrations.md`
- `docs/engineering/error_handling.md`

---

## 3.9 Si la tarea es de deploy o release
Leer:

- `docs/operations/deployment.md`
- `docs/operations/runbook.md`
- skill `skills/deploy-app.md`
- workflow `workflows/deploy.md`
- `config/env_map.md`
- `config/secrets_policy.md`

Agregar si hace falta:
- `docs/architecture/sdd.md`
- `infra/*`

---

## 3.10 Si la tarea es de investigación documental
Leer:

- objetivo de investigación en `tasks/current/active_task.md`
- skill `skills/summarize-docs.md`
- workflow `workflows/documentation-update.md`

Usar externo si aplica:
- NotebookLM para análisis de fuentes externas

Volver al repo solo con:
- contexto comprimido
- `integration-notes.md`
- resumen accionable
- riesgos o decisiones relevantes

---

## 3.11 Si la tarea es de actualización de memoria
Leer:

- `memory/project_facts.md`
- `memory/known_issues.md`
- `memory/patterns.md`
- skill `skills/memory-update.md`
- workflow `workflows/memory-update.md`

Agregar si hace falta:
- `decisions/decision_log.md`
- `docs/product/spec.md`
- `docs/architecture/sdd.md`

---

## 3.12 Si la tarea es de mantenimiento del framework o del proyecto
Leer:

- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `AGENTS.md`
- skill `skills/framework-maintainer.md`
- skill `skills/project-organizer.md`

Agregar si hace falta:
- `memory/project_facts.md`
- `decisions/decision_log.md`
- `docs/architecture/sdd.md`

---

## 4. Contexto que debe evitarse por defecto
Evitar cargar de entrada:

- todo `docs/`
- todas las ADRs
- todo el repo
- todo `memory/`
- todos los tests
- todos los scripts

Solo cargar eso si la tarea lo justifica.

---

## 5. Regla sobre SPEC y SDD
No cargar `spec.md` y `sdd.md` por defecto en toda tarea.

Usarlos así:

| Documento | Cargar cuando |
|---|---|
| `docs/product/spec.md` | el cambio es funcional |
| `docs/architecture/sdd.md` | el cambio es técnico o arquitectónico |

---

## 6. Regla sobre contexto comprimido
Si existe alguno de estos documentos, priorizarlos antes de releer material crudo:

- `repo-summary.md`
- `incident-summary.md`
- `integration-notes.md`
- `module-map.md`
- `decision-summary.md`

---

## 7. Regla sobre conocimiento satélite
No usar Obsidian como fuente operativa del proyecto.

### Obsidian
Sirve para:
- ideas
- comparativas
- aprendizaje
- conocimiento transversal

### Repo
Sirve para:
- ejecución
- decisiones
- memoria operativa
- contexto oficial

---

## 8. Regla final
Si una tarea necesita demasiados archivos para ser entendida, primero revisar:

- si falta contexto comprimido
- si falta `CONTEXT_INDEX.md`
- si SPEC o SDD están desactualizados
- si el proyecto está mal modularizado

El objetivo de este archivo es reducir carga cognitiva y de tokens, no aumentarla.

docs/product/spec.md
Este archivo actúa como el contrato funcional de cada tarea. Su propósito es definir con total claridad qué se va a construir antes de decidir cómo se va a programar. Es la herramienta principal para mitigar el riesgo de errores lógicos y evitar el desperdicio de recursos en implementaciones incorrectas.
# SPEC

## 1. Objetivo
[Describir qué debe lograr esta funcionalidad o producto.]

Ejemplo:
Permitir bloquear automáticamente la creación de órdenes para clientes marcados como bloqueados.

---

## 2. Problema
[Describir el problema real que se busca resolver.]

Ejemplo:
Actualmente el sistema permite registrar órdenes para clientes bloqueados, generando errores operativos posteriores.

---

## 3. Contexto
[Explicar brevemente el contexto de negocio o proceso.]

Ejemplo:
La validación debe ocurrir antes de confirmar la orden para evitar reprocesos y errores en sistemas downstream.

---

## 4. Alcance
[Definir qué sí cubre este cambio.]

- [Punto 1]
- [Punto 2]
- [Punto 3]

---

## 5. No alcance
[Definir qué NO cubre este cambio.]

- [Punto 1]
- [Punto 2]

---

## 6. Actor o usuario principal
[Quién usa esta funcionalidad o quién se ve afectado.]

Ejemplo:
Operador interno / usuario de Backoffice / sistema integrador.

---

## 7. Reglas de negocio
[Listar reglas explícitas.]

- [Regla 1]
- [Regla 2]
- [Regla 3]

Ejemplo:
- Si `customer.status = blocked`, no se puede confirmar la orden.
- Debe mostrarse un mensaje de error claro al usuario.

---

## 8. Casos de uso
### Caso 1
**Dado** [contexto]
**Cuando** [acción]
**Entonces** [resultado esperado]

### Caso 2
**Dado** [contexto]
**Cuando** [acción]
**Entonces** [resultado esperado]

---

## 9. Casos borde / edge cases
- [Caso borde 1]
- [Caso borde 2]
- [Caso borde 3]

---

## 10. Criterios de aceptación
- [Criterio 1]
- [Criterio 2]
- [Criterio 3]

Ejemplo:
- No se crean órdenes para clientes bloqueados.
- El sistema devuelve mensaje claro.
- La validación queda cubierta por test.

---

## 11. Riesgos funcionales
- [Riesgo 1]
- [Riesgo 2]

---

## 12. Dependencias
- [Dependencia de sistema]
- [Dependencia de dato]
- [Dependencia de proceso]

---

## 13. Impacto esperado
[Qué mejora se espera conseguir.]

Ejemplo:
Reducir errores operativos, evitar reprocesos y aumentar control preventivo.

---

## 14. Referencias
- [Link o documento relacionado]
- [Decision log / ADR]
- [Tarea actual]

docs/architecture/sdd.md
El Software Design Document se utiliza para definir el diseño técnico de cambios estructurales, integraciones nuevas o refactorizaciones importantes antes de tocar el código
# SDD

## 1. Propósito
[Describir qué parte del diseño técnico cubre este documento.]

Ejemplo:
Definir la arquitectura técnica para validar clientes bloqueados antes de confirmar una orden.

---

## 2. Resumen del diseño
[Explicar en pocas líneas cómo se resolverá técnicamente.]

Ejemplo:
La validación se implementará en el backend antes de la confirmación de la orden, consultando el estado del cliente y bloqueando la operación si aplica.

---

## 3. Componentes involucrados
- [Componente 1]
- [Componente 2]
- [Componente 3]

Ejemplo:
- API Orders
- Service Customer Validation
- Base de datos / proveedor de estado de cliente

---

## 4. Flujo técnico
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
4. [Paso 4]

Ejemplo:
1. El frontend envía solicitud de confirmación.
2. El backend consulta el estado del cliente.
3. Si está bloqueado, rechaza la operación.
4. Si está activo, continúa el flujo normal.

---

## 5. Diagrama o referencia de flujo
[Agregar link o referencia si existe un diagrama.]

---

## 6. Estructura de módulos / archivos afectados
- [Archivo / módulo 1]
- [Archivo / módulo 2]
- [Archivo / módulo 3]

---

## 7. Contratos o interfaces
### Endpoint / interfaz 1
- Método:
- Ruta:
- Input:
- Output:
- Errores posibles:

### Servicio / interfaz interna
- Nombre:
- Input:
- Output:
- Reglas:

---

## 8. Modelo de datos afectado
- [Entidad / tabla / campo]
- [Cambio esperado]
- [Impacto]

---

## 9. Integraciones
- [Integración 1]
- [Integración 2]

Para cada una indicar:
- propósito
- dirección del flujo
- dependencia
- riesgo

---

## 10. Manejo de errores
- [Error 1]
- [Error 2]
- [Error 3]

Ejemplo:
- Cliente no encontrado
- Servicio de estado no disponible
- Timeout de integración

---

## 11. Riesgos técnicos
- [Riesgo 1]
- [Riesgo 2]
- [Riesgo 3]

---

## 12. Restricciones técnicas
- [Restricción 1]
- [Restricción 2]

---

## 13. Observabilidad / logging
- Qué se debe loguear
- Qué no se debe loguear
- Eventos importantes a monitorear

---

## 14. Testing esperado
- Unit tests
- Integration tests
- E2E si aplica

---

## 15. Impacto en arquitectura
[Explicar si el cambio modifica diseño, acoplamientos, performance o mantenibilidad.]

---

## 16. Decisiones relacionadas
- `decisions/decision_log.md`
- ADR relacionada
- SPEC relacionada

---

## 17. Pendientes
- [Pendiente 1]
- [Pendiente 2]

tasks/current/active_task.md
Describe la tarea inmediata, su objetivo, estado (pendiente, en curso, etc.) y los criterios de éxito específicos
# ACTIVE TASK

## 1. Nombre de la tarea
[Nombre corto y claro]

Ejemplo:
Bloquear confirmación de órdenes para clientes bloqueados

---

## 2. Objetivo inmediato
[Qué se busca lograr ahora.]

---

## 3. Estado
[Elegir uno]
- pendiente
- en análisis
- en implementación
- en revisión
- bloqueada
- terminada

---

## 4. Tipo de tarea
[Elegir uno o más]
- feature
- bug
- refactor
- research
- arquitectura
- deploy
- documentación
- testing

---

## 5. Alcance
[Qué incluye esta tarea.]

- [Punto 1]
- [Punto 2]

---

## 6. No alcance
[Qué no incluye esta tarea.]

- [Punto 1]
- [Punto 2]

---

## 7. Resultado esperado
[Definir entregable concreto.]

Ejemplo:
Validación implementada, testeada y documentada.

---

## 8. Archivos o módulos afectados
- [Archivo 1]
- [Archivo 2]
- [Archivo 3]

---

## 9. Documentos que deben cargarse
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- [skill relevante]
- [workflow relevante]
- [spec o sdd si aplica]

---

## 10. Riesgos o bloqueos
- [Bloqueo 1]
- [Bloqueo 2]

---

## 11. Próximo paso recomendado
[Definir la siguiente acción más concreta.]

---

## 12. Referencias
- SPEC:
- SDD:
- Decision log:
- Ticket / issue:

memory/project_facts.md
Almacena hechos técnicos y de negocio que son estables y no cambian con frecuencia
# PROJECT FACTS

## 1. Propósito del archivo
Este archivo contiene solo hechos vigentes del proyecto.

Reglas:
- no opiniones
- no debates
- no hipótesis
- no histórico antiguo
- no decisiones narradas

---

## 2. Nombre del proyecto
[Nombre oficial]

---

## 3. Propósito del proyecto
[Resumen corto del objetivo del sistema]

---

## 4. Stack principal
- Frontend:
- Backend:
- Base de datos:
- Testing:
- Deploy:
- Automatización:
- Observabilidad:

---

## 5. Herramientas aprobadas
- [Herramienta 1]
- [Herramienta 2]
- [Herramienta 3]

---

## 6. Agente principal definido
- [Cline / Codex / otro]

---

## 7. Entornos
- local
- dev
- staging
- prod

[Indicar cuáles existen realmente]

---

## 8. Fuente de verdad operativa
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `tasks/current/active_task.md`
- `decisions/decision_log.md`

---

## 9. Documentos funcionales y técnicos oficiales
- `docs/product/spec.md`
- `docs/architecture/sdd.md`

---

## 10. Integraciones vigentes
- [Integración 1]
- [Integración 2]
- [Integración 3]

---

## 11. Restricciones estructurales vigentes
- [Restricción 1]
- [Restricción 2]

---

## 12. Estado actual del proyecto
[Ejemplo: MVP / en desarrollo / productivo / mantenimiento]

---

## 13. Owner técnico
[Nombre o rol]

---

## 14. Última actualización
[Fecha] # PROJECT FACTS

## 1. Propósito del archivo
Este archivo contiene solo hechos vigentes del proyecto.

Reglas:
- no opiniones
- no debates
- no hipótesis
- no histórico antiguo
- no decisiones narradas

---

## 2. Nombre del proyecto
[Nombre oficial]

---

## 3. Propósito del proyecto
[Resumen corto del objetivo del sistema]

---

## 4. Stack principal
- Frontend:
- Backend:
- Base de datos:
- Testing:
- Deploy:
- Automatización:
- Observabilidad:

---

## 5. Herramientas aprobadas
- [Herramienta 1]
- [Herramienta 2]
- [Herramienta 3]

---

## 6. Agente principal definido
- [Cline / Codex / otro]

---

## 7. Entornos
- local
- dev
- staging
- prod

[Indicar cuáles existen realmente]

---

## 8. Fuente de verdad operativa
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `tasks/current/active_task.md`
- `decisions/decision_log.md`

---

## 9. Documentos funcionales y técnicos oficiales
- `docs/product/spec.md`
- `docs/architecture/sdd.md`

---

## 10. Integraciones vigentes
- [Integración 1]
- [Integración 2]
- [Integración 3]

---

## 11. Restricciones estructurales vigentes
- [Restricción 1]
- [Restricción 2]

---

## 12. Estado actual del proyecto
[Ejemplo: MVP / en desarrollo / productivo / mantenimiento]

---

## 13. Owner técnico
[Nombre o rol]

---

## 14. Última actualización
[Fecha]

config/env_map.md
Mapea las variables de entorno necesarias, indicando su propósito y el servicio al que pertenecen, sin exponer valores reales
# ENV MAP

## 1. Propósito
Este archivo documenta las variables de entorno necesarias para el proyecto.

Reglas:
- no guardar valores reales
- no guardar secretos
- documentar solo nombre, propósito y uso

---

## 2. Variables de entorno

| Variable | Obligatoria | Entorno | Uso | Servicio asociado | Notas |
|---|---|---|---|---|---|
| `APP_ENV` | Sí | todos | definir entorno | app | local/dev/staging/prod |
| `DATABASE_URL` | Sí | local/dev/prod | conexión DB | postgres/supabase | no guardar valor real |
| `API_BASE_URL` | Sí | dev/prod | URL de backend | api | |
| `OPENAI_API_KEY` | Opcional | según uso | llamadas IA | OpenAI | no guardar valor |
| `SUPABASE_URL` | Opcional | según uso | conexión supabase | Supabase | |
| `SUPABASE_KEY` | Opcional | según uso | autenticación supabase | Supabase | |
| `N8N_WEBHOOK_URL` | Opcional | según uso | integración workflow | n8n | |
| `PLAYWRIGHT_BASE_URL` | Opcional | test | pruebas E2E | Playwright | |

---

## 3. Reglas
- Toda variable nueva debe agregarse aquí
- Toda variable real debe vivir fuera del repo
- `.env.example` debe mantenerse sincronizado con este archivo

.env.example

# ENV MAP

## 1. Propósito
Este archivo documenta las variables de entorno necesarias para el proyecto.

Reglas:
- no guardar valores reales
- no guardar secretos
- documentar solo nombre, propósito y uso

---

## 2. Variables de entorno

| Variable | Obligatoria | Entorno | Uso | Servicio asociado | Notas |
|---|---|---|---|---|---|
| `APP_ENV` | Sí | todos | definir entorno | app | local/dev/staging/prod |
| `DATABASE_URL` | Sí | local/dev/prod | conexión DB | postgres/supabase | no guardar valor real |
| `API_BASE_URL` | Sí | dev/prod | URL de backend | api | |
| `OPENAI_API_KEY` | Opcional | según uso | llamadas IA | OpenAI | no guardar valor |
| `SUPABASE_URL` | Opcional | según uso | conexión supabase | Supabase | |
| `SUPABASE_KEY` | Opcional | según uso | autenticación supabase | Supabase | |
| `N8N_WEBHOOK_URL` | Opcional | según uso | integración workflow | n8n | |
| `PLAYWRIGHT_BASE_URL` | Opcional | test | pruebas E2E | Playwright | |

---

## 3. Reglas
- Toda variable nueva debe agregarse aquí
- Toda variable real debe vivir fuera del repo
- `.env.example` debe mantenerse sincronizado con este archivo

manager.md
Define la identidad y responsabilidades del orquestador del sistema. Su función es interpretar la intención del usuario, gestionar el ruteo de tareas, mantener la documentación de alto nivel y asegurar que el flujo de trabajo sea eficiente y alineado con los objetivos del proyecto.
# MANAGER AGENT

## 1. Propósito
Orquestar la ejecución del proyecto.

## 2. Cuándo se activa
- nueva intención del usuario
- cambio de tarea
- necesidad de routing
- necesidad de decidir contexto
- necesidad de decidir agente responsable

## 3. Cuándo NO se activa
- implementación técnica ya claramente delegada
- revisión puntual de diff
- debugging profundo ya asignado

## 4. Inputs esperados
- intención del usuario
- `PROJECT_GUIDE.md`
- `CONTEXT_INDEX.md`
- `tasks/current/active_task.md`

## 5. Orden de lectura
1. `PROJECT_GUIDE.md`
2. `CONTEXT_INDEX.md`
3. `tasks/current/active_task.md`
4. skill o workflow si aplica
5. documento dirigido si aplica

## 6. Responsabilidades
- clasificar tarea
- decidir contexto
- activar workflow
- activar skill
- asignar agente responsable
- decidir si corresponde actualizar memoria o decisiones

## 7. Herramientas permitidas
- agente principal del proyecto
- skills
- workflows
- documentación oficial

## 8. Herramientas prohibidas
- no debe usar contexto ampliado sin justificación
- no debe tocar código directamente salvo excepción explícita

## 9. Output esperado
- tipo de tarea
- agente asignado
- contexto a cargar
- workflow a usar
- siguiente paso claro

## 10. Fallback
Si falta contexto:
- detener ejecución amplia
- pedir o generar estructura mínima
- registrar incertidumbre en `open_questions.md`

coder.md
Establece el marco operativo para la implementación técnica. Su foco principal es la generación de código limpio y funcional, siguiendo estrictamente las especificaciones de diseño y los estándares de programación definidos, sin añadir complejidad innecesaria.
# CODER AGENT

## 1. Propósito
Implementar cambios técnicos dentro del alcance definido.

## 2. Cuándo se activa
- nueva funcionalidad
- cambio de código
- refactor
- integración
- corrección técnica ya entendida

## 3. Cuándo NO se activa
- tarea aún no clasificada
- debugging sin causa probable
- revisión de calidad final

## 4. Inputs esperados
- `active_task.md`
- skill técnica relevante
- workflow de implementación
- archivos afectados
- `spec.md` o `sdd.md` si aplica

## 5. Orden de lectura
1. `tasks/current/active_task.md`
2. skill relevante
3. workflow relevante
4. archivos afectados
5. `docs/product/spec.md` si el cambio es funcional
6. `docs/architecture/sdd.md` si el cambio es técnico

## 6. Responsabilidades
- implementar
- modificar código
- mantener coherencia
- respetar alcance
- producir cambios revisables

## 7. Herramientas permitidas
- agente principal
- Aider si aplica
- documentación técnica
- tests

## 8. Herramientas prohibidas
- no redefinir arquitectura sin decisión
- no inventar reglas de negocio
- no tocar áreas fuera de alcance

## 9. Output esperado
- cambio implementado
- resumen de lo hecho
- archivos tocados
- riesgos detectados
- recomendación de revisión

## 10. Fallback
Si el contexto es insuficiente:
- detener implementación amplia
- pedir `spec.md`, `sdd.md` o skill correspondiente
- registrar duda en `open_questions.md`

reviewer.md
Describe las funciones de control de calidad y cumplimiento. Actúa como un filtro crítico que valida que las implementaciones cumplan con los criterios de aceptación, no introduzcan deuda técnica y respeten las políticas de seguridad y arquitectura del sistema.
# REVIEWER AGENT

## 1. Propósito
Validar calidad, coherencia e impacto de los cambios.

## 2. Cuándo se activa
- después de implementación
- antes de merge
- antes de deploy
- cuando hay cambio sensible

## 3. Cuándo NO se activa
- cuando aún no hay cambio concreto
- cuando la tarea sigue en exploración inicial

## 4. Inputs esperados
- diff o archivos modificados
- `active_task.md`
- skill de revisión
- reglas técnicas
- decisiones relevantes

## 5. Orden de lectura
1. `tasks/current/active_task.md`
2. skill `review-diff.md`
3. `docs/engineering/coding_standards.md`
4. diff o archivos modificados
5. `decision_log.md` si aplica
6. `sdd.md` si el cambio es estructural

## 6. Responsabilidades
- revisar calidad
- evaluar riesgos
- verificar coherencia
- detectar efectos colaterales
- recomendar ajustes

## 7. Herramientas permitidas
- agente principal
- documentación técnica
- diff
- tests y resultados

## 8. Herramientas prohibidas
- no redefinir el objetivo de negocio
- no implementar rediseños grandes sin devolución explícita

## 9. Output esperado
- hallazgos
- riesgos
- cambios recomendados
- veredicto: aprobado / aprobado con cambios / no aprobado

## 10. Fallback
Si faltan decisiones o contexto:
- marcar revisión incompleta
- indicar qué documento falta
- no aprobar ciegamente

debugger.md
Define el protocolo especializado para la resolución de anomalías. Su misión es realizar análisis de causa raíz (RCA) ante fallos técnicos, proponer soluciones definitivas en lugar de parches temporales y mantener actualizada la memoria de problemas conocidos.
# REVIEWER AGENT

## 1. Propósito
Validar calidad, coherencia e impacto de los cambios.

## 2. Cuándo se activa
- después de implementación
- antes de merge
- antes de deploy
- cuando hay cambio sensible

## 3. Cuándo NO se activa
- cuando aún no hay cambio concreto
- cuando la tarea sigue en exploración inicial

## 4. Inputs esperados
- diff o archivos modificados
- `active_task.md`
- skill de revisión
- reglas técnicas
- decisiones relevantes

## 5. Orden de lectura
1. `tasks/current/active_task.md`
2. skill `review-diff.md`
3. `docs/engineering/coding_standards.md`
4. diff o archivos modificados
5. `decision_log.md` si aplica
6. `sdd.md` si el cambio es estructural

## 6. Responsabilidades
- revisar calidad
- evaluar riesgos
- verificar coherencia
- detectar efectos colaterales
- recomendar ajustes

## 7. Herramientas permitidas
- agente principal
- documentación técnica
- diff
- tests y resultados

## 8. Herramientas prohibidas
- no redefinir el objetivo de negocio
- no implementar rediseños grandes sin devolución explícita

## 9. Output esperado
- hallazgos
- riesgos
- cambios recomendados
- veredicto: aprobado / aprobado con cambios / no aprobado

## 10. Fallback
Si faltan decisiones o contexto:
- marcar revisión incompleta
- indicar qué documento falta
- no aprobar ciegamente
decisions/decision_log.md
Este archivo es la "caja negra" del proyecto. Su función es evitar que el agente (o vos mismo en un mes) pierda tiempo rediscutiendo por qué se eligió una tecnología o camino
# DECISION LOG

## 1. Propósito
[cite_start]Registrar decisiones estructurales y técnicas de forma cronológica para evitar redundancia en el análisis[cite: 82].

## 2. Registro de Decisiones
| ID | Fecha | Decisión | Motivo | Impacto | Ref. ADR |
|:---|:---|:---|:---|:---|:---|
| DEC-001 | YYYY-MM-DD | Ejemplo: Uso de FastAPI | Alta velocidad y tipado | Backend | [ADR-001] |

## 3. Reglas de Mantenimiento
- [cite_start]No registrar tareas diarias, solo cambios de dirección técnica o funcional[cite: 82].
- Cada entrada debe ser breve; el detalle va en la carpeta `adr/` si es complejo.

memory/known_issues.md
Indispensable para que el agente Debugger no intente arreglar algo que ya sabemos que está roto por causas externas o deuda técnica asumida
# KNOWN ISSUES

## 1. Problemas Activos
| ID | Descripción | Workaround / Solución Temporal | Prioridad |
|:---|:---|:---|:---|
| BUG-001 | El deploy falla si la clave API no se refresca | Reiniciar el túnel n8n manualmente | Alta |

## 2. Limitaciones del Sistema (Deuda Técnica)
- [Limitación 1]: Explicar por qué no se puede resolver ahora.

## 3. Instrucción para Agentes
[cite_start]Antes de iniciar un proceso de debugging, consultar este archivo para evitar "hallucinations" sobre errores ya identificados[cite: 94].

skills/route-task.md
Este es el cerebro del Manager. Clasifica la intención del usuario y asigna el workflow correcto para no improvisar prompts
# SKILL: ROUTE TASK

## 1. Propósito
[cite_start]Interpretar la intención del usuario y activar el flujo operativo más eficiente[cite: 14, 55].

## 2. Lógica de Enrutamiento
- [cite_start]**Si es un error/fallo:** Activar `workflows/debugging.md` y agente `Debugger`[cite: 148].
- **Si es un feature nuevo:** Activar `workflows/spec.md` -> `workflows/implementation.md`.
- **Si es un cambio de arquitectura:** Requiere actualización de `docs/architecture/sdd.md`.
- **Si es una duda técnica:** Consultar `memory/` y `docs/` antes de responder.

## 3. Selección de Contexto
[cite_start]El Manager debe decidir qué archivos de `docs/` o `skills/` son estrictamente necesarios para la tarea actual[cite: 173].

workflows/spec.md
Define el "qué" antes del "cómo". Ningún código se toca sin una SPEC aprobada si el cambio es funcional.
# WORKFLOW: SPECIFICATION (SPEC)

## 1. Entrada
- Intención del usuario clara en `active_task.md`.

## 2. Pasos Obligatorios
1. [cite_start]**Definir Objetivo:** ¿Qué problema real resolvemos?[cite: 159, 160].
2. [cite_start]**Alcance:** Listar qué entra y, sobre todo, qué queda fuera[cite: 161].
3. [cite_start]**Reglas de Negocio:** Lógica pura (ej: "Si X > 0, entonces Y")[cite: 162].
4. [cite_start]**Criterios de Aceptación:** ¿Cómo sabemos que terminamos y funciona?[cite: 163].

## 3. Salida
- Archivo `docs/product/spec.md` actualizado y validado.

workflows/implementation.md
La guía paso a paso para el Coder. Asegura que el código sea consistente con el estándar.
# WORKFLOW: IMPLEMENTATION

## 1. Pre-requisitos
- `active_task.md` en estado "en análisis".
- [cite_start]`spec.md` o `sdd.md` consultados (contexto dirigido)[cite: 180].

## 2. Secuencia de Ejecución
1. **Plan de Implementación:** Crear el paso a paso en `tasks/current/implementation_plan.md`.
2. [cite_start]**Coding:** Modificar archivos respetando `coding_standards.md`[cite: 240].
3. **Self-Testing:** Validar cambios con tests unitarios o manuales definidos en la SPEC.
4. [cite_start]**Documentación:** Actualizar `memory/` o `docs/` si la realidad del proyecto cambió[cite: 183].

## 3. Cierre
- Solicitar revisión al agente `Reviewer`.

config/secrets_policy.md
La barrera de seguridad. Este archivo no guarda secretos, dicta cómo NO guardarlos.
# SECRETS POLICY

## 1. Prohibiciones Críticas
- [cite_start]**NUNCA** escribir API Keys, tokens o passwords en archivos `.md`, logs o commits[cite: 151, 183].
- [cite_start]**NUNCA** subir archivos `.env` al repositorio[cite: 155].

## 2. Protocolo de Gestión
- Las credenciales viven en el entorno (Vercel, GitHub Secrets, local `.env` ignorado).
- [cite_start]Consultar `config/env_map.md` para ver los nombres oficiales de las variables[cite: 153, 154].

## 3. Rotación
- Si un secreto se filtra en un chat de IA, debe considerarse comprometido y rotarse inmediatamente.



| VS Code | Git y GitHub | NotebookLM | Vercel | TypeScript |
| --- | --- | --- | --- | --- |
| Cline | GitHub Actions | n8n | Docker | modelos locales |
| Codex | Playwright | Supabase | FastAPI | OpenRouter / OpenCode como opcionales |
| Aider | Stagehand | Postgres | Next.js |  |
| Escenario / intención | Herramienta principal | Herramientas de apoyo | Contexto mínimo a cargar | Salida esperada | Cuándo NO usar (antipatrón) |
| --- | --- | --- | --- | --- | --- |
| Necesito avanzar una tarea de código end-to-end con gobernanza, reglas y memoria | Cline | VS Code, Git/GitHub | PROJECT_GUIDE.md + CONTEXT_INDEX.md + tasks/current/active_task.md | Cambios implementados + diff revisable + notas/decisiones si corresponde | Si tu prioridad es “cero configuración” y quieres mínima fricción inicial |
| Quiero la ruta más simple/productiva dentro de OpenAI para implementar tareas | Codex | VS Code, Git/GitHub | PROJECT_GUIDE.md + tasks/current/active_task.md (y CONTEXT_INDEX.md si el repo es mediano/grande) | Implementación + comandos/steps reproducibles | Si el proyecto requiere gobernanza documental estricta y routing de contexto más formal |
| Necesito un cambio quirúrgico con control de diff y rollback fácil | Aider | Git (commits/diffs), VS Code para revisar | active_task.md + 1–3 archivos objetivo (solo los necesarios) | Commits limpios + cambio puntual | Cuando la tarea requiere coordinación amplia del repo o decisiones arquitectónicas |
| Tengo que investigar documentación extensa (PDFs / múltiples fuentes) y devolver un resumen comprimido | NotebookLM | (Luego) Cline/Codex para ejecutar en el repo | Fuentes externas + objetivo de síntesis (preguntas concretas) | Resumen estructurado + puntos accionables + “qué falta por confirmar” | Usarlo como fuente de verdad del proyecto o “memoria viva” dentro del repo |
| Necesito automatizar procesos repetitivos entre apps (APIs, correos, hojas, bots) | n8n | (Si hay lógica compleja) Python/FastAPI | Definición del workflow + entradas/salidas + credenciales gestionadas fuera del repo | Workflow trazable + logs básicos + documentación del flujo | Meter lógica de negocio compleja dentro del flujo por comodidad |
| Estoy partiendo un proyecto nuevo y necesito decidir el “cerebro principal” | Cline o Codex (elige uno) | Git/GitHub, VS Code | PROJECT_GUIDE.md + CONTEXT_INDEX.md (si aplica) + active_task.md | Regla oficial definida + setup mínimo operativo | Usar ambos como “cerebro” del mismo proyecto (duplica patrones y confunde gobernanza) |
| Criterio | Claude Code | Cline | Codex | OpenCode |
| --- | --- | --- | --- | --- |
| Tipo de producto | Agente de codificación de Anthropic, disponible en terminal, IDE, desktop, web y otras superficies. (Claude API Docs) | Extensión/agente centrado en IDE con Memory Bank, rules, skills, workflows y subagents. (docs.cline.bot) | Agente de OpenAI para IDE/CLI/cloud que lee, edita y ejecuta código. (Desarrolladores de OpenAI) | Agente open source multi-provider con soporte de modelos remotos y locales. (OpenCode) |
| Proveedor / lock-in | Alto lock-in con Anthropic, aunque admite ciertos proveedores soportados en algunas superficies. (Claude API Docs) | El lock-in depende del modelo que conectes, pero la herramienta está muy asociada a su ecosistema y flujo propio. (docs.cline.bot) | Alto lock-in con OpenAI. (Desarrolladores de OpenAI) | Bajo lock-in: soporta 75+ proveedores y modelos locales. (OpenCode) |
| Fortaleza principal | Razonamiento agentic fuerte sobre el repo, ejecución de comandos y configuración avanzada con skills y subagents. (Claude API Docs) | Gobernanza del contexto: Memory Bank, rules condicionales, skills y subagents para mantener limpio el contexto principal. (docs.cline.bot) | Productividad práctica y menor fricción si ya trabajas en OpenAI/ChatGPT. (Desarrolladores de OpenAI) | Flexibilidad estructural: agentes, subagents, skills, commands, AGENTS.md, permisos y soporte multi-provider/local. (OpenCode) |
| Memoria / contexto persistente | Sí, pero más vía archivos/configuración del ecosistema .claude y CLAUDE.md que mediante un patrón “memory bank” tan explícito como Cline. (Claude API Docs) | Muy fuerte: Memory Bank está documentado como capacidad central. (docs.cline.bot) | Tiene configuración compartida entre IDE y CLI, pero su propuesta oficial pone más énfasis en el agente operativo que en una memoria documental nativa estilo Cline. (Desarrolladores de OpenAI) | Usa AGENTS.md, config por proyecto y skills on-demand; fuerte en reglas, pero menos prescriptivo que Cline en “memoria del proyecto” como patrón oficial. (OpenCode) |
| Skills | Sí, con SKILL.md y uso directo o por relevancia. (Claude API Docs) | Sí. Skills son parte oficial de la personalización. (docs.cline.bot) | No es el eje distintivo de su documentación pública en IDE; su fortaleza pública está más en el agente y las tareas end-to-end. (Desarrolladores de OpenAI) | Sí, con skills cargadas bajo demanda mediante el tool nativo skill. (OpenCode) |
| Subagentes | Sí; Anthropic documenta subagents y carpetas dedicadas para ellos. (Claude API Docs) | Sí; documentados como feature experimental para investigación paralela sin ensuciar el contexto principal. (docs.cline.bot) | No es la capacidad más visible de la oferta pública del IDE extension. (Desarrolladores de OpenAI) | Sí; distingue primary agents y subagents, con built-ins como Build/Plan y subagents General/Explore. (OpenCode) |
| Reglas de proyecto | Sí, con CLAUDE.md y settings jerárquicos por usuario/proyecto/local. (Claude API Docs) | Sí, con Rules y reglas condicionales. (docs.cline.bot) | Sí, pero menos “file-centric” como propuesta pública que Cline/OpenCode/Claude Code. (Desarrolladores de OpenAI) | Sí, con AGENTS.md global y por proyecto, y compatibilidad con CLAUDE.md. (OpenCode) |
| Comandos personalizados | Sí, a través de skills y flags de system prompt, además de comandos del CLI. (Claude API Docs) | Sí, vía workflows, skills y personalización del agente. (docs.cline.bot) | Más orientado a la interacción directa con el agente que a un sistema abierto de commands markdown. (Desarrolladores de OpenAI) | Sí, con archivos markdown en commands/ y frontmatter para agente/modelo. (OpenCode) |
| Modelos locales | No como propuesta principal del producto. (Claude API Docs) | Puede trabajar con distintos proveedores, pero no está posicionado principalmente como plataforma multi-local. (docs.cline.bot) | No como propuesta principal. (Desarrolladores de OpenAI) | Sí, explícitamente soporta modelos locales. (OpenCode) |
| Encaje con este framework | Muy bueno si decides centrarte en Anthropic y quieres un agente fuerte con skills, configuración y subagentes. (Claude API Docs) | Excelente si el foco del framework es gobernanza documental, memoria y control de contexto. (docs.cline.bot) | Excelente si el foco es simplicidad operativa, productividad y consolidación en OpenAI. (Desarrolladores de OpenAI) | Excelente como capa abierta de evolución, laboratorio o soberanía técnica; menos ideal como camino único inicial para principiantes. (OpenCode) |
| Costo / acceso | Requiere suscripción Claude Pro/Max/Team/Enterprise, Claude Console o acceso mediante ciertos cloud providers soportados. (Claude API Docs) | Depende del modelo/proveedor conectado. (docs.cline.bot) | Incluido en ChatGPT Plus, Pro, Business, Edu y Enterprise según OpenAI. (Desarrolladores de OpenAI) | El software es abierto; el costo depende del proveedor/modelo elegido o del cómputo local. (OpenCode) |
| Dificultad de arranque | Media. Potente, pero con más decisiones de configuración que un flujo extremadamente simple. (Claude API Docs) | Media. Gana mucho valor cuando ya tienes reglas, memoria y estructura documental. (docs.cline.bot) | Baja a media. Es la ruta más simple si ya estás en OpenAI. (Desarrolladores de OpenAI) | Media a alta. Requiere más criterio para proveedores, config y modos de operación. (OpenCode) |
| Mejor uso recomendado | Proyectos donde quieres un agente principal potente y no te molesta el ecosistema Anthropic. | Frameworks con fuerte énfasis en contexto, memoria y routing. | Equipos o usuarios que quieren producir rápido y consolidar stack OpenAI. | Frameworks avanzados, laboratorio multi-provider, costos controlados y modelos locales. |
| Escenario | Herramienta(s) recomendada(s) | Prerequisito mínimo | Salida esperada | Cuándo NO usar (antipatrón) |
| --- | --- | --- | --- | --- |
| Quiero bloquear errores antes de merge (estándar mínimo de calidad) | GitHub Actions (CI) | Repo en GitHub + scripts reproducibles (lint/test/build) | Checks automáticos en PR (pass/fail) + artefactos/logs | Implementar CI sin tests ni comandos reproducibles (solo “por tenerlo”) |
| Necesito validar flujos críticos en la UI (login, compra, formularios) | Playwright (E2E) | Ambiente de prueba estable + selectores razonables + datos de prueba | Suite E2E reproducible local/CI | Usarlo para exploración muy abierta donde el DOM cambia a cada rato (mejor Stagehand) |
| Necesito automatizar navegación en un sitio cambiante o con selectores frágiles | Stagehand (capa semántica) + (si aplica) Playwright | Objetivo claro del flujo + límites (qué tocar / qué extraer) | Script/flujo que interactúa y/o extrae datos con mayor resiliencia | Usarlo como reemplazo estándar de E2E serio o para CI determinista |
| Tengo un backend Python y necesito una API mantenible | FastAPI | Contrato de endpoints + modelos de datos + reglas de estructura del repo | Endpoints claros + validación básica + docs automáticas | Montar FastAPI si solo necesitas un script puntual sin servicio |
| Estoy construyendo una app web con UI moderna y deploy rápido | Next.js + TypeScript + Vercel | Repositorio listo + variables de entorno definidas | Preview deployments + producción simple | Forzar Next.js si no hay UI web o si la prioridad real es solo backend/automatización |
| Quiero base de datos relacional como fuente de verdad | Postgres (local o managed) + (opcional) Supabase | Modelo de datos inicial + migraciones/semillas (aunque sea mínimo) | Esquema claro + datos persistentes + consultas SQL trazables | Meter DB antes de validar si el producto realmente requiere persistencia |
| Quiero acelerar auth + DB + storage sin operar infraestructura | Supabase | Definición de roles/permisos + entorno (dev/prod) + políticas de secretos | Auth funcionando + DB managed + storage integrado | Usarlo sin definir reglas mínimas (RLS/roles) y terminar con permisos inseguros |
| Necesito que el backend corra igual en dev/staging/prod o fuera de mi máquina | Docker | Comandos de build/run documentados + variables externas (no hardcode) | Contenedor reproducible + ejecución consistente | Agregar Docker en un POC pequeño si solo añade fricción y nadie desplegará aún |
| Ya hay usuarios o uso real y necesito saber qué falla en producción | Sentry | Entorno productivo + tagging básico (release/env) | Alertas + trazas de error accionables | Instrumentarlo en prototipo temprano sin usuarios (ruido y costo sin retorno) |
| Necesito una ruta “mínima viable” para pasar de código a algo usable | Vercel (frontend) + Supabase (backend managed) + GitHub Actions (CI mínimo) | Repo ordenado + env vars + checklist mínimo de deploy | URL funcional + pipeline básico + rollback simple | Diseñar microservicios/k8s/observabilidad completa antes de tener un MVP |
| Elemento | Qué es | Para qué sirve |
| --- | --- | --- |
| tasks/current/active_task.md | Contexto operativo | Saber qué se está haciendo ahora |
| decisions/decision_log.md | Memoria de decisiones | Evitar rediscutir lo ya resuelto |
| memory/project_facts.md | Memoria estable | Recordar hechos vigentes del proyecto |
| memory/patterns.md | Memoria reusable | Reaplicar patrones válidos sin reinventar |
| docs/engineering/coding-standards.md | Regla técnica reusable | Mantener coherencia técnica |
| Problema | Cómo lo resuelve CONTEXT_INDEX.md |
| --- | --- |
| El usuario no recuerda dónde está la información | Da una ruta directa de consulta |
| El agente “adivina” qué leer | Reduce inferencia innecesaria |
| Se carga demasiado contexto | Limita la lectura a lo pertinente |
| El repo crece y se vuelve difícil de navegar | Lo convierte en un sistema navegable |
| Tipo de información | Fuente principal |
| --- | --- |
| Estructura del proyecto | PROJECT_GUIDE.md |
| Ruta de consulta | CONTEXT_INDEX.md |
| Trabajo actual | tasks/current/active_task.md |
| Plan actual | tasks/current/implementation_plan.md |
| Dudas abiertas | tasks/current/open_questions.md |
| Decisiones previas | decisions/decision_log.md y ADRs |
| Hechos estables | memory/project_facts.md |
| Restricciones | memory/constraints.md |
| Problemas conocidos | memory/known_issues.md |
| Patrones aprobados | memory/patterns.md |
| Reglas técnicas | docs/engineering/*, skills y workflows |
| Archivo | Función |
| --- | --- |
| project_facts.md | Hechos vigentes del proyecto |
| constraints.md | Restricciones técnicas, de negocio, acceso, seguridad o costo |
| known_issues.md | Problemas conocidos y workarounds |
| glossary.md | Términos del dominio y siglas |
| patterns.md | Patrones aprobados del proyecto |
| Herramienta | Rol correcto | Qué no debe hacer |
| --- | --- | --- |
| NotebookLM | Research aplicado sobre fuentes externas | No debe ser memoria viva del repo |
| Obsidian | Knowledge base personal y transversal | No debe ser fuente oficial del proyecto |
| Repo Git | Fuente de verdad operativa del proyecto | No debe absorber notas personales sin gobernanza |
| Carpeta | Propósito |
| --- | --- |
| 00_inbox/ | Capturas rápidas, ideas sueltas, notas sin procesar |
| 01_framework/ | Evolución del framework general |
| 02_tools/ | Notas sobre herramientas |
| 03_architecture/ | Mapas, conceptos y diseño |
| 04_learning/ | Apuntes de aprendizaje |
| 05_project-notes/ | Notas personales ligadas a proyectos |
| 06_comparisons/ | Comparativas formales |
| 07_patterns/ | Patrones reusables |
| 99_archive/ | Material inactivo |
| Escenario | Qué cargar primero | Qué agregar solo si hace falta | Qué evitar |
| --- | --- | --- | --- |
| Tarea técnica normal | PROJECT_GUIDE.md, CONTEXT_INDEX.md, active_task.md | Skill + workflow + archivo técnico puntual | Leer todo docs/ |
| Debugging moderado | Base mínima + known_issues.md + guía de errores | Decisión previa + archivos afectados | Releer toda la arquitectura |
| Refactor grande | Base mínima + skill + workflow + decisiones relevantes | Módulos relacionados + contexto ampliado justificado | Mandar todo el repo al agente |
| Research documental | NotebookLM + objetivo claro | Resumen comprimido al repo | Usar NotebookLM como fuente oficial |
| Conocimiento personal | Obsidian | Comparativas, patrones, aprendizaje | Guardar ahí la tarea activa oficial |
| Elemento | Rol |
| --- | --- |
| Agente | Ejecuta |
| Skill | Guía cómo ejecutar |
| Workflow | Define secuencia |
| Tipo de tarea | Agente |
| --- | --- |
| Nueva funcionalidad | Coder |
| Validación | Reviewer |
| Error | Debugger |
| Coordinación | Manager |
| Capa | Función |
| --- | --- |
| Agente | Decide qué hacer |
| Herramienta | Ejecuta en el entorno (IDE, CLI, etc.) |
| Modelo | Genera razonamiento / output |
| Agente | Tipo de tarea | Herramienta recomendada | Modelo recomendado (base) | Modelo premium (cuando escalar) | Benchmark calidad | Benchmark costo | Benchmark velocidad | Observación crítica |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Manager | Clasificación, planificación, routing | Cline / Codex / OpenCode | GPT-4.1-mini / Qwen / DeepSeek | GPT-5 / Claude Opus | Medio-alto | Bajo | Muy rápido | No necesita modelo caro si el contexto está bien estructurado |
| Coder | Implementación, refactor, integración | Codex / Cline / Aider | GPT-4.1 / DeepSeek / Qwen | GPT-5 / Claude Sonnet/Opus | Alto | Medio | Medio | Aquí está el mayor ROI de usar modelos medios |
| Reviewer | Validación, calidad, riesgos | Codex / Cline | GPT-4.1 / Claude Sonnet | GPT-5 / Claude Opus | Muy alto | Medio-alto | Medio | Reviewer es donde más se justifica subir calidad |
| Debugger | Análisis de errores, causa raíz | Codex / Cline | Claude Sonnet / GPT-4.1 | GPT-5 / Claude Opus | Muy alto | Medio-alto | Medio-lento | Debugging complejo es el caso más caro pero más crítico |
| Modelo | Calidad | Costo | Velocidad | Mejor uso |
| --- | --- | --- | --- | --- |
| Qwen / DeepSeek (local o barato) | Media | Muy bajo | Muy rápido | Clasificación, parsing, tareas simples |
| GPT-4.1-mini | Media-alta | Bajo | Muy rápido | Manager, preprocesamiento |
| GPT-4.1 | Alta | Medio | Medio | Coder estándar |
| Claude Sonnet | Muy alta | Medio-alto | Medio | Debugging, análisis profundo |
| GPT-5 / Claude Opus | Máxima | Alto | Más lento | Arquitectura, problemas críticos |
| Herramienta | Mejor encaje | Comentario crítico |
| --- | --- | --- |
| Codex | Coder / Reviewer | Mejor equilibrio general |
| Cline | Manager / sistemas complejos | Mejor gobernanza de contexto |
| Aider | Coder quirúrgico | Cambios controlados |
| OpenCode | Multi-model / avanzado | Más flexible pero más complejo |
| Paso | Agente | Modelo |
| --- | --- | --- |
| Clasificación | Manager | GPT-4.1-mini |
| Implementación | Coder | GPT-4.1 |
| Revisión | Reviewer | Claude Sonnet |
| Debug complejo | Debugger | GPT-5 |
| Tipo | Ejemplo | Nivel de complejidad |
| --- | --- | --- |
| Script local | Automatización Excel / scraping | Bajo |
| Bot automatizado | n8n + API + Gmail | Medio |
| API / backend | FastAPI + DB | Medio-alto |
| SaaS completo | Web + backend + auth | Alto |
| Situación | Acción |
| --- | --- |
| Prueba o exploración | Script local |
| Tarea repetitiva | n8n / automatización |
| Integración entre sistemas | API |
| Producto o herramienta | SaaS |
| Componente | Herramienta |
| --- | --- |
| Frontend | Next.js |
| Backend | FastAPI |
| DB | Supabase |
| Auth | Clerk / Supabase |
| Hosting | Vercel |
| Backend deploy | Railway / Render |
| Plataforma | Uso ideal | Complejidad | Costo | Comentario |
| --- | --- | --- | --- | --- |
| Vercel | Frontend | Bajo | Bajo | Ideal para Next.js |
| Railway | Backend simple | Bajo | Bajo-medio | Muy rápido de levantar |
| Render | Backend estable | Medio | Medio | Más robusto |
| Supabase | DB + Auth | Bajo | Bajo | Muy potente |
| Hostinger VPS | Control total | Alto | Bajo | Requiere conocimiento |
| Firebase | Apps simples | Bajo | Medio | Bueno pero limitado |
| Caso | Herramienta |
| --- | --- |
| Web simple | Playwright |
| Web compleja / dinámica | Stagehand |
| Herramienta | Uso |
| --- | --- |
| Sentry | Errores |
| Logs Python | Debug |
| Grafana | Métricas |
| n8n logs | Flujos |
| Componente | Costo |
| --- | --- |
| Vercel | Gratis - bajo |
| Supabase | Gratis - bajo |
| n8n | Gratis (self-hosted) |
| Railway | Bajo |
| Modelos IA | Variable |
| Tipo | Ejemplo |
| --- | --- |
| Guía | PROJECT_GUIDE |
| Índice | CONTEXT_INDEX |
| Técnico | docs/ |
| Operativo | tasks/ |
| Memoria | memory/ |
| Decisiones | decisions/ |
| Tipo de tarea | Cargar SPEC | Cargar SDD |
| --- | --- | --- |
| Nuevo feature | Sí | A veces |
| Cambio funcional | Sí | A veces |
| Refactor técnico | No | Sí |
| Bug pequeño | No | No |
| Cambio arquitectónico | A veces | Sí |
| Nueva integración | A veces | Sí |
| Skill | Rol |
| --- | --- |
| route-task.md | Clasificar tarea y decidir flujo |
| project-organizer.md | Mantener orden documental |
| summarize-docs.md | Crear contexto comprimido |
| plan-change.md | Planificar cambios antes de tocar código |
| review-diff.md | Revisar impacto y coherencia |
| debug-issue.md | Estructurar debugging |
| memory-update.md | Decidir qué debe pasar a memoria |
| framework-maintainer.md | Mantener el framework sano |
| spec-writer.md | Crear o actualizar SPEC |
| architecture-review.md | Revisar o actualizar SDD |
| Skill | Cuándo se vuelve obligatoria |
| --- | --- |
| python-backend.md | Si hay backend Python |
| deploy-app.md | Si hay despliegue |
| playwright-testing.md | Si hay UI automation/testing |
| stagehand-automation.md | Si hay scraping o navegación semántica |
| Workflow | Rol |
| --- | --- |
| spec.md | Convertir necesidad en especificación funcional |
| architecture.md | Convertir cambio técnico en diseño |
| implementation.md | Ejecutar feature o cambio |
| debugging.md | Investigar fallos |
| documentation-update.md | Sincronizar docs |
| memory-update.md | Persistir conocimiento reusable |
| deploy.md | Estandarizar despliegue |
| pr-review.md | Validar cambios antes de merge |
| Capa | Función |
| --- | --- |
| Agente | Ejecuta rol |
| Skill | Indica cómo ejecutar bien |
| Workflow | Define secuencia |
| Herramienta | Ejecuta en entorno real |
| Modelo | Proporciona razonamiento |