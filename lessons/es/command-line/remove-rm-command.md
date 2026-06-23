---
index: 13
lang: "es"
title: "rm (Eliminar)"
meta_title: "rm (Eliminar) - Línea de Comandos"
meta_description: "Aprende el comando Linux rm con ejemplos seguros para eliminar archivos, borrar directorios, usar rm -r, rm -i y evitar errores con rm -rf."
meta_keywords: "comando linux rm, comando rm, rm -r, rm -i, rm -f, rm -rf, eliminar archivos linux, borrar directorio linux, rmdir"
---

## Lesson Content

En Linux, es común acumular archivos que ya no se necesitan. Para eliminarlos, se usa el comando `rm` (remove), una utilidad fundamental para gestionar tu sistema de archivos. La sintaxis básica es:

```bash
rm [OPTIONS] FILE...
```

El comando `rm` elimina entradas de directorio del sistema de archivos. En términos normales, borra archivos. A diferencia de muchos entornos de escritorio, la eliminación desde la línea de comandos usualmente no mueve los archivos a una papelera, por lo que debes revisar tu comando antes de presionar Enter.

### Eliminar un solo archivo

Para eliminar un archivo, pasa el nombre del archivo a `rm`.

```bash
$ rm file1
```

Puedes eliminar varios archivos a la vez listándolos uno tras otro.

```bash
$ rm notes.txt old-report.txt draft.md
```

Esto es útil para una limpieza rápida, pero también significa que un error tipográfico puede borrar más de lo que pretendías.

### Eliminar archivos con comodines

Los comodines del shell te permiten coincidir con varios archivos. Por ejemplo, esto elimina todos los archivos `.tmp` en el directorio actual:

```bash
$ rm *.tmp
```

Antes de usar `rm` con un comodín, es más seguro previsualizar la coincidencia con `ls`.

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

Recuerda que el shell expande `*.tmp` antes de que `rm` se ejecute. Si el patrón coincide con más archivos de los esperados, `rm` recibirá todos ellos.

### Eliminación interactiva con -i

Para un enfoque más seguro, usa la opción `-i`. Te pregunta antes de eliminar cada archivo.

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

Usa `rm -i` al eliminar archivos de un directorio compartido, limpiar muchos archivos o aprender el comando por primera vez.

### Eliminación forzada con -f

La opción `-f` significa "force" (forzar). Ignora archivos inexistentes y no solicita confirmación.

```bash
$ rm -f old-cache.txt
```

Esto es útil en scripts donde la limpieza debe continuar incluso si un archivo ya no existe.

```bash
$ rm -f build.log
```

Ten cuidado: `-f` también suprime algunas advertencias de seguridad, por lo que puede ocultar errores.

### Eliminar directorios con -r

Por defecto, `rm` no puede eliminar un directorio.

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

Para eliminar un directorio y todo su contenido, usa `-r` o `-R` para eliminación recursiva.

```bash
$ rm -r old-project
```

La eliminación recursiva recorre el árbol de directorios y elimina archivos, subdirectorios y su contenido.

### Los peligros de rm -rf

El comando `rm -rf` combina eliminación recursiva con eliminación forzada.

```bash
$ rm -rf old-project
```

Este comando puede ser apropiado para eliminar carpetas generadas como resultados de compilación, pero es peligroso porque elimina todo un árbol sin preguntar. Siempre verifica:

- ¿Estás en el directorio que crees? Usa `pwd`.
- ¿Tu comodín se expandió correctamente? Previsualiza con `ls`.
- ¿La ruta es absoluta o relativa? `/tmp/cache` y `tmp/cache` son muy diferentes.
- ¿Hay un espacio accidental? `rm -rf old-project` y `rm -rf old project` apuntan a rutas diferentes.

### Usar rmdir para directorios vacíos

Como alternativa más segura, elimina un directorio vacío con `rmdir`.

```bash
$ rmdir empty-directory
```

El comando `rmdir` solo tendrá éxito si el directorio está completamente vacío, lo que lo hace una opción más segura que `rm -r` para tareas de limpieza.

### Opciones comunes de rm

Aquí están las opciones que verás más a menudo:

- `-i`: Preguntar antes de cada eliminación.
- `-I`: Preguntar una vez antes de eliminar más de tres archivos o eliminar recursivamente.
- `-f`: Forzar eliminación e ignorar archivos inexistentes.
- `-r` o `-R`: Eliminar directorios y su contenido recursivamente.
- `-v`: Mostrar qué se eliminó.

Por ejemplo, puedes combinar opciones:

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

### Preguntas comunes

**¿Puedo deshacer rm?** Usualmente no. Una vez que un archivo se elimina con `rm`, no hay un comando incorporado para deshacer. Las copias de seguridad, el control de versiones y las herramientas de recuperación de sistema de archivos son la verdadera red de seguridad.

**¿Por qué rm dice "Permiso denegado"?** No tienes permiso para eliminar ese archivo o para modificar el directorio que lo contiene. Revisa la propiedad y permisos con `ls -l`.

**¿Por qué rm dice "No existe el archivo o directorio"?** El archivo no existe en esa ruta, o estás en un directorio diferente al que esperabas. Usa `pwd` y `ls` para confirmar.

**¿Debo usar sudo con rm?** Solo cuando entiendas completamente la ruta que estás eliminando. `sudo rm -r` puede eliminar archivos del sistema que tu cuenta de usuario normal no puede tocar.

## Exercise

Practice is key. Here are some hands-on exercises to solidify your understanding of file and directory removal in Linux:

1. **[Linux rm Command: File Removing](https://labex.io/es/labs/linux-linux-rm-command-file-removing-209741)** - Learn how to use the `rm` command for removing files and directories, including various options like `-r` and `-i`, and practice safe and effective file deletion.
2. **[Organizing Files and Directories](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills, including using the `rm` command to clean up unnecessary directories, in a practical challenge.

These labs will help you apply these concepts in real-world scenarios and build confidence with the `linux rm command`.

## Quiz Question

How do you remove a file named `myfile`? Your answer must be in English and use the exact, case-sensitive command.

## Quiz Answer

rm myfile
