---
lang: "es"
title: "ps (Procesos)"
meta_description: "Aprende sobre el comando 'ps' de Linux para ver los procesos en ejecución y entender los IDs de proceso (PIDs). Obtén una guía para principiantes sobre la gestión de procesos."
meta_keywords: "comando ps, procesos Linux, ID de proceso, PID, tutorial Linux, principiante, guía, comando top"
---

## Lesson Content

Los procesos son los programas que se están ejecutando en tu máquina. Son gestionados por el kernel, y cada proceso tiene un ID asociado llamado **ID de proceso (PID)**. Este PID se asigna en el orden en que se crean los procesos.

Ejecuta el comando `ps` para ver una lista de los procesos en ejecución:

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Esto te muestra una instantánea rápida de los procesos actuales:

- PID: Process ID
- TTY: Controlling terminal associated with the process (lo veremos en detalle más adelante)
- STAT: Process status code
- TIME: Total CPU usage time
- CMD: Name of executable/command

Si miras la página man de `ps`, verás que hay muchas opciones de comando que puedes pasar. Variarán dependiendo de las opciones que quieras usar — BSD, GNU o Unix. En mi opinión, el estilo BSD es más popular, así que usaremos ese. Si tienes curiosidad, la diferencia entre los estilos es la cantidad de guiones que usas y las banderas.

```bash
ps aux
```

La **a** muestra todos los procesos en ejecución, incluidos los que son ejecutados por otros usuarios. La **u** muestra más detalles sobre los procesos. Y finalmente, la **x** lista todos los procesos que no tienen un TTY asociado. Estos programas mostrarán un `?` en el campo TTY; son más comunes en procesos daemon que se inician como parte del arranque del sistema.

Notarás que ahora estás viendo muchos más campos. No es necesario memorizarlos todos; en un curso posterior sobre procesos avanzados, repasaremos algunos de ellos:

- USER: The effective user (the one whose access we are using)
- PID: Process ID
- %CPU: CPU time used divided by the time the process has been running
- %MEM: Ratio of the process's resident set size to the physical memory on the machine
- VSZ: Virtual memory usage of the entire process
- RSS: Resident set size, the non-swapped physical memory that a task has used
- TTY: Controlling terminal associated with the process
- STAT: Process status code
- START: Start time of the process
- TIME: Total CPU usage time
- COMMAND: Name of executable/command

El comando `ps` puede ser un poco complicado de ver. Por ahora, los campos que más veremos son PID, STAT y COMMAND.

Otro comando muy útil es el comando **top**. `top` te da información en tiempo real sobre los procesos que se ejecutan en tu sistema en lugar de una instantánea. Por defecto, obtendrás una actualización cada 10 segundos. `top` es una herramienta extremadamente útil para ver qué procesos están consumiendo muchos de tus recursos.

```bash
top
```

## Exercise

Usa el comando `ps` con diferentes banderas y observa cómo cambia la salida.

## Quiz Question

¿Qué bandera de `ps` se usa para ver información detallada sobre los procesos?

## Quiz Answer

u
