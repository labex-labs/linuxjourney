---
lesson_id: "controlling-terminal"
course_id: "processes"
lang: "es"
order_index: 2
title: "Terminal de control"
description: "Aprende cómo las terminales de control conectan las sesiones con la entrada interactiva, las señales y el control de trabajos del shell."
meta_title: "Terminal de control - Procesos"
meta_description: "Descubre qué es una terminal de control en Linux, la diferencia entre TTY y PTS y cómo interpretar la columna TTY de ps."
meta_keywords: "terminal de control, ps tty, qué es tty, TTY, PTS, terminal Linux, proceso daemon, procesos Linux"
---

Una sesión interactiva de inicio puede tener una terminal de control: un dispositivo de terminal asociado a la sesión y utilizado por el kernel para las señales generadas por la terminal y el control de trabajos. El campo `TTY` de los listados de procesos ayuda a identificar esa asociación.

## Dispositivos de terminal y pseudoterminal

El nombre TTY procede de los teletipos históricos. En Linux moderno, las interfaces de terminal son abstracciones de dispositivos y no necesariamente equipos físicos.

Una consola virtual del sistema puede aparecer con un nombre como `tty1`. Las combinaciones de teclas del escritorio para cambiar de consola varían según la distribución y no deben darse por supuestas. Un emulador de terminal, un inicio de sesión remoto o un multiplexor suele usar un par de pseudoterminales, cuyo lado interactivo aparece con un nombre como `pts/3`.

Muestra la terminal conectada a la entrada estándar de la orden actual con:

```bash
$ tty
/dev/pts/3
```

Este resultado está relacionado con el concepto más amplio de terminal de control, pero no es idéntico. Un proceso puede redirigir su entrada o salida estándar y seguir perteneciendo a una sesión con terminal de control.

:::single-choice{#controlling-terminal-pts-meaning}
¿Qué suele identificar un nombre como `pts/3`?

::option[Un ID de proceso asignado al tercer shell.]{#controlling-terminal-pts-pid explanation="Un PID es un metadato numérico de proceso y no se expresa como un nombre de dispositivo `pts/N`."}
::option[Un dispositivo pseudoterminal usado por una sesión interactiva.]{#controlling-terminal-pts-device .correct explanation="Las entradas de `/dev/pts` son dispositivos esclavos de pseudoterminal usados habitualmente por emuladores y sesiones remotas."}
::option[Una partición del sistema de archivos que contiene programas de terminal.]{#controlling-terminal-pts-partition explanation="El nombre identifica una interfaz de dispositivo de terminal, no una partición de almacenamiento."}
:::

## Sesiones, grupos de procesos y control de trabajos

Una terminal de control pertenece a una sesión, no únicamente a la orden que abrió una ventana. Dentro de esa sesión, la terminal mantiene un grupo de procesos en primer plano. El shell coloca una tubería en primer plano dentro de ese grupo para que pueda leer la entrada y recibir señales generadas por la terminal.

Por ejemplo, al pulsar `Ctrl-C`, el controlador de la terminal suele enviar `SIGINT` al grupo de procesos en primer plano. Un grupo en segundo plano que intenta leer de la terminal puede recibir `SIGTTIN`. Estas reglas permiten al shell coordinar trabajos en primer y segundo plano.

:::single-choice{#controlling-terminal-ctrl-c-target}
¿A qué procesos dirige normalmente una terminal la señal generada por `Ctrl-C`?

::option[A todos los procesos propiedad del usuario actual.]{#controlling-terminal-ctrl-c-user explanation="Las señales generadas por la terminal se limitan al grupo de procesos en primer plano, no a todos los procesos del usuario."}
::option[Únicamente al shell de inicio, sin importar el trabajo en primer plano.]{#controlling-terminal-ctrl-c-shell explanation="Mientras otro trabajo está en primer plano, el grupo de ese trabajo es el destino normal de la señal."}
::option[Al grupo de procesos en primer plano de la terminal.]{#controlling-terminal-ctrl-c-foreground .correct explanation="El controlador de terminal envía `SIGINT` al grupo de procesos que está actualmente en primer plano."}
:::

## Leer la columna `TTY`

Solicita campos de proceso concretos cuando quieras una vista estable:

```bash
$ ps -o pid,tty,stat,cmd
```

Un nombre de terminal como `pts/3` identifica la terminal de control registrada para ese proceso. Un signo de interrogación (`?`) suele significar que el proceso no tiene terminal de control.

Muchos procesos de servicios no tienen terminal de control porque un gestor de servicios los inicia independientemente de una sesión interactiva. Sin embargo, la ausencia de TTY no demuestra por sí sola que un proceso sea un daemon, y un trabajo del shell en segundo plano puede conservar una terminal de control.

:::single-choice{#controlling-terminal-question-mark}
¿Qué significa normalmente `?` en la columna `TTY` de `ps`?

::option[El proceso no tiene terminal de control.]{#controlling-terminal-no-tty .correct explanation="El signo de interrogación es la representación habitual cuando no hay una terminal de control asociada al proceso."}
::option[No se pudo leer la terminal del proceso porque está ocupada.]{#controlling-terminal-busy-tty explanation="El marcador representa la ausencia de terminal de control, no una contención temporal del dispositivo."}
::option[El proceso siempre es un hilo del kernel.]{#controlling-terminal-kernel-only explanation="Los hilos del kernel suelen carecer de terminal, pero también muchos servicios del espacio de usuario."}
:::

## Cierre de la terminal y hangups

Cuando desaparece una conexión de terminal, el kernel o el software de terminal y sesión puede enviar `SIGHUP` a los procesos asociados. Un proceso puede terminar, capturar la señal, ignorarla o haberse configurado previamente para sobrevivir. Funciones del shell como `disown`, utilidades como `nohup`, multiplexores y gestores de servicios afectan al ciclo de vida.

Por tanto, cerrar una terminal no garantiza que todas las órdenes iniciadas desde ella terminen. Cuando importe la persistencia, consulta la sesión, el tratamiento de señales, las redirecciones y el supervisor del proceso.

:::single-choice{#controlling-terminal-close-effect}
¿Por qué es incorrecto afirmar que cerrar una terminal siempre termina todos los procesos iniciados en ella?

::option[Las terminales de Linux nunca generan señales al cerrarse.]{#controlling-terminal-never-signals explanation="Las señales de hangup son un comportamiento real de terminales y sesiones, aunque no garanticen la terminación."}
::option[Únicamente los procesos con PID numéricos pueden recibir hangups.]{#controlling-terminal-pid-hangup explanation="Todos los procesos normales tienen PID numéricos; este hecho no determina si sobreviven al cierre de una terminal."}
::option[Los procesos pueden tratar o evitar el hangup y estar gestionados de forma independiente.]{#controlling-terminal-hangup-handling .correct explanation="La disposición de señales, el shell, los multiplexores y los supervisores pueden permitir que un proceso continúe después del cierre."}
:::

El laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) ofrece un entorno seguro para comparar trabajos en primer y segundo plano y sus campos `TTY`.

## Resumen

Ahora puedes relacionar una terminal de control con la gestión de procesos interactivos.

1. Distingue terminales virtuales de pseudoterminales.
2. Relaciona las señales de terminal con el grupo de procesos en primer plano.
3. Interpreta los nombres de terminal y `?` en la salida de `ps`.
4. Trata el cierre de la terminal como una señalización, no como una terminación garantizada.
