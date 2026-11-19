---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "es"
order_index: 5
title: "Referencias de tráfico"
description: "Aprende a comparar intervalos de tráfico similares antes de considerar anómalo un cambio."
meta_title: "Referencias de tráfico - Monitorización de redes"
meta_description: "Aprende a comparar intervalos de tráfico similares antes de considerar anómalo un cambio."
meta_keywords: "referencias de tráfico, monitorización de redes, ciberseguridad, Linux Journey"
---

Una **referencia** describe el comportamiento que sueles observar en unas condiciones definidas. Al monitorizar el tráfico, puede ser un recuento habitual o un rango de valores para el mismo servicio y la misma hora del día.

## Elegir intervalos comparables

Una página pública puede recibir más tráfico durante la jornada laboral. Si quieres detectar un cambio, compara intervalos con rutinas similares. Este ejemplo cuenta las peticiones a un servicio en intervalos de cinco minutos.

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

Las 230 peticiones se salen del rango habitual de las mañanas laborables. El rango nocturno sería menos útil para comparar.

:::single-choice{#network-traffic-baselines-baseline-fit} ¿Qué fila sirve como referencia para el intervalo de las 09:00 de hoy?

::option[Las noches habituales a las 02:00.]{#network-traffic-baselines-baseline-fit-b explanation="Ese horario tiene otro patrón de tráfico."}
::option[Las 230 peticiones observadas hoy, por sí solas.]{#network-traffic-baselines-baseline-fit-c explanation="Para saber qué cambió, necesitas comparar el recuento actual con otro dato."}
::option[Los días laborables habituales a las 09:00.]{#network-traffic-baselines-baseline-fit-a .correct explanation="Coincide con la hora y el servicio que estás revisando."}
:::

## Buscar contexto

Un aviso en la página o una tarea programada pueden explicar un cambio. Revisa las rutas, los horarios y los cambios aprobados antes de decidir si debes investigar más. La referencia destaca una diferencia y te da una pregunta por la que empezar.

:::single-choice{#network-traffic-baselines-baseline-explain} El tráfico se duplicó después de un lanzamiento anunciado. ¿Qué debes comprobar?

::option[Dar por hecho que la diferencia demuestra que una cuenta fue comprometida.]{#network-traffic-baselines-baseline-explain-a explanation="El recuento por sí solo no indica una causa ni un evento relacionado con una cuenta."}
::option[Comparar las horas y las rutas del tráfico con las que se esperaban del lanzamiento.]{#network-traffic-baselines-baseline-explain-b .correct explanation="Así compruebas una explicación plausible con datos relacionados."}
::option[Ignorar el cambio porque un lanzamiento siempre explica cualquier pico.]{#network-traffic-baselines-baseline-explain-c explanation="Un cambio previsto puede coincidir con actividad ajena al lanzamiento."}
:::

## Revisar cómo se tomaron las mediciones

Un cambio en la recogida de datos puede alterar el recuento aunque el tráfico siga igual. Si ayer se empezó a monitorizar otra red, comprueba qué tráfico incluye cada intervalo. Anota el servicio, el punto de observación, la hora y la unidad junto con la comparación.

:::single-choice{#network-traffic-baselines-changed-coverage} El sistema de recogida empezó a registrar un segundo sitio. ¿Cómo haces que la próxima comparación sea más útil?

::option[Comparar recuentos del mismo sitio que cubran los mismos orígenes.]{#network-traffic-baselines-changed-coverage-c .correct explanation="Mantener el mismo alcance ayuda a distinguir un cambio en el tráfico de un cambio en la cobertura."}
::option[Comparar ambos totales sin comprobar qué incluyen.]{#network-traffic-baselines-changed-coverage-a explanation="El cambio en la recogida de datos hace que esos totales sean menos comparables."}
::option[Comparar el nuevo total con el de ayer después de ampliar el intervalo.]{#network-traffic-baselines-changed-coverage-b explanation="Un intervalo más largo seguirá mezclando alcances si los totales incluyen sitios y orígenes distintos."}
:::

## Resumen

Ya puedes determinar si una comparación de red tiene una referencia adecuada.

1. Comprueba que coincidan el servicio, el horario y la unidad.
2. Busca cambios previstos antes de interpretar una diferencia.
3. Comprueba si cambió la cobertura de la recogida de datos.
