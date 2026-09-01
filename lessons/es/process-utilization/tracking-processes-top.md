---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "es"
order_index: 1
title: "Seguimiento de procesos: top"
description: "Aprende a utilizar top para interpretar la carga del sistema, la CPU, la memoria y la actividad de cada proceso."
meta_title: "Seguimiento de procesos: top - Utilización de procesos"
meta_description: "Aprende a supervisar recursos del sistema y procesos con top, e interpreta métricas como carga, VIRT y RES."
meta_keywords: "orden top Linux, supervisar procesos, utilización del sistema, rendimiento Linux, VIRT, RES"
---

`top` proporciona una vista actualizada repetidamente de la actividad del sistema y de los procesos en ejecución. Resulta útil para formular una hipótesis sobre el rendimiento, pero una sola muestra con mucha actividad no demuestra la causa de un problema. Compara varias actualizaciones y relaciónalas con registros y métricas específicas de la carga de trabajo.

## Leer el resumen del sistema

Una pantalla habitual comienza con líneas de resumen seguidas de una tabla de procesos:

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

La primera línea contiene la hora actual, el tiempo de actividad, el número de usuarios con sesión iniciada y los promedios de carga de 1, 5 y 15 minutos. La línea de tareas cuenta los estados de los procesos. El promedio de carga no es un porcentaje directo de CPU; en Linux refleja las tareas preparadas para ejecutarse y las que están en espera ininterrumpible, así que interprétalo junto con el número de CPU, la actividad de E/S y la latencia.

:::single-choice{#top-load-average-periods} ¿Qué representan los tres valores de promedio de carga de `top`?

::option[La carga media durante 1, 5 y 15 minutos.]{#top-one-five-fifteen .correct explanation="Los valores resumen intervalos recientes de duración progresivamente mayor."}
::option[El uso de CPU de los tres procesos con más actividad.]{#top-three-processes explanation="La CPU de cada proceso aparece en la tabla de procesos, no en estos tres valores de resumen."}
::option[La memoria libre, la caché y el intercambio en megabytes.]{#top-three-memory-values explanation="La memoria y el intercambio tienen líneas de resumen independientes."}
:::

## Interpretar el tiempo de CPU

Entre los campos habituales de CPU se encuentran:

- `us`: tiempo de ejecución en el espacio de usuario.
- `sy`: tiempo de ejecución del kernel.
- `ni`: tiempo en el espacio de usuario de tareas con niceness.
- `id`: tiempo inactivo.
- `wa`: tiempo inactivo mientras existe una solicitud de E/S pendiente.
- `hi` y `si`: gestión de interrupciones de hardware y software.
- `st`: tiempo de CPU virtual que el hipervisor dedica a otros huéspedes.

Un valor alto de `wa` puede respaldar una hipótesis de espera de E/S, pero no identifica un dispositivo ni demuestra que el almacenamiento sea el único cuello de botella. Examina la latencia del dispositivo y el comportamiento de la aplicación antes de concluir.

:::single-choice{#top-cpu-wa-meaning} ¿Qué comunica el campo de CPU `wa`?

::option[El tiempo dedicado a ejecutar código ordinario del usuario.]{#top-wa-user explanation="La ejecución en el espacio de usuario se comunica mediante `us`."}
::option[Las páginas de memoria escritas en el intercambio desde el arranque.]{#top-wa-swap explanation="La actividad de intercambio no es una categoría de tiempo de CPU."}
::option[El tiempo de CPU inactivo mientras existe una solicitud de E/S pendiente.]{#top-wa-io .correct explanation="El campo es tiempo de espera de E/S y necesita pruebas complementarias del dispositivo para diagnosticar."}
:::

## Leer la tabla de procesos

Entre las columnas importantes suelen encontrarse:

- `PID`, `USER` y `COMMAND`: identidad y propiedad.
- `S`: estado, como en ejecución (`R`), espera (`S`), espera ininterrumpible (`D`), detenido (`T`) o zombi (`Z`).
- `%CPU` y `%MEM`: actividad de CPU muestreada y proporción de memoria física.
- `TIME+`: tiempo de CPU acumulado.
- `VIRT`: espacio de direcciones virtual total asociado a la tarea.
- `RES`: memoria física residente, no intercambiada, atribuida actualmente a la tarea.
- `SHR`: memoria residente que puede compartirse con otros procesos.

`VIRT` no es la cantidad de RAM física consumida. Puede incluir archivos mapeados, bibliotecas compartidas, espacio de direcciones reservado y páginas intercambiadas. Incluso `RES` debe interpretarse con cuidado porque las páginas compartidas complican la atribución.

:::single-choice{#top-res-versus-virt} ¿Qué campo se aproxima más a la memoria física actualmente residente de un proceso?

::option[`TIME+`]{#top-time-field explanation="Este campo acumula tiempo de CPU, no memoria."}
::option[`VIRT`]{#top-virt-field explanation="El tamaño virtual incluye espacio de direcciones que no tiene por qué residir en RAM."}
::option[`RES`]{#top-res-field .correct explanation="El tamaño residente refleja páginas físicas residentes actualmente para el proceso, con las salvedades de la memoria compartida."}
:::

## Centrar y ordenar la vista

Supervisa directamente PID conocidos:

```bash
$ top -p 1234,5678
```

Dentro de `top`, pulsa `P` para ordenar por CPU, `M` para ordenar por memoria, `1` para alternar las líneas de cada CPU y `q` para salir en las implementaciones habituales de procps-ng. Pulsa `h` para consultar la ayuda interactiva local, porque las teclas y los campos pueden variar según la implementación.

Registra el PID, la orden, la marca de tiempo y varias muestras antes de actuar. Que un proceso alcance brevemente la primera posición puede ser normal, y terminarlo puede provocar pérdida de datos o una interrupción del servicio.

:::single-choice{#top-monitor-known-pid} ¿Qué invocación limita la pantalla al PID 1234?

::option[`top -u 1234`]{#top-user-filter explanation="La forma `-u` filtra por usuario en vez de tratar el valor como un PID."}
::option[`top -d 1234`]{#top-delay-filter explanation="La opción `-d` controla el intervalo de actualización en las implementaciones habituales."}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="La opción `-p` selecciona uno o varios identificadores de proceso para supervisarlos."}
:::

## Resumen

Ahora puedes utilizar `top` para formular y comprobar una hipótesis sobre el rendimiento del sistema.

1. Interpreta los promedios de carga como carga en intervalos de tiempo, no como porcentajes de CPU.
2. Compara las categorías de CPU entre varias muestras.
3. Distingue el espacio de direcciones virtual de la memoria residente.
4. Céntrate en PID conocidos y verifica las pruebas antes de actuar.
