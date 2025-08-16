---
lang: "es"
title: "niceness"
description: "Aprende sobre la "niceness" y la prioridad de procesos en Linux. Comprende los comandos nice y renice para gestionar el tiempo de CPU para los procesos. ¡Mejora el rendimiento del sistema!"
keywords: "Linux niceness, prioridad de procesos, comando nice, comando renice, tutorial de Linux, planificación de CPU, Linux para principiantes, guía de Linux"
---

## Lesson Content

Cuando ejecutas varias cosas en tu computadora, como Chrome, Microsoft Word o Photoshop al mismo tiempo, puede parecer que estos procesos se ejecutan simultáneamente, pero eso no es del todo cierto.

Los procesos usan la CPU por una pequeña cantidad de tiempo llamada "time slice" (segmento de tiempo). Luego se pausan por milisegundos, y otro proceso obtiene un pequeño "time slice". Por defecto, la planificación de procesos ocurre de esta manera "round-robin". Cada proceso obtiene suficientes "time slices" hasta que termina de procesar. El kernel maneja todos estos cambios de proceso, y lo hace bastante bien la mayor parte del tiempo.

Los procesos no pueden decidir cuándo y por cuánto tiempo obtienen tiempo de CPU. Si todos los procesos se comportaran normalmente, cada uno obtendría (aproximadamente) una cantidad igual de tiempo de CPU. Sin embargo, hay una manera de influir en el algoritmo de planificación de procesos del kernel con un valor "nice". "Niceness" es un nombre bastante extraño, pero lo que significa es que los procesos tienen un número para determinar su prioridad para la CPU. Un número alto significa que el proceso es "nice" (amable) y tiene una prioridad más baja para la CPU, y un número bajo o negativo significa que el proceso no es muy "nice" y quiere obtener la mayor cantidad de CPU posible.

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

¿Qué procesos no son muy "nice" y por qué?

## Quiz Question

Si quiero que un proceso obtenga más prioridad de CPU, ¿uso un número "nice" más bajo o más alto?

## Quiz Answer

lower
