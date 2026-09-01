---
lesson_id: "process-states"
course_id: "processes"
lang: "es"
order_index: 9
title: "Estados de los procesos"
description: "Aprende a interpretar los códigos habituales de estado de procesos de Linux en instantáneas de `ps`."
meta_title: "Estados de los procesos - Procesos"
meta_description: "Una guía completa sobre los estados de los procesos de Linux. Aprende qué significan R, S, D, Z y T y cómo interpretarlos con la orden ps."
meta_keywords: "estados de procesos Linux, estado de proceso, orden ps, códigos STAT, gestión de procesos"
---

Una tarea de Linux pasa por distintos estados de ejecución mientras se ejecuta, espera, se detiene y termina. El campo `STAT` de `ps` captura un instante, así que, para diagnosticar un comportamiento, resulta más útil repetir las observaciones que basarse en una sola letra.

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

El primer carácter de `STAT` indica el estado principal. Los caracteres adicionales son modificadores que describen propiedades como el liderazgo de una sesión o la pertenencia al grupo de procesos en primer plano. Consulta el manual local de `ps` para ver el conjunto completo.

## Ejecución y espera interrumpible

- `R` significa que la tarea está en ejecución o preparada para ejecutarse. Está usando una CPU o esperando tiempo de CPU en una cola de ejecución.
- `S` significa espera interrumpible. La tarea espera un suceso y puede despertarse mediante una señal o un suceso apropiados.

La espera es normal. Los programas interactivos y los servicios pasan gran parte del tiempo esperando entradas, temporizadores, tráfico de red, bloqueos u otros sucesos, en lugar de consumir CPU continuamente.

:::single-choice{#process-states-runnable-code} ¿Qué significa el estado principal `R`?

::option[Que la tarea se ejecuta en una CPU o está preparada para hacerlo.]{#process-states-r-running .correct explanation="`R` agrupa las tareas que se ejecutan en ese momento y las que esperan servicio de CPU estando preparadas para ejecutarse."}
::option[Que fue recolectada después de que su padre obtuviera el estado.]{#process-states-r-reaped explanation="Un proceso completamente recolectado ya no aparece como una entrada normal en la tabla de procesos."}
::option[Que espera en un estado de espera ininterrumpible.]{#process-states-r-uninterruptible explanation="La espera ininterrumpible se representa con `D`."}
:::

:::single-choice{#process-states-interruptible-code} ¿Qué estado principal representa la espera interrumpible?

::option[`D`]{#process-states-sleep-d explanation="`D` indica una espera ininterrumpible."}
::option[`Z`]{#process-states-sleep-z explanation="`Z` indica un proceso hijo que terminó y cuyo estado aún no se ha recolectado."}
::option[`S`]{#process-states-sleep-s .correct explanation="`S` es el código convencional de `ps` para una espera interrumpible."}
:::

## Espera ininterrumpible

`D` significa espera ininterrumpible, normalmente mientras la tarea aguarda dentro de una operación del kernel, como ciertas operaciones de E/S de almacenamiento o de un sistema de archivos de red. La tarea no actúa sobre señales ordinarias hasta salir de esa espera; mientras tanto, una señal puede quedar pendiente.

Un estado `D` breve puede ser normal. La presencia persistente o abundante de tareas en `D` puede indicar una E/S lenta, no disponible o defectuosa, pero el estado por sí solo no identifica la causa. Antes de extraer conclusiones, examina el canal de espera, los registros del kernel, el estado del almacenamiento y de la red, y el subsistema correspondiente.

:::single-choice{#process-states-uninterruptible-code} ¿Qué estado principal indica una espera ininterrumpible?

::option[`T`]{#process-states-d-stopped explanation="`T` identifica una tarea detenida."}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="`D` se utiliza para una tarea que espera en un estado de espera ininterrumpible del kernel."}
::option[`R`]{#process-states-d-runnable explanation="`R` identifica una tarea en ejecución o preparada para ejecutarse."}
:::

## Estados detenido y zombi

- `T` suele significar que la tarea fue detenida por una acción de control de trabajos, como `SIGTSTP`, o por `SIGSTOP`. Algunas herramientas emplean la `t` minúscula para una detención provocada por rastreo.
- `Z` significa zombi: el proceso terminó, pero su padre todavía no ha recolectado el registro de terminación.

Cuando corresponda, reanuda una tarea detenida por el control de trabajos con `SIGCONT`. Un zombi no se puede reanudar ni matar porque ya no se está ejecutando; su padre o un proceso recolector que lo haya adoptado debe recolectarlo.

:::single-choice{#process-states-zombie-code} ¿Qué identifica el estado principal `Z`?

::option[Un proceso terminado cuyo registro de terminación espera ser recolectado.]{#process-states-z-zombie .correct explanation="Un zombi conserva una cantidad mínima de información de estado visible para su padre después de que la ejecución haya terminado."}
::option[Un proceso pausado por una señal de suspensión de la terminal.]{#process-states-z-terminal-stop explanation="Una detención por control de trabajos suele mostrarse como `T`."}
::option[Un proceso que está utilizando un núcleo de CPU completo.]{#process-states-z-cpu explanation="Una tarea activa se representa con `R`, mientras que un zombi no ejecuta instrucciones."}
:::

## Interpretar los estados en su contexto

Los códigos de estado son observaciones, no diagnósticos. Combínalos con el tiempo transcurrido, el uso de CPU, los canales de espera, las relaciones de parentesco, los registros y muestras repetidas. Una tarea puede cambiar de estado entre el instante en que el kernel lo comunica y el instante en que tú lees la pantalla.

El laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) ofrece un entorno seguro para observar tareas en primer plano, en espera, detenidas y terminadas.

## Resumen

Ahora puedes interpretar los estados principales de proceso más habituales.

1. Interpreta `R` como en ejecución o preparada para ejecutarse, y `S` como espera interrumpible.
2. Investiga un estado `D` persistente como síntoma de una espera, no como un diagnóstico.
3. Distingue el estado detenido `T` del estado terminado pero no recolectado `Z`.
4. Utiliza observaciones repetidas y las pruebas que las rodean.
