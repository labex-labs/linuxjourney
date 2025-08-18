---
index: 4
lang: "es"
title: "Instalación del Kernel"
meta_title: "Instalación del Kernel - Kernel"
meta_description: "Aprende a instalar y gestionar kernels de Linux. Descubre las versiones de kernel, usa `uname -r` y los comandos apt. ¡Comienza tu viaje con el kernel de Linux!"
meta_keywords: "kernel de Linux, instalar kernel, uname -r, apt dist-upgrade, gestión de kernel, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Bien, ahora que hemos dejado de lado todo ese material aburrido, hablemos de cómo instalar y modificar kernels. Puedes instalar múltiples kernels en tu sistema; ¿recuerdas nuestra lección sobre el proceso de arranque? En nuestro menú GRUB, podemos elegir con qué kernel arrancar.

Para ver qué versión de kernel tienes en tu sistema, usa el siguiente comando:

```bash
$ uname -r
3.19.0-43-generic
```

El comando `uname` imprime información del sistema; la opción `-r` imprimirá la versión de lanzamiento del kernel.

Puedes instalar el Linux kernel de diferentes maneras: puedes descargar el paquete fuente y compilar desde el código fuente, o puedes instalarlo usando herramientas de gestión de paquetes.

```bash
sudo apt install linux-generic-lts-vivid
```

Y luego simplemente reinicia con el kernel que instalaste. Sencillo, ¿verdad? Más o menos. También necesitarás instalar otros paquetes de Linux como `linux-headers`, `linux-image-generic`, etc. También puedes especificar el número de versión, por lo que el comando anterior puede verse así: **`sudo apt install 3.19.0-43-generic`**

Alternativamente, si solo quieres la versión actualizada del kernel, simplemente usa `dist-upgrade`; realiza actualizaciones de todos los paquetes en tu sistema:

```bash
sudo apt dist-upgrade
```

Existen muchas versiones diferentes de kernel. Algunas se usan como LTS (Long Term Support), otras son las más recientes y avanzadas. La compatibilidad puede ser muy diferente entre las versiones de kernel, por lo que quizás quieras probar diferentes kernels.

## Exercise

1. Averigua qué versión de kernel tienes.
2. Investiga las diferentes versiones de kernels disponibles.

## Quiz Question

¿Cómo se ve la versión del kernel de tu sistema?

## Quiz Answer

uname -r
