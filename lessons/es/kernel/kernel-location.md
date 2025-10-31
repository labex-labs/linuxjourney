---
index: 5
lang: "es"
title: "Ubicación del Kernel"
meta_title: "Ubicación del Kernel - Kernel"
meta_description: "Descubra dónde se almacena el kernel en Linux. Esta guía explica la ubicación del kernel de Linux en el directorio /boot, detallando archivos clave como vmlinuz e initrd."
meta_keywords: "ubicacion kernel linux, donde esta el kernel, ubicacion kernel, donde esta ubicado el kernel, donde se almacena el kernel en linux, vmlinuz, directorio /boot"
---

## Lesson Content

Cuando instala un nuevo kernel, su sistema agrega varios archivos importantes a un directorio específico. Si alguna vez se ha preguntado **dónde se almacena el kernel en Linux**, la respuesta suele ser el directorio `/boot`. Este directorio es la **ubicación estándar del kernel de Linux** en la mayoría de los sistemas.

### El Directorio /boot

El directorio `/boot` contiene todos los archivos necesarios para iniciar el proceso de arranque. Cuando mira dentro, a menudo verá archivos correspondientes a diferentes versiones del kernel, lo que le permite arrancar con un kernel anterior si uno nuevo causa problemas. Comprender esta **ubicación del kernel** es crucial para el mantenimiento del sistema.

### Archivos Clave del Kernel

Entonces, **dónde se encuentra el kernel** dentro de este directorio? Está acompañado por algunos otros archivos críticos. Aquí están los principales que encontrará:

- `vmlinuz`: Este es el kernel de Linux ejecutable y comprimido. La 'z' al final indica que está comprimido.
- `initrd`: Este es el disco RAM inicial. Como hemos discutido, el `initrd` es un sistema de archivos raíz temporal cargado en la memoria durante el inicio para montar el sistema de archivos raíz real.
- `System.map`: Este archivo contiene una tabla de símbolos, que mapea los nombres de las funciones del kernel a sus direcciones de memoria. Se utiliza principalmente para depurar pánicos y errores del kernel (oops).
- `config`: Este archivo almacena la configuración que se utilizó para compilar esa versión específica del kernel. Detalla qué controladores y características se incluyeron.

### Gestión de Archivos del Kernel

Con el tiempo, su directorio `/boot` puede llenarse con archivos de kernels antiguos. Si se queda sin espacio, puede eliminar los archivos de versiones antiguas y no utilizadas. La forma más segura de hacerlo es utilizando el gestor de paquetes de su distribución (como `apt` o `dnf`). Eliminar archivos manualmente puede ser arriesgado, así que tenga mucho cuidado de no eliminar los archivos del kernel que está utilizando actualmente.

## Exercise

Aplique sus conocimientos con este laboratorio práctico para reforzar su comprensión del proceso de arranque de Linux y la gestión del kernel:

1. **[Personalizar el menú de arranque GRUB2 en Linux](https://labex.io/es/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Practique la modificación de la configuración de GRUB2, que afecta directamente a cómo su sistema Linux arranca y selecciona las versiones del kernel. Este laboratorio le ayudará a comprender las implicaciones prácticas de los archivos discutidos en el directorio `/boot`.

Este laboratorio le ayudará a aplicar estos conceptos en un escenario del mundo real y a ganar confianza con la gestión del kernel y el arranque de Linux.

## Quiz Question

En el directorio `/boot`, ¿cuál es el nombre típico del archivo de imagen del kernel de Linux comprimido? Por favor, responda en inglés, prestando atención a la sensibilidad a mayúsculas y minúsculas.

## Quiz Answer

vmlinuz
