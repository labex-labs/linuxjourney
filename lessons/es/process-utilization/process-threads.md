---
index: 3
lang: "es"
title: "Hilos de Proceso"
meta_title: "Hilos de Proceso - Utilización del Proceso"
meta_description: "Una guía sobre los hilos de procesos en Linux. Aprenda la diferencia entre procesos monohilo y multihilo y cómo usar el comando ps para mostrar hilos."
meta_keywords: "hilos Linux, hilos de proceso, ps mostrar hilos, ps m, multihilo, monohilo, proceso ligero, gestión de procesos Linux"
---

## Lesson Content

### ¿Qué son los Hilos de Procesos?

Es posible que haya oído los términos de un solo hilo (single-threaded) y de múltiples hilos (multi-threaded). Los hilos son unidades de ejecución dentro de un proceso y a menudo se les llama "procesos ligeros" (lightweight processes). Mientras que los procesos operan con sus propios recursos de sistema aislados, los hilos dentro del mismo proceso pueden compartir estos recursos, como la memoria. Este modelo de recursos compartidos hace que la comunicación entre hilos sea mucho más rápida y eficiente que la comunicación entre procesos separados.

### Un Solo Hilo vs. Múltiples Hilos

Cada proceso tiene al menos un hilo. Un proceso con un solo hilo se denomina de un solo hilo, mientras que un proceso con más de uno se denomina de múltiples hilos.

Por ejemplo, cuando utiliza un editor de texto moderno, este podría ejecutarse como un solo proceso. Sin embargo, dentro de ese proceso, un hilo podría estar gestionando su entrada de teclado, mientras que otro hilo se ejecuta en segundo plano para realizar la corrección ortográfica o el autoguardado. Esta ejecución concurrente hace que la aplicación se sienta más receptiva. Utilizar múltiples hilos es a menudo más eficiente que iniciar múltiples procesos para tareas relacionadas.

### Cómo Mostrar Hilos con ps

Para inspeccionar los procesos en ejecución y sus hilos, puede utilizar el comando `ps`. Aunque `ps` tiene muchas opciones, una forma común de **mostrar hilos** es con la bandera `m`.

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

### Interpretación de la Salida

En la salida anterior, las líneas con un `PID` (ID de Proceso) representan el proceso principal. Las líneas directamente debajo, que tienen un guion (`-`) en lugar de un `PID`, representan los hilos que pertenecen a ese proceso. En este ejemplo, tanto los procesos `bash` como `ps m` son de un solo hilo, ya que cada uno solo tiene un hilo principal listado.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de los procesos de Linux y su gestión:

1. **[Gestionar y Supervisar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderá habilidades esenciales para gestionar y supervisar procesos en un sistema Linux. Explorará cómo interactuar con procesos en primer plano y en segundo plano, inspeccionarlos con `ps`, supervisar recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Este laboratorio le ayudará a aplicar los conceptos de gestión de procesos en escenarios reales y a ganar confianza con la supervisión de la actividad del sistema.

## Quiz Question

Verdadero o falso, todos los procesos comienzan siendo de un solo hilo.

## Quiz Answer

True
