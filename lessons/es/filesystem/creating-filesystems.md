---
index: 5
lang: "es"
title: "Creando Sistemas de Archivos"
meta_title: "Creando Sistemas de Archivos - El Filesystem"
meta_description: "Aprende a crear sistemas de archivos en Linux usando mkfs. Esta guía para principiantes cubre ext4 y el particionamiento de discos. ¡Comienza tu viaje en Linux!"
meta_keywords: "mkfs, crear sistema de archivos, ext4, particionamiento Linux, tutorial Linux, Linux para principiantes, gestión de discos, guía Linux"
---

## Lesson Content

¡Ahora que has particionado un disco, vamos a crear un sistema de archivos!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

¡Así de simple! La herramienta **mkfs** (make filesystem) nos permite especificar el tipo de sistema de archivos que queremos y dónde lo queremos. Solo querrás crear un sistema de archivos en un disco recién particionado o si estás reparticionando uno antiguo. Lo más probable es que dejes tu sistema de archivos en un estado corrupto si intentas crear uno sobre uno existente.

## Exercise

Make an ext4 filesystem on the USB drive.

## Quiz Question

¿Qué comando se utiliza para crear un sistema de archivos?

## Quiz Answer

mkfs
