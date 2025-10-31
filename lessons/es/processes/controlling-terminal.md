---
index: 2
lang: "es"
title: "Controlando la Terminal"
meta_title: "Controlando la Terminal - Procesos"
meta_description: "Explore el concepto de terminal controladora en Linux. Aprenda qué es una TTY, la diferencia entre TTY y PTS, y cómo usar la salida de `ps tty` para identificar procesos sin terminal controladora, como los daemons."
meta_keywords: "terminal controladora, ps tty, qué es tty, cómo usar ps, TTY, PTS, terminal Linux, proceso daemon, procesos Linux"
---

## Lesson Content

Cuando inspeccionas los procesos en ejecución, notarás un campo `TTY` en la salida del comando `ps`. Este campo es importante ya que indica la **terminal de control** que ejecutó el comando. Comprender este concepto es clave para gestionar procesos de manera efectiva.

### ¿Qué es una TTY?

TTY es la abreviatura de "Teletype" (Teleimpresora), que históricamente era un dispositivo físico para interactuar con una computadora. En los sistemas Linux modernos, una TTY se refiere a la terminal que proporciona la entrada y salida estándar para un proceso.

Hay dos tipos principales de terminales que encontrarás: dispositivos de terminal y dispositivos de terminal virtual (pseudo-terminales).

### Dispositivos de Terminal vs. Pseudo-terminales

Un dispositivo de terminal verdadero es una consola nativa que te permite escribir comandos y ver la salida directamente. Puedes experimentarlo cambiando a una consola virtual. En muchos sistemas, puedes presionar `Ctrl-Alt-F1` para acceder a TTY1. Verás un indicador de inicio de sesión en un entorno puramente basado en texto, sin interfaz gráfica. Este es un dispositivo de terminal clásico. Para volver a tu sesión gráfica, normalmente puedes usar `Ctrl-Alt-F7` (la combinación exacta de teclas puede variar).

Un pseudo-terminal (PTS), por otro lado, es lo que usas con más frecuencia. Cuando abres una aplicación de terminal dentro de tu entorno de escritorio gráfico, estás usando un PTS. Estos emulan una terminal dentro de una ventana. Si revisas la salida de `ps tty` para tu shell, verás su TTY listada como `pts/*`.

### El Rol de la Terminal de Control

La mayoría de los procesos están vinculados a una **terminal de control**. Esto significa que el ciclo de vida del proceso está ligado a la sesión de terminal que lo inició. Por ejemplo, si ejecutas un programa como `find` en tu ventana de terminal y luego cierras esa ventana, el proceso `find` también será terminado.

### Procesos Sin Terminal de Control

Algunos procesos, conocidos como daemons (servicios en segundo plano), están diseñados para ejecutarse en segundo plano y gestionar servicios del sistema. Estos procesos a menudo se inician cuando el sistema arranca y solo se detienen cuando se apaga.

Para evitar que sean terminados accidentalmente, los daemons no están adjuntos a una **terminal de control**. Cuando aprendes **cómo usar ps** para examinar estos procesos, verás un signo de interrogación (`?`) en la columna TTY. Este `?` significa que el proceso no tiene una terminal de control y se está ejecutando independientemente de cualquier sesión de usuario.

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de los procesos de Linux y su interacción con las terminales:

1. **[Gestionar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderás habilidades esenciales para gestionar y monitorear procesos en un sistema Linux. Explorarás cómo interactuar con procesos en primer plano y segundo plano, inspeccionarlos con `ps`, monitorear recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Este laboratorio te ayudará a aplicar los conceptos de gestión de procesos en escenarios reales y a ganar confianza al comprender cómo se ejecutan e interactúan los procesos con el sistema.

## Quiz Question

¿Qué valor se asigna a un proceso que no tiene una terminal de control?

## Quiz Answer

?
