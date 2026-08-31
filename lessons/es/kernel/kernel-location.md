---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "es"
order_index: 5
title: "Ubicación del kernel"
description: "Aprende dónde colocan las distribuciones las imágenes del kernel, los archivos initramfs, la configuración, los símbolos y los módulos asociados a cada versión."
meta_title: "Ubicación del kernel - Kernel"
meta_description: "Descubre dónde se almacena el kernel en Linux. Esta guía explica su ubicación en el directorio /boot y detalla archivos esenciales como vmlinuz e initrd."
meta_keywords: "ubicación kernel linux, dónde está el kernel, ubicación kernel, dónde se encuentra el kernel, dónde se almacena el kernel en linux, vmlinuz, directorio /boot"
---

Las distribuciones Linux suelen almacenar los artefactos arrancables del kernel bajo `/boot`, pero las disposiciones de UEFI y de la especificación del cargador de arranque también pueden colocar artefactos en una partición del sistema EFI o una partición de arranque ampliada montada en rutas como `/boot`, `/boot/efi` o `/efi`. Inspecciona los montajes y la configuración del cargador en lugar de suponer que existe una ruta universal.

## Archivos asociados a versiones bajo `/boot`

Una disposición tradicional de una distribución puede contener:

- `vmlinuz-KERNEL_RELEASE`: una imagen arrancable del kernel de Linux
- `initrd.img-KERNEL_RELEASE` o `initramfs-KERNEL_RELEASE.img`: una imagen del espacio de usuario inicial
- `config-KERNEL_RELEASE`: la configuración utilizada para compilar ese kernel empaquetado
- `System.map-KERNEL_RELEASE`: el mapa de direcciones de símbolos de la compilación del kernel

Los nombres varían. En una distribución moderna, un archivo cuyo nombre contiene `initrd` suele incluir un archivo initramfs. La convención de nombres `vmlinuz` no revela la compresión interna exacta ni el formato de arranque de la plataforma; inspecciónalo con las herramientas de la distribución.

:::single-choice{#kernel-location-vmlinuz}
¿Qué contiene normalmente un archivo `vmlinuz-*` asociado a una versión?

::option[Una imagen arrancable del kernel de Linux.]{#kernel-location-kernel-image .correct explanation="El cargador de arranque o el firmware carga este artefacto del kernel específico de la arquitectura."}
::option[Todos los módulos cargables de todos los kernels instalados.]{#kernel-location-all-modules explanation="Los módulos se almacenan por separado en un árbol específico de cada versión."}
::option[El historial del shell del usuario del arranque anterior.]{#kernel-location-shell-history explanation="Las imágenes del kernel de arranque no contienen el historial personal de comandos."}
:::

## Sistema de archivos RAM inicial y metadatos de compilación

El initramfs debe contener los módulos y las herramientas iniciales que necesiten su kernel correspondiente y el diseño del almacenamiento raíz. Que el nombre del archivo coincida no es suficiente: una generación obsoleta o fallida aún puede producir una entrada de arranque inutilizable.

`config-*` ayuda a determinar qué funciones se integraron, se compilaron como módulos o se omitieron. `System.map-*` puede ayudar con la interpretación de símbolos y la depuración, pero la aleatorización de direcciones, la información de depuración separada y las herramientas de la distribución afectan a su uso. Estos archivos son artefactos auxiliares, no kernels alternativos.

:::single-choice{#kernel-location-initramfs-match}
¿Por qué está vinculado un initramfs a una versión concreta del kernel y a la configuración del sistema?

::option[Almacena permanentemente el contenido de todos los sistemas de archivos montados.]{#kernel-location-all-filesystems explanation="Un initramfs es un pequeño entorno de arranque inicial, no una copia de seguridad completa del sistema."}
::option[Asigna UID nuevos a los usuarios durante cada arranque.]{#kernel-location-user-ids explanation="La gestión de identidades de las cuentas queda fuera de su función habitual."}
::option[Contiene los módulos y las herramientas iniciales que necesita esa ruta de arranque.]{#kernel-location-early-modules .correct explanation="La ABI de los módulos y los componentes necesarios para ensamblar el almacenamiento deben coincidir con el kernel elegido."}
:::

## Módulos asociados a versiones del kernel

Los módulos cargables de la versión en ejecución suelen residir bajo:

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

En disposiciones con sistemas de archivos combinados, esta ruta puede resolverse como `/usr/lib/modules/KERNEL_RELEASE`. Cada kernel instalado necesita un árbol de módulos compatible y sus índices de dependencias. `modprobe` utiliza metadatos específicos de la versión en lugar de buscar archivos `.ko` arbitrarios por todo el disco.

:::single-choice{#kernel-location-module-tree}
¿Qué directorio contiene convencionalmente los módulos de la versión del kernel en ejecución?

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="Los directorios personales de los usuarios no son el árbol estándar de módulos del sistema."}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="El componente de versión separa la ABI de los módulos y los datos de dependencias de cada kernel instalado."}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="`/proc/modules` informa de los módulos cargados y no es un directorio de binarios de módulos."}
:::

## Imágenes unificadas del kernel y rutas del firmware

Una imagen unificada del kernel, o UKI, es un único ejecutable EFI firmado que puede incluir un kernel, un initrd, una línea de comandos y metadatos. Las UKI suelen almacenarse en una ubicación de arranque accesible para EFI en lugar de representarse mediante archivos `vmlinuz` e initramfs separados.

Por tanto, que una disposición tradicional de `/boot` parezca vacía no demuestra que no haya ningún kernel instalado. Utiliza `findmnt`, la base de datos de paquetes, las herramientas del gestor de arranque y la configuración del cargador para relacionar los artefactos activos.

:::single-choice{#kernel-location-uki}
¿Qué puede combinar una imagen unificada del kernel?

::option[Todos los directorios personales de los usuarios en una cabecera GPT.]{#kernel-location-uki-homes explanation="Una UKI es un ejecutable de arranque, no un contenedor de datos de usuarios ni una tabla de particiones."}
::option[Todos los paquetes instalados en un único script de shell.]{#kernel-location-uki-packages explanation="Empaqueta componentes de arranque, no el repositorio completo del sistema operativo."}
::option[El kernel, el initrd, la línea de comandos y los metadatos en un ejecutable EFI.]{#kernel-location-uki-components .correct explanation="El artefacto combinado puede participar en un flujo de arranque UEFI firmado."}
:::

## Gestionar el espacio de forma segura

Si el sistema de archivos de arranque está lleno, primero identifica las rutas de arranque montadas y consulta qué paquete posee cada artefacto. Utiliza el flujo de limpieza de kernels del gestor de paquetes, conserva el kernel en ejecución y una alternativa de funcionamiento comprobado, regenera o inspecciona las entradas de arranque y comprueba después el espacio libre.

No elimines manualmente `vmlinuz`, initramfs, UKI o árboles de módulos solo por su antigüedad. Un archivo puede ser la única entrada arrancable de recuperación aunque no se esté ejecutando en ese momento.

## Resumen

Ahora puedes relacionar un paquete de kernel con sus artefactos de arranque y módulos.

1. Inspecciona los montajes reales de `/boot` y los relacionados con EFI.
2. Distingue la imagen del kernel, el initramfs, la configuración y el mapa de símbolos.
3. Haz coincidir los árboles de módulos con la versión exacta del kernel.
4. Ten en cuenta las imágenes unificadas del kernel y las disposiciones específicas de la distribución.
5. Recupera espacio de arranque únicamente mediante un plan verificado de paquetes y alternativas.
