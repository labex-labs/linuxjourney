---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "es"
order_index: 1
title: "ps (procesos)"
description: "Aprende a obtener instantáneas de procesos con ps y a supervisar actividad cambiante con top."
meta_title: "ps (procesos) - Procesos"
meta_description: "Aprende a usar ps, ps aux y ps -ef para ver procesos en ejecución, interpretar PID y PPID y supervisar actividad cambiante con top."
meta_keywords: "orden ps, ps -ef Linux, ps aux, procesos Linux, ID de proceso, PID, orden top, supervisar procesos"
---

Un proceso es una instancia en ejecución de un programa, junto con su memoria, credenciales, recursos abiertos y estado de ejecución. Linux identifica cada proceso activo mediante un identificador numérico de proceso, o PID. Un PID es único entre los procesos que existen al mismo tiempo, pero el kernel puede reutilizarlo después de que un proceso termine.

## Obtener una instantánea básica

Ejecuta `ps` sin opciones para ver una instantánea seleccionada según los valores predeterminados de la implementación, normalmente los procesos asociados a tu terminal y usuario actuales:

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

Entre los campos habituales se encuentran:

- `PID`: identificador del proceso.
- `TTY`: terminal de control, o `?` cuando no hay ninguna asociada.
- `TIME`: tiempo de CPU acumulado, no tiempo de reloj transcurrido.
- `CMD`: nombre o línea de la orden, según el formato seleccionado.

Las columnas exactas y los valores predeterminados de selección varían entre implementaciones y entornos de `ps`.

:::single-choice{#ps-command-pid-meaning}
¿Qué identifica la columna `PID`?

::option[El número del directorio actual del proceso.]{#ps-command-pid-directory explanation="Un directorio actual es una referencia del sistema de archivos y no está representado por el PID."}
::option[El tiempo de CPU acumulado en segundos.]{#ps-command-pid-cpu explanation="El uso de CPU aparece en un campo independiente, como `TIME`."}
::option[El identificador del proceso asignado por el kernel.]{#ps-command-pid-kernel .correct explanation="El PID es el identificador numérico usado para referirse a un proceso activo."}
:::

## Enumerar procesos con opciones de estilo BSD

`ps` de Linux acepta varios estilos de opciones. Las opciones de estilo BSD suelen escribirse sin guion inicial:

```bash
$ ps aux
```

En esta combinación:

- `a` amplía la selección a procesos de otros usuarios que tienen terminal.
- `x` también incluye procesos sin terminal de control y amplía la selección cuando se combina con `a`.
- `u` selecciona un formato orientado al usuario con campos como `USER`, `%CPU`, `%MEM`, `VSZ` y `RSS`.

Como los significados de las opciones pueden interactuar, interpreta la combinación completa en vez de tratar cada letra como una orden independiente.

:::single-choice{#ps-command-aux-user-format}
En `ps aux`, ¿qué opción solicita el formato de salida orientado al usuario?

::option[`u`]{#ps-command-aux-u .correct explanation="La opción `u` de estilo BSD selecciona un conjunto de columnas orientado al usuario."}
::option[`x`]{#ps-command-aux-x explanation="La opción `x` afecta a la selección de procesos, especialmente a los que no tienen terminal de control."}
::option[`a`]{#ps-command-aux-a explanation="La opción `a` amplía la selección más allá de los procesos de la terminal del usuario actual."}
:::

## Usar opciones de estilo estándar

La orden de estilo estándar ampliamente utilizada `ps -ef` escribe las opciones con un guion inicial:

```bash
$ ps -ef
```

- `-e` selecciona todos los procesos visibles para quien la invoca.
- `-f` solicita un listado de formato completo.

La salida suele incluir `UID`, `PID`, `PPID`, hora de inicio e información de la orden. `PPID` es el identificador del proceso padre. Este listado no es jerárquico por sí mismo; usa una opción como `--forest` cuando esté disponible o un visor de árboles específico como `pstree` cuando importe la disposición entre padres e hijos.

:::single-choice{#ps-command-ef-selection}
¿Qué solicita `-e` en `ps -ef`?

::option[Una actualización cada segundo hasta que se interrumpa.]{#ps-command-e-refresh explanation="`ps` produce una instantánea; la actualización continua es una función de herramientas como `top`."}
::option[Una selección que contiene todos los procesos visibles para quien ejecuta la orden.]{#ps-command-e-every .correct explanation="La opción `-e` de estilo estándar amplía la instantánea a todos los procesos seleccionables."}
::option[Únicamente procesos cuya orden terminó con un error.]{#ps-command-e-errors explanation="La selección de procesos no se basa en el posible estado final de salida de una orden."}
:::

## Supervisar la actividad a lo largo del tiempo

`ps` termina después de producir una instantánea. Usa `top` para obtener una vista interactiva que se actualiza periódicamente:

```bash
$ top
```

`top` ayuda a identificar consumidores cambiantes de CPU y memoria, pero sus valores son muestras y pueden fluctuar. Confirma un problema sospechado mediante varias observaciones y relaciona los porcentajes con la cantidad de CPU, la contabilidad de memoria y la carga de trabajo de la máquina.

:::single-choice{#ps-command-snapshot-versus-top}
¿Qué herramienta presentada aquí actualiza periódicamente su visualización de procesos de forma predeterminada?

::option[`top`]{#ps-command-top-refresh .correct explanation="`top` es un monitor interactivo que actualiza su visualización a intervalos."}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="Esta orden imprime una instantánea de procesos con formato completo y después termina."}
::option[`ls -l`]{#ps-command-ls-files explanation="`ls -l` muestra entradas del sistema de archivos, no un monitor de procesos activo."}
:::

Para practicar, usa [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) para comparar instantáneas con un monitor interactivo, o explora la ordenación y el filtrado en el laboratorio [Orden top de Linux](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500).

## Resumen

Ahora puedes elegir una vista de procesos e interpretar sus identificadores básicos.

1. Trata un PID como un identificador reutilizable de un proceso activo actualmente.
2. Usa `ps` sin opciones para una instantánea pequeña predeterminada.
3. Usa `ps aux` o `ps -ef` para selecciones más amplias y columnas más completas.
4. Usa `top` cuando importen los cambios a lo largo del tiempo.
