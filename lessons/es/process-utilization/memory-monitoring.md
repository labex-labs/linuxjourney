---
lesson_id: "memory-monitoring"
course_id: "process-utilization"
lang: "es"
order_index: 6
title: "Supervisión de la memoria"
description: "Aprende a interpretar muestras de memoria, paginación, procesos, E/S y CPU de vmstat."
meta_title: "Supervisión de la memoria - Utilización de procesos"
meta_description: "Aprende a supervisar la memoria de Linux con vmstat e interpreta la memoria, la paginación, la E/S y la CPU."
meta_keywords: "supervisión de memoria, vmstat, memoria Linux, paginación, rendimiento del sistema"
---

Linux utiliza deliberadamente la memoria que de otro modo estaría inactiva para cachés, por lo que un valor `free` pequeño no demuestra por sí solo presión de memoria. `vmstat` ayuda a relacionar la memoria con las tareas preparadas para ejecutarse, la paginación, la E/S y la actividad de CPU.

## Tomar muestras con vmstat

Recopila una muestra por segundo:

```bash
$ vmstat 1
```

La primera fila de datos suele comunicar promedios desde el arranque; las filas posteriores abarcan cada intervalo. Detén la orden con `Ctrl-C` después de capturar un período representativo. Las unidades y los campos disponibles varían, así que consulta `vmstat --unit` y el manual local.

:::single-choice{#vmstat-interval-rows}
¿Qué filas son más adecuadas para observar cambios segundo a segundo con `vmstat 1`?

::option[Las filas posteriores al informe inicial.]{#vmstat-later-rows .correct explanation="Las filas posteriores describen cada intervalo solicitado en vez del período acumulado."}
::option[Únicamente los encabezados situados sobre la primera fila de datos.]{#vmstat-headings explanation="Los encabezados definen campos, pero no contienen muestras de actividad."}
::option[Únicamente una fila copiada de otro equipo.]{#vmstat-other-host explanation="Un sistema distinto no representa la carga de trabajo actual."}
:::

## Procesos y memoria

Los campos habituales de procesos son `r`, tareas preparadas para ejecutarse, y `b`, tareas bloqueadas en espera ininterrumpible. Los campos de memoria incluyen intercambio utilizado (`swpd`), memoria inactiva (`free`), búferes (`buff`) y caché (`cache`). Son valores de todo el sistema, no consumo por proceso.

Para obtener una vista más sencilla de la memoria disponible actualmente, compárala con:

```bash
$ free -h
```

La estimación `available` suele ser más útil que `free` por sí sola, porque la caché recuperable puede satisfacer asignaciones nuevas.

:::single-choice{#vmstat-free-memory}
¿Por qué puede ser normal un valor `free` bajo en Linux?

::option[Porque el valor siempre excluye toda la RAM física.]{#vmstat-excludes-ram explanation="Es un campo de memoria, aunque debe comprobarse su unidad exacta."}
::option[Porque el kernel puede utilizar la memoria inactiva para cachés recuperables.]{#vmstat-reclaimable-cache .correct explanation="La memoria en caché suele poder recuperarse cuando las aplicaciones la necesitan."}
::option[Porque poca memoria libre demuestra que la CPU está apagada.]{#vmstat-cpu-off explanation="La asignación de memoria y el estado de energía de la CPU no guardan esa relación."}
:::

## Paginación y E/S

`si` y `so` muestran las tasas de entrada y salida del intercambio. Una paginación sostenida combinada con latencia y actividad de recuperación de memoria puede indicar presión, pero un uso del intercambio (`swpd`) distinto de cero no demuestra por sí solo un problema actual. `bi` y `bo` comunican tasas de entrada y salida de bloques, y no se limitan al tráfico de intercambio.

:::single-choice{#vmstat-swap-pressure}
¿Qué prueba respalda mejor un diagnóstico de presión de memoria actual?

::option[Un valor `swpd` distinto de cero sin ninguna otra observación.]{#vmstat-swpd-alone explanation="Las páginas pueden permanecer en el intercambio después de una presión anterior, por lo que la cantidad por sí sola no basta."}
::option[Paginación sostenida relacionada con actividad de recuperación y latencia de la carga de trabajo.]{#vmstat-correlated-pressure .correct explanation="Las pruebas repetidas y relacionadas conectan el comportamiento de la memoria con el impacto actual."}
::option[El nombre del equipo mostrado al iniciar sesión.]{#vmstat-hostname explanation="Un nombre de equipo no mide la recuperación ni la actividad de paginación."}
:::

## CPU y actividad del sistema

Las columnas de CPU suelen incluir porcentajes de usuario (`us`), sistema (`sy`), inactividad (`id`), espera de E/S (`wa`) y sustracción (`st`). Las columnas del sistema incluyen interrupciones (`in`) y cambios de contexto (`cs`) por segundo. Interpreta los picos frente a una referencia; las tasas altas de cambios de contexto pueden ser normales para algunas cargas.

:::single-choice{#vmstat-r-column}
¿Qué representa el campo de procesos `r`?

::option[Sistemas de archivos montados como solo lectura.]{#vmstat-readonly explanation="Los indicadores de montaje del sistema de archivos no se representan mediante este campo de procesos."}
::option[Usuarios remotos con shells activos.]{#vmstat-remote-users explanation="Otras herramientas comunican las sesiones iniciadas."}
::option[Tareas preparadas para ejecutarse o que esperan CPU.]{#vmstat-runnable .correct explanation="Comparar este número con la capacidad de CPU puede ayudar a identificar demanda de procesamiento."}
:::

## Resumen

Ahora puedes interpretar `vmstat` como una vista del sistema relacionada en el tiempo.

1. Separa el informe acumulado inicial de las muestras de cada intervalo.
2. Trata la caché como memoria potencialmente recuperable.
3. Relaciona la paginación con la recuperación y el impacto en la aplicación.
4. Lee conjuntamente los campos de procesos, E/S, sistema y CPU.
