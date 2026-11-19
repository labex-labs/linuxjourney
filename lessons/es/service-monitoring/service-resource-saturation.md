---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "es"
order_index: 5
title: "Saturación de recursos"
description: "Aprende a usar la utilización y las colas para detectar dónde puede estar un servicio llegando a su límite."
meta_title: "Saturación de recursos - Monitorización de servicios"
meta_description: "Aprende a usar la utilización y las colas para detectar dónde puede estar un servicio llegando a su límite."
meta_keywords: "saturación de recursos, monitorización de servicios, DevOps, Linux Journey"
---

Cuando un servicio recibe más trabajo del que uno de sus recursos puede atender en el momento, las peticiones pueden quedar en espera. Si la espera se prolonga, puede reflejarse en una cola y en respuestas más lentas.

## Interpretar la capacidad y la demanda

La **utilización** indica qué parte de un recurso está en uso. Por ejemplo, un grupo de procesos de trabajo puede admitir cuatro tareas a la vez. Si los cuatro procesos están ocupados, el grupo está al máximo de su capacidad en ese momento. Si llega otra tarea, puede esperar en una cola hasta que se libere un proceso.

:::single-choice{#service-resource-saturation-worker-capacity} Los cuatro procesos de trabajo están ocupados y hay tres tareas en cola. ¿Qué sabes?

::option[Hay exactamente siete procesos de trabajo en ejecución.]{#service-resource-saturation-worker-capacity-b explanation="Tres tareas aún esperan y no ocupan ninguna plaza."}
::option[Ya han fallado todas las peticiones.]{#service-resource-saturation-worker-capacity-c explanation="El trabajo en espera puede completarse cuando quede un proceso libre."}
::option[Todas las plazas están ocupadas y hay trabajo en espera.]{#service-resource-saturation-worker-capacity-a .correct explanation="El número de procesos ocupados indica el uso actual y la cola revela el exceso de demanda."}
:::

## Comparar a lo largo del tiempo

Un pico breve es distinto de una cola que crece en varias mediciones consecutivas. Compara la cola con la latencia y el tráfico de las peticiones en el mismo intervalo.

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

En este ejemplo, el grupo ocupado al completo y la cola creciente indican que el trabajo parece llegar más rápido de lo que se completa. Comprueba en qué están ocupados los procesos.

:::single-choice{#service-resource-saturation-sustained-pressure} ¿Qué observación sugiere con más claridad que el recurso sigue al límite?

::option[Dos procesos de trabajo ocupados a las 09:10.]{#service-resource-saturation-sustained-pressure-a explanation="Esa fila muestra que quedaba capacidad y que no había tareas en espera."}
::option[La cola crece mientras todos los procesos siguen ocupados.]{#service-resource-saturation-sustained-pressure-b .correct explanation="El trabajo en espera se acumula mientras se usa toda la capacidad."}
::option[Una respuesta tarda más y la cola permanece vacía.]{#service-resource-saturation-sustained-pressure-c explanation="Una respuesta lenta merece atención. Una cola que crece durante varias mediciones con toda la capacidad ocupada indica con más claridad que la presión se mantiene."}
:::

![Métricas simuladas de los procesos de trabajo con utilización plena y una cola creciente](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## Investigar la causa

Los procesos pueden estar ocupados porque llegan peticiones más rápido, porque se ha ralentizado una dependencia o porque un cambio reciente hace que cada tarea tarde más. Compara el volumen de peticiones, el tiempo de procesamiento y los datos de las dependencias. Otra señal puede ayudarte a decidir cómo responder.

:::single-choice{#service-resource-saturation-next-observation} El volumen de peticiones se mantuvo estable, pero las tareas empezaron a tardar más. ¿Qué puede ayudar a explicar la acumulación?

::option[Revisar juntos la duración de las tareas y los tiempos de respuesta de las dependencias.]{#service-resource-saturation-next-observation-c .correct explanation="Así puedes averiguar por qué el trabajo ocupa las plazas durante más tiempo."}
::option[Cambiar la capacidad antes de recoger más datos.]{#service-resource-saturation-next-observation-a explanation="Aumentar la capacidad quizá no resuelva un bloqueo causado por una dependencia."}
::option[Contar los roles del repositorio.]{#service-resource-saturation-next-observation-b explanation="Esos roles no indican por qué esperan los procesos de trabajo."}
:::

## Resumen

Ya puedes distinguir entre un recurso ocupado y trabajo que sigue acumulado en la cola.

1. Relaciona el recuento de procesos ocupados con la capacidad total del grupo.
2. Compara las colas con el comportamiento de las peticiones a lo largo del tiempo.
3. Investiga qué trabajo ocupa el recurso cuya capacidad se está agotando.
