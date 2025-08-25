---
index: 2
lang: "es"
title: "syslog"
meta_title: "syslog - Registro"
meta_description: "Aprenda sobre syslog y rsyslog en Linux, cómo administrar los registros del sistema y usar el comando logger. ¡Comience con este tutorial para principiantes!"
meta_keywords: "syslog, rsyslog, registros de Linux, comando logger, /var/log/syslog, tutorial de Linux, Linux para principiantes, registro del sistema"
---

## Lesson Content

El servicio syslog gestiona y envía registros al registrador del sistema. Rsyslog es una versión avanzada de syslog; la mayoría de las distribuciones de Linux deberían estar usando esta nueva versión. La salida de todos los registros que recopila el servicio syslog se puede encontrar en `/var/log/syslog` (todos los mensajes excepto los mensajes de autenticación).

Para saber qué archivos mantiene nuestro registrador del sistema, consulte los archivos de configuración en `/etc/rsyslog.d`:

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

Estas reglas para archivos de registro se denotan por el selector en la columna izquierda y la acción en la columna derecha. La acción nos dice dónde enviar la información de registro: a un archivo, consola, etc. Recuerde, no todas las aplicaciones y servicios usan rsyslog para gestionar sus registros, por lo que si desea saber específicamente qué se registra, tendrá que buscar dentro de este directorio.

Veamos el registro en acción; puede enviar un registro manualmente con el comando `logger`:

```bash
logger -s Hello
```

¡Ahora mire dentro de su `/var/log/syslog`, y debería ver esta entrada en sus registros!

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del registro de Linux y la visualización de archivos:

1. **[Visualización de archivos de registro y configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practique habilidades esenciales de línea de comandos de Linux para ver y navegar eficientemente por archivos de texto, incluidos registros del sistema y archivos de configuración.
2. **[Comando tail de Linux: Visualización del final del archivo](https://labex.io/es/labs/linux-linux-tail-command-file-end-display-214303)** - Aprenda el comando `tail` de Linux para ver y monitorear el final de los archivos de texto, lo cual es particularmente útil para el análisis de registros en tiempo real.
3. **[Buscar texto con grep en Linux](https://labex.io/es/labs/comptia-search-text-with-grep-in-linux-590841)** - Aprenda a buscar patrones de texto específicos dentro de archivos, una habilidad invaluable para examinar entradas de registro y encontrar información crítica.

Estos laboratorios le ayudarán a aplicar los conceptos de gestión de registros e inspección de archivos en escenarios reales y a generar confianza con la administración de sistemas Linux.

## Quiz Question

¿Qué comando puede usar para registrar un mensaje manualmente?

## Quiz Answer

logger
