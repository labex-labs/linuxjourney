---
lesson_id: "ci-overview"
course_id: "continuous-integration"
lang: "es"
order_index: 1
title: "Integración continua"
description: "Aprende cómo la integración continua comprueba cambios pequeños antes de incorporarlos a una rama compartida."
meta_title: "Integración continua - Integración continua"
meta_description: "Aprende cómo la integración continua comprueba cambios pequeños antes de incorporarlos a una rama compartida."
meta_keywords: "integración continua, CI, DevOps, Linux Journey"
---

Un cambio en la página de inicio puede verse bien en tu navegador y aun así fallarle a otra persona. La **integración continua**, o CI, reúne cambios con frecuencia y ejecuta comprobaciones que pueden repetirse sobre revisiones concretas.

## Relacionar un cambio con su comprobación

Una revisión identifica la versión de los archivos que se comprueba. Cuando un cambio propuesto modifica `index.html`, la CI puede comprobar esa versión e indicar si cumple una condición. En este sitio, por ejemplo, la comprobación podría buscar el encabezado requerido. El equipo puede usar el resultado para decidir si fusiona los cambios.

:::single-choice{#ci-overview-revision-result} Una comprobación pasó el lunes. Un nuevo commit cambia la página el martes. ¿Qué demuestra el resultado del lunes?

::option[Que las dos revisiones cumplen la condición.]{#ci-overview-revision-result-b explanation="El commit posterior necesita su propio resultado."}
::option[Que la revisión del lunes pasó la comprobación.]{#ci-overview-revision-result-a .correct explanation="El resultado corresponde a la revisión que se comprobó."}
::option[Que la página nueva ya está disponible para los visitantes.]{#ci-overview-revision-result-c explanation="Comprobar los archivos fuente no da información sobre un despliegue activo."}
:::

## Leer una comprobación fallida

Supón que una comprobación indica que falta el encabezado esperado. La persona que propuso el cambio ya sabe por dónde empezar a investigar. Lee qué se esperaba y cuál fue el resultado antes de cambiar la página. A veces hay un error en el archivo. Otras veces cambia el comportamiento esperado y hay que actualizar la comprobación.

:::single-choice{#ci-overview-failed-action} ¿Qué debes revisar primero si falla la comprobación del encabezado?

::option[El encabezado esperado y el archivo de la revisión comprobada.]{#ci-overview-failed-action-b .correct explanation="Al compararlos puedes ver qué provocó la diferencia."}
::option[El artefacto de la última ejecución exitosa.]{#ci-overview-failed-action-a explanation="Ese artefacto contiene un resultado anterior. La comprobación que falló y el archivo actual dan pistas más directas."}
::option[Los ajustes de red de los visitantes.]{#ci-overview-failed-action-c explanation="Esta comprobación lee un archivo sin hacer peticiones desde el navegador."}
:::

## Distinguir comprobación y entrega

Una canalización puede comprobar archivos, generar una salida y entregarla a una etapa de despliegue. Una **compilación** prepara algo que usarán etapas posteriores, como una carpeta de archivos listos para servir. Un **despliegue** instala o pone en marcha una versión en un entorno. Tu primer flujo de CI comprueba una página antes de entregarla.

:::single-choice{#ci-overview-output-vs-live} Las pruebas pasaron y se generó un archivo comprimido del sitio. ¿Cómo sabes si los visitantes ya pueden usar esa versión?

::option[Con una segunda copia del registro de la comprobación.]{#ci-overview-output-vs-live-a explanation="El registro describe la comprobación y la compilación."}
::option[Con la existencia del archivo comprimido.]{#ci-overview-output-vs-live-b explanation="El archivo puede existir sin que el servidor lo esté usando."}
::option[Con un registro de despliegue y una petición exitosa a la página esperada.]{#ci-overview-output-vs-live-c .correct explanation="Así puedes asociar la versión generada con una respuesta del entorno de destino."}
:::

## Resumen

Ya puedes explicar qué papel tiene la CI en el recorrido de un cambio.

1. Asocia cada resultado con una revisión concreta.
2. Usa una comprobación fallida para decidir qué investigar primero.
3. Distingue entre comprobar, compilar y desplegar.
