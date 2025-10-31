---
index: 8
lang: "es"
title: "El Bit Pegajoso"
meta_title: "El Bit Pegajoso - Permisos"
meta_description: "Explore el propósito del bit pegajoso en los permisos de archivos de Linux y Unix. Aprenda cómo el bit pegajoso protege archivos en directorios compartidos como /tmp y cómo configurarlo usando chmod."
meta_keywords: "bit pegajoso, bit pegajoso linux, permisos de archivos unix bit pegajoso, chmod +t, directorio /tmp, permisos de archivos, seguridad linux"
---

## Lesson Content

Más allá de los permisos estándar de lectura, escritura y ejecución, Linux ofrece permisos especiales para un control de acceso avanzado. El último de estos permisos especiales que cubriremos es el **bit adhesivo** (sticky bit).

### ¿Qué es el Bit Adhesivo?

El bit adhesivo es una configuración de permiso que se puede aplicar a un directorio. Cuando se establece el bit adhesivo en un directorio, los archivos dentro de ese directorio solo pueden ser eliminados o renombrados por el propietario del archivo, el propietario del directorio o el usuario root. Esto es particularmente útil para directorios compartidos donde varios usuarios necesitan crear y administrar sus propios archivos sin interferir con los demás. Este concepto es una parte clave de la gestión del **permiso de archivo Unix sticky bit**.

### Un Ejemplo Práctico: El Directorio /tmp

Un caso de uso común para el **sticky bit en Linux** es el directorio `/tmp`, que es una ubicación escribible por todos para archivos temporales. Examinemos sus permisos:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

Observe la `t` al final de la cadena de permisos (`rwxrwxrwt`). Esta `t` indica que el bit adhesivo está establecido. Debido a esto, aunque cualquier usuario puede crear archivos en `/tmp`, no pueden eliminar ni mover archivos creados por otros usuarios. Esto evita que un usuario interrumpa el trabajo de otro en este espacio compartido.

### Cómo Establecer el Bit Adhesivo

Puede establecer el bit adhesivo usando el comando `chmod` de dos maneras: modo simbólico o modo octal (numérico).

Para agregar el bit adhesivo usando el modo simbólico:

```bash
chmod +t mi_dir_compartido
```

Para establecer permisos usando el modo octal, antepone un `1` al código de permiso estándar de tres dígitos. La representación numérica para el bit adhesivo es **1**.

```bash
# Esto establece los permisos a rwxr-xr-x con el bit adhesivo
chmod 1755 mi_dir_compartido
```

Comprender el bit adhesivo es esencial para administrar entornos multiusuario y asegurar directorios compartidos de manera efectiva.

## Exercise

Para solidificar su comprensión de los permisos de archivos, incluidos los permisos especiales como el bit adhesivo, pruebe estos laboratorios prácticos. Le ayudarán a ver cómo se aplican estos conceptos en escenarios del mundo real.

1.  **[Grupo de Usuarios de Linux y Permisos de Archivos](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Practique la creación de usuarios y grupos, y la manipulación de la propiedad y los permisos de los archivos. Este laboratorio proporciona una base para comprender cómo funcionan los permisos especiales.
2.  **[Eliminar y Mover Archivos](https://labex.io/es/labs/linux-delete-and-move-files-7777)** - Aprenda a eliminar y mover archivos, y vea cómo los permisos, incluido el bit adhesivo en un directorio, pueden restringir estas acciones.
3.  **[Encontrar un Archivo](https://labex.io/es/labs/linux-find-a-file-17993)** - Practique la localización de archivos y el establecimiento de controles de acceso, reforzando la importancia de los permisos de archivos en la gestión del acceso y modificación de archivos.

## Quiz Question

En una lista de directorios larga (ls -l), ¿qué carácter único en la cadena de permisos representa que el bit adhesivo está establecido? Por favor, responda con una sola letra minúscula en inglés.

## Quiz Answer

t
