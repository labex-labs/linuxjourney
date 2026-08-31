---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "es"
order_index: 11
title: "mv (Mover)"
description: "Aprende a renombrar y mover archivos o directorios evitando sobrescrituras involuntarias."
meta_title: "mv (Mover) - Línea de Comandos"
meta_description: "Aprende el comando mv de Linux con ejemplos para mover archivos, renombrar archivos y directorios, mover múltiples archivos y evitar sobrescrituras."
meta_keywords: "comando linux mv, comando mv, mover archivos linux, renombrar archivo linux, renombrar directorio linux, mv -i, mv -n, mv -t"
---

El comando `mv`, abreviatura de "mover", es una utilidad fundamental en cualquier entorno Linux. Sirve para dos propósitos principales: renombrar archivos o directorios y moverlos a una ubicación diferente.

La sintaxis básica es:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

A diferencia de `cp`, que crea una copia, `mv` cambia dónde se encuentra el elemento original o cómo se llama.

## Cambio de nombre de archivos y directorios

Uno de los usos más comunes de `mv` es renombrar. La sintaxis es sencilla: especifica el nombre antiguo y el nuevo nombre.

Para renombrar un archivo:

```bash
$ mv oldfile newfile
```

Esta misma lógica se aplica para renombrar directorios:

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv}
¿Qué orden cambia el nombre de `cat` a `dog` en el directorio actual?

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` trata `cat` como la ruta de origen y `dog` como su nueva ruta de destino."}
::option[`mv dog cat`]{#rename-dog explanation="El orden de los operandos está invertido. Esta orden intentaría cambiar el nombre de un `dog` existente a `cat`."}
::option[`cp cat dog`]{#copy-cat explanation="`cp` crearía una copia llamada `dog` y conservaría `cat`. No realizaría el cambio de nombre solicitado."}
:::

## Traslado de elementos a un directorio

La otra función principal del comando `mv` es mover elementos de una ubicación a otra.

Para mover un solo archivo a un directorio diferente:

```bash
$ mv file2 /home/pete/Documents
```

También puedes mover múltiples archivos a la vez. Simplemente lista todos los archivos origen seguidos del directorio destino:

```bash
$ mv file_1 file_2 somedirectory/
```

En sistemas GNU/Linux, una opción útil para esto es `-t`, que permite especificar primero el directorio destino. Esto puede ser más claro al mover muchos archivos.

```bash
$ mv -t somedirectory/ file_1 file_2
```

A diferencia del comando `cp`, no necesitas una opción recursiva para mover un directorio. `mv` maneja directorios por defecto.

:::single-choice{#move-multiple-files}
¿Qué orden mueve `file_1` y `file_2` al directorio existente `archive/`?

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="Sin la opción GNU `-t`, un traslado con varios orígenes espera el directorio de destino al final. Este no es el orden estándar."}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` no utiliza `-r` para mover archivos o directorios. La forma normal con varios orígenes ya realiza el traslado solicitado."}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="Con varios orígenes, el directorio de destino existente es el último operando y recibe ambos archivos."}
:::

## Control de destinos existentes

De forma predeterminada, `mv` puede sustituir un destino existente. Inspecciona las rutas de origen y destino antes de ejecutar el traslado y elige una política de sobrescritura cuando sea necesario:

- `-i`: pide confirmación antes de sustituir un destino existente.

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n`: no sobrescribe un destino existente.

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b`: en GNU/Linux, crea una copia de seguridad del destino que se sustituiría. El sufijo predeterminado suele ser `~`.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v`: muestra cada traslado a medida que ocurre.

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting}
¿Qué orden mueve `draft.txt` a `finished/` únicamente si no sobrescribe un destino existente?

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="La opción `-i` pregunta qué hacer si existe el destino. Aun así podría sobrescribirse si el usuario lo confirma."}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="La opción `-b` permite sustituir el destino y conserva una copia de seguridad del anterior. No evita la sobrescritura."}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="La opción `-n` omite cualquier traslado que sobrescribiría un destino existente."}
:::

## Traslado de directorios y coincidencias de comodines

Puedes mover un directorio sin `-r`:

```bash
$ mv project /home/pete/Documents/
```

Los comodines de la shell pueden seleccionar varios orígenes:

```bash
$ ls *.txt
$ mv *.txt notes/
```

Previsualiza las coincidencias de comodines con `ls` antes de mover muchos archivos.

:::single-choice{#move-directory-without-recursion}
¿Qué orden mueve el directorio `project/` a `/srv/archive/`?

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv` no necesita ni admite `-r` para este propósito. Los directorios se tratan mediante la operación normal de traslado."}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="La sintaxis normal de `mv` mueve un directorio a un directorio de destino existente sin ninguna opción recursiva."}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="Un `cp` sencillo no mueve el directorio y necesitaría una opción recursiva para copiarlo. Además, el original permanecería en su lugar."}
:::

:::single-choice{#preview-text-file-move}
Planeas ejecutar `mv *.txt notes/`. ¿Qué orden previsualiza las rutas seleccionadas por el mismo comodín?

::option[`ls '*.txt'`]{#literal-text-pattern explanation="Las comillas impiden que la shell expanda `*`, por lo que esta orden busca un nombre literal con un asterisco en vez de previsualizar los elementos."}
::option[`ls *.txt`]{#list-text-matches .correct explanation="La shell expande `*.txt` para `ls` igual que lo haría para `mv`, lo que permite examinar primero los nombres no ocultos seleccionados."}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="El modo detallado informa de los traslados mientras se realizan. Ejecuta la operación, no ofrece una previsualización de solo lectura."}
:::

Para practicar el traslado y cambio de nombre de elementos, prueba estos laboratorios:

1. **[Comando Linux mv: Mover y Renombrar Archivos](https://labex.io/es/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Practica usando el comando `mv` para mover y renombrar archivos y directorios, incluyendo la comprensión de sus diversas opciones y comportamientos.
2. **[Organización de Archivos y Directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Aplica tu conocimiento de `mv` (junto con `cp` y `rm`) en un desafío práctico para organizar la estructura de un proyecto, mover archivos y limpiar directorios.

## Resumen

Ahora puedes renombrar y mover archivos o directorios protegiendo los destinos existentes.

1. Colocar el origen antes de su nueva ruta.
2. Situar el directorio de destino después de varios orígenes.
3. Preguntar, omitir o crear una copia de seguridad antes de sustituir un destino.
4. Mover directorios sin una opción recursiva.
5. Previsualizar las coincidencias de comodines antes de un traslado masivo.
