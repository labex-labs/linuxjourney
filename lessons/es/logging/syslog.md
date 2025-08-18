---
lang: "es"
title: "syslog"
meta_description: "Aprenda sobre syslog y rsyslog en Linux, cómo gestionar los registros del sistema y usar el comando logger. ¡Comience con este tutorial para principiantes!"
meta_keywords: "syslog, rsyslog, registros de Linux, comando logger, /var/log/syslog, tutorial de Linux, Linux para principiantes, registro del sistema"
---

## Lesson Content

El servicio syslog gestiona y envía registros al registrador del sistema. Rsyslog es una versión avanzada de syslog; la mayoría de las distribuciones de Linux deberían estar usando esta nueva versión. La salida de todos los registros que recopila el servicio syslog se puede encontrar en `/var/log/syslog` (todos los mensajes excepto los mensajes de autenticación).

Para saber qué archivos mantiene nuestro registrador del sistema, examine los archivos de configuración en `/etc/rsyslog.d`:

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

Estas reglas para los archivos de registro se denotan por el selector en la columna izquierda y la acción en la columna derecha. La acción nos dice dónde enviar la información de registro: a un archivo, consola, etc. Recuerde, no todas las aplicaciones y servicios usan rsyslog para gestionar sus registros, por lo que si desea saber específicamente qué se registra, tendrá que buscar dentro de este directorio.

Veamos el registro en acción; puede enviar manualmente un registro con el comando `logger`:

```bash
logger -s Hello
```

¡Ahora mire dentro de su `/var/log/syslog`, y debería ver esta entrada en sus registros!

## Exercise

Mire su archivo de configuración `/etc/rsyslog.d` y vea qué más se está registrando a través del registrador del sistema.

## Quiz Question

¿Qué comando puede usar para registrar un mensaje manualmente?

## Quiz Answer

logger
