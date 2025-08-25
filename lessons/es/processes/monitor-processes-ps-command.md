---
index: 1
lang: "es"
title: "ps (Procesos)"
meta_title: "ps (Procesos) - Procesos"
meta_description: "Aprende sobre el comando 'ps' de Linux para ver los procesos en ejecución y entender los ID de proceso (PIDs). Obtén una guía para principiantes sobre la gestión de procesos."
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

- PID: ID de proceso
- TTY: Terminal de control asociada con el proceso (entraremos en detalle sobre esto más adelante)
- STAT: Código de estado del proceso
- TIME: Tiempo total de uso de la CPU
- CMD: Nombre del ejecutable/comando

Si miras la página man de `ps`, verás que hay muchas opciones de comando que puedes pasar. Variarán dependiendo de las opciones que quieras usar: BSD, GNU o Unix. En mi opinión, el estilo BSD es más popular, así que usaremos ese. Si tienes curiosidad, la diferencia entre los estilos es la cantidad de guiones que usas y las banderas.

```bash
ps aux
```

La **a** muestra todos los procesos en ejecución, incluidos los que son ejecutados por otros usuarios. La **u** muestra más detalles sobre los procesos. Y finalmente, la **x** lista todos los procesos que no tienen un TTY asociado. Estos programas mostrarán un `?` en el campo TTY; son más comunes en procesos demonio que se inician como parte del arranque del sistema.

Notarás que ahora estás viendo muchos más campos. No es necesario memorizarlos todos; en un curso posterior sobre procesos avanzados, repasaremos algunos de ellos nuevamente:

- USER: El usuario efectivo (aquel cuyo acceso estamos utilizando)
- PID: ID de proceso
- %CPU: Tiempo de CPU utilizado dividido por el tiempo que el proceso ha estado en ejecución
- %MEM: Relación entre el tamaño del conjunto residente del proceso y la memoria física de la máquina
- VSZ: Uso de memoria virtual de todo el proceso
- RSS: Tamaño del conjunto residente, la memoria física no intercambiada que ha utilizado una tarea
- TTY: Terminal de control asociada con el proceso
- STAT: Código de estado del proceso
- START: Hora de inicio del proceso
- TIME: Tiempo total de uso de la CPU
- COMMAND: Nombre del ejecutable/comando

El comando `ps` puede ser un poco complicado de ver. Por ahora, los campos que más veremos son PID, STAT y COMMAND.

Otro comando muy útil es el comando **top**. `top` te da información en tiempo real sobre los procesos que se ejecutan en tu sistema en lugar de una instantánea. Por defecto, obtendrás una actualización cada 10 segundos. `top` es una herramienta extremadamente útil para ver qué procesos están consumiendo muchos de tus recursos.

```bash
top
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los procesos de Linux y su monitoreo:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica habilidades esenciales para administrar y monitorear procesos en un sistema Linux, incluyendo la interacción con procesos en primer plano/segundo plano, la inspección con `ps`, el monitoreo con `top` y la terminación con `kill`.
2. **[Comando top de Linux: Monitoreo del Sistema en Tiempo Real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprende a usar el comando `top` de Linux para el monitoreo del sistema en tiempo real, incluyendo la clasificación de procesos, el ajuste de los intervalos de actualización y el filtrado por usuario.

Estos laboratorios te ayudarán a aplicar los conceptos de identificación y monitoreo de procesos en escenarios reales y a desarrollar confianza con la administración de sistemas Linux.

## Quiz Question

¿Qué bandera de `ps` se utiliza para ver información detallada sobre los procesos?

## Quiz Answer

u
