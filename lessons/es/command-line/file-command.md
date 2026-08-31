---
lesson_id: "file-command"
course_id: "command-line"
lang: "es"
order_index: 6
title: "file"
description: "Aprende a identificar el tipo de contenido probable de un archivo sin depender de su nombre o extensión."
meta_title: "file - Línea de Comandos"
meta_description: "Aprende el comando file en Linux con ejemplos para identificar archivos de texto, imágenes, scripts, archivos comprimidos, binarios y tipos MIME."
meta_keywords: "comando linux file, comando file, identificar tipo de archivo linux, tipo mime linux, archivo de texto, archivo binario, archivo comprimido"
---

En la lección anterior utilizaste `touch` para crear un archivo sin añadirle una extensión. En Linux, los nombres de archivo no tienen por qué describir su contenido: un archivo llamado `funny.gif` no es necesariamente una imagen GIF.

Utiliza la orden `file` para inspeccionar un archivo e informar de su tipo probable:

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## Por qué las extensiones de archivo no bastan

Las herramientas de Linux normalmente no necesitan una extensión para determinar el tipo de un archivo. Un script de shell puede llamarse `backup`, un archivo de texto puede llamarse `README` y una imagen puede tener una extensión engañosa. La orden `file` examina propiedades como los metadatos del sistema de archivos y patrones reconocibles del contenido.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

El resultado es una clasificación, no una garantía. Un archivo poco común, incompleto o dañado puede recibir una descripción general como `data` en vez de un tipo preciso.

:::single-choice{#identify-misleading-extension}
Un archivo llamado `report.jpg` podría no contener una imagen. ¿Qué orden comprueba su tipo de contenido probable?

::option[`ls report.jpg`]{#list-report explanation="`ls` confirma que el nombre existe y puede mostrar metadatos, pero no clasifica el contenido del archivo."}
::option[`file report.jpg`]{#inspect-report .correct explanation="La orden `file` examina el archivo e informa de un tipo probable. No se basa únicamente en el sufijo `.jpg`."}
::option[`touch report.jpg`]{#touch-report explanation="`touch` actualiza marcas de tiempo o crea un archivo ausente. No identifica el tipo de contenido."}
:::

## Comprobación de varios archivos

Puedes comprobar varios archivos a la vez:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

También puedes pasar un comodín de la shell. La shell expande `*` a los nombres coincidentes antes de que `file` los examine:

```bash
$ file *
```

:::single-choice{#inspect-multiple-files}
¿Qué orden pide a `file` que inspeccione todos los nombres no ocultos del directorio actual que coincidan con `*`?

::option[`file *`]{#file-wildcard .correct explanation="La shell expande `*` a los nombres no ocultos que coincidan y `file` inspecciona cada operando resultante."}
::option[`file .`]{#file-current-directory explanation="Un solo punto representa el directorio actual. Esta orden clasifica ese directorio en vez de cada elemento que contiene."}
::option[`file -b`]{#file-brief-no-operand explanation="La opción `-b` cambia el formato de salida, pero esta orden no proporciona ningún archivo que inspeccionar."}
:::

## Visualización de información MIME

La opción `-i` muestra información al estilo MIME, incluido un tipo de medio y, cuando está disponible, un juego de caracteres. Este formato resulta útil cuando otro programa espera valores como `text/html`.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information}
¿Qué orden muestra información al estilo MIME para `index.html`?

::option[`file -b index.html`]{#brief-index explanation="La opción `-b` omite el nombre del archivo en la descripción habitual. No solicita específicamente una salida al estilo MIME."}
::option[`file -i index.html`]{#mime-index .correct explanation="La opción `-i` solicita una salida al estilo MIME, como `text/html` junto con la información del juego de caracteres."}
::option[`file -L index.html`]{#follow-index explanation="La opción `-L` controla el tratamiento de los enlaces simbólicos. No selecciona el formato de salida MIME."}
:::

## Opciones útiles de file

- `-i`: Muestra información al estilo MIME.
- `-b`: Utiliza el modo breve y omite el nombre del archivo en la salida.
- `-L`: Sigue los enlaces simbólicos y clasifica sus destinos.
- `-z`: Intenta examinar el contenido de archivos comprimidos.

Por ejemplo:

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output}
¿Qué orden clasifica `notes.txt`, pero omite su nombre en la salida?

::option[`file -i notes.txt`]{#mime-notes explanation="La opción `-i` solicita información al estilo MIME. Normalmente la salida sigue incluyendo el nombre del archivo."}
::option[`file -z notes.txt`]{#compressed-notes explanation="La opción `-z` pide a `file` que examine los datos comprimidos cuando sea posible. No activa la salida breve."}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="El modo breve, seleccionado con `-b`, muestra la clasificación sin el prefijo del nombre de archivo."}
:::

## Resumen

Ahora puedes utilizar `file` para investigar qué es probable que contenga un archivo.

1. Clasificar un archivo sin confiar en su extensión.
2. Inspeccionar varias rutas con una sola orden.
3. Solicitar información al estilo MIME.
4. Ajustar el tratamiento de enlaces, datos comprimidos y etiquetas de salida.
