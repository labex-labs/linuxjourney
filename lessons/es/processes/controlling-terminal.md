---
lang: "es"
title: "Controlando el Terminal"
description: "Aprende sobre el control de terminales en Linux, incluyendo TTY vs. PTS, y cómo los procesos se vinculan a ellos. Comprende los procesos daemon. ¡Comienza tu viaje en Linux!"
keywords: "terminal de control, TTY, PTS, terminal de Linux, procesos daemon, principiante de Linux, tutorial de Linux, guía de Linux"
---

## Lesson Content

Discutimos cómo hay un campo TTY en la salida de `ps`. El TTY es el terminal que ejecutó el comando.

Hay dos tipos de terminales: **dispositivos de terminal** regulares y **dispositivos de pseudoterminal**. Un dispositivo de terminal regular es un dispositivo de terminal nativo en el que puedes escribir y enviar la salida a tu sistema. Esto suena como la aplicación de terminal que has estado iniciando para acceder a tu shell, pero no lo es.

Vamos a hacer un paréntesis para que puedas ver esto en acción. Adelante y escribe Ctrl-Alt-F1 para entrar en TTY1 (la primera consola virtual). Notarás que no tienes nada excepto el terminal, sin gráficos, etc. Esto se considera un dispositivo de terminal regular. Puedes salir de esto con Ctrl-Alt-F7.

Un pseudoterminal es en lo que has estado acostumbrado a trabajar. Emulan terminales con la ventana de terminal de shell y se denotan por PTS. Si miras `ps` de nuevo, verás tu proceso de shell bajo `pts/*`.

Bien, ahora volviendo al terminal de control: los procesos suelen estar vinculados a un terminal de control. Por ejemplo, si estuvieras ejecutando un programa en tu ventana de shell, como `find`, y cerraras la ventana, tu proceso también terminaría con ella.

Existen procesos como los procesos daemon, que son procesos especiales que esencialmente mantienen el sistema en funcionamiento. A menudo se inician al arrancar el sistema y generalmente se terminan cuando el sistema se apaga. Se ejecutan en segundo plano, y como no queremos que estos procesos especiales se terminen, no están vinculados a un terminal de control. En la salida de `ps`, el TTY se lista como un **?**, lo que significa que no tiene un terminal de control.

## Exercise

Look at your `ps` output and list all the unique TTY values.

## Quiz Question

¿Qué valor se le da a un proceso que no tiene un terminal de control?

## Quiz Answer

?
