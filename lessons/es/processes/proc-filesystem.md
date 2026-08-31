---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "es"
order_index: 10
title: "Sistema de archivos /proc"
description: "Aprende cómo Linux expone información actual de los procesos y del kernel mediante el sistema de archivos virtual `/proc`."
meta_title: "Sistema de archivos /proc - Procesos"
meta_description: "Descubre el sistema de archivos /proc de Linux, un directorio virtual que ofrece una vista del kernel y de los procesos en ejecución."
meta_keywords: "sistema de archivos /proc, proc Linux, información de procesos, kernel Linux, procesos Linux"
---

Linux suele montar `procfs` en `/proc`. Este sistema de archivos virtual presenta interfaces generadas por el kernel como archivos y directorios; su contenido no son archivos persistentes ordinarios almacenados en disco. Expone tanto el estado de los procesos como cierta información del kernel relativa a todo el sistema.

## Localizar directorios de procesos

Muestra el montaje y las entradas del nivel superior con:

```bash
$ findmnt /proc
$ ls /proc
```

Los nombres de directorio numéricos corresponden a los identificadores de procesos visibles en el espacio de nombres de PID del proceso que realiza la consulta. Por ejemplo, `/proc/12345` representa el PID 12345 en el instante en que existe. `/proc/self` es un enlace simbólico que se resuelve al directorio propio del proceso que observa, y `/proc/thread-self` identifica el hilo actual.

La visibilidad y el acceso dependen de las credenciales, los espacios de nombres, la política de seguridad y opciones de montaje de procfs como `hidepid`. Un proceso puede terminar entre el listado de un directorio y la apertura de uno de sus archivos, por lo que su desaparición es una condición de carrera normal que las herramientas de inspección deben saber gestionar.

:::single-choice{#proc-filesystem-numeric-directory}
¿Qué representa normalmente el directorio numérico `/proc/12345`?

::option[El bloque de disco número 12345.]{#proc-filesystem-disk-block explanation="`/proc` es una interfaz virtual del kernel, no un directorio de bloques de disco sin procesar."}
::option[El proceso visible en ese momento con el PID 12345.]{#proc-filesystem-pid-directory .correct explanation="Los datos de procfs correspondientes a cada proceso se agrupan bajo un directorio cuyo nombre es el PID visible."}
::option[La cuenta de usuario cuyo UID es 12345.]{#proc-filesystem-user-directory explanation="Los directorios numéricos de procesos del nivel superior se identifican mediante el PID, no el UID."}
:::

## Leer información de un proceso

Cuando los permisos lo permitan, examina el archivo de estado de un proceso:

```bash
$ less /proc/12345/status
```

Incluye campos como el nombre y el estado del proceso, identificadores, credenciales, contadores de memoria, capacidades y máscaras de señales. Otras entradas útiles son:

- `/proc/12345/cmdline`: argumentos de la línea de órdenes separados por bytes nulos
- `/proc/12345/environ`: entradas del entorno, sujetas a controles de acceso y potencialmente confidenciales
- `/proc/12345/fd/`: enlaces simbólicos que representan descriptores de archivo abiertos
- `/proc/12345/maps`: asignaciones actuales de memoria
- `/proc/12345/cwd`: enlace simbólico al directorio de trabajo actual

Trátalas como observaciones cambiantes. Los campos pueden variar según la versión del kernel, un proceso puede cambiar de estado durante la lectura de varios archivos y algunos contadores tienen matices que sus nombres no reflejan por sí solos.

:::single-choice{#proc-filesystem-status-file}
¿Qué ruta contiene un resumen legible y organizado en campos para el PID 12345?

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="Los archivos de cada proceso están dentro del directorio que lleva el nombre de su PID, no bajo un directorio `status` en el nivel superior."}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="La interfaz `status` de cada proceso presenta identificadores, estado, memoria, señales y credenciales."}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="`/proc/cpuinfo` es una interfaz de todo el sistema, no un directorio con archivos de estado para cada PID."}
:::

## Leer interfaces de todo el sistema

No todas las entradas de `/proc` pertenecen a un proceso. Algunos ejemplos son:

- `/proc/cpuinfo`, con información de la CPU proporcionada por el kernel
- `/proc/meminfo`, con contadores de memoria del sistema
- `/proc/mounts`, con la vista de los montajes que tiene el proceso actual
- `/proc/loadavg`, con información sobre la carga media y las tareas preparadas para ejecutarse
- `/proc/sys/`, con parámetros del kernel durante la ejecución

Algunos archivos, sobre todo los situados bajo `/proc/sys`, son interfaces de configuración en las que se puede escribir. No escribas en ellos solo porque parezcan archivos normales. Antes de realizar un cambio autorizado en el sistema, comprende el parámetro, su alcance, el mecanismo para hacerlo persistente y cómo revertirlo.

:::single-choice{#proc-filesystem-system-interface}
¿Qué entrada proporciona contadores de memoria de todo el sistema en vez del estado de un único proceso?

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="Esta ruta se resuelve al estado del propio proceso que realiza la observación."}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="`meminfo` contiene estadísticas de la memoria del sistema proporcionadas por el kernel."}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="Este directorio representa los descriptores de archivo pertenecientes al PID 1, sujetos a controles de acceso."}
:::

## Utilizar `/proc` mediante herramientas

Las implementaciones de Linux de herramientas como `ps`, `top` y `free` obtienen gran parte de sus datos de procfs y de otras interfaces del kernel, y después los etiquetan, calculan y presentan. En el trabajo habitual, prefiere esas herramientas cuando proporcionen el campo que necesitas; lee `/proc` directamente para obtener detalles concretos o crear scripts solo después de estudiar la documentación de la interfaz.

Los lectores directos deben analizar los formatos correctamente, tolerar la desaparición de procesos, proteger la información confidencial y evitar suponer que una lectura constituye una instantánea atómica del sistema.

:::single-choice{#proc-filesystem-live-data}
¿Por qué puede desaparecer `/proc/PID` entre dos órdenes de inspección?

::option[Porque cada archivo de procfs cambia automáticamente de nombre una vez por segundo.]{#proc-filesystem-renamed explanation="No existe ninguna regla que cambie periódicamente el nombre de todas las entradas de procfs."}
::option[Porque leer `status` elimina el directorio del proceso.]{#proc-filesystem-read-delete explanation="La inspección de estado es de solo lectura y no termina ni elimina el proceso."}
::option[Porque el proceso puede terminar mientras se observa.]{#proc-filesystem-process-exit .correct explanation="Procfs refleja el estado actual, por lo que el kernel elimina el directorio de un proceso cuando este deja de existir."}
:::

## Resumen

Ahora puedes utilizar procfs como una interfaz actual del kernel sujeta a controles de acceso.

1. Asocia los directorios numéricos de `/proc` con los PID visibles.
2. Lee archivos concretos de cada proceso teniendo en cuenta las condiciones de carrera y la confidencialidad.
3. Distingue los directorios de procesos de las interfaces de todo el sistema.
4. Para una inspección habitual y fiable, prefiere herramientas y formatos documentados.
