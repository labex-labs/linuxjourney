---
index: 8
lang: "es"
title: "niceness"
meta_title: "niceness - Procesos"
meta_description: "Aprende sobre la 'niceness' y la prioridad de procesos en Linux. Comprende los comandos nice y renice para gestionar el tiempo de CPU de los procesos. ¡Mejora el rendimiento del sistema!"
meta_keywords: "Linux niceness, prioridad de procesos, comando nice, comando renice, tutorial de Linux, programación de CPU, Linux para principiantes, guía de Linux"
---

## Lesson Content

Cuando ejecutas varias cosas en tu computadora, como quizás Chrome, Microsoft Word o Photoshop al mismo tiempo, puede parecer que estos procesos se están ejecutando simultáneamente, pero eso no es del todo cierto.

Los procesos usan la CPU por una pequeña cantidad de tiempo llamada "time slice" (segmento de tiempo). Luego se pausan por milisegundos, y otro proceso obtiene un pequeño segmento de tiempo. Por defecto, la programación de procesos ocurre de esta manera "round-robin" (por turnos). Cada proceso obtiene suficientes segmentos de tiempo hasta que termina de procesar. El kernel maneja todos estos cambios de proceso, y lo hace bastante bien la mayor parte del tiempo.

Los procesos no pueden decidir cuándo y por cuánto tiempo obtienen tiempo de CPU. Si todos los procesos se comportaran normalmente, cada uno (aproximadamente) obtendría una cantidad igual de tiempo de CPU. Sin embargo, hay una manera de influir en el algoritmo de programación de procesos del kernel con un valor "nice". "Niceness" es un nombre bastante extraño, pero lo que significa es que los procesos tienen un número para determinar su prioridad para la CPU. Un número alto significa que el proceso es "nice" (amable) y tiene una prioridad más baja para la CPU, y un número bajo o negativo significa que el proceso no es muy "nice" y quiere obtener la mayor cantidad de CPU posible.

```bash
top
```

Puedes ver una columna para `NI` ahora mismo; ese es el nivel de "niceness" de un proceso.

Para cambiar el nivel de "niceness", puedes usar los comandos `nice` y `renice`:

```bash
nice -n 5 apt upgrade
```

El comando `nice` se usa para establecer la prioridad de un nuevo proceso. El comando `renice` se usa para establecer la prioridad de un proceso existente.

```bash
renice 10 -p 3245
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión y programación de procesos en Linux:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica la interacción con procesos en primer y segundo plano, inspeccionándolos con `ps`, monitoreando recursos con `top`, ajustando la prioridad con `renice` y terminándolos con `kill`.

Este laboratorio te ayudará a aplicar los conceptos de programación de procesos y "niceness" en escenarios reales y a desarrollar confianza en la gestión de procesos en Linux.

## Quiz Question

Si quiero que un proceso obtenga más prioridad de CPU, ¿uso un número "nice" más bajo o más alto?

## Quiz Answer

lower
