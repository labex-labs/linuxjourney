---
index: 3
lang: "es"
title: "Nombres de dispositivos"
meta_title: "Nombres de dispositivos - Dispositivos"
meta_description: "Aprenda los nombres de dispositivos Linux como SCSI (sd), pseudo y PATA (hd). Comprenda /dev/sda, /dev/null y más en esta guía para principiantes."
meta_keywords: "nombres de dispositivos Linux, /dev, dispositivos SCSI, pseudodispositivos, dispositivos PATA, tutorial de Linux, Linux para principiantes, archivos de dispositivos"
---

## Lesson Content

Aquí están los nombres de dispositivos más comunes que encontrará:

### Dispositivos SCSI

Si tiene algún tipo de almacenamiento masivo en su máquina, lo más probable es que esté utilizando el protocolo SCSI (pronunciado "scuzzy"). SCSI significa Small Computer System Interface; es un protocolo utilizado para permitir la comunicación entre discos, impresoras, escáneres y otros periféricos y su sistema. Es posible que haya oído hablar de los dispositivos SCSI, que en realidad no se utilizan en los sistemas modernos; sin embargo, nuestros sistemas Linux corresponden los discos SCSI con las unidades de disco duro en `/dev`. Se representan con un prefijo `sd` (disco SCSI):

Archivos de dispositivos SCSI comunes:

- `/dev/sda` - Primer disco duro
- `/dev/sdb` - Segundo disco duro
- `/dev/sda3` - Tercera partición en el primer disco duro

### Pseudodispositivos

Como comentamos anteriormente, los pseudodispositivos no están realmente conectados físicamente a su sistema. La mayoría de los pseudodispositivos comunes son dispositivos de caracteres:

- `/dev/zero` - acepta y descarta toda la entrada, produce un flujo continuo de bytes NULL (valor cero)
- `/dev/null` - acepta y descarta toda la entrada, no produce salida
- `/dev/random` - produce números aleatorios

### Dispositivos PATA

A veces, en sistemas más antiguos, es posible que vea discos duros a los que se hace referencia con un prefijo `hd`:

- `/dev/hda` - Primer disco duro
- `/dev/hdd2` - Segunda partición en el cuarto disco duro

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de los nombres de dispositivos Linux y la gestión del almacenamiento:

1. **[Administrar particiones y sistemas de archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practique la creación, el formato y el montaje de particiones, lo que implica directamente trabajar con nombres de dispositivos.
2. **[Explorar dispositivos de hardware en Linux](https://labex.io/es/labs/comptia-explore-hardware-devices-in-linux-590861)** - Aprenda a identificar e inspeccionar varios dispositivos de hardware y sus nombres asociados dentro de un entorno Linux.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza en la gestión del almacenamiento y la comprensión del hardware en Linux.

## Quiz Question

¿Cuál sería comúnmente el nombre del dispositivo para la primera partición en el segundo disco SCSI?

## Quiz Answer

sdb1
