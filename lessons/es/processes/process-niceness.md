---
index: 8
lang: "es"
title: "Amabilidad"
meta_title: "Amabilidad - Procesos"
meta_description: "Descubra qué es la amabilidad (niceness) en Linux y cómo afecta la prioridad de los procesos. Esta lección explica la amabilidad de procesos en Linux, utilizando los comandos nice y renice para gestionar la planificación de la CPU y mejorar el rendimiento del sistema."
meta_keywords: "amabilidad linux, niceness linux, qué es niceness en linux, amabilidad de procesos linux, niceness de proceso, prioridad de proceso, comando nice, comando renice, planificación de CPU"
---

## Lesson Content

Cuando ejecutas múltiples aplicaciones en tu computadora, parece que se están ejecutando simultáneamente. En realidad, la CPU está cambiando rápidamente entre ellas, dándole a cada proceso una pequeña cantidad de tiempo de procesamiento.

### Cómo la CPU Gestiona los Procesos

Cada proceso recibe una pequeña cantidad de tiempo de CPU llamada "quantum" (o "time slice"). Después de su quantum, un proceso se pausa y la CPU pasa al siguiente. Por defecto, el kernel de Linux programa los procesos de forma rotatoria (round-robin), asegurando que cada proceso reciba una parte justa del tiempo de CPU hasta que se complete. El planificador del kernel es muy eficiente gestionando estos cambios rápidos.

### ¿Qué es la "Niceness" en Linux?

Aunque los procesos no pueden controlar directamente su tiempo de CPU, puedes influir en las decisiones de programación del kernel. Esto se hace ajustando el valor de **niceness de linux** de un proceso. El término "niceness" (amabilidad) se refiere a cuán "amable" es un proceso con los otros procesos en el sistema.

La **niceness de un proceso** se representa con un número que va de -20 (prioridad más alta) a 19 (prioridad más baja).

- Un valor de niceness alto (ej. 19) significa que el proceso es muy "amable" y tiene baja prioridad, cediendo tiempo de CPU a otros.
- Un valor de niceness bajo o negativo (ej. -20) significa que el proceso no es "amable" y exige más tiempo de CPU, dándole una prioridad más alta.

Comprender la **niceness de los procesos en linux** es clave para gestionar los recursos del sistema de manera efectiva.

### Ajuste de la Prioridad del Proceso

Puedes ver el nivel de niceness actual de los procesos en ejecución usando el comando `top`. Busca la columna `NI`, que muestra el valor de niceness.

```bash
top
```

Para controlar el valor de **niceness linux**, puedes usar los comandos `nice` y `renice`.

Usa el comando `nice` para iniciar un nuevo proceso con un nivel de niceness específico. Por ejemplo, el siguiente comando inicia `apt upgrade` con un niceness de 5.

```bash
nice -n 5 apt upgrade
```

Para cambiar la prioridad de un proceso ya en ejecución, usa el comando `renice`. El siguiente comando cambia el niceness de un proceso con PID 3245 a 10.

```bash
renice 10 -p 3245
```

## Exercise

Aplica tus conocimientos con este laboratorio práctico para reforzar tu comprensión de la gestión y programación de procesos en Linux:

1. **[Gestionar y Monitorizar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica la interacción con procesos en primer y segundo plano, inspeccionándolos con `ps`, monitorizando recursos con `top`, ajustando la prioridad con `renice` y terminándolos con `kill`.

Este laboratorio te ayudará a aplicar los conceptos de programación de procesos y niceness en escenarios reales y a ganar confianza gestionando procesos en Linux.

## Quiz Question

Si quieres que un proceso obtenga más prioridad de CPU, ¿deberías usar un número nice más bajo o más alto? Por favor, responde con una sola palabra en inglés, todo en minúsculas.

## Quiz Answer

lower
