---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "es"
order_index: 4
title: "ls (Listar directorios)"
description: "Aprende a usar las opciones de `ls` para inspeccionar archivos, elementos ocultos, detalles, tamaños y criterios de ordenación."
meta_title: "ls (Listar Directorios) - Línea de Comandos"
meta_description: "Aprende el comando Linux ls con ejemplos para listar archivos, archivos ocultos, salida en formato largo, tamaños legibles, ordenamiento y combinación de opciones."
meta_keywords: "comando ls, linux ls, listar archivos linux, listar directorios, ls -a, ls -l, ls -lh, ls -r, archivos ocultos"
---

Ahora que sabemos cómo movernos por el sistema de archivos, ¿cómo descubrimos qué está disponible para nosotros? El comando `ls` lista archivos y directorios para que puedas inspeccionar tu ubicación actual o una ruta diferente.

## Uso básico de la orden ls

Por defecto, el comando `ls` listará los directorios y archivos en tu directorio actual. Sin embargo, también puedes especificar una ruta para listar el contenido de otro directorio.

```bash
$ ls
$ ls /home/pete
```

También puedes listar un archivo específico:

```bash
$ ls /etc/hosts
/etc/hosts
```

:::single-choice{#list-another-directory} ¿Qué orden muestra el contenido de `/home/pete` sin cambiar a ese directorio?

::option[`ls /home/pete`]{#ls-target-path .correct explanation="Al pasar una ruta de directorio a `ls`, se muestra su contenido. La shell permanece en su directorio de trabajo actual."}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd` cambia el directorio de trabajo de la shell. Por sí sola no realiza la enumeración solicitada."}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd` informa del directorio de trabajo actual y no acepta un destino que deba enumerar. Utiliza `ls` con la ruta."}
:::

## Visualización de archivos ocultos

No todos los archivos en un directorio son visibles por defecto. En Linux, los nombres de archivo que comienzan con un punto (`.`) están ocultos. Puedes verlos con la opción `-a`, que significa todos.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

Los archivos cuyos nombres empiezan por punto están ocultos de forma predeterminada y suelen guardar configuraciones, como `.bashrc`.

:::single-choice{#show-hidden-files} ¿Qué orden incluye los archivos ocultos en la lista?

::option[`ls -l`]{#long-format explanation="La opción `-l` añade columnas detalladas, pero no incluye por sí sola los nombres ocultos."}
::option[`ls -r`]{#reverse-order explanation="La opción `-r` invierte el orden. No cambia si se incluyen o no los archivos ocultos."}
::option[`ls -a`]{#all-files .correct explanation="La opción `-a` significa «todos», por lo que `ls` incluye los nombres que comienzan con un punto."}
:::

## Obtención de información detallada

Otra opción esencial de `ls` es `-l` para formato largo. Muestra permisos de archivo, número de enlaces, propietario, grupo, tamaño, hora de modificación y nombre.

```bash
$ ls -l
```

Aquí hay un ejemplo de la salida:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

Para tamaños de archivo más fáciles de leer, añade `-h` para salida legible para humanos:

```bash
$ ls -lh
```

:::single-choice{#show-readable-file-details} ¿Qué orden muestra detalles en formato largo con tamaños fáciles de leer?

::option[`ls -la`]{#long-all explanation="Esta orden combina el formato largo con los archivos ocultos. No solicita unidades de tamaño fáciles de leer."}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l` selecciona el formato largo y `-h` facilita la lectura de los tamaños. Las dos opciones pueden combinarse en una sola orden."}
::option[`ls -ltr`]{#long-time-reverse explanation="Esta orden combina formato largo, ordenación por fecha de modificación y orden inverso. No incluye la opción de tamaño `-h`."}
:::

## Ordenación inversa

A veces puedes querer cambiar el orden de clasificación. La opción `-r` lista archivos y directorios en orden inverso.

```bash
$ ls -r
```

Puedes ordenar por tiempo de modificación con `-t`, luego invertirlo con `-r`:

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last} ¿Qué orden clasifica por fecha de modificación y coloca al final los elementos más recientes?

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t` clasifica por fecha de modificación y `-r` invierte ese orden. Juntas colocan los elementos antiguos antes que los nuevos."}
::option[`ls -lt`]{#time-default explanation="Esta orden clasifica por fecha de modificación, pero mantiene el orden predeterminado con los más recientes primero."}
::option[`ls -lr`]{#reverse-name-order explanation="Esta orden usa el formato largo e invierte la clasificación predeterminada por nombre. Sin `-t`, la fecha de modificación no controla el orden."}
:::

## Combinación de opciones

Los comandos tienen flags, también llamados opciones, para añadir más funcionalidad. Como vimos con `-a` y `-l`, puedes combinarlos en un solo comando como `ls -la`. El orden de los flags a menudo no importa, así que `ls -al` funciona igual.

```bash
$ ls -la
```

Combinaciones útiles incluyen:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

## Opciones habituales de ls

- `-a`: Muestra todos los archivos, incluidos los ocultos.
- `-l`: Usa formato largo.
- `-h`: Muestra tamaños legibles para humanos con `-l`.
- `-r`: Invierte el orden de clasificación.
- `-t`: Ordena por tiempo de modificación.
- `-S`: Ordena por tamaño de archivo.
- `-d`: Lista el directorio en sí en lugar de su contenido.

:::single-choice{#list-directory-entry-itself} ¿Qué orden muestra la entrada del directorio `projects/` en vez de su contenido?

::option[`ls -d projects/`]{#directory-entry .correct explanation="La opción `-d` indica a `ls` que muestre la entrada del directorio en vez de abrirlo para enumerar su contenido."}
::option[`ls projects/`]{#directory-contents explanation="Sin `-d`, pasar una ruta de directorio hace que `ls` muestre los elementos que contiene."}
::option[`cd projects/`]{#change-to-directory explanation="`cd` cambia el directorio de trabajo. No muestra la entrada de directorio solicitada."}
:::

Algunos sistemas muestran la salida de `ls` con colores diferentes según el tipo de archivo. Este comportamiento suele proceder de un alias o una variable de entorno, por lo que los colores pueden variar de un sistema a otro.

Para reforzar tu comprensión de la orden `ls`, prueba este laboratorio práctico:

- **[Orden ls de Linux: enumerar contenido](https://labex.io/es/labs/linux-linux-ls-command-content-listing-219205)** - Practica el uso de `ls` para enumerar y analizar archivos y directorios. Aprenderás a obtener listas detalladas, mostrar archivos ocultos, usar tamaños legibles y aplicar distintos criterios de ordenación.

## Resumen

Ahora puedes utilizar `ls` para inspeccionar el contenido de los directorios y controlar cómo se muestran los elementos.

1. Enumerar el directorio actual u otra ruta.
2. Incluir archivos ocultos en una lista.
3. Mostrar información detallada con tamaños fáciles de leer.
4. Ordenar de forma inversa por fecha de modificación.
5. Mostrar la entrada de un directorio sin enumerar su contenido.
