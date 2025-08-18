---
index: 6
lang: "es"
title: "Módulos del Kernel"
meta_title: "Módulos del Kernel - Kernel"
meta_description: "Aprende sobre los módulos del kernel de Linux: cómo cargarlos, descargarlos y gestionarlos. Comprende los comandos `modprobe` y `lsmod` para extender la funcionalidad del kernel. ¡Comienza tu viaje en Linux!"
meta_keywords: "módulos del kernel de Linux, modprobe, lsmod, gestión del kernel, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Digamos que tengo un coche increíble; invierto mucho tiempo y dinero en él. Le añado un alerón, un enganche, un portabicicletas y otras cosas aleatorias. Estos componentes no cambian la funcionalidad principal del coche, y puedo quitarlos y ponerlos muy fácilmente. El kernel utiliza el mismo concepto con los módulos del kernel.

El kernel en sí mismo es una pieza de software monolítica. Cuando queremos añadir soporte para un nuevo tipo de teclado, no escribimos este código directamente en el código del kernel. Al igual que no fusionaríamos un portabicicletas a nuestro coche (bueno, quizás algunas personas lo harían). Los módulos del kernel son piezas de código que pueden cargarse y descargarse en el kernel bajo demanda. Nos permiten extender la funcionalidad del kernel sin añadir realmente al código central del kernel. También podemos añadir módulos y no tener que reiniciar el sistema (en la mayoría de los casos).

### View a list of currently loaded modules

```bash
lsmod
```

### Load a module

```bash
sudo modprobe bluetooth
```

`modprobe` carga el módulo desde `/lib/modules/(kernel version)/kernel/drivers`. Los módulos del kernel también pueden tener dependencias; `modprobe` carga las dependencias de nuestro módulo si aún no están cargadas.

### Remove a module

```bash
sudo modprobe -r bluetooth
```

### Load on bootup

También puedes cargar módulos durante el arranque del sistema, en lugar de cargarlos temporalmente con `modprobe` (que se descargarán al reiniciar). Simplemente modifica el directorio `/etc/modprobe.d` y añade un archivo de configuración en él de la siguiente manera:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

Un ejemplo un tanto extravagante, pero si tuvieras un módulo llamado `peanut_butter` y quisieras añadir un parámetro del kernel para `type=almond`, puedes hacer que se cargue al inicio usando este archivo de configuración. Además, ten en cuenta que los módulos del kernel tienen sus propios parámetros del kernel, por lo que querrás leer específicamente sobre el módulo para obtener más información.

### Do not load on bootup

También puedes asegurarte de que un módulo no se cargue al inicio añadiendo un archivo de configuración de la siguiente manera:

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

Descarga tu módulo Bluetooth con `modprobe` y mira qué sucede. ¿Cómo solucionarás esto?

## Quiz Question

¿Qué comando se utiliza para descargar un módulo?

## Quiz Answer

modprobe -r
