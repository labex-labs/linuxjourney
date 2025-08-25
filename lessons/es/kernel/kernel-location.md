---
index: 5
lang: "es"
title: "Ubicación del Kernel"
meta_title: "Ubicación del Kernel - Kernel"
meta_description: "Aprende sobre la ubicación del kernel de Linux en el directorio /boot, entendiendo vmlinuz, initrd y System.map. Explora los archivos del kernel y gestiona el espacio de forma eficaz."
meta_keywords: "kernel de Linux, directorio /boot, vmlinuz, initrd, System.map, principiante de Linux, tutorial de kernel, guía de Linux"
---

## Lesson Content

¿Qué sucede cuando instalas un nuevo kernel? Bueno, en realidad añade un par de archivos a tu sistema; estos archivos suelen añadirse al directorio `/boot`.

Verás múltiples archivos para diferentes versiones del kernel:

- `vmlinuz` - este es el kernel de Linux real
- `initrd` - como hemos comentado antes, el `initrd` se utiliza como un sistema de archivos temporal, usado antes de cargar el kernel
- `System.map` - tabla de búsqueda simbólica
- `config` - configuración del kernel; si estás compilando tu propio kernel, puedes establecer qué módulos se pueden cargar

Si tu directorio `/boot` se queda sin espacio, siempre puedes eliminar versiones antiguas de estos archivos o simplemente usar un gestor de paquetes. Pero ten cuidado al realizar el mantenimiento en este directorio, y no borres accidentalmente el kernel que estás usando actualmente.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del proceso de arranque de Linux y la gestión del kernel:

1. **[Personalizar el menú de arranque GRUB2 en Linux](https://labex.io/es/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Practica la modificación de la configuración de GRUB2, lo que afecta directamente cómo arranca tu sistema Linux y selecciona las versiones del kernel. Este laboratorio te ayudará a comprender las implicaciones prácticas de los archivos discutidos en el directorio `/boot`.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a generar confianza con la gestión del kernel y el arranque de Linux.

## Quiz Question

¿Cómo se llama la imagen del kernel en `/boot`?

## Quiz Answer

vmlinuz
