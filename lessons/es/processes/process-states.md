---
index: 9
lang: "es"
title: "Estados de los Procesos"
meta_title: "Estados de los Procesos - Procesos"
meta_description: "Aprenda los estados de los procesos de Linux (R, S, D, Z, T) usando `ps aux`. Comprenda los códigos STAT comunes y gestione los procesos de forma eficaz. ¡Comience su viaje en Linux!"
meta_keywords: "estados de procesos de Linux, ps aux, gestión de procesos, tutorial de Linux, Linux para principiantes, códigos STAT, guía de Linux"
---

## Lesson Content

Echemos un vistazo al comando `ps aux` nuevamente:

```bash
ps aux
```

En la columna STAT, verá muchos valores. Un proceso de Linux puede estar en varios estados diferentes. Los códigos de estado más comunes que verá se describen a continuación:

- **R**: En ejecución o ejecutable; solo está esperando que la CPU lo procese.
- **S**: Suspensión interrumpible; esperando que se complete un evento, como la entrada desde la terminal.
- **D**: Suspensión ininterrumpible; procesos que no pueden ser eliminados o interrumpidos con una señal. Usualmente, para hacer que desaparezcan, debe reiniciar o solucionar el problema.
- **Z**: Zombie; discutimos en una lección anterior que los zombies son procesos terminados que están esperando que se recopilen sus estados.
- **T**: Detenido; un proceso que ha sido suspendido/detenido.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión y los estados de los procesos de Linux:

1. **[Gestionar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderá habilidades esenciales para gestionar y monitorear procesos en un sistema Linux. Explorará cómo interactuar con procesos en primer plano y en segundo plano, inspeccionarlos con `ps`, monitorear recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Este laboratorio le ayudará a aplicar los conceptos de estados de proceso en escenarios reales y a desarrollar confianza con la gestión de procesos de Linux.

## Quiz Question

¿Qué código STAT se utiliza para representar una suspensión ininterrumpible?

## Quiz Answer

D
