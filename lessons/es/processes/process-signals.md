---
lang: "es"
title: "Señales"
description: "Aprende sobre las señales de Linux, su propósito, tipos comunes como SIGINT y SIGKILL, y cómo los procesos las manejan. Comprende los conceptos básicos de las señales para un mejor control de Linux."
keywords: "señales de Linux, SIGKILL, SIGINT, comunicación de procesos, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Una señal es una notificación a un proceso de que algo ha sucedido.

### Why We Have Signals

Son interrupciones de software y tienen muchos usos:

- Un usuario puede escribir uno de los caracteres especiales del terminal (Ctrl-C) o (Ctrl-Z) para terminar, interrumpir o suspender procesos.
- Pueden ocurrir problemas de hardware, y el kernel quiere notificar al proceso.
- Pueden ocurrir problemas de software, y el kernel quiere notificar al proceso.
- Básicamente son formas en que los procesos pueden comunicarse.

### Signal Process

Cuando una señal es generada por algún evento, es entregada a un proceso; se considera en un estado pendiente hasta que es entregada. Cuando el proceso se ejecuta, la señal será entregada. Sin embargo, los procesos tienen máscaras de señal, y pueden configurar la entrega de señales para que sea bloqueada si se especifica. Cuando una señal es entregada, un proceso puede hacer una multitud de cosas:

- Ignorar la señal.
- "Capturar" la señal y realizar una rutina de manejo específica.
- El proceso puede ser terminado, a diferencia de la llamada normal al sistema exit.
- Bloquear la señal, dependiendo de la máscara de señal.

### Common Signals

Cada señal se define por enteros con nombres simbólicos que tienen la forma de SIGxxx. Algunas de las señales más comunes son:

- SIGHUP or HUP or 1: Hangup
- SIGINT or INT or 2: Interrupt
- SIGKILL or KILL or 9: Kill
- SIGSEGV or SEGV or 11: Segmentation fault
- SIGTERM or TERM or 15: Software termination
- SIGSTOP or STOP: Stop

Los números pueden variar con las señales, por lo que generalmente se les conoce por sus nombres.

Algunas señales son inbloqueables; un ejemplo es la señal SIGKILL. La señal KILL destruye el proceso.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué señal es inbloqueable?

## Quiz Answer

SIGKILL
