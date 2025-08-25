---
index: 2
lang: "es"
title: "Control de Terminal"
meta_title: "Control de Terminal - Procesos"
meta_description: "Aprende sobre el control de terminales en Linux, incluyendo TTY vs. PTS, y cómo los procesos están vinculados a ellos. Comprende los procesos demonio. ¡Comienza tu viaje en Linux!"
meta_keywords: "terminal de control, TTY, PTS, terminal Linux, procesos demonio, Linux para principiantes, tutorial de Linux, guía de Linux"
---

## Lesson Content

Discutimos cómo hay un campo TTY en la salida de `ps`. El TTY es el terminal que ejecutó el comando.

Hay dos tipos de terminales: **dispositivos de terminal** regulares y **dispositivos de pseudoterminal**. Un dispositivo de terminal regular es un dispositivo de terminal nativo en el que puedes escribir y enviar la salida a tu sistema. Esto suena como la aplicación de terminal que has estado iniciando para acceder a tu shell, pero no lo es.

Vamos a hacer una digresión para que puedas ver esto en acción. Adelante, escribe Ctrl-Alt-F1 para entrar en TTY1 (la primera consola virtual). Notarás que no tienes nada excepto el terminal, sin gráficos, etc. Esto se considera un dispositivo de terminal regular. Puedes salir de esto con Ctrl-Alt-F7.

Un pseudoterminal es en lo que has estado acostumbrado a trabajar. Emulan terminales con la ventana del terminal de shell y se denotan por PTS. Si miras `ps` de nuevo, verás tu proceso de shell bajo `pts/*`.

Bien, volviendo al terminal de control: los procesos suelen estar vinculados a un terminal de control. Por ejemplo, si estuvieras ejecutando un programa en la ventana de tu shell, como `find`, y cerraras la ventana, tu proceso también terminaría con ella.

Existen procesos como los procesos demonio, que son procesos especiales que esencialmente mantienen el sistema en funcionamiento. A menudo se inician al arrancar el sistema y suelen terminar cuando el sistema se apaga. Se ejecutan en segundo plano, y dado que no queremos que estos procesos especiales terminen, no están vinculados a un terminal de control. En la salida de `ps`, el TTY aparece como un **?**, lo que significa que no tiene un terminal de control.

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de los procesos de Linux y su interacción con los terminales:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderás habilidades esenciales para administrar y monitorear procesos en un sistema Linux. Explorarás cómo interactuar con procesos en primer y segundo plano, inspeccionarlos con `ps`, monitorear recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Este laboratorio te ayudará a aplicar los conceptos de gestión de procesos en escenarios reales y a generar confianza en la comprensión de cómo se ejecutan los procesos e interactúan con el sistema.

## Quiz Question

¿Qué valor se le da a un proceso que no tiene un terminal de control?

## Quiz Answer

?
