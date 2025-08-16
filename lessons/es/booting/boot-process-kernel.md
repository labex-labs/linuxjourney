---
lang: "es"
title: "Proceso de Arranque: Kernel"
description: "Aprende sobre el proceso de arranque de Linux, la inicialización del kernel y el papel de initramfs. Comprende cómo el kernel monta el sistema de archivos raíz. Guía del proceso de arranque de Linux."
keywords: "proceso de arranque de Linux, arranque del kernel, initramfs, initrd, sistema de archivos raíz, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Ahora que nuestro cargador de arranque ha pasado los parámetros necesarios, veamos cómo se inicia:

### Initrd vs Initramfs

Existe un pequeño problema del huevo y la gallina cuando hablamos del arranque del kernel. El kernel gestiona el hardware de nuestro sistema; sin embargo, no todos los controladores están disponibles para el kernel durante el arranque. Por lo tanto, dependemos de un sistema de archivos raíz temporal que contiene solo los módulos esenciales que el kernel necesita para acceder al resto del hardware. En versiones anteriores de Linux, esta tarea se asignaba a initrd (initial ramdisk). El kernel montaba el initrd, obtenía los controladores de arranque necesarios y, una vez que terminaba de cargar todo lo que necesitaba, reemplazaba el initrd con el sistema de archivos raíz real. Hoy en día, tenemos algo llamado initramfs; este es un sistema de archivos raíz temporal que está integrado en el propio kernel para cargar todos los controladores necesarios para el sistema de archivos raíz real, por lo que ya no es necesario localizar el archivo initrd.

### Mounting the root filesystem

Ahora el kernel tiene todos los módulos que necesita para crear un dispositivo raíz y montar la partición raíz. Antes de continuar, la partición raíz se monta primero en modo de solo lectura para que fsck pueda ejecutarse de forma segura y verificar la integridad del sistema. Posteriormente, vuelve a montar el sistema de archivos raíz en modo de lectura-escritura. Luego, el kernel localiza el programa init y lo ejecuta.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué se utiliza en los sistemas modernos para cargar un sistema de archivos raíz temporal?

## Quiz Answer

initramfs
