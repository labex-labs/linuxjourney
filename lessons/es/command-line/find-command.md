---
index: 14
lang: "es"
title: "find"
meta_title: "find - Command Line"
meta_description: "Aprende a usar el comando 'find' de Linux para localizar archivos y directorios. Descubre opciones básicas de búsqueda y mejora tus habilidades de gestión de archivos en Linux."
meta_keywords: "comando find de Linux, encontrar archivos Linux, búsqueda de directorios Linux, tutorial del comando find, gestión de archivos Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Con todos estos archivos que tenemos en el sistema, puede ser un poco caótico intentar encontrar uno específico. Bueno, ¡hay un comando que podemos usar para eso: `find`!

```bash
find /home -name puppies.jpg
```

Con `find`, tendrás que especificar el directorio en el que buscarás y lo que estás buscando. En este caso, estamos intentando encontrar un archivo con el nombre de `puppies.jpg`.

Puedes especificar qué tipo de archivo estás intentando encontrar.

```bash
find /home -type d -name MyFolder
```

Puedes ver que configuré el tipo de archivo que estoy intentando encontrar como `d` para directorio, y sigo buscando por el nombre de `MyFolder`.

Una cosa interesante a tener en cuenta es que `find` no se detiene en el directorio que estás buscando; también buscará dentro de cualquier subdirectorio que ese directorio pueda tener.

## Exercise

1. Find a file from the root directory that has the word "net" in it.

## Quiz Question

¿Qué opción debo especificar para `find` si quiero buscar por nombre?

## Quiz Answer

-name
