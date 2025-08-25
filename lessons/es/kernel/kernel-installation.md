---
index: 4
lang: "es"
title: "Instalación del Kernel"
meta_title: "Instalación del Kernel - Kernel"
meta_description: "Aprende a instalar y gestionar kernels de Linux. Descubre versiones de kernel, usa `uname -r` y comandos apt. ¡Comienza tu viaje con el kernel de Linux!"
meta_keywords: "kernel de Linux, instalar kernel, uname -r, apt dist-upgrade, gestión de kernel, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Bien, ahora que hemos dejado de lado todo ese aburrido material, hablemos de cómo instalar y modificar realmente los kernels. Puedes instalar múltiples kernels en tu sistema; ¿recuerdas nuestra lección sobre el proceso de arranque? En nuestro menú GRUB, podemos elegir con qué kernel arrancar.

Para ver qué versión de kernel tienes en tu sistema, usa el siguiente comando:

```bash
$ uname -r
3.19.0-43-generic
```

El comando `uname` imprime información del sistema; la opción `-r` imprimirá la versión de lanzamiento del kernel.

Puedes instalar el kernel de Linux de diferentes maneras: puedes descargar el paquete fuente y compilarlo desde el código fuente, o puedes instalarlo usando herramientas de gestión de paquetes.

```bash
sudo apt install linux-generic-lts-vivid
```

Y luego simplemente reinicia con el kernel que instalaste. Sencillo, ¿verdad? Más o menos. También necesitarás instalar otros paquetes de Linux como `linux-headers`, `linux-image-generic`, etc. También puedes especificar el número de versión, por lo que el comando anterior puede verse así: **`sudo apt install 3.19.0-43-generic`**

Alternativamente, si solo quieres la versión actualizada del kernel, simplemente usa `dist-upgrade`; realiza actualizaciones de todos los paquetes de tu sistema:

```bash
sudo apt dist-upgrade
```

Existen muchas versiones diferentes de kernel. Algunas se utilizan como LTS (Soporte a Largo Plazo), otras son las más recientes y avanzadas. La compatibilidad puede ser muy diferente entre las versiones del kernel, por lo que es posible que desees probar diferentes kernels.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión del kernel de Linux y las tareas de administración del sistema relacionadas:

1. **[Personalizar el menú de arranque GRUB2 en Linux](https://labex.io/es/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Practica la modificación del menú de arranque GRUB2, lo cual es esencial al gestionar múltiples versiones de kernel y seleccionar con cuál arrancar.
2. **[Gestionar módulos del kernel en Linux](https://labex.io/es/labs/comptia-manage-kernel-modules-in-linux-590865)** - Aprende a listar, inspeccionar, cargar y descargar módulos del kernel, un aspecto fundamental de la gestión del kernel y la comprensión de cómo el hardware interactúa con tu sistema.
3. **[Instalación de software en Linux](https://labex.io/es/labs/linux-software-installation-on-linux-18005)** - Adquiere experiencia práctica con varios métodos para instalar y gestionar software, incluido el uso de gestores de paquetes, que es una forma común de instalar y actualizar kernels.

Estos laboratorios te ayudarán a aplicar los conceptos de gestión del kernel, procesos de arranque y gestión de paquetes en escenarios reales, generando confianza en la administración del sistema.

## Quiz Question

¿Cómo se ve la versión del kernel de tu sistema?

## Quiz Answer

uname -r
