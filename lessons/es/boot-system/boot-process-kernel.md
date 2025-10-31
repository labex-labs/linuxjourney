---
index: 4
lang: "es"
title: "Proceso de Arranque: Kernel"
meta_title: "Proceso de Arranque: Kernel - Arrancar el Sistema"
meta_description: "Explora el proceso de arranque del kernel de Linux. Aprende cómo initramfs carga controladores desde un sistema de archivos temporal para montar la partición raíz de arranque final. Entiende los pasos desde la carga del kernel hasta la ejecución de init."
meta_keywords: "raíz de arranque, initramfs, arranque kernel, partición de arranque, initramfs ubuntu, /etc/default/grub, proceso de arranque Linux, sistema de archivos raíz, inicialización del kernel"
---

## Lesson Content

Una vez que el gestor de arranque (bootloader) ha cargado el kernel en la memoria y le ha pasado los parámetros necesarios, el kernel toma el control del sistema. Exploremos qué sucede a continuación.

### Inicialización del Kernel y el Initramfs

Un desafío clásico durante el arranque es que el kernel necesita controladores (drivers) para acceder a los dispositivos de hardware, pero esos controladores a menudo residen en un dispositivo de almacenamiento al que el kernel aún no puede acceder. Para resolver esto, Linux utiliza un sistema de archivos raíz temporal.

En sistemas más antiguos, esto se manejaba mediante un `initrd` (disco RAM inicial). El kernel cargaba esta imagen de disco, encontraba los controladores necesarios y luego cambiaba al sistema de archivos raíz real. Los sistemas modernos, incluidas distribuciones como Ubuntu, utilizan `initramfs` (sistema de archivos RAM inicial). A diferencia de `initrd`, `initramfs` es un archivo `cpio` que se descomprime en un sistema de archivos temporal directamente en la memoria. Este enfoque es más eficiente ya que evita la sobrecarga de crear y montar un dispositivo de bloque. El `initramfs` contiene solo los módulos esenciales que el kernel necesita para acceder a la partición de arranque real (`boot partition`) y otro hardware.

### Montaje del Sistema de Archivos Raíz de Arranque

Con los controladores cargados desde `initramfs`, el kernel ahora puede localizar y montar el sistema de archivos raíz principal (`boot root`). La ubicación de este sistema de archivos generalmente se pasa como un parámetro por el gestor de arranque, lo cual se puede configurar en archivos como `/etc/default/grub`.

Primero, el kernel monta la partición raíz de arranque (`boot root`) en modo solo lectura. Esta es una medida de seguridad que permite que la utilidad `fsck` (comprobación del sistema de archivos) se ejecute y verifique la integridad del sistema de archivos sin arriesgar la corrupción de datos. Después de que la comprobación se completa con éxito, el kernel vuelve a montar el sistema de archivos en modo lectura/escritura.

Finalmente, con el sistema de archivos raíz totalmente disponible, el kernel inicia el primer programa del espacio de usuario: `init`. Este programa es responsable de poner en línea el resto del sistema.

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión del proceso de arranque de Linux:

- **[Personalizar el menú de arranque GRUB2 en Linux](https://labex.io/es/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Aprende a modificar el menú de arranque GRUB2, incluyendo el cambio del tiempo de espera y la entrada predeterminada, y a aplicar estos cambios. Este laboratorio te ayudará a comprender cómo se puede configurar el gestor de arranque.

Este laboratorio te ayudará a aplicar los conceptos en un escenario real y a ganar confianza con la configuración de arranque de Linux.

## Quiz Question

What is used in modern systems to load a temporary root filesystem? Please answer in English, using only lowercase letters.

## Quiz Answer

initramfs
