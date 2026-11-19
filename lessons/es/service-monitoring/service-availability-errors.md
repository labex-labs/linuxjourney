---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "es"
order_index: 3
title: "Disponibilidad y errores"
description: "Aprende a comparar los errores de las peticiones a partir del intervalo y del total de peticiones."
meta_title: "Disponibilidad y errores - Monitorización de servicios"
meta_description: "Aprende a comparar los errores de las peticiones a partir del intervalo y del total de peticiones."
meta_keywords: "disponibilidad y errores, monitorización de servicios, DevOps, Linux Journey"
---

Un servicio puede responder a la mayoría de los visitantes aunque algunas peticiones fallen. Usa el total de peticiones y el número de fallos del mismo intervalo para estimar qué proporción de las peticiones observadas falló.

## Calcular la tasa de errores

Para calcular la **tasa de errores**, divide el número de peticiones fallidas entre el total de peticiones observadas. Multiplica el resultado por 100 para expresarlo como porcentaje.

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

En el primer intervalo hay dos fallos en cien peticiones, es decir, un 2 %. En el siguiente también hay dos fallos, pero esta vez hubo veinte peticiones, lo que da un 10 %.

:::single-choice{#service-availability-errors-compare-windows} ¿En qué intervalo fue mayor la proporción de fallos?

::option[De 09:05 a 09:10.]{#service-availability-errors-compare-windows-b .correct explanation="Dos fallos en veinte peticiones representan una proporción mayor que dos en cien."}
::option[Fue igual en ambos, porque los dos tuvieron dos fallos.]{#service-availability-errors-compare-windows-a explanation="El número total de peticiones es distinto."}
::option[De 09:00 a 09:05, porque hubo más tráfico.]{#service-availability-errors-compare-windows-c explanation="Al haber más peticiones, el mismo número de fallos representa una proporción menor."}
:::

## Comparar peticiones con el mismo alcance

Fíjate en el intervalo, la ruta y lo que se considera un fallo. Un punto de acceso de comprobación de estado puede responder correctamente aunque falle una página que necesita otro servicio. Si quieres comprobar lo que experimentan los usuarios de esa página, cuenta las peticiones a esa página.

:::single-choice{#service-availability-errors-route-scope} El punto de acceso de comprobación de estado siempre responde correctamente, pero los clientes informan de errores al finalizar la compra. ¿Qué debes examinar?

::option[Solo las respuestas del punto de acceso de comprobación de estado.]{#service-availability-errors-route-scope-b explanation="Esas respuestas corresponden a otra operación."}
::option[El nombre de la cuenta de servicio.]{#service-availability-errors-route-scope-c explanation="Ese dato no indica cuántas peticiones se vieron afectadas."}
::option[Las peticiones a la ruta de finalización de compra y sus fallos.]{#service-availability-errors-route-scope-a .correct explanation="Esa es la ruta donde los clientes encontraron el problema."}
:::

## Interpretar periodos con poco tráfico

Si llegan dos peticiones y falla una, la tasa observada es del 50 %. Ese resultado describe la muestra. Con pocas peticiones, la tasa puede variar mucho, así que indica el total junto al porcentaje. Si no hubo peticiones, el porcentaje de errores del tráfico real queda sin definir. Una prueba programada aparte puede indicar si el servicio respondió a una petición.

:::single-choice{#service-availability-errors-zero-traffic} En un intervalo no hubo peticiones de visitantes. ¿Qué debes informar sobre su porcentaje de errores?

::option[Demuestra que la disponibilidad fue perfecta.]{#service-availability-errors-zero-traffic-a explanation="No hubo ninguna petición de visitantes que permita afirmarlo."}
::option[El intervalo no contiene datos de peticiones para calcular un porcentaje de errores.]{#service-availability-errors-zero-traffic-c .correct explanation="Si necesitas saber si el servicio responde, usa una prueba aparte."}
::option[Es del 100 % con total seguridad.]{#service-availability-errors-zero-traffic-b explanation="No se observó ninguna petición que pueda servir de denominador."}
:::

## Resumen

Ya puedes explicar una tasa de errores con el contexto que necesita.

1. Compara los fallos con el total de peticiones del mismo intervalo.
2. Elige la ruta y la definición de fallo que correspondan a lo que quieres comprobar.
3. Indica el número de peticiones cuando haya poco tráfico.
