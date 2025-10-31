---
index: 12
lang: "es"
title: "Enlaces simbólicos"
meta_title: "Enlaces simbólicos - El Sistema de Archivos"
meta_description: "Explora los enlaces simbólicos (symlinks) y enlaces duros de Linux. Aprende a crearlos con el comando ln, verificar el conteo de enlaces en Linux con ls, y entiende la diferencia en las salidas de ls para enlaces simbólicos y duros."
meta_keywords: "Enlaces simbólicos Linux, enlaces duros, comando ln, enlaces simbólicos, ls enlace simbólico, conteo de enlaces en linux, ls enlaces simbólicos, ls enlaces, sistema de archivos Linux, tutorial Linux"
---

## Lesson Content

Cuando lista archivos en detalle, ve mucha información. Veamos un ejemplo anterior de información de inodo del comando `ls -li`:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Anteriormente pasamos por alto el tercer campo en esta salida. Este campo es el recuento de enlaces.

### El Recuento de Enlaces en Linux

El **recuento de enlaces en linux** es el número total de enlaces físicos (hard links) que tiene un archivo. Para entender lo que esto significa, primero debemos discutir qué son los enlaces. En Linux, hay dos tipos de enlaces: enlaces simbólicos (symlinks) y enlaces físicos (hard links).

### Entendiendo los Symlinks

En el sistema operativo Windows, tiene accesos directos, que son esencialmente alias que apuntan a otros archivos. En Linux, el equivalente es un enlace simbólico, también conocido como enlace suave o **symlink**. Un symlink es un tipo especial de archivo que apunta a otro archivo o directorio por su nombre.

Veamos esto en la práctica. Crearemos algunos archivos y luego un symlink.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

Aquí, hemos creado un enlace simbólico llamado `myfilelink` que apunta a `myfile`. Cuando usa `ls` para ver un `ls symlink`, se identifica claramente por la `l` al principio de la cadena de permisos y el símbolo `->` que apunta al destino. Tenga en cuenta que el symlink tiene su propio número de inodo único (93403). Debido a que los symlinks apuntan a nombres de archivo en lugar de inodos, pueden abarcar diferentes sistemas de archivos.

### Entendiendo los Enlaces Físicos (Hard Links)

El otro tipo de enlace es un enlace físico. Un enlace físico crea otra entrada de archivo que apunta directamente al mismo inodo que el archivo original.

Creemos un enlace físico para `myfile2`:

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

Observe que `myhardlink` comparte el número de inodo exacto (93401) que `myfile2`. El recuento de enlaces para ambos archivos también ha aumentado a 2. Esto se debe a que dos entradas de archivo ahora apuntan al mismo inodo. Si modifica el contenido de `myfile2`, los cambios se reflejarán en `myhardlink`, y viceversa. Si elimina `myfile2`, los datos del archivo seguirán siendo accesibles a través de `myhardlink`. El inodo y sus datos solo se eliminan del disco cuando el recuento de enlaces llega a cero. Debido a que los enlaces físicos apuntan a inodos, que son únicos dentro de un solo sistema de archivos, no pueden abarcar diferentes sistemas de archivos.

### Creación de Symlinks y Enlaces Físicos

Puede crear ambos tipos de enlaces utilizando el comando `ln`. La sintaxis es sencilla.

Para crear un enlace simbólico, use la opción `-s`:

```bash
ln -s /ruta/al/original /ruta/al/enlace
```

Para crear un enlace físico, omita la opción `-s`:

```bash
ln /ruta/al/original /ruta/al/enlace
```

Usar los comandos `ls symlinks` o `ls links` generales con la opción `-l` es esencial para administrar e identificar estos diferentes tipos de archivos.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la administración de archivos, enlaces e inodos:

1. **[Administrar Archivos y Directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Practique la creación, copia, movimiento y eliminación de archivos y directorios, y aprenda específicamente sobre enlaces simbólicos y físicos, y cómo analizar inodos.
2. **[Navegar por el Sistema de Archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Domine comandos esenciales como `pwd`, `cd` y `ls` para moverse eficientemente por el sistema de archivos de Linux, una habilidad fundamental para comprender dónde residen los archivos y sus inodos.

Estos laboratorios le ayudarán a aplicar los conceptos de administración de archivos y enlaces en escenarios reales y a ganar confianza con el sistema de archivos de Linux.

## Quiz Question

¿Cuál es el comando y su opción principal utilizada para crear un symlink? Su respuesta debe estar en inglés y distingue entre mayúsculas y minúsculas. Por favor, incluya el espacio entre el comando y la opción.

## Quiz Answer

ln -s
