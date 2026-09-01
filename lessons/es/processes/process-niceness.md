---
lesson_id: "process-niceness"
course_id: "processes"
lang: "es"
order_index: 8
title: "Niceness"
description: "Aprende cómo los valores nice influyen en el peso de planificación de CPU de los procesos normales de Linux."
meta_title: "Niceness - Procesos"
meta_description: "Descubre cómo los valores nice influyen en la prioridad relativa de procesos y cómo usar nice y renice para ajustar la planificación de CPU."
meta_keywords: "niceness Linux, valor nice, prioridad de procesos, orden nice, orden renice, planificación de CPU"
---

Linux puede ejecutar hilos simultáneamente en distintos núcleos de CPU y compartir un núcleo entre más hilos ejecutables de los que puede ejecutar a la vez. El planificador toma esas decisiones según la política, la prioridad, la afinidad y la carga de trabajo. Un valor nice es una de las entradas de las políticas normales de tiempo compartido.

## Interpretar los valores nice

El intervalo convencional de nice va de `-20` a `19`:

- Un valor menor concede a una tarea mayor peso de planificación respecto a tareas comparables.
- Un valor mayor la hace más «amable» al concederle menos peso relativo.
- El valor predeterminado suele ser `0`.

Niceness no reserva un porcentaje de CPU ni garantiza una ejecución inmediata. Su efecto es más visible cuando tareas ejecutables comparables compiten por tiempo de CPU. Las políticas en tiempo real, los cgroups, la afinidad de CPU, las esperas de E/S y otros controles pueden dominar el comportamiento observado.

:::single-choice{#process-niceness-lower-value} Bajo la misma política normal de planificación, ¿qué valor nice concede un mayor peso relativo de CPU?

::option[`10`]{#process-niceness-value-ten explanation="Un valor positivo es más amable y normalmente tiene menos peso que cero o un valor negativo."}
::option[`19`]{#process-niceness-value-nineteen explanation="Este es el extremo más amable del intervalo convencional y tiene un peso relativamente bajo."}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="Los valores nice menores corresponden a un mayor peso relativo entre tareas normales comparables."}
:::

## Consultar niceness

En `top`, la columna `NI` muestra el valor nice. También puedes solicitarlo a `ps`:

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI` es el valor nice visible para el usuario. Una columna `PRI` o similar puede ser una prioridad derivada del planificador y su escala varía según la herramienta y la clase de planificación, así que no supongas que ambas columnas son intercambiables.

:::single-choice{#process-niceness-top-column} ¿Qué columna de `top` suele mostrar el valor nice?

::option[`PID`]{#process-niceness-column-pid explanation="`PID` identifica un proceso en vez de mostrar su ajuste de planificación."}
::option[`TTY`]{#process-niceness-column-tty explanation="`TTY` identifica una asociación con una terminal de control."}
::option[`NI`]{#process-niceness-column-ni .correct explanation="`NI` es la abreviatura convencional del valor nice de un proceso o hilo."}
:::

## Iniciar una orden con `nice`

Usa `nice` para iniciar una orden nueva con un valor ajustado:

```bash
$ nice -n 5 long-computation
```

Puedes consultar en el manual local el ajuste solicitado y la sintaxis aceptada. Un usuario sin privilegios suele poder hacer una orden más amable aumentando su valor. Concederle un valor nice menor y, por tanto, un peso de planificación más favorable, requiere los privilegios apropiados o límites de recursos configurados.

:::single-choice{#process-niceness-nice-command} ¿Qué hace `nice -n 5 long-computation`?

::option[Inicia la orden con el valor nice 5, si está permitido.]{#process-niceness-start-five .correct explanation="`nice` inicia una orden nueva con el ajuste de planificación solicitado."}
::option[Cambia el PID 5 al valor nice más bajo posible.]{#process-niceness-pid-five explanation="El operando posterior a `-n` es un valor nice, no un PID de destino."}
::option[Garantiza a la orden exactamente un cinco por ciento de una CPU.]{#process-niceness-five-percent explanation="Los valores nice expresan peso relativo y no reservan porcentajes fijos de CPU."}
:::

## Cambiar un proceso existente con `renice`

Usa `renice` para un proceso que ya está en ejecución:

```bash
$ renice -n 10 -p 3245
```

Esto solicita el valor nice `10` para el PID `3245`. Verifica primero el destino porque los PID pueden reutilizarse y confirma después el valor resultante. Los permisos dependen de la propiedad, los privilegios, los límites de recursos y la política del sistema. Aumentar el valor nice suele estar permitido para un proceso propio; revertir ese cambio puede no estarlo sin privilegios.

:::single-choice{#process-niceness-renice-purpose} ¿Qué herramienta cambia el valor nice de un proceso existente?

::option[`nice`]{#process-niceness-tool-nice explanation="`nice` se usa principalmente para iniciar una orden nueva con un valor ajustado."}
::option[`kill`]{#process-niceness-tool-kill explanation="`kill` envía señales y no es el editor normal de niceness."}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="`renice` apunta a un PID, grupo de procesos o usuario existente según sus opciones."}
:::

El laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) ofrece un entorno controlado para consultar y cambiar valores nice. Compara tareas que consuman CPU y compitan entre sí en vez de esperar una diferencia visible en un sistema inactivo.

## Resumen

Ahora puedes interpretar y ajustar niceness sin tratarlo como una garantía de CPU.

1. Interpreta los valores nice menores como un mayor peso relativo de planificación.
2. Consulta `NI` por separado de los campos de prioridad derivados.
3. Usa `nice` al iniciar una orden.
4. Usa `renice` para un proceso existente y verificado.
