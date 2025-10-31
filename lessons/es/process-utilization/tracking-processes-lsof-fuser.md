---
index: 2
lang: "es"
title: "lsof y fuser"
meta_title: "lsof y fuser - Uso de Procesos"
meta_description: "Explore los comandos lsof y fuser en Linux para identificar qué procesos están utilizando archivos específicos. Aprenda a resolver errores de 'Dispositivo o Recurso Ocupado', compare fuser vs lsof, y use opciones como fuser -k para gestionar archivos abiertos eficazmente."
meta_keywords: "lsof, fuser, comando fuser, fuser linux, fuser vs lsof, lsof vs fuser, fuser -k linux, archivos abiertos, gestión de procesos, dispositivo ocupado, comandos Linux"
---

## Lesson Content

¿Alguna vez ha intentado desmontar una unidad USB y ha recibido un error de "Dispositivo o recurso ocupado"? Este problema común ocurre cuando un proceso todavía está utilizando un archivo o directorio en el dispositivo. Para resolver esto, necesita averiguar qué proceso está reteniendo el recurso. Dos utilidades potentes para esta tarea son `lsof` y `fuser`.

### Usando lsof para listar archivos abiertos

En Linux, casi todo se trata como un archivo, incluidos discos, tuberías, sockets de red y dispositivos. El comando `lsof` (abreviatura de "list open files" o listar archivos abiertos) le muestra una lista detallada de todos los archivos abiertos y los procesos que los utilizan.

Para ver qué procesos están utilizando el directorio actual (`.`), puede ejecutar:

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
```

La salida muestra el comando (`COMMAND`), el ID de proceso (`PID`) y el usuario (`USER`) asociados con cada archivo abierto. Con esta información, puede identificar los procesos que le impiden desmontar un dispositivo.

### El comando fuser

Otra excelente herramienta es el comando `fuser` (abreviatura de "file user" o usuario de archivo). Esta utilidad identifica qué procesos están utilizando archivos, sockets o sistemas de archivos específicos. El comando `linux fuser` es una forma rápida de ver los PID de los procesos que acceden a un recurso en particular.

El uso de la opción `-v` (verbose o detallado) proporciona una salida más detallada:

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

Aquí, podemos ver claramente qué procesos están utilizando nuestro directorio actual. La columna `ACCESS` muestra cómo se está utilizando el archivo (por ejemplo, `c` para directorio actual).

### Terminación de procesos con fuser

Una característica clave del comando `fuser` es su capacidad para terminar procesos que están utilizando un recurso. La opción `fuser -k` envía una señal `SIGKILL` a cada proceso que accede al archivo o sistema de archivos especificado. Esto es particularmente útil para desmontar un dispositivo ocupado.

Por ejemplo, para eliminar todos los procesos que utilizan un punto de montaje en `/mnt/usb`, ejecutaría:

```bash
sudo fuser -k /mnt/usb
```

Usar `fuser -k` en Linux es una forma rápida y efectiva de liberar un recurso.

### fuser vs lsof

Entonces, ¿cuándo debe usar `fuser` vs `lsof`?

- **`lsof`** es excelente para la investigación detallada. Proporciona información exhaustiva sobre todos los archivos abiertos, lo que lo hace ideal para la solución de problemas complejos.
- **`fuser`** es más directo. Es perfecto para identificar rápidamente y, si es necesario, terminar procesos en un archivo o punto de montaje específico. El `fuser command` es a menudo la opción más rápida para resolver errores de "Dispositivo o recurso ocupado".

Ambas herramientas son esenciales para cualquier usuario de Linux. Familiarícese con ellas para administrar archivos y procesos de manera eficiente.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de procesos y la solución de conflictos de recursos:

1. **[Administrar y monitorear procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción con procesos en primer plano y en segundo plano, inspeccionándolos con `ps`, monitoreando recursos con `top` y terminándolos con `kill`. Este laboratorio le ayudará a identificar y administrar procesos que puedan estar reteniendo recursos, como archivos en una unidad USB.

Este laboratorio le ayudará a aplicar estos conceptos en escenarios del mundo real y a ganar confianza en la identificación y gestión de procesos del sistema.

## Quiz Question

What command is used to list open files and their associated process information? (Please answer in English, using only lowercase letters.)

## Quiz Answer

lsof
