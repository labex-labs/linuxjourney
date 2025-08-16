---
title: "sysfs"
description: "Aprenda sobre sysfs, un sistema de archivos virtual para información detallada y gestión de dispositivos Linux. Entienda /sys vs /dev. ¡Comience su viaje en Linux!"
keywords: "sysfs, directorio /sys, dispositivos Linux, sistema de archivos virtual, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Sysfs fue creado hace mucho tiempo para gestionar mejor los dispositivos en nuestro sistema, una tarea que el directorio `/dev` no lograba hacer adecuadamente. Sysfs es un sistema de archivos virtual, la mayoría de las veces montado en el directorio `/sys`. Nos proporciona información más detallada de la que podríamos ver en el directorio `/dev`. Ambos directorios, `/sys` y `/dev`, parecen muy similares y lo son en algunos aspectos, pero tienen diferencias importantes. Básicamente, el directorio `/dev` es simple; permite que otros programas accedan a los dispositivos, mientras que el sistema de archivos `/sys` se utiliza para ver información y gestionar el dispositivo.

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

Revise el contenido del directorio `/sys` y vea qué archivos se encuentran allí.

## Quiz Question

¿Qué directorio se utiliza para ver información detallada sobre los dispositivos?

## Quiz Answer

/sys
