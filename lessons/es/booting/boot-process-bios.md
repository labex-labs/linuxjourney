---
index: 2
lang: "es"
title: "Proceso de arranque: BIOS"
meta_title: "Proceso de arranque: BIOS - Arrancar el sistema"
meta_description: "Aprenda sobre el proceso de arranque de Linux, BIOS y MBR. Comprenda cómo se inicia su sistema con esta guía para principiantes. ¡Explore los conceptos de UEFI!"
meta_keywords: "proceso de arranque de Linux, BIOS, MBR, UEFI, tutorial de Linux, bootloader, Linux para principiantes, inicio del sistema"
---

## Lesson Content

### BIOS

El primer paso en el proceso de arranque de Linux es el BIOS, que realiza comprobaciones de integridad del sistema. El BIOS es un firmware que es más común en las computadoras compatibles con IBM PC, el tipo dominante de computadoras hoy en día. Probablemente haya utilizado el firmware del BIOS para cambiar el orden de arranque de sus discos duros, verificar la hora del sistema, la dirección MAC de su máquina, etc. El objetivo principal del BIOS es encontrar el bootloader del sistema.

Entonces, una vez que el BIOS arranca el disco duro, busca el bloque de arranque para determinar cómo arrancar el sistema. Dependiendo de cómo particione su disco, buscará el Master Boot Record (MBR) o GPT. El MBR se encuentra en el primer sector del disco duro, los primeros 512 bytes. El MBR contiene el código para cargar otro programa en algún lugar del disco; este programa, a su vez, carga nuestro bootloader.

Ahora, si particionó su disco con GPT, la ubicación del bootloader cambia un poco.

### UEFI

Hay otra forma de arrancar su sistema en lugar de usar BIOS, y es con UEFI (que significa "Unified Extensible Firmware Interface"). UEFI fue diseñado para ser el sucesor del BIOS; la mayoría del hardware actual viene con firmware UEFI incorporado. Las máquinas Macintosh han estado usando el arranque EFI durante años, y Windows ha movido la mayoría de sus cosas al arranque UEFI. El formato GPT fue diseñado para usarse con EFI. No necesariamente necesita EFI si está arrancando un disco GPT. El primer sector de un disco GPT está reservado para un "MBR protector" para que sea posible arrancar una máquina basada en BIOS.

UEFI almacena toda la información sobre el inicio en un archivo `.efi`. Este archivo se almacena en una partición especial llamada EFI System Partition en el hardware. Dentro de esta partición, contendrá el bootloader. UEFI viene con muchas mejoras con respecto al firmware BIOS tradicional. Sin embargo, dado que estamos usando Linux, la mayoría de nosotros estamos usando BIOS. Así que todas estas lecciones se basarán en esa premisa.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de usuarios y grupos de Linux:

1. **[Administrar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practique el ciclo de vida completo de la administración de usuarios, desde la creación y seguridad de nuevas cuentas hasta su modificación y eliminación.
2. **[Administrar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Obtenga experiencia práctica con utilidades de línea de comandos para la administración de grupos, incluida la creación de nuevos grupos, la modificación de membresías de usuarios y la eliminación de grupos.
3. **[Configurar cuentas de usuario y privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas esenciales para administrar cuentas de usuario y privilegios sudo para mejorar la seguridad de un sistema Linux.

Estos laboratorios lo ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la administración de usuarios y grupos en Linux.

## Quiz Question

¿Qué carga el BIOS?

## Quiz Answer

bootloader
