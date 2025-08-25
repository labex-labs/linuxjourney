---
index: 1
lang: "es"
title: "Registro del sistema"
meta_title: "Registro del sistema - Registro"
meta_description: "Aprenda sobre el registro del sistema Linux, syslog y cómo ver archivos de registro en /var/log. Comprenda rsyslogd y monitoree eventos del sistema con esta guía para principiantes."
meta_keywords: "registro de Linux, syslog, rsyslogd, var log, registros del sistema, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Los servicios, el kernel, los demonios, etc., de su sistema están constantemente haciendo algo. Estos datos se envían para ser guardados en su sistema en forma de registros (logs). Esto nos permite tener un diario legible por humanos de los eventos que están ocurriendo en nuestro sistema. Estos datos generalmente se guardan en el directorio `/var`; ¡el directorio `/var` es donde guardamos nuestros datos variables, como los registros!

¿Cómo se reciben estos mensajes en su sistema? Hay un servicio llamado syslog que envía esta información al registrador del sistema.

Syslog en realidad contiene muchos componentes. Uno de los importantes es un demonio en ejecución llamado `syslogd` (las distribuciones de Linux más nuevas usan `rsyslogd`), que espera que ocurran mensajes de eventos y filtra los que le interesan. Dependiendo de lo que se supone que debe hacer con ese mensaje, lo enviará a un archivo, a su consola, o no hará nada con él.

Uno pensaría que este registrador del sistema es el lugar centralizado para administrar los registros, pero desafortunadamente, no lo es. Verá muchas aplicaciones que escriben sus propias reglas de registro y generan diferentes archivos de registro. Sin embargo, en general, el formato de los registros debe incluir una marca de tiempo y los detalles del evento.

Aquí hay un ejemplo de una línea de syslog:

```plaintext
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

Aquí podemos ver que el 27 de enero a las 07:41:32, nuestro servicio cron ejecutó la tarea `cron.weekly`. Puede ver todos los mensajes de eventos que syslog recopila dentro del archivo `/var/log/syslog`.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de los registros de Linux y la visualización de archivos:

1. **[Visualización de archivos de registro y configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Aprenda habilidades esenciales de la línea de comandos de Linux para ver y navegar eficientemente por archivos de texto, incluidos los registros del sistema y los archivos de configuración. Practique el uso de comandos como `cat`, `more` y `less` para extraer información crítica de varios tipos de archivos.
2. **[Comando tail de Linux: Visualización del final del archivo](https://labex.io/es/labs/linux-linux-tail-command-file-end-display-214303)** - Aprenda el comando `tail` de Linux para ver y monitorear el final de los archivos de texto. Esto es particularmente útil para el análisis de registros en tiempo real.
3. **[Buscar texto con grep en Linux](https://labex.io/es/labs/comptia-search-text-with-grep-in-linux-590841)** - En este laboratorio, aprenderá a buscar texto en archivos en un sistema Linux usando el comando `grep`. Esto es invaluable para encontrar entradas específicas dentro de archivos de registro grandes.

Estos laboratorios le ayudarán a aplicar los conceptos de gestión y análisis de archivos de registro en escenarios reales y a generar confianza con la monitorización del sistema Linux.

## Quiz Question

¿Cuál es el demonio que gestiona los registros en los sistemas Linux más nuevos?

## Quiz Answer

rsyslogd
