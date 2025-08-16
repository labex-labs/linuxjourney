---
title: "Registro del sistema"
description: "Aprenda sobre el registro del sistema Linux, syslog y cómo ver los archivos de registro en /var/log. Comprenda rsyslogd y monitoree los eventos del sistema con esta guía para principiantes."
keywords: "registro de Linux, syslog, rsyslogd, var log, registros del sistema, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Los servicios, el kernel, los demonios, etc., de su sistema están constantemente haciendo algo. Estos datos se envían para guardarse en su sistema en forma de registros (logs). Esto nos permite tener un diario legible por humanos de los eventos que ocurren en nuestro sistema. Estos datos generalmente se guardan en el directorio `/var`; ¡el directorio `/var` es donde guardamos nuestros datos variables, como los registros!

¿Cómo se reciben estos mensajes en su sistema? Hay un servicio llamado syslog que envía esta información al registrador del sistema.

Syslog en realidad contiene muchos componentes. Uno de los importantes es un demonio en ejecución llamado `syslogd` (las distribuciones de Linux más nuevas usan `rsyslogd`), que espera a que ocurran mensajes de eventos y filtra los que le interesan. Dependiendo de lo que se supone que debe hacer con ese mensaje, lo enviará a un archivo, a su consola o no hará nada con él.

Uno pensaría que este registrador del sistema es el lugar centralizado para administrar los registros, pero desafortunadamente, no lo es. Verá muchas aplicaciones que escriben sus propias reglas de registro y generan diferentes archivos de registro. Sin embargo, en general, el formato de los registros debe incluir una marca de tiempo y los detalles del evento.

Aquí hay un ejemplo de una línea de syslog:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Aquí podemos ver que el 27 de enero a las 07:41:32, nuestro servicio cron ejecutó el trabajo `cron.weekly`. Puede ver todos los mensajes de eventos que syslog recopila dentro del archivo `/var/log/syslog`.

## Exercise

Examine su archivo `/var/log/syslog` y vea qué más está sucediendo en su máquina.

## Quiz Question

¿Cuál es el demonio que gestiona los registros en los sistemas Linux más nuevos?

## Quiz Answer

rsyslogd
