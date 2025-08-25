---
index: 4
lang: "es"
title: "sysfs"
meta_title: "sysfs - Dispositivos"
meta_description: "Aprenda sobre sysfs, un sistema de archivos virtual para información y gestión detallada de dispositivos Linux. Entienda /sys vs /dev. ¡Comience su viaje en Linux!"
meta_keywords: "sysfs, directorio /sys, dispositivos Linux, sistema de archivos virtual, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Sysfs fue creado hace mucho tiempo para gestionar mejor los dispositivos en nuestro sistema, una tarea que el directorio `/dev` no pudo realizar adecuadamente. Sysfs es un sistema de archivos virtual, que a menudo se monta en el directorio `/sys`. Nos proporciona información más detallada de la que podríamos ver en el directorio `/dev`. Ambos directorios, `/sys` y `/dev`, parecen muy similares y lo son en algunos aspectos, pero tienen diferencias importantes. Básicamente, el directorio `/dev` es simple; permite que otros programas accedan a los dispositivos, mientras que el sistema de archivos `/sys` se utiliza para ver información y gestionar el dispositivo.

El sistema de archivos `/sys` básicamente contiene toda la información de todos los dispositivos de su sistema, como el fabricante y el modelo, dónde está conectado el dispositivo, el estado del dispositivo, la jerarquía de los dispositivos y más. Los archivos que ve aquí no son nodos de dispositivo, por lo que realmente no interactúa con los dispositivos desde el directorio `/sys`; más bien, está gestionando dispositivos.

Eche un vistazo al contenido del directorio `/sys`:

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la exploración de dispositivos de hardware en Linux:

1. **[Explorar dispositivos de hardware en Linux](https://labex.io/es/labs/comptia-explore-hardware-devices-in-linux-590861)** - Practique la identificación e inspección de dispositivos de hardware dentro de un entorno Linux, de manera similar a cómo el sistema de archivos `/sys` proporciona información del dispositivo.

Este laboratorio le ayudará a aplicar los conceptos de comprensión del hardware del sistema y su representación en Linux, generando confianza con la exploración de dispositivos.

## Quiz Question

¿Qué directorio se utiliza para ver información detallada sobre los dispositivos?

## Quiz Answer

/sys
