---
lang: "es"
title: "Registro del Kernel"
description: "Aprenda sobre el registro del kernel de Linux con dmesg y kern.log. Comprenda los mensajes de arranque y los problemas de hardware. Explore los registros del kernel para obtener información del sistema."
keywords: "dmesg, kern.log, registro de Linux, mensajes del kernel, registro de arranque, tutorial de Linux, guía para principiantes"
---

## Lesson Content

### /var/log/dmesg

Durante el arranque, su sistema registra información sobre el búfer circular del kernel. Esto nos muestra información sobre los controladores de hardware, información del kernel y el estado durante el arranque, entre otras cosas. Este archivo de registro se puede encontrar en `/var/log/dmesg` y se reinicia en cada arranque. Puede que ahora no le vea ninguna utilidad, pero si alguna vez tuviera problemas con algo durante el arranque o un problema de hardware, `dmesg` es el mejor lugar para buscar. También puede ver este registro usando el comando `dmesg`.

### /var/log/kern.log

Otro registro que puede usar para ver la información del kernel es el archivo `/var/log/kern.log`. Este registra información y eventos del kernel en su sistema; también registra la salida de `dmesg`.

## Exercise

Look at your `dmesg` and `kern` logs. What differences do you notice?

## Quiz Question

¿Qué comando se puede usar para ver los mensajes de arranque del kernel?

## Quiz Answer

dmesg
