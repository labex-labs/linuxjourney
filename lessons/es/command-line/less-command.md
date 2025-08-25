---
index: 8
lang: "es"
title: "less"
meta_title: "less - Línea de Comandos"
meta_description: "Aprenda a usar el comando 'less' de Linux para una visualización y navegación eficiente de archivos de texto. Domine la paginación, la búsqueda y la salida con esta guía para principiantes."
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

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la visualización y navegación de archivos de texto en Linux:

1. **[Comando Linux less: Paginación de archivos](https://labex.io/es/labs/linux-linux-less-command-file-paging-214301)** - Aprenda el comando 'less' de Linux para una visualización y navegación eficiente de archivos de texto, incluyendo búsqueda, números de línea y coincidencia de patrones.
2. **[Comando Linux more: Desplazamiento de archivos](https://labex.io/es/labs/linux-linux-more-command-file-scrolling-214299)** - Aprenda el comando 'more' de Linux para una visualización eficiente de archivos de texto, cubriendo el uso básico, comenzando desde líneas específicas y personalizando la visualización.
3. **[Visualización de archivos de registro y configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Aprenda habilidades esenciales de línea de comandos de Linux para ver y navegar eficientemente archivos de texto, incluyendo registros del sistema y archivos de configuración, usando comandos como `cat`, `more` y `less`.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la manipulación y navegación de archivos de texto.

## Quiz Question

¿Cómo se sale de un comando `less`?

## Quiz Answer

q
