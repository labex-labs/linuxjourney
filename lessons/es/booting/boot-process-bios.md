---
lang: "es"
title: "Proceso de arranque: BIOS"
description: "Aprenda sobre el proceso de arranque de Linux, BIOS y MBR. Comprenda cómo se inicia su sistema con esta guía para principiantes. ¡Explore los conceptos de UEFI!"
keywords: "proceso de arranque de Linux, BIOS, MBR, UEFI, tutorial de Linux, bootloader, Linux para principiantes, inicio del sistema"
---

## Lesson Content

### BIOS

El primer paso en el proceso de arranque de Linux es el BIOS, que realiza comprobaciones de integridad del sistema. El BIOS es un firmware que es más común en las computadoras compatibles con IBM PC, el tipo dominante de computadoras hoy en día. Probablemente haya usado el firmware del BIOS para cambiar el orden de arranque de sus discos duros, verificar la hora del sistema, la dirección MAC de su máquina, etc. El objetivo principal del BIOS es encontrar el bootloader del sistema.

Entonces, una vez que el BIOS arranca el disco duro, busca el boot block para averiguar cómo arrancar el sistema. Dependiendo de cómo particione su disco, buscará el Master Boot Record (MBR) o GPT. El MBR se encuentra en el primer sector del disco duro, los primeros 512 bytes. El MBR contiene el código para cargar otro programa en algún lugar del disco; este programa a su vez carga nuestro bootloader.

Ahora, si particionó su disco con GPT, la ubicación del bootloader cambia un poco.

### UEFI

Hay otra forma de arrancar su sistema en lugar de usar BIOS, y es con UEFI (que significa "Unified Extensible Firmware Interface"). UEFI fue diseñado para ser el sucesor de BIOS; la mayoría del hardware actual viene con firmware UEFI incorporado. Las máquinas Macintosh han estado usando el arranque EFI durante años, y Windows ha movido la mayoría de sus cosas al arranque UEFI. El formato GPT fue diseñado para usarse con EFI. No necesariamente necesita EFI si está arrancando un disco GPT. El primer sector de un disco GPT está reservado para un "protective MBR" para hacer posible arrancar una máquina basada en BIOS.

UEFI almacena toda la información sobre el inicio en un archivo `.efi`. Este archivo se almacena en una partición especial llamada EFI System Partition en el hardware. Dentro de esta partición, contendrá el bootloader. UEFI viene con muchas mejoras con respecto al firmware BIOS tradicional. Sin embargo, dado que estamos usando Linux, la mayoría de nosotros estamos usando BIOS. Así que todas estas lecciones seguirán esa premisa.

## Exercise

Go into your BIOS menu and see if you have UEFI booting enabled.

## Quiz Question

¿Qué carga el BIOS?

## Quiz Answer

bootloader
