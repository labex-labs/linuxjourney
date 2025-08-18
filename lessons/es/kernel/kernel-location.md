---
lang: "es"
title: "Ubicación del Kernel"
meta_title: "Ubicación del Kernel - Kernel"
meta_description: "Aprende sobre la ubicación del kernel de Linux en el directorio /boot, entendiendo vmlinuz, initrd y System.map. Explora los archivos del kernel y gestiona el espacio de forma eficaz."
meta_keywords: "kernel de Linux, directorio /boot, vmlinuz, initrd, System.map, principiante en Linux, tutorial de kernel, guía de Linux"
---

## Lesson Content

¿Qué sucede cuando instalas un nuevo kernel? Bueno, en realidad añade un par de archivos a tu sistema; estos archivos suelen añadirse al directorio `/boot`.

Verás múltiples archivos para diferentes versiones del kernel:

- `vmlinuz` - este es el kernel de Linux real
- `initrd` - como hemos comentado antes, el `initrd` se utiliza como un sistema de archivos temporal, usado antes de cargar el kernel
- `System.map` - tabla de búsqueda simbólica
- `config` - configuración del kernel; si estás compilando tu propio kernel, puedes establecer qué módulos se pueden cargar

Si tu directorio `/boot` se queda sin espacio, siempre puedes eliminar versiones antiguas de estos archivos o simplemente usar un gestor de paquetes. Pero ten cuidado al realizar el mantenimiento en este directorio y no elimines accidentalmente el kernel que estás utilizando actualmente.

## Exercise

Go into your boot directory and see what files are in there.

## Quiz Question

¿Cómo se llama la imagen del kernel en `/boot`?

## Quiz Answer

vmlinuz
