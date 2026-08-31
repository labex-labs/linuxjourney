---
lesson_id: "cpu-monitoring"
course_id: "process-utilization"
lang: "es"
order_index: 4
title: "Supervisión de la CPU"
description: "Aprende a interpretar los promedios de carga de Linux junto con el número de CPU, la utilización y el estado de las tareas."
meta_title: "Supervisión de la CPU - Utilización de procesos"
meta_description: "Aprende a supervisar la CPU de Linux con uptime e interpreta el promedio de carga, la capacidad y el rendimiento."
meta_keywords: "uptime, supervisión CPU Linux, promedio de carga, rendimiento del sistema, utilización de procesos"
---

La investigación de la CPU comienza separando la carga, la utilización y la capacidad de respuesta. Ningún número por sí solo establece un cuello de botella, así que compara varios intervalos de tiempo y relaciona las métricas del equipo con la carga de trabajo que experimentan realmente los usuarios.

## Leer uptime

`uptime` proporciona un punto de partida compacto:

```text
$ uptime
 17:23:35 up 1 day, 5:59, 2 users, load average: 0.00, 0.02, 0.05
```

Los tres valores finales son promedios de carga de aproximadamente 1, 5 y 15 minutos. Compararlos muestra la tendencia: un valor de 1 minuto mucho mayor puede indicar que la carga aumenta, mientras que un valor de 15 minutos mayor puede indicar que disminuye.

:::single-choice{#cpu-uptime-windows}
¿En qué orden muestra `uptime` los intervalos del promedio de carga?

::option[15, 5 y 1 segundos.]{#cpu-windows-seconds explanation="Los valores son promedios a escala de minutos y no se muestran del más largo al más corto."}
::option[1, 5 y 15 minutos.]{#cpu-windows-one-five-fifteen .correct explanation="El intervalo reciente más corto aparece primero y el más largo, al final."}
::option[Porcentajes actual, mínimo y máximo de CPU.]{#cpu-windows-percentages explanation="El promedio de carga no es un porcentaje mínimo o máximo de CPU."}
:::

## Comprender la carga de Linux

El promedio de carga de Linux cuenta las tareas preparadas para ejecutarse, incluidas las que utilizan o esperan CPU, además de las tareas en espera ininterrumpible, asociadas habitualmente con la E/S. Por tanto, no equivale a la utilización de la CPU.

Una carga de `4.0` tiene implicaciones distintas en sistemas con una y dieciséis CPU lógicas. Averigua el número de unidades de procesamiento disponibles para el sistema con:

```bash
$ nproc
```

Las cuotas de CPU, la afinidad, la virtualización y los límites de contenedores pueden reducir la capacidad visible para una carga de trabajo concreta, por lo que el número de CPU del equipo es solo un punto de partida.

:::single-choice{#cpu-load-not-percentage}
¿Por qué el promedio de carga no es un porcentaje de utilización de CPU?

::option[Porque solo comunica la frecuencia de reloj de la CPU.]{#cpu-load-clock explanation="La velocidad del reloj es una métrica distinta del hardware o del escalado."}
::option[Porque solo mide la memoria física libre.]{#cpu-load-memory explanation="La disponibilidad de memoria se comunica mediante otras métricas."}
::option[Porque incluye tareas preparadas para ejecutarse y tareas en espera ininterrumpible.]{#cpu-load-task-count .correct explanation="La carga se basa en la demanda y el estado de espera de las tareas, no en un porcentaje del tiempo de CPU transcurrido."}
:::

## Comparar la carga con la actividad de CPU

Recopila varias muestras en vez de depender de una sola salida. Algunas herramientas complementarias útiles son:

```bash
$ top
$ vmstat 1
$ mpstat -P ALL 1
```

`top` combina vistas del equipo y de los procesos. `vmstat` muestra el número de tareas preparadas y bloqueadas junto con categorías de CPU. `mpstat`, proporcionado por `sysstat` en muchas distribuciones, muestra la actividad de cada CPU. La disponibilidad y los campos exactos varían, así que utiliza los manuales locales.

Una carga alta con las CPU ocupadas puede indicar demanda de CPU. Una carga alta con una cantidad notable de tareas bloqueadas, latencia de E/S u observaciones de espera de E/S apunta a otro recurso limitado. Una utilización media baja también puede ocultar una CPU saturada o un pico breve de latencia.

:::single-choice{#cpu-high-load-next-step}
¿Cuál es el mejor paso después de observar un promedio de carga alto?

::option[Comparar mediciones repetidas de CPU, estados de tareas, E/S y carga de trabajo.]{#cpu-load-correlate .correct explanation="Las muestras relacionadas permiten distinguir explicaciones contrapuestas de la carga."}
::option[Reiniciar de inmediato sin recopilar otros datos.]{#cpu-load-reboot explanation="Reiniciar elimina pruebas y puede interrumpir servicios sin identificar la causa."}
::option[Suponer que todas las CPU están completamente utilizadas.]{#cpu-load-assume explanation="La carga puede incluir tareas ininterrumpibles y distribuirse de forma desigual entre las CPU."}
:::

## Evaluar la capacidad y el impacto

No existe una regla universal que exija mantener siempre la carga por debajo del número de CPU. Los sistemas por lotes pueden aceptar colas, mientras que los servicios interactivos pueden incumplir sus objetivos de latencia antes de alcanzar ese punto. Establece una referencia para el mismo equipo y la misma carga de trabajo y compara después el tiempo de respuesta, el rendimiento, la tasa de errores, la saturación y el uso de recursos.

:::single-choice{#cpu-capacity-threshold}
¿Qué debe determinar si la carga observada es aceptable?

::option[El requisito de que el valor permanezca siempre por debajo de uno.]{#cpu-below-one explanation="La capacidad multinúcleo y los objetivos de la carga de trabajo hacen que este umbral fijo sea poco fiable."}
::option[Únicamente el número de usuarios que muestra `uptime`.]{#cpu-user-count explanation="Los usuarios con una sesión de shell iniciada no representan toda la demanda de la carga de trabajo."}
::option[La referencia y los objetivos de servicio de la carga de trabajo.]{#cpu-baseline-objectives .correct explanation="La aceptabilidad depende del comportamiento esperado y del rendimiento visible para el usuario, no de un umbral universal."}
:::

## Resumen

Ahora puedes interpretar el promedio de carga como una parte de una investigación de CPU.

1. Lee los intervalos de carga de 1, 5 y 15 minutos.
2. Distingue la carga de tareas de los porcentajes de tiempo de CPU.
3. Compara la carga con la capacidad de procesamiento disponible.
4. Relaciona mediciones repetidas del equipo con los resultados del servicio.
