---
lang: "es"
title: "Hilos de Procesos"
description: "Aprende sobre los hilos de procesos de Linux, los conceptos de un solo hilo frente a múltiples hilos, y cómo verlos usando 'ps m'. ¡Comprende los procesos ligeros de manera eficiente!"
keywords: "hilos de Linux, hilos de procesos, comando ps m, multi-hilo, single-hilo, procesos de Linux, Linux para principiantes, tutorial de Linux"
---

## Lesson Content

Es posible que hayas oído hablar de los términos procesos de un solo hilo (single-threaded) y de múltiples hilos (multi-threaded). Los hilos son muy similares a los procesos, ya que se utilizan para ejecutar el mismo programa; a menudo se les denomina procesos ligeros. Si un proceso tiene un hilo, es de un solo hilo, y si un proceso tiene más de un hilo, es de múltiples hilos. Sin embargo, todos los procesos tienen al menos un hilo.

Los procesos operan con sus propios recursos de sistema aislados; sin embargo, los hilos pueden compartir estos recursos entre sí fácilmente, lo que facilita su comunicación. A veces, es más eficiente tener una aplicación de múltiples hilos que una aplicación de múltiples procesos.

Básicamente, digamos que abres LibreOffice Writer y Chrome; cada uno es su propio proceso separado. Ahora entras en Writer y empiezas a editar texto. Cuando editas el texto, se guarda automáticamente. Estos dos "procesos ligeros" paralelos de guardar y editar son hilos.

Para ver los hilos de un proceso, puedes usar:

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

Los procesos se indican con cada PID, y debajo de los procesos están sus hilos (indicados por un `--`). Así que puedes ver que los procesos anteriores son ambos de un solo hilo.

## Exercise

Ejecuta el comando `ps m` y mira qué procesos tienes en ejecución que son de múltiples hilos.

## Quiz Question

Verdadero o falso, todos los procesos comienzan con un solo hilo.

## Quiz Answer

True
