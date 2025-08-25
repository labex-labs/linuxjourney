---
index: 5
lang: "es"
title: "Creación de sistemas de archivos"
meta_title: "Creación de sistemas de archivos - El sistema de archivos"
meta_description: "Aprenda a crear sistemas de archivos en Linux usando mkfs. Esta guía para principiantes cubre ext4 y el particionamiento de discos. ¡Comience su viaje en Linux!"
meta_keywords: "mkfs, crear sistema de archivos, ext4, particionamiento de Linux, tutorial de Linux, Linux para principiantes, gestión de discos, guía de Linux"
---

## Lesson Content

Ahora que realmente ha particionado un disco, ¡vamos a crear un sistema de archivos!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

¡Así de simple! La herramienta **mkfs** (make filesystem) nos permite especificar el tipo de sistema de archivos que queremos y dónde lo queremos. Solo querrá crear un sistema de archivos en un disco recién particionado o si está reparticionando uno antiguo. Lo más probable es que deje su sistema de archivos en un estado corrupto si intenta crear uno encima de uno existente.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de sistemas de archivos Linux:

1. **[Administrar particiones y sistemas de archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - En este laboratorio, aprenderá a administrar particiones de disco y sistemas de archivos en Linux. Utilizará fdisk para crear una nueva partición, formatearla con ext4 (usando `mkfs`), montarla, configurar el montaje persistente en /etc/fstab y crear una partición de intercambio, todo en un disco virtual secundario seguro.

Este laboratorio le ayudará a aplicar los conceptos de creación y gestión de sistemas de archivos en escenarios reales y a generar confianza con la gestión de discos en Linux.

## Quiz Question

¿Qué comando se utiliza para crear un sistema de archivos?

## Quiz Answer

mkfs
