---
index: 8
lang: "es"
title: "less"
meta_title: "less - Línea de Comandos"
meta_description: "Aprenda a usar el comando 'less' de Linux para una visualización y navegación eficientes de archivos de texto. Domine la paginación, la búsqueda y la salida con esta guía para principiantes."
meta_keywords: "comando less, Linux less, ver archivos de texto, navegar archivos, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Si está viendo archivos de texto más grandes que una simple salida, `less` es más. (En realidad, hay un comando llamado `more` que hace algo similar, lo cual es irónico). El texto se muestra de forma paginada, por lo que puede navegar por un archivo de texto página por página.

Continúe y vea el contenido de un archivo con `less`. Una vez que esté en el comando `less`, puede usar otros comandos de teclado para navegar por el archivo.

```bash
less /home/pete/Documents/text1
```

Utilice los siguientes comandos para navegar por `less`:

- `q` - Se utiliza para salir de `less` y volver a su shell.
- `Page up`, `Page down`, `Up` y `Down` - Navegue usando las teclas de flecha y las teclas de página.
- `g` - Se mueve al principio del archivo de texto.
- `G` - Se mueve al final del archivo de texto.
- `/search` - Puede buscar texto específico dentro del documento de texto. Anteponga las palabras que desea buscar con `/`.
- `h` - Si necesita un poco de ayuda sobre cómo usar `less` mientras está en `less`, use la ayuda.

## Exercise

Ejecute `less` en un archivo, luego suba y baje por el archivo. Intente buscar una palabra específica. Navegue rápidamente al principio o al final del archivo.

Para practicar con el comando `less`, pruebe este laboratorio interactivo:

- [Linux less Command: File Paging](https://labex.io/es/labs/linux-linux-less-command-file-paging-214301)

## Quiz Question

¿Cómo se sale de un comando `less`?

## Quiz Answer

q
