---
index: 6
lang: "es"
title: "Señales"
meta_title: "Señales - Procesos"
meta_description: "Aprende sobre las señales de Linux, su propósito, tipos comunes como SIGINT y SIGKILL, y cómo los procesos las manejan. Comprende los conceptos básicos de las señales para un mejor control de Linux."
meta_keywords: "señales de Linux, SIGKILL, SIGINT, comunicación de procesos, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Una señal es una notificación a un proceso de que algo ha sucedido.

### Por qué tenemos señales

Son interrupciones de software y tienen muchos usos:

- Un usuario puede escribir uno de los caracteres especiales del terminal (Ctrl-C) o (Ctrl-Z) para matar, interrumpir o suspender procesos.
- Pueden ocurrir problemas de hardware, y el kernel quiere notificar al proceso.
- Pueden ocurrir problemas de software, y el kernel quiere notificar al proceso.
- Básicamente, son formas en que los procesos pueden comunicarse.

### Proceso de señal

Cuando una señal es generada por algún evento, es entregada a un proceso; se considera en un estado pendiente hasta que es entregada. Cuando el proceso se ejecuta, la señal será entregada. Sin embargo, los procesos tienen máscaras de señal, y pueden configurar la entrega de señales para que sea bloqueada si se especifica. Cuando una señal es entregada, un proceso puede hacer una multitud de cosas:

- Ignorar la señal.
- "Capturar" la señal y realizar una rutina de manejo específica.
- El proceso puede ser terminado, a diferencia de la llamada normal al sistema `exit`.
- Bloquear la señal, dependiendo de la máscara de señal.

### Señales comunes

Cada señal se define por enteros con nombres simbólicos que tienen la forma de SIGxxx. Algunas de las señales más comunes son:

- SIGHUP o HUP o 1: Hangup
- SIGINT o INT o 2: Interrupt
- SIGKILL o KILL o 9: Kill
- SIGSEGV o SEGV o 11: Segmentation fault
- SIGTERM o TERM o 15: Software termination
- SIGSTOP o STOP: Stop

Los números pueden variar con las señales, por lo que generalmente se les conoce por sus nombres.

Algunas señales no se pueden bloquear; un ejemplo es la señal SIGKILL. La señal KILL destruye el proceso.

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de los procesos y cómo se utilizan las señales para interactuar con ellos:

1. **[Administrar y monitorear procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderás habilidades esenciales para administrar y monitorear procesos en un sistema Linux. Explorarás cómo interactuar con procesos en primer y segundo plano, inspeccionarlos con `ps`, monitorear recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`. Terminar procesos con `kill` es una aplicación directa del envío de señales.

Este laboratorio te ayudará a aplicar los conceptos de gestión de procesos y el uso subyacente de señales en escenarios reales y a generar confianza con la administración de sistemas Linux.

## Quiz Question

¿Qué señal no se puede bloquear?

## Quiz Answer

SIGKILL
