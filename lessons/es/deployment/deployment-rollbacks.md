---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "es"
order_index: 5
title: "Reversiones"
description: "Aprende a elegir una versión que funcionaba y a comprobar si basta con revertir la aplicación."
meta_title: "Reversiones - Despliegue"
meta_description: "Aprende a elegir una versión que funcionaba y a comprobar si basta con revertir la aplicación."
meta_keywords: "reversiones, rollback, compatibilidad de datos, despliegue, DevOps, Linux Journey"
---

Una **reversión** (rollback) devuelve el servicio a una versión anterior que funcionaba. Usa el historial de despliegues para elegir esa versión. Antes de revertir, comprueba si la versión también modificó datos o ajustes compartidos.

## Elegir una versión anterior

En este ejemplo, una petición falla después de desplegar una versión nueva. La última versión verificada fue la 2. Las etiquetas de referencia del ejemplo representan los resúmenes criptográficos completos que aparecerían en un registro real.

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

La versión 2 es una candidata razonable si aún funciona en el entorno actual. Usa la referencia registrada del artefacto para encontrarla.

:::single-choice{#deployment-rollbacks-previous-version} ¿Qué imagen investigarías primero para la reversión?

::option[La imagen más reciente de la caché del anfitrión.]{#deployment-rollbacks-previous-version-a explanation="El orden de la caché no indica cuál era la versión que funcionaba."}
::option[Digest-C, porque es el despliegue más reciente.]{#deployment-rollbacks-previous-version-c explanation="El registro relaciona ese artefacto con la comprobación fallida."}
::option[Digest-B, que pasó las comprobaciones pertinentes.]{#deployment-rollbacks-previous-version-b .correct explanation="El registro la vincula con la última versión verificada."}
:::

## Comprobar la compatibilidad con los datos

Una versión de la aplicación también puede cambiar una base de datos u otro recurso compartido. Iniciar una imagen anterior deja ese estado externo tal como estaba. Averigua si la aplicación anterior puede leer los datos actuales. Si hay que restaurarlos, sigue el plan de recuperación del equipo y ten en cuenta los cambios hechos desde la copia de seguridad.

:::single-choice{#deployment-rollbacks-external-state} La versión 3 cambió el formato de una base de datos. ¿Qué debes verificar antes de iniciar la versión 2 con esa base?

::option[Si la versión 2 pasó la comprobación anterior de la página de inicio.]{#deployment-rollbacks-external-state-b explanation="El resultado anterior hace de la versión 2 una candidata, pero no dice nada sobre el formato actual de la base de datos."}
::option[Si la versión 2 admite el formato actual.]{#deployment-rollbacks-external-state-a .correct explanation="Cambiar la imagen de la aplicación no revierte los datos compartidos."}
::option[Si el nombre de la base de datos aparece en las notas de la versión.]{#deployment-rollbacks-external-state-c explanation="Lo que importa es si el código anterior puede usar los datos actuales."}
:::

## Confirmar el resultado

Después de la reversión, verifica la versión en ejecución y repite la misma comprobación desde la perspectiva del usuario que había fallado. Vuelve a examinar las dependencias importantes. Registra la hora, la versión restaurada y los resultados para que otras personas puedan distinguir el fallo de la recuperación.

:::single-choice{#deployment-rollbacks-rollback-proof} El comando de reversión terminó. ¿Qué dos resultados indican que el servicio se recuperó?

::option[El punto de acceso indica la versión 2 y la comprobación que falló ahora pasa.]{#deployment-rollbacks-rollback-proof-c .correct explanation="Así confirmas la versión prevista y el comportamiento que estaba afectado."}
::option[Dos descargas correctas de la imagen.]{#deployment-rollbacks-rollback-proof-a explanation="Las descargas preparan los archivos, pero no comprueban el servicio en ejecución."}
::option[Una captura anterior de la versión 2.]{#deployment-rollbacks-rollback-proof-b explanation="La captura muestra un estado pasado."}
:::

## Resumen

Ya puedes planificar una reversión a partir de resultados comprobables.

1. Elige una versión que haya demostrado funcionar.
2. Comprueba la compatibilidad con los datos y los ajustes compartidos.
3. Verifica la versión restaurada y el comportamiento visible para el usuario.
