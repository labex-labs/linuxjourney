---
lang: "es"
title: "Proceso de arranque: Init"
description: "Aprende sobre los sistemas init de Linux: System V, Upstart y systemd. Comprende sus roles en el proceso de arranque y cómo gestionan los servicios. ¡Comienza tu viaje en Linux!"
keywords: "Linux init, systemd, System V init, proceso de arranque de Linux, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Hemos hablado de init en lecciones anteriores y sabemos que es el primer proceso que se inicia, y que inicia todos los demás servicios esenciales en nuestro sistema. ¿Pero cómo?

En realidad, hay tres implementaciones principales de init en Linux:

### System V init (sysv)

Este es el sistema init tradicional. Inicia y detiene procesos secuencialmente basándose en scripts de inicio. El estado de la máquina se denota mediante runlevels; cada runlevel inicia o detiene una máquina de una manera diferente.

### Upstart

Este es el init que encontrarás en instalaciones antiguas de Ubuntu. Upstart utiliza la idea de jobs y events y funciona iniciando jobs que realizan ciertas acciones en respuesta a events.

### Systemd

Este es el nuevo estándar para init; está orientado a objetivos. Básicamente, tienes un objetivo que quieres lograr, y systemd intenta satisfacer las dependencias del objetivo para completarlo.

Tenemos un curso completo sobre sistemas Init donde profundizaremos en cada uno de estos sistemas con más detalle.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuál es el estándar más reciente para init?

## Quiz Answer

systemd
