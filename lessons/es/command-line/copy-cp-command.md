---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "es"
order_index: 10
title: "cp (Copiar)"
description: "Aprende a copiar archivos y árboles de directorios controlando las sobrescrituras y los atributos conservados."
meta_title: "cp (Copiar) - Línea de Comandos"
meta_description: "Aprende el comando cp de Linux con ejemplos para copiar archivos, directorios, múltiples archivos, comodines, copias de seguridad y opciones como cp -r, cp -i y cp -p."
meta_keywords: "comando linux cp, comando cp, copiar archivos linux, cp -r, cp -i, cp -p, cp -a, cp -u, copia recursiva, comodines linux"
---

El comando `cp` es la herramienta estándar para copiar archivos y directorios en Linux. Crea una nueva copia dejando el archivo original en su lugar. Su sintaxis básica es:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Puedes copiar un archivo a otro archivo, uno o más archivos a un directorio, o un árbol completo de directorios con la opción adecuada.

## Copia de un archivo

Para copiar un archivo, especificas el archivo fuente y el directorio o ruta de destino.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

En este ejemplo, `mycoolfile` es el archivo fuente, y `/home/pete/Documents/cooldocs` es el directorio de destino. También puedes copiar un archivo y darle un nuevo nombre en el destino.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

Si el destino es un directorio existente, el archivo copiado mantiene su nombre original. Si el destino es un nombre de archivo, `cp` crea una copia con ese nuevo nombre.

:::single-choice{#copy-file-under-new-name} ¿Qué orden copia `draft.txt` en un archivo llamado `final.txt` y conserva `draft.txt`?

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv` cambia el nombre o mueve la ruta original. No deja en su lugar la copia de origen solicitada."}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="Aquí se han invertido el origen y el destino. Esta orden copiaría `final.txt` sobre `draft.txt`."}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp` lee `draft.txt` y crea o sustituye `final.txt`, mientras que el origen sigue disponible."}
:::

## Copia de varios archivos en un directorio

Para copiar varios archivos al mismo directorio, lista todas las fuentes primero y coloca el directorio de destino al final.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

El último argumento debe ser un directorio cuando proporcionas más de una fuente.

:::single-choice{#copy-multiple-files} ¿Qué orden copia `a.txt` y `b.txt` en el directorio existente `archive/`?

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="En esta forma de `cp`, el directorio de destino debe situarse al final. Colocarlo primero cambia la interpretación de los operandos."}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="Con varios orígenes, `cp` trata el último directorio existente como destino de todos los archivos anteriores."}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="Todos los operandos de origen deben aparecer antes del destino. El directorio existente debe ser el último operando."}
:::

## Selección de archivos con comodines

Los comodines son caracteres especiales que te ayudan a seleccionar múltiples archivos basados en patrones, proporcionando gran flexibilidad.

- `*`: Coincide con cualquier secuencia de caracteres.
- `?`: Coincide con cualquier carácter individual.
- `[]`: Coincide con cualquiera de los caracteres encerrados en los corchetes.

Por ejemplo, para copiar todas las imágenes JPEG desde tu ubicación actual al directorio `Pictures`:

```bash
$ cp *.jpg /home/pete/Pictures
```

Puedes previsualizar los archivos que coinciden antes de copiar:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern} Antes de copiar `*.jpg`, ¿qué orden muestra los nombres no ocultos que coinciden actualmente con el patrón?

::option[`cp *.jpg`]{#copy-no-destination explanation="Esta orden intenta copiar sin un destino claro cuando coinciden varios nombres. No es una operación de previsualización."}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="La shell expande el mismo patrón para `ls`, lo que te permite examinar los nombres coincidentes antes de copiarlos."}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="Las comillas impiden expandir el comodín, así que `file` recibe los caracteres literales `*.jpg`. No muestra las coincidencias normales."}
:::

## Copia de árboles de directorios

Si intentas copiar un directorio usando `cp` sin opciones, recibirás un error. Para copiar un directorio y todo su contenido, incluidos subdirectorios, debes usar la bandera `-r` (recursiva).

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Este comando copia el directorio `Pumpkin` y todo lo que contiene a tu directorio `Documents`.

También puedes ver `-R`, que tiene el mismo propósito recursivo en sistemas Linux típicos:

```bash
$ cp -R website /home/pete/backups/
```

El modo de archivo, `-a`, resulta útil para copias de seguridad. Copia de forma recursiva y conserva los enlaces y muchos atributos:

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree} Quieres una copia recursiva de `project/` al estilo de una copia de seguridad que conserve enlaces y numerosos atributos. ¿Qué orden cumple el objetivo?

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p` conserva ciertos atributos, pero por sí sola no hace que la copia de un directorio sea recursiva."}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u` controla cuándo se copian los archivos según el estado del destino. No activa por sí sola la copia recursiva de directorios."}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="El modo de archivo incluye la copia recursiva y conserva enlaces y un amplio conjunto de atributos para obtener un resultado adecuado como respaldo."}
:::

## Control de las sobrescrituras

Por defecto, `cp` sobrescribirá un archivo en el destino si tiene el mismo nombre. Para evitar la pérdida accidental de datos, usa la bandera `-i` (interactiva), que solicita confirmación antes de sobrescribir.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Otra opción de seguridad útil es `-n`, que significa "no sobrescribir". Evita sobrescribir un archivo existente en el destino.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

La opción `-f` indica a GNU `cp` que intente eliminar un destino existente cuando no pueda abrirlo para escribir y que vuelva a intentar la copia. No sustituye la comprobación cuidadosa de los destinos. Los alias de la shell también pueden añadir opciones como `-i`, así que investiga cualquier prompt inesperado en vez de suponer una configuración concreta.

:::single-choice{#skip-existing-destination} ¿Qué orden copia `report.txt` en `backup/`, pero omite un destino existente con el mismo nombre?

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="La opción `-n` impide que `cp` sobrescriba un archivo de destino existente."}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i` pregunta antes de sobrescribir, por lo que el resultado depende de la respuesta. No omite automáticamente todos los destinos existentes."}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f` puede ayudar a sustituir un destino que inicialmente no puede abrirse. No ofrece un comportamiento de no sobrescritura."}
:::

## Conservación o actualización de archivos

Cuando copias un archivo, sus metadatos, como la hora de modificación y la propiedad, normalmente se actualizan. Para preservar estos atributos originales, usa la opción `-p`.

La opción `cp -p` es particularmente útil para copias de seguridad o cuando migras archivos donde preservar las marcas de tiempo es importante.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Esto copia `mycoolfile` preservando su modo, propiedad donde sea posible, y marcas de tiempo.

La opción `-u` copia solo cuando el archivo fuente es más nuevo que el archivo destino o cuando el archivo destino no existe.

```bash
$ cp -u *.txt /home/pete/Documents/
```

Esto es útil cuando actualizas una carpeta sin reescribir archivos que ya están al día.

Otras opciones habituales son `-f`, que intenta forzar la sustitución del destino, y `-v`, que muestra cada archivo a medida que se copia.

Para practicar la copia de archivos y árboles de directorios, prueba estos laboratorios:

1. **[Orden cp de Linux: copiar archivos](https://labex.io/es/labs/linux-linux-cp-command-file-copying-209744)** - Practica el uso básico, la copia recursiva, la conservación de atributos y los comodines para copiar archivos y directorios con eficacia.
2. **[Organización de archivos y directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practica la gestión de archivos con `cp`, `mv` y `rm` para organizar un proyecto y limpiar elementos innecesarios.

## Resumen

Ahora puedes copiar archivos y árboles de directorios mientras controlas el tratamiento de los destinos.

1. Colocar los operandos de origen antes del destino.
2. Previsualizar las coincidencias de comodines antes de una copia masiva.
3. Copiar árboles de directorios de forma recursiva o en modo de archivo.
4. Confirmar, omitir o sustituir deliberadamente destinos existentes.
5. Conservar atributos o copiar solo orígenes más recientes cuando sea necesario.
