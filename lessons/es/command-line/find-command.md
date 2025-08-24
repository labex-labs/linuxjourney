---
index: 14
lang: "es"
title: "find"
meta_title: "find - Línea de Comandos"
meta_description: "Aprende a usar el comando 'find' de Linux para localizar archivos y directorios. Descubre opciones básicas de búsqueda y mejora tus habilidades de gestión de archivos en Linux."
meta_keywords: "comando find Linux, encontrar archivos Linux, búsqueda de directorios Linux, tutorial comando find, gestión de archivos Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

Con todos estos archivos que tenemos en el sistema, puede ser un poco agitado tratar de encontrar uno específico. Bueno, hay un comando que podemos usar para eso: `find`!

```bash
find /home -name puppies.jpg
```

Con `find`, tendrás que especificar el directorio en el que buscarás y lo que estás buscando. En este caso, estamos tratando de encontrar un archivo con el nombre de `puppies.jpg`.

Puedes especificar qué tipo de archivo estás tratando de encontrar.

```bash
find /home -type d -name MyFolder
```

Puedes ver que configuré el tipo de archivo que estoy tratando de encontrar como `d` para directorio, y sigo buscando por el nombre de `MyFolder`.

Una cosa genial a tener en cuenta es que `find` no se detiene en el directorio que estás buscando; también buscará dentro de cualquier subdirectorio que ese directorio pueda tener.

## Exercise

1. Encuentra un archivo desde el directorio raíz que contenga la palabra "net".

Para practicar con el comando `find`, prueba este laboratorio interactivo:

- [Linux find Command: File Searching](https://labex.io/es/labs/linux-linux-find-command-file-searching-219191)

## Quiz Question

¿Qué opción debo especificar para `find` si quiero buscar por nombre?

## Quiz Answer

-name
