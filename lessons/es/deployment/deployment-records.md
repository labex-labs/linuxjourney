---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "es"
order_index: 6
title: "Registros de despliegue"
description: "Aprende a reconstruir un despliegue y una reversión a partir de un registro cronológico breve."
meta_title: "Registros de despliegue - Despliegue"
meta_description: "Aprende a reconstruir un despliegue y una reversión a partir de un registro cronológico breve."
meta_keywords: "registros de despliegue, cronología, reversión, DevOps, Linux Journey"
---

Un registro de despliegue ayuda a relacionar un resultado visible para los usuarios con un cambio. Empieza por anotar la hora, el entorno, la revisión de origen y el artefacto. Añade el resultado de la comprobación y las medidas que se tomaron después.

## Indicar qué cambió

Este registro de prácticas sigue un despliegue concreto. Los identificadores están abreviados para facilitar la lectura.

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200 indica una respuesta exitosa. HTTP 503 indica que el servicio no estaba disponible para esa petición. En un registro real, anota también la comprobación y la dirección consultada.

:::single-choice{#deployment-records-first-prod-change} ¿Qué fila contiene el primer resultado observado en producción para digest-C?

::option[La fila 09:12 prod.]{#deployment-records-first-prod-change-b .correct explanation="Indica la versión que se intentó desplegar en producción y el fallo de la comprobación."}
::option[La fila 09:00 staging.]{#deployment-records-first-prod-change-a explanation="Esa comprobación se ejecutó en otro entorno."}
::option[La fila 09:18 prod.]{#deployment-records-first-prod-change-c explanation="Esa fila registra otro artefacto después de la reversión."}
:::

![Cronología simulada con una prueba exitosa en preproducción, un HTTP 503 en producción y una reversión a la versión 2](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## Explicar la reversión

La última fila muestra que se volvió a digest-B. La comprobación de versión y el resultado de la petición a la página de inicio describen el estado tras la reversión. Esos datos no explican la causa concreta del fallo anterior. Registra por separado las hipótesis hasta tener datos que las respalden.

:::single-choice{#deployment-records-rollback-evidence} ¿Qué puedes afirmar sobre el resultado de las 09:18?

::option[El fallo de las 09:12 se debió a que faltaba una base de datos.]{#deployment-records-rollback-evidence-b explanation="El registro no contiene datos sobre las dependencias."}
::option[Todas las peticiones posteriores tuvieron éxito.]{#deployment-records-rollback-evidence-c explanation="Una comprobación exitosa solo indica el resultado de esa petición."}
::option[Producción volvió a la versión 2 y esa petición a la página de inicio tuvo éxito.]{#deployment-records-rollback-evidence-a .correct explanation="La fila registra la versión restaurada y la respuesta HTTP observada."}
:::

## Entregar el registro a otra persona

Quien revise el caso después debe poder reproducir la observación en las mismas condiciones. Indica cómo se hizo la comprobación, una marca de tiempo con zona horaria y, si está disponible, un enlace a la compilación de origen. Si la causa sigue siendo desconocida, anota qué revisar a continuación.

:::single-choice{#deployment-records-handoff-detail} ¿Qué detalle ayudaría a repetir la comprobación de la página de inicio?

::option[Solo el identificador de la versión anterior.]{#deployment-records-handoff-detail-a explanation="La versión anterior sirve de referencia, pero no permite saber dónde ni cuándo se ejecutó la comprobación."}
::option[La dirección exacta consultada y la hora de la comprobación.]{#deployment-records-handoff-detail-c .correct explanation="Así se puede verificar la misma ruta y comparar otras señales del mismo intervalo."}
::option[La hora en que se creó el commit de origen.]{#deployment-records-handoff-detail-b explanation="Ese dato identifica un evento anterior. Para repetir la comprobación hacen falta la hora y el destino de la petición."}
:::

## Registrar qué imagen se ejecutó

La etiqueta que figura en una nota de despliegue puede reasignarse después de publicar la versión. Si el servicio ya indica la versión 2, registra tanto el artefacto que se está ejecutando como su etiqueta legible. Con esos dos datos podrás comparar la versión más adelante, aunque haya cambiado la etiqueta del registro de imágenes.

:::single-choice{#deployment-records-final-application} La nota de la versión indica site:2. ¿Qué detalle adicional permite comparar con más fiabilidad después?

::option[El resumen criptográfico que obtuvo la última persona que descargó site:2.]{#deployment-records-final-application-c explanation="Una descarga posterior puede devolver un contenido distinto del que está ejecutando el servicio."}
::option[El resumen criptográfico completo de la imagen que se ejecutó.]{#deployment-records-final-application-a .correct explanation="Así puedes identificar el contenido exacto aunque la etiqueta legible apunte después a otro."}
::option[La misma etiqueta copiada en un segundo campo.]{#deployment-records-final-application-b explanation="Repetir la etiqueta no resuelve la ambigüedad."}
:::

## Resumen

Ya puedes leer una cronología de despliegue y entregársela a otra persona.

1. Identifica el entorno, la revisión y el artefacto de un registro.
2. Describe la reversión a partir del resultado observado.
3. Conserva los detalles necesarios para la siguiente comprobación.
