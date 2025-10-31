---
index: 9
lang: "es"
title: "Estados de los Procesos"
meta_title: "Estados de los Procesos - Procesos"
meta_description: "Una guía completa sobre los estados de los procesos en Linux. Aprenda sobre los diferentes estados de procesos en Linux (R, S, D, Z, T) y cómo interpretarlos usando el comando `ps`."
meta_keywords: "estados de procesos linux, estados de procesos en linux, estado de proceso linux, estado de proceso en linux, estados de procesos linux explicados, comando ps, códigos STAT, gestión de procesos"
---

## Lesson Content

Cuando inspeccionas los procesos en ejecución, por ejemplo con el comando `ps aux`, notarás una columna STAT. Comprender los códigos en esta columna es clave para dominar la gestión de procesos. Cada código representa un **estado de proceso de Linux** específico.

```bash
ps aux
```

Un **estado de proceso en Linux** proporciona una instantánea de lo que un proceso está haciendo actualmente. ¿Está utilizando activamente la CPU, esperando entrada o ha terminado? Exploremos los estados más comunes que encontrarás.

### Decodificación de los Códigos de Estado Comunes

La columna STAT revela el **estado de proceso de Linux** actual. Aunque hay muchos estados posibles, los siguientes son los que verás con más frecuencia. Tener estos **estados de proceso de Linux explicados** te ayudará a diagnosticar el comportamiento del sistema.

- **R (Running o Ejecutable)**: Un proceso en este estado se está ejecutando activamente en un núcleo de CPU o está en la cola de ejecución, listo para ejecutarse tan pronto como un núcleo de CPU esté disponible.

- **S (Sleep Interrumpible)**: Este es uno de los **estados de proceso en Linux** más comunes. El proceso está esperando que se complete un evento, como la entrada del usuario desde la terminal o la llegada de un paquete de red. Es "interrumpible", lo que significa que puede ser despertado por señales.

- **D (Sleep Ininterrumpible)**: Este proceso también está durmiendo, pero está en un estado donde no puede ser interrumpido por una señal. Esto se usa típicamente durante períodos cortos en operaciones de E/S donde interrumpir el proceso podría provocar un estado corrupto. Si un proceso permanece en este estado durante mucho tiempo, puede indicar un problema con el hardware o un controlador.

- **Z (Zombie)**: Un proceso zombie ha terminado su ejecución, pero todavía tiene una entrada en la tabla de procesos. Está esperando que su proceso padre lea su estado de salida. Unos pocos zombies son normales, pero un número grande puede indicar un error en la aplicación padre.

- **T (Stopped o Detenido)**: Un proceso entra en este estado cuando ha sido suspendido por una señal de control de trabajos (como presionar `Ctrl+Z`) o porque está siendo rastreado por un depurador. Puede reanudarse con la señal `SIGCONT`.

Al comprender estos **estados de proceso de Linux** fundamentales, puedes obtener una visión más profunda de la actividad de tu sistema y gestionar las aplicaciones en ejecución de manera más efectiva.

## Exercise

Aplica tus conocimientos con práctica práctica. El siguiente laboratorio te ayudará a reforzar tu comprensión de la gestión y los estados de los procesos de Linux:

1. **[Gestionar y Supervisar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderás habilidades esenciales para gestionar y supervisar procesos en un sistema Linux. Explorarás cómo interactuar con procesos en primer plano y en segundo plano, inspeccionarlos con `ps`, supervisar recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Este laboratorio te ayudará a aplicar los conceptos de estados de proceso en escenarios reales y a ganar confianza con la gestión de procesos de Linux.

## Quiz Question

¿Qué código STAT se utiliza para representar un sueño ininterrumpible? (Por favor, proporcione la única letra mayúscula en inglés para el código de estado.)

## Quiz Answer

D
