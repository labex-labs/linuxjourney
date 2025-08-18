---
index: 3
lang: "es"
title: "Detalles del Proceso"
meta_title: "Detalles del Proceso - Procesos"
meta_description: "Aprende sobre los detalles de los procesos de Linux, cómo el kernel gestiona los recursos y qué son los procesos. Comprende los conceptos de procesos para principiantes."
meta_keywords: "procesos de Linux, kernel, gestión de procesos, ps aux, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Antes de entrar en aplicaciones más prácticas de los procesos, primero debemos entender qué son y cómo funcionan. Esta parte puede ser confusa ya que nos estamos adentrando en los detalles, así que siéntete libre de volver a esta lección si no quieres aprender sobre esto ahora.

Un proceso, como dijimos antes, es un programa en ejecución en el sistema. Más precisamente, es el sistema asignando memoria, CPU y E/S para que el programa se ejecute. Un proceso es una instancia de un programa en ejecución. Abre 3 ventanas de terminal. En dos ventanas, ejecuta el comando `cat` sin pasar ninguna opción (el proceso `cat` permanecerá abierto como un proceso porque espera stdin). Ahora, en la tercera ventana, ejecuta: `ps aux | grep cat`. Verás que hay dos procesos para `cat`, aunque estén llamando al mismo programa.

El kernel está a cargo de los procesos. Cuando ejecutamos un programa, el kernel carga el código del programa en la memoria, determina y asigna recursos, y luego lleva un registro de cada proceso. Sabe:

- El estado del proceso
- Los recursos que el proceso está usando y recibe
- El propietario del proceso
- Manejo de señales (más sobre esto más adelante)
- Y básicamente todo lo demás

Todos los procesos intentan obtener una parte de ese dulce pastel de recursos. Es trabajo del kernel asegurarse de que los procesos obtengan la cantidad correcta de recursos según las demandas del proceso. Cuando un proceso termina, los recursos que utilizó se liberan para otros procesos.

## Exercise

No hay ejercicios para esta lección.

## Quiz Question

¿Qué gestiona y controla los procesos?

## Quiz Answer

kernel
