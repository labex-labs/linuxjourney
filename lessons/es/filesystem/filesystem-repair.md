---
lang: "es"
title: "Reparación del sistema de archivos"
meta_title: "Reparación del sistema de archivos - El Filesystem"
meta_description: "Aprende a usar fsck para la reparación del sistema de archivos de Linux y la recuperación de datos. Comprende cómo verificar y corregir errores de disco con este comando esencial. ¡Comienza tu viaje en Linux!"
meta_keywords: "fsck, reparación del sistema de archivos, comandos de Linux, errores de disco, recuperación de datos, tutorial de Linux, guía para principiantes"
---

## Lesson Content

A veces, nuestro sistema de archivos no siempre está en las mejores condiciones. Si tenemos un apagado repentino, nuestros datos pueden corromperse. Depende del sistema intentar que volvamos a un estado de funcionamiento (aunque ciertamente podemos intentarlo nosotros mismos).

El comando **fsck** (filesystem check) se utiliza para verificar la consistencia de un sistema de archivos e incluso puede intentar repararlo por nosotros. Usualmente, cuando inicias un disco, fsck se ejecutará antes de que tu disco sea montado para asegurarse de que todo esté bien. Sin embargo, a veces tu disco está tan mal que necesitarás hacer esto manualmente. Asegúrate de hacerlo mientras estés en un disco de rescate o en algún lugar donde puedas acceder a tu sistema de archivos sin que esté montado.

```bash
sudo fsck /dev/sda
```

## Exercise

Look at the manpage for fsck to see what else it can do.

## Quiz Question

¿Qué comando se utiliza para verificar la integridad de un sistema de archivos?

## Quiz Answer

fsck
