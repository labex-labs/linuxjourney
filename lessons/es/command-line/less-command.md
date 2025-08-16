---
lang: "es"
title: "less"
description: "Aprenda a usar el comando 'less' de Linux para una visualización y navegación eficiente de archivos de texto. Domine la paginación, la búsqueda y la salida con esta guía para principiantes."
keywords: "comando less, Linux less, ver archivos de texto, navegar archivos, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

Si está viendo archivos de texto más grandes que una salida simple, `less` es más. (En realidad, hay un comando llamado `more` que hace algo similar, lo cual es irónico). El texto se muestra de forma paginada, por lo que puede navegar por un archivo de texto página por página.

Continúe y vea el contenido de un archivo con `less`. Una vez que esté en el comando `less`, puede usar otros comandos de teclado para navegar por el archivo.

```bash
less /home/pete/Documents/text1
```

Use los siguientes comandos para navegar por `less`:

- `q` - Se usa para salir de `less` y volver a su shell.
- `Page up`, `Page down`, `Up` y `Down` - Navegue usando las teclas de flecha y las teclas de página.
- `g` - Se mueve al principio del archivo de texto.
- `G` - Se mueve al final del archivo de texto.
- `/search` - Puede buscar texto específico dentro del documento de texto. Anteponga las palabras que desea buscar con `/`.
- `h` - Si necesita un poco de ayuda sobre cómo usar `less` mientras está en `less`, use help.

## Exercise

Ejecute `less` en un archivo, luego suba y baje por el archivo. Intente buscar una palabra específica. Navegue rápidamente al principio o al final del archivo.

## Quiz Question

¿Cómo se sale de un comando `less`?

## Quiz Answer

q
