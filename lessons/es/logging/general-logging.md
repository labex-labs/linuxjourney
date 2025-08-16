---
title: "Registro General"
description: "Aprende sobre los archivos de registro de Linux como /var/log/messages y syslog. Comprende sus diferencias para una solución de problemas efectiva del sistema. ¡Comienza tu viaje en Linux!"
keywords: "Registros de Linux, syslog, var/log/messages, solución de problemas de Linux, Linux para principiantes, guía de Linux, registros del sistema"
---

## Lesson Content

Hay muchos archivos de registro que puedes ver en tu sistema; muchos importantes se encuentran en `/var/log`. No los revisaremos todos, pero discutiremos un par de los principales.

Hay dos archivos de registro generales que puedes ver para tener una idea de lo que está haciendo tu sistema:

### `/var/log/messages`

Este registro contiene todos los mensajes no críticos y no de depuración, incluidos los mensajes registrados durante el arranque (dmesg), auth, cron, daemon, etc. Es muy útil para tener una idea de cómo se está comportando tu máquina.

### `/var/log/syslog`

Esto registra todo excepto los mensajes de auth; es extremadamente útil para depurar errores en tu máquina.

Estos dos registros deberían ser más que suficientes al solucionar problemas con tu sistema. Sin embargo, si solo deseas ver un componente de registro específico, también hay registros separados para ellos.

## Exercise

Look at your `/var/log/messages` and `/var/log/syslog` files and see what the differences are.

## Quiz Question

¿Qué archivo de registro registra todo excepto los mensajes de auth?

## Quiz Answer

syslog
