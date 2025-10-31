---
index: 4
lang: "es"
title: "sysfs"
meta_title: "sysfs - Dispositivos"
meta_description: "Explore qué es sysfs y su papel en el sistema sys de Linux. Esta guía explica el directorio /sys de Linux, un sistema de archivos virtual para información de dispositivos, y lo contrasta con /dev."
meta_keywords: "sysfs, qué es sysfs, /sys, linux /sys, sistema sys, sistema sys, sistema de archivos virtual, dispositivos linux, /dev"
---

## Lesson Content

El sistema de archivos `sysfs` se introdujo para proporcionar una mejor manera de gestionar los dispositivos en un sistema Linux, una tarea para la cual el directorio `/dev` no estaba completamente equipado. Comprender **qué es /sys en Linux** es clave para la administración moderna del sistema.

### ¿Qué es sysfs?

`sysfs` es un sistema de archivos virtual, normalmente montado en `/sys`, que exporta información sobre objetos del kernel, dispositivos de hardware y controladores desde el modelo de dispositivos del kernel al userspace. A diferencia de los archivos en un disco físico, los archivos y directorios dentro de `/sys` se generan sobre la marcha y representan el estado actual del **sistema sys**.

### El papel del directorio linux /sys

El propósito principal del directorio **linux /sys** es proporcionar una vista estructurada de todos los dispositivos en su sistema. Contiene información detallada como el fabricante y el modelo, dónde está conectado el dispositivo, su estado actual y su posición en la jerarquía de dispositivos.

Los archivos que ve aquí no son nodos de dispositivos como los que se encuentran en `/dev`. Usted no interactúa directamente con el dispositivo a través de `/sys`; más bien, lo utiliza para ver información y gestionar los atributos del dispositivo.

### sysfs vs. /dev

Aunque `/sys` y `/dev` están relacionados con los dispositivos, sirven para diferentes funciones.

- El directorio `/dev` proporciona nodos de dispositivos, que son archivos especiales que permiten a los programas acceder a los dispositivos en sí.
- El sistema de archivos `/sys` se utiliza para ver información sobre los dispositivos y gestionarlos. Expone el modelo de dispositivo subyacente.

Por ejemplo, inspeccionemos el contenido de un directorio de dispositivo de bloque dentro de `/sys`:

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

Esta salida muestra varios atributos y subdirectorios relacionados con el disco duro `sda`, ofreciendo una vista mucho más detallada que solo `/dev/sda`.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la exploración de dispositivos de hardware en Linux:

1. **[Explorar dispositivos de hardware en Linux](https://labex.io/es/labs/comptia-explore-hardware-devices-in-linux-590861)** - Practique la identificación e inspección de dispositivos de hardware dentro de un entorno Linux, de manera similar a cómo el sistema de archivos `/sys` proporciona información del dispositivo.

Este laboratorio le ayudará a aplicar los conceptos de comprensión del hardware del sistema y su representación en Linux, aumentando la confianza con la exploración de dispositivos.

## Quiz Question

What directory is used to view detailed information on devices? Please answer in English.

## Quiz Answer

/sys
