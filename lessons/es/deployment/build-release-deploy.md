---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "es"
order_index: 1
title: "Compilación, versión y despliegue"
description: "Aprende a seguir una revisión de origen a través de los registros de compilación, aprobación y despliegue."
meta_title: "Compilación, versión y despliegue - Despliegue"
meta_description: "Aprende a seguir una revisión de origen a través de los registros de compilación, aprobación y despliegue."
meta_keywords: "compilación, versión aprobada, despliegue, DevOps, Linux Journey"
---

Alguien del equipo dice que la versión 2 está lista. Puede significar que sus archivos ya se han generado, que la versión se ha aprobado o que los visitantes ya pueden acceder a ella. Consulta los registros para saber en qué etapa está.

## Identificar la compilación

Una compilación genera un resultado a partir de una revisión concreta del código fuente. En el ejemplo, un sitio web pequeño se empaqueta como imagen de contenedor y se guarda en un registro de imágenes. Anota el commit de origen junto a la referencia de la imagen resultante.

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

Este registro indica qué se generó. Puede que el sitio todavía sirva una versión anterior.

:::single-choice{#build-release-deploy-build-record} ¿Qué registro relaciona la imagen empaquetada con la revisión de origen?

::option[Un marcador en el navegador.]{#build-release-deploy-build-record-b explanation="El marcador contiene una dirección sin indicar cómo se generaron los archivos."}
::option[La compilación 81.]{#build-release-deploy-build-record-a .correct explanation="Incluye tanto el commit de origen como la imagen resultante."}
::option[El nombre de la rama local más reciente.]{#build-release-deploy-build-record-c explanation="Una rama puede cambiar de commit y su nombre no identifica esta compilación."}
:::

## Leer la aprobación de una versión

Una **versión aprobada** (release) identifica una versión que se puede distribuir. Por ejemplo, un registro de aprobación puede autorizar para preproducción la imagen exacta de la compilación 81. Así se puede seguir usando el mismo artefacto tras la aprobación, sin volver a generarlo.

:::single-choice{#build-release-deploy-release-record} La versión 2 está aprobada para preproducción. ¿Qué demuestra eso?

::option[El artefacto registrado está aprobado para ese uso.]{#build-release-deploy-release-record-b .correct explanation="El registro indica qué artefacto se autorizó para preproducción."}
::option[Todos los entornos ya sirven la versión 2.]{#build-release-deploy-release-record-a explanation="La aprobación permite continuar. Para saber qué versión se está ejecutando, hace falta otro registro."}
::option[La versión 2 recibe más peticiones.]{#build-release-deploy-release-record-c explanation="Un registro de aprobación no mide el tráfico."}
:::

## Identificar la versión desplegada

Un **despliegue** coloca una versión concreta en un entorno e inicia o actualiza allí la aplicación. Un entorno, como preproducción o producción, tiene sus propios ajustes y recursos. Una petición exitosa a un punto de acceso que indica la versión puede ayudarte a comprobar cuál está respondiendo.

```text
Staging version response: 2
Production version response: 1
```

En este ejemplo, la versión nueva responde en preproducción, mientras que en producción sigue respondiendo la versión 1.

:::single-choice{#build-release-deploy-running-version} Una persona quiere verificar que la versión 2 responde en producción. ¿Qué dato le serviría directamente?

::option[Una segunda respuesta de preproducción con la versión 2.]{#build-release-deploy-running-version-a explanation="Esa petición sigue comprobando preproducción."}
::option[El mensaje de aprobación de la versión.]{#build-release-deploy-running-version-b explanation="La aprobación no comprueba el servicio en ejecución."}
::option[Una respuesta de la dirección de producción que indique la versión.]{#build-release-deploy-running-version-c .correct explanation="Así se comprueba el entorno que interesa."}
:::

## Resumen

Ya puedes distinguir los registros que aparecen al preparar y desplegar una versión.

1. Relaciona el resultado de una compilación con sus fuentes.
2. Identifica el artefacto cuya distribución se aprobó.
3. Confirma qué versión responde en el entorno previsto.
