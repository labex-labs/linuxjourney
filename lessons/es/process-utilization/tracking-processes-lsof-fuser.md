---
lesson_id: "tracking-processes-lsof-fuser"
course_id: "process-utilization"
lang: "es"
order_index: 2
title: "lsof y fuser"
description: "Aprende a identificar los procesos que utilizan archivos, directorios, puntos de montaje y sockets de red."
meta_title: "lsof y fuser - Utilización de procesos"
meta_description: "Aprende a usar lsof y fuser para identificar qué procesos utilizan archivos, sistemas de archivos y sockets."
meta_keywords: "lsof, fuser, archivos abiertos, dispositivo ocupado, procesos Linux, fuser -k"
---

Un sistema de archivos puede seguir ocupado porque un proceso mantiene un archivo abierto, asigna un archivo en memoria o utiliza un directorio como directorio de trabajo actual. `lsof` y `fuser` ayudan a identificar esas relaciones. Primero investiga; detener procesos es una decisión independiente con consecuencias para el funcionamiento.

## Mostrar archivos abiertos con lsof

`lsof` significa «list open files», es decir, mostrar archivos abiertos. Consulta una ruta para ver los registros de archivos abiertos coincidentes:

```bash
$ sudo lsof -- /mnt/usb
```

Para recorrer todo un árbol de directorios del mismo sistema de archivos, las implementaciones suelen admitir `+D`, pero los recorridos recursivos pueden ser costosos:

```bash
$ sudo lsof +D /mnt/usb
```

Entre las columnas útiles se encuentran `COMMAND`, `PID`, `USER`, el descriptor de archivo (`FD`), el tipo, el dispositivo y `NAME`. Un registro cuyo `FD` sea `cwd` indica que el proceso utiliza el directorio como directorio de trabajo actual. La salida sin privilegios puede estar incompleta para procesos de otros usuarios.

:::single-choice{#lsof-cwd-record}
¿Qué indica `cwd` en la columna `FD`?

::option[Que el proceso utiliza ese directorio como directorio de trabajo actual.]{#lsof-current-directory .correct explanation="El directorio actual de un proceso puede mantener ocupado un sistema de archivos montado."}
::option[Que el archivo se cerró mientras se escribía.]{#lsof-closed-write explanation="El marcador describe una relación con un directorio, no un suceso de cierre."}
::option[Que el proceso es propietario del dispositivo del sistema de archivos.]{#lsof-device-owner explanation="La propiedad del sistema de archivos no se representa mediante la etiqueta de descriptor `cwd`."}
:::

## Identificar usuarios con fuser

`fuser` comunica los identificadores de los procesos que utilizan un archivo o sistema de archivos indicado. La salida detallada añade usuarios, tipos de acceso y nombres de órdenes:

```bash
$ sudo fuser -v /mnt/usb
```

Para tratar el argumento como un sistema de archivos montado y encontrar los procesos que acceden a archivos situados dentro de él, utiliza la opción de montaje compatible con `fuser` de procps:

```bash
$ sudo fuser -vm /mnt/usb
```

Comprueba con herramientas como `findmnt --target /mnt/usb` que la ruta sea el punto de montaje pretendido. Los montajes enlazados, los espacios de nombres, los permisos y las condiciones de carrera pueden afectar a lo que revela una sola consulta.

:::single-choice{#fuser-verbose-purpose}
¿Por qué utilizar `fuser -v` en vez de `fuser` sin opciones durante una investigación?

::option[Porque desmonta automáticamente el sistema de archivos seleccionado.]{#fuser-verbose-unmount explanation="El modo detallado comunica información y no solicita un desmontaje."}
::option[Porque añade contexto como el usuario, el tipo de acceso y la orden.]{#fuser-verbose-details .correct explanation="Las columnas adicionales ayudan a evaluar con qué procesos es seguro coordinarse o cuáles se pueden detener."}
::option[Porque impide permanentemente que los procesos vuelvan a abrir archivos.]{#fuser-verbose-prevent explanation="Mostrar información no crea una regla de control de acceso."}
:::

## Gestionar un sistema de archivos ocupado

Sigue una secuencia deliberada en vez de matar de inmediato todos los PID coincidentes:

1. Confirma el equipo, la ruta, la fuente del montaje y el mantenimiento pretendido.
2. Identifica los procesos con ambas herramientas cuando sea práctico.
3. Determina si cada proceso puede detenerse, salir del directorio o terminar su trabajo.
4. Detenlo mediante su gestor de servicios o la interfaz de la aplicación cuando existan.
5. Vuelve a consultar y después desmonta y verifica el resultado.

`fuser -k` envía una señal a los procesos coincidentes. En las implementaciones habituales de procps, la señal predeterminada es `SIGKILL`, por lo que no permite un cierre ordenado. Si resulta necesaria una terminación aprobada explícitamente, elige una señal apropiada, verifica el PID y el propietario, y comprende que el conjunto de procesos puede cambiar entre la inspección y la acción.

:::single-choice{#fuser-k-risk}
¿Por qué `fuser -k /mnt/usb` es un mal primer paso para resolver un problema?

::option[Porque solo muestra el espacio libre del sistema de archivos.]{#fuser-k-space explanation="La opción se dirige a procesos, no comunica capacidad."}
::option[Porque puede matar varios procesos coincidentes sin una limpieza ordenada.]{#fuser-k-kills .correct explanation="La acción amplia de señalización puede interrumpir escrituras o servicios, así que primero deben investigarse y coordinarse."}
::option[Porque cambia el directorio de trabajo de todos los procesos coincidentes.]{#fuser-k-chdir explanation="Envía una señal y no traslada los directorios de los procesos."}
:::

## Elegir la herramienta

Utiliza `lsof` cuando necesites registros detallados de archivos abiertos, descriptores o información de sockets. Utiliza `fuser` para una vista orientada a rutas de los PID y tipos de acceso coincidentes. Ningún resultado por sí solo indica si es seguro terminar un proceso.

Para sockets de red, utiliza un espacio de nombres de protocolo explícito con `fuser` o una herramienta centrada en sockets como `ss`:

```bash
$ sudo fuser -v 22/tcp
$ sudo ss -lntp
```

:::single-choice{#lsof-fuser-tool-choice}
¿Qué herramienta resulta adecuada para obtener una lista detallada de descriptores de archivos abiertos y sus procesos propietarios?

::option[`lsof`]{#lsof-detailed-records .correct explanation="Su salida se organiza alrededor de registros de archivos abiertos y los metadatos de sus procesos."}
::option[`uptime`]{#lsof-uptime explanation="Uptime comunica el tiempo de actividad y los promedios de carga, no descriptores abiertos."}
::option[`free`]{#lsof-free explanation="Free resume la memoria, no el uso de archivos."}
:::

## Resumen

Ahora puedes investigar el uso de archivos y sistemas de archivos sin tratar la terminación como respuesta predeterminada.

1. Utiliza `lsof` para obtener registros detallados de archivos abiertos.
2. Utiliza `fuser` para obtener información de PID y acceso orientada a rutas.
3. Confirma el montaje y ten en cuenta los permisos y las condiciones de carrera.
4. Coordina una detención ordenada antes de plantearte una señal.
5. Vuelve a consultar y verifica el resultado del desmontaje o del servicio.
