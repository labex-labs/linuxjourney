---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "es"
order_index: 3
title: "Proceso de arranque: cargador"
description: "Aprende cómo un cargador selecciona los elementos de Linux, construye la línea de órdenes del kernel y transfiere el control."
meta_title: "Proceso de arranque: cargador - Arrancar el sistema"
meta_description: "Aprende cómo un cargador como GRUB selecciona el kernel y el initramfs, pasa parámetros y transfiere el control."
meta_keywords: "cargador de arranque Linux, GRUB, parámetros del kernel, initramfs, root, quiet"
---

Un cargador de arranque sirve de puente entre el descubrimiento del firmware y la ejecución del kernel. GRUB es habitual en los PC con Linux, pero systemd-boot, U-Boot, la carga por el firmware de un kernel con EFI stub y otros diseños implementan partes distintas de esta función.

## Seleccionar los elementos de arranque

Una entrada del cargador puede identificar:

- una imagen del kernel de Linux
- una imagen initramfs opcional o initrd heredada
- una línea de órdenes del kernel
- metadatos específicos de la plataforma o el cargador de otro sistema operativo

GRUB puede presentar varios kernels y entradas de recuperación. Un kernel alternativo solo resulta útil si sus módulos e initramfs correspondientes siguen disponibles y se han probado. El cargador lee archivos mediante sus módulos compatibles de almacenamiento y sistemas de archivos; no depende del VFS de Linux, que todavía no está en ejecución.

:::single-choice{#bootloader-primary-handoff}
¿A qué transfiere normalmente el control un cargador de arranque de Linux?

::option[A un shell interactivo de usuario con todos los servicios ya en ejecución.]{#bootloader-user-shell explanation="Los shells del espacio de usuario solo aparecen después de iniciarse el kernel y el sistema init."}
::option[A la imagen de kernel seleccionada después de cargar los elementos de arranque necesarios.]{#bootloader-selected-kernel .correct explanation="El cargador prepara el kernel, los parámetros y, a menudo, un initramfs antes de ejecutar el punto de entrada del kernel."}
::option[Al gestor de paquetes del sistema de archivos para resolver dependencias.]{#bootloader-package-manager explanation="La gestión de paquetes no es la siguiente etapa de control del procesador durante el arranque."}
:::

## Parámetros de la línea de órdenes del kernel

El cargador pasa una línea de texto que analizan el kernel y el espacio de usuario inicial. Algunos ejemplos habituales son:

- `root=...` para identificar el sistema de archivos raíz previsto o una especificación de fuente para el espacio de usuario inicial
- `ro` o `rw` para solicitar un modo inicial de montaje de la raíz
- `quiet` para reducir los mensajes del kernel en la consola
- `init=...` para solicitar otro primer programa del espacio de usuario en una recuperación especializada
- parámetros `rd.*` específicos de la distribución que interpretan las herramientas de initramfs

`initrd` suele ser una directiva del cargador que nombra una imagen, no un parámetro genérico del kernel. `BOOT_IMAGE=` puede aparecer en una línea generada por algunas configuraciones de GRUB, pero no es el mecanismo que carga el kernel.

Examina la línea utilizada en el arranque actual con:

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter}
¿Cuál es la finalidad del parámetro `root=` de la línea de órdenes del kernel?

::option[Identificar el sistema de archivos raíz que deberá utilizar finalmente el arranque.]{#bootloader-root-filesystem .correct explanation="El kernel o initramfs interpreta el valor como parte de la localización y ensamblaje de la raíz real."}
::option[Establecer la contraseña de inicio de sesión de la cuenta root.]{#bootloader-root-password explanation="Los secretos de autenticación no deben pasarse como texto ordinario en la línea de órdenes del kernel."}
::option[Cambiar el nombre del PID 1 a la palabra `root`.]{#bootloader-root-pid explanation="El nombre de los procesos no guarda relación con este parámetro de almacenamiento."}
:::

:::single-choice{#bootloader-quiet-parameter}
¿Qué solicita normalmente el parámetro `quiet`?

::option[Acceso de solo lectura a todos los sistemas de archivos montados.]{#bootloader-quiet-readonly explanation="La política inicial de escritura de la raíz utiliza parámetros como `ro`, no `quiet`."}
::option[Reducir los mensajes del kernel impresos durante el arranque.]{#bootloader-quiet-console .correct explanation="Suprime muchos mensajes informativos, pero no garantiza el silencio de todos los componentes del arranque."}
::option[Deshabilitar todos los ventiladores del hardware.]{#bootloader-quiet-fans explanation="El parámetro afecta a la cantidad de mensajes, no al control acústico del hardware."}
:::

## Edición temporal y recuperación

GRUB suele permitir que un usuario de consola autorizado edite una entrada para un único arranque, a menudo mediante una tecla de edición mostrada por el menú. Esto resulta útil para retirar `quiet`, elegir parámetros de recuperación o corregir un identificador de raíz incorrecto. La interfaz y la autorización varían, especialmente con Secure Boot y configuraciones de GRUB protegidas con contraseña.

Los parámetros pueden exponer texto confidencial mediante `/proc/cmdline`, los registros de arranque y los informes de fallos. También pueden debilitar la seguridad o hacer imposible arrancar el sistema. Nunca introduzcas secretos y conserva una entrada válida conocida y una vía de recuperación mediante consola.

:::single-choice{#bootloader-temporary-edit}
¿Cuál es una propiedad habitual de editar interactivamente una entrada de GRUB para un arranque?

::option[Reescribe automáticamente todas las imágenes de kernel instaladas.]{#bootloader-rewrites-kernels explanation="Cambiar el texto de las órdenes no modifica los binarios del kernel."}
::option[Deshabilita permanentemente la verificación del firmware en todos los discos.]{#bootloader-disables-firmware explanation="La política del firmware es independiente y una edición de una entrada no la modifica universalmente."}
::option[El cambio se aplica a ese arranque salvo que se guarde por separado en la configuración.]{#bootloader-one-boot-change .correct explanation="Editar el menú suele modificar la entrada en memoria y no la configuración fuente persistente."}
:::

## Configuración persistente de GRUB

Las distribuciones suelen generar la configuración final de GRUB a partir de plantillas, valores predeterminados, scripts y kernels detectados. No edites directamente el `grub.cfg` generado salvo que la distribución documente explícitamente ese flujo; volver a generarlo puede sobrescribirlo.

Realiza un cambio limitado en la fuente, ejecuta la orden de regeneración documentada por la distribución, examina su salida y prueba conservando una entrada anterior válida y un medio de recuperación arrancable. La orden y la ruta de salida difieren entre Debian, Fedora y las instalaciones UEFI y BIOS.

:::single-choice{#bootloader-generated-config}
¿Por qué suele ser poco fiable editar directamente un `grub.cfg` generado?

::option[Porque el archivo nunca puede contener texto legible.]{#bootloader-config-binary explanation="La configuración de GRUB es texto, pero sigue importando que sea un archivo generado."}
::option[Porque GRUB solo lee archivos en el directorio personal de cada usuario.]{#bootloader-grub-home explanation="La configuración de arranque pertenece al sistema y debe estar disponible antes de las sesiones personales."}
::option[Porque una regeneración posterior puede sobrescribir el cambio manual.]{#bootloader-regeneration-overwrites .correct explanation="Los ajustes persistentes suelen corresponder a las fuentes de configuración y al flujo de generación de la distribución."}
:::

Utiliza [Personalizar el menú de arranque de GRUB2](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) únicamente en su entorno de laboratorio con capacidad de recuperación.

## Resumen

Ahora puedes separar las directivas del cargador de los parámetros de la línea de órdenes del kernel.

1. Identifica el kernel, initramfs, la línea de órdenes y las entradas alternativas.
2. Utiliza `root=`, `ro` y `quiet` conforme a sus funciones reales.
3. Examina los parámetros del arranque en ejecución mediante `/proc/cmdline`.
4. Trata las ediciones interactivas como temporales y sensibles para la seguridad.
5. Cambia la configuración generada persistente mediante el flujo de la distribución.
