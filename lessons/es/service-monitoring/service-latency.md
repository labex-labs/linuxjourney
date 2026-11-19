---
lesson_id: "service-latency"
course_id: "service-monitoring"
lang: "es"
order_index: 4
title: "Latencia"
description: "Aprende a comparar los tiempos habituales de las peticiones con los más lentos."
meta_title: "Latencia - Monitorización de servicios"
meta_description: "Aprende a comparar los tiempos habituales de las peticiones con los más lentos."
meta_keywords: "latencia, monitorización de servicios, DevOps, Linux Journey"
---

La **latencia** es el tiempo que tarda una petición. Una sola cifra puede ocultar diferencias en lo que experimentan los usuarios. Compara una petición típica con las más lentas de la misma ruta y del mismo intervalo.

## Leer una muestra pequeña

Los cinco tiempos siguientes están en milisegundos. Cuatro peticiones tardaron menos de 100 milisegundos y una tardó dos segundos.

```text
40  50  60  70  2000
```

La **mediana**, también llamada percentil 50, es el valor central de la muestra ordenada. Aquí es de 60 milisegundos. La petición más lenta tardó 2000 milisegundos. La media, que se calcula dividiendo la suma entre cinco, es de 444 milisegundos.

:::single-choice{#service-latency-sample-median} ¿Qué valor corresponde a la petición que queda en medio al ordenar la muestra?

::option[444 milisegundos.]{#service-latency-sample-median-a explanation="Es la media, en la que influye el tiempo de la petición más lenta."}
::option[60 milisegundos.]{#service-latency-sample-median-b .correct explanation="El tercero de los cinco valores ordenados es la mediana."}
::option[2000 milisegundos.]{#service-latency-sample-median-c explanation="Ese es el mayor valor observado."}
:::

## Examinar las peticiones más lentas

Un **percentil** indica el valor por debajo del cual queda una parte de las observaciones. El percentil 95 de latencia, que suele mostrarse como p95, indica un umbral en el extremo de los tiempos más altos de una muestra amplia. Usa siempre la misma definición del panel. Con muy pocas peticiones, las estimaciones de ese extremo pueden variar mucho.

:::single-choice{#service-latency-slow-end} La mediana apenas cambia, pero los visitantes siguen informando de demoras ocasionales. ¿Qué datos conviene mirar?

::option[Los tiempos más altos de la distribución de latencia y el número de peticiones.]{#service-latency-slow-end-a .correct explanation="Las respuestas más lentas pueden tardar más aunque el valor central apenas cambie."}
::option[Solo la mediana otra vez.]{#service-latency-slow-end-b explanation="Así puedes pasar por alto cambios que afectan a una pequeña parte de las visitas."}
::option[El tamaño total del archivo de registro.]{#service-latency-slow-end-c explanation="El tamaño del archivo no indica cuánto tardaron las peticiones."}
:::

## Comparar peticiones similares

Compara la misma ruta con un tráfico similar. Es normal que una descarga tarde más que una pequeña consulta de estado. Si una ruta destaca por su lentitud, examina sus registros de peticiones y sus dependencias en el mismo intervalo. Usa la métrica para localizar el problema y los demás datos para investigarlo.

:::single-choice{#service-latency-compare-route} ¿Qué comparación te permite comprobar mejor si la misma página de inicio se volvió más lenta tras publicar una versión?

::option[Las respuestas de la página de inicio de hoy con las descargas del mes pasado.]{#service-latency-compare-route-a explanation="Las operaciones y los periodos son distintos, así que cuesta interpretar la comparación."}
::option[Una sola petición por versión, sin contexto temporal.]{#service-latency-compare-route-b explanation="Una medición aislada dejará fuera las variaciones."}
::option[La latencia de la página de inicio en intervalos comparables antes y después de la publicación.]{#service-latency-compare-route-c .correct explanation="Comparar la misma ruta con una carga similar facilita interpretar el cambio."}
:::

## Resumen

Ya puedes interpretar juntos los tiempos habituales y los de las peticiones más lentas.

1. Encuentra la mediana de una muestra pequeña ordenada.
2. Revisa los tiempos más altos junto con el número de peticiones.
3. Compara peticiones similares antes de investigar las diferencias.
