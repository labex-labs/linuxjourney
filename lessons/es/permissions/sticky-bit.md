---
index: 8
lang: "es"
title: "El Sticky Bit"
meta_title: "El Sticky Bit - Permisos"
meta_description: "Aprende sobre el sticky bit de Linux, su propósito en directorios compartidos como /tmp, y cómo establecerlo usando chmod. ¡Comprende este permiso de archivo clave!"
meta_keywords: "sticky bit de Linux, chmod +t, directorio /tmp, permisos de Linux, seguridad de archivos, tutorial de Linux, Linux para principiantes"
---

## Lesson Content

El último bit de permiso especial del que quiero hablar es el sticky bit.

Este bit de permiso "adhiere un archivo/directorio", lo que significa que solo el propietario o el usuario root pueden eliminar o modificar el archivo. Esto es muy útil para directorios compartidos. Echa un vistazo al siguiente ejemplo:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Verás un bit de permiso especial al final aquí **t**. Esto significa que todos pueden añadir archivos, escribir archivos y modificar archivos en el directorio `/tmp`, pero solo root puede eliminar el directorio `/tmp`.

### Modificar el sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

La representación numérica para el sticky bit es **1**.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los permisos de archivos de Linux y su impacto en la gestión de archivos y directorios:

1. **[Grupo de usuarios de Linux y permisos de archivos](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Practica la creación y gestión de usuarios y grupos, la comprensión de los permisos de archivos y la manipulación de la propiedad de los archivos. Este laboratorio proporciona el conocimiento fundamental para entender cómo funcionan los permisos especiales como el sticky bit.
2. **[Eliminar y mover archivos](https://labex.io/es/labs/linux-delete-and-move-files-7777)** - Aprende a eliminar y mover archivos en sistemas Linux. Este laboratorio te ayudará a comprender las implicaciones prácticas de los permisos, incluyendo cómo pueden restringir estas acciones.
3. **[Encontrar un archivo](https://labex.io/es/labs/linux-find-a-file-17993)** - Practica la localización de archivos y el establecimiento de la autoridad de acceso. Este laboratorio refuerza la importancia de los permisos de archivos y cómo controlan el acceso y la modificación.

Estos laboratorios te ayudarán a aplicar los conceptos de permisos de archivos en escenarios reales y a ganar confianza en la gestión del acceso a archivos en Linux.

## Quiz Question

¿Qué símbolo representa el sticky bit?

## Quiz Answer

t
