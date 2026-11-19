---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "es"
order_index: 3
title: "Cronología de incidentes"
description: "Aprende a situar las pruebas en una sola cronología e indicar qué horas son inciertas."
meta_title: "Cronología de incidentes - Respuesta a incidentes"
meta_description: "Aprende a situar las pruebas en una sola cronología e indicar qué horas son inciertas."
meta_keywords: "cronología de incidentes, respuesta a incidentes, ciberseguridad, Linux Journey"
---

Una cronología de un incidente ordena las observaciones procedentes de varias fuentes. Usa una zona horaria común y conserva visible la marca de tiempo original en tus registros. Una vez ordenados los datos, puedes preguntarte qué eventos podrían estar relacionados.

## Convertir una marca de tiempo

En este caso, un informe web usa UTC y un registro de despliegue tiene un desfase de dos horas por delante de UTC.

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

En un sistema Linux con GNU date, `-d` lee la marca de tiempo que le pasas y `-u` solicita la salida en UTC. El argumento que empieza por `+` fija el formato de visualización.

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

El resultado es `2026-11-19 09:17:00 UTC`. En este ejemplo es cinco minutos anterior al informe web.

:::single-choice{#incident-timelines-earlier-event} ¿Qué entrada ocurrió primero al convertir ambas a la misma zona horaria?

::option[El registro del despliegue.]{#incident-timelines-earlier-event-a .correct explanation="Al convertir la hora con su desfase se obtienen las 09:17 UTC, antes del informe de las 09:22."}
::option[El informe web.]{#incident-timelines-earlier-event-b explanation="La hora que se ve en el informe es menor porque usa otra zona horaria."}
::option[Ocurrieron exactamente al mismo tiempo.]{#incident-timelines-earlier-event-c explanation="Las horas convertidas difieren en cinco minutos."}
:::

![Conversión registrada con GNU date de las 11:17 con desfase +02:00 a las 09:17 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## Distinguir observaciones de estimaciones

Un informe puede indicar que el primer fallo ocurrió hacia las 09:19. Conserva esa hora como una estimación. La hora a la que el usuario avisó es un dato distinto de la hora real de la primera petición fallida. Indica la fuente y la precisión de la hora en cada fila.

:::single-choice{#incident-timelines-estimated-time} Un compañero dice que fue hacia las 09:19. ¿Cómo debes anotarlo?

::option[Como las 09:19:00 exactas, confirmadas por un registro.]{#incident-timelines-estimated-time-a explanation="La fuente proporciona una estimación."}
::option[Como un evento sin fuente.]{#incident-timelines-estimated-time-c explanation="La fuente ayuda a decidir cuánta confianza depositar en la hora."}
::option[Como una hora aproximada atribuida a ese informe.]{#incident-timelines-estimated-time-b .correct explanation="Así conservas tanto lo que dijo la fuente como el grado de precisión."}
:::

## Ordenar los eventos sin atribuirles una causa

Un despliegue puede preceder a un problema del servicio sin causarlo. Comprueba si cambió la ruta afectada y si otras señales respaldan la relación. Mantén visibles las preguntas abiertas junto a la cronología.

:::single-choice{#incident-timelines-timeline-cause} ¿Qué demuestra por sí sola la secuencia ordenada?

::option[El despliegue causó el fallo público.]{#incident-timelines-timeline-cause-a explanation="El orden sugiere una posibilidad, pero hacen falta más pruebas para determinar la causa."}
::option[El despliegue registrado es anterior al informe web.]{#incident-timelines-timeline-cause-c .correct explanation="Esa es la relación temporal que muestran los registros."}
::option[Ningún otro evento puede ser relevante.]{#incident-timelines-timeline-cause-b explanation="La cronología recoge una selección de observaciones."}
:::

## Resumen

Ya puedes construir una cronología que conserve tanto las pruebas como la incertidumbre.

1. Convierte las horas de los registros a una misma zona horaria.
2. Indica la fuente de cada hora y señala cuáles son estimadas.
3. Usa la secuencia para elegir las siguientes comprobaciones.
