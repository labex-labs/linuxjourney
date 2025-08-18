---
lang: "es"
title: "El Sticky Bit"
meta_title: "El Sticky Bit - Permisos"
meta_description: "Aprende sobre el sticky bit de Linux, su propósito en directorios compartidos como /tmp, y cómo configurarlo usando chmod. ¡Comprende este permiso de archivo clave!"
meta_keywords: "sticky bit de Linux, chmod +t, directorio /tmp, permisos de Linux, seguridad de archivos, tutorial de Linux, Linux para principiantes"
---

## Lesson Content

Un último bit de permiso especial del que quiero hablar es el sticky bit.

Este bit de permiso "adhiere un archivo/directorio", lo que significa que solo el propietario o el usuario root pueden eliminar o modificar el archivo. Esto es muy útil para directorios compartidos. Observa el siguiente ejemplo:

```bash
$ ls -ld /tmp
drwxrwxrwx+t 6 root root 4096 Dec 15 11:45 /tmp
```

Verás un bit de permiso especial al final aquí **t**. Esto significa que todos pueden añadir archivos, escribir archivos y modificar archivos en el directorio `/tmp`, pero solo root puede eliminar el directorio `/tmp`.

### Modify sticky bit

```bash
sudo chmod +t mydir

sudo chmod 1755 mydir
```

La representación numérica para el sticky bit es **1**.

## Exercise

¿Qué otros archivos y directorios crees que tienen el sticky bit habilitado?

## Quiz Question

¿Qué símbolo representa el sticky bit?

## Quiz Answer

t
