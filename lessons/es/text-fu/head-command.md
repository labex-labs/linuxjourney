---
lesson_id: "head-command"
course_id: "text-fu"
lang: "es"
order_index: 8
title: "head"
description: "Aprende a mostrar una cantidad controlada de líneas o bytes del principio de una entrada."
meta_title: "head - Text-Fu"
meta_description: "Guía de Linux para principiantes sobre el uso del comando head para ver el inicio de un archivo. Aprenda a usar la opción head -n para controlar el número de líneas, una habilidad esencial para cualquier tutorial de Linux."
meta_keywords: "comando head, Linux head, ver inicio archivo, tutorial Linux, comandos Linux, Linux principiantes, head -n, guía Linux, archivos de texto, línea de comandos"
---

La orden `head` muestra el principio de un archivo o flujo de entrada. Resulta útil para comprobar encabezados, previsualizar datos estructurados o tomar una muestra de la salida sin imprimirla por completo.

## Visualización de las primeras diez líneas

Sin una opción de cantidad, `head` muestra las primeras 10 líneas de cada archivo indicado:

```bash
$ head events.log
```

El archivo no se modifica. Si contiene menos de 10 líneas, se muestran todas las disponibles.

:::single-choice{#head-default-lines} ¿Qué muestra `head events.log` de forma predeterminada?

::option[Las últimas 10 líneas, o todas si el archivo es más corto.]{#head-last-ten explanation="Mostrar el final de la entrada es la función de `tail`. `head` selecciona desde el principio."}
::option[Las primeras 10 líneas, o todas si el archivo es más corto.]{#head-first-ten .correct explanation="Sin una opción de cantidad, `head` selecciona como máximo las primeras diez líneas de la entrada."}
::option[Únicamente la primera línea, sin importar la longitud.]{#head-first-one explanation="Para mostrar una línea se necesita una cantidad explícita como `-n 1`; la cantidad predeterminada es diez."}
:::

## Elección de una cantidad de líneas

Utiliza `-n NUMBER` para elegir cuántas líneas mostrar:

```bash
$ head -n 15 events.log
```

GNU `head` también acepta la forma compacta `-15`, pero `-n 15` expresa con mayor claridad el significado de la opción.

:::single-choice{#head-five-lines} ¿Qué orden muestra las primeras cinco líneas de `report.txt`?

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="La opción `-c` cuenta bytes en vez de líneas, por lo que podría detenerse en mitad de la primera línea."}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="La opción `-n` selecciona una cantidad de líneas y `5` solicita las primeras cinco."}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="Esta orden muestra las últimas cinco líneas del archivo, no el principio."}
:::

## Elección de una cantidad de bytes

Utiliza `-c NUMBER` cuando necesites bytes en vez de líneas completas:

```bash
$ head -c 20 archive.bin
```

Esta orden muestra los primeros 20 bytes. La salida puede terminar en mitad de una línea de texto o, en textos multibyte, en mitad de un carácter codificado. Para previsualizar texto normal, utiliza el modo de líneas.

:::single-choice{#head-first-bytes} ¿Qué orden escribe en stdout los primeros 100 bytes de `payload.bin`?

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="La opción `-c` selecciona una cantidad de bytes, por lo que se solicitan los primeros 100 bytes disponibles."}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="La opción `-n` cuenta líneas, no bytes. Podría producir muchos más o muchos menos de 100 bytes."}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="Esta orden selecciona la posición 100 de cada línea, no los primeros 100 bytes de toda la entrada."}
:::

## Lectura de stdin y de varios archivos

Cuando no se indica un archivo, `head` lee stdin:

```bash
$ generate-report | head -n 5
```

Cuando se indican varios archivos, `head` suele añadir un encabezado que identifica la salida de cada uno:

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

Utiliza `-q` para suprimir estos encabezados o `-v` para mostrar uno incluso con un solo archivo.

:::single-choice{#head-pipeline-preview} En `generate-report | head -n 5`, ¿qué lee `head`?

::option[Stdout de `generate-report` a través de stdin.]{#head-pipe-input .correct explanation="La tubería conecta stdout del productor con stdin de `head`, que selecciona las primeras cinco líneas."}
::option[Los primeros cinco nombres de archivo del directorio actual.]{#head-directory-names explanation="No interviene ninguna orden que enumere el directorio. `head` recibe un flujo por la tubería."}
::option[Cinco bytes de un archivo llamado `generate-report`.]{#head-producer-file explanation="La parte izquierda se ejecuta como una orden y `-n` cuenta líneas, no bytes."}
:::

:::single-choice{#head-suppress-filename-headers} ¿Qué opción suprime los encabezados de nombre de archivo cuando `head` lee varios archivos?

::option[`-v`]{#head-verbose explanation="La opción `-v` solicita encabezados incluso cuando solo se proporciona un archivo, lo contrario de suprimirlos."}
::option[`-c`]{#head-byte-option explanation="La opción `-c` cambia la unidad de selección a bytes. No controla los encabezados de nombres."}
::option[`-q`]{#head-quiet .correct explanation="La opción `-q`, o silenciosa, evita que `head` muestre etiquetas de encabezado para cada archivo."}
:::

Para practicar la previsualización del principio de los archivos, prueba estos laboratorios:

1. **[Orden head de Linux: mostrar el principio de un archivo](https://labex.io/es/labs/linux-linux-head-command-file-beginning-display-214302)** - Practica la visualización de las primeras líneas y el cambio de su cantidad.
2. **[Visualización de registros y archivos de configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Consulta y recorre archivos de texto como registros y configuraciones del sistema.
3. **[Detección rápida de amenazas](https://labex.io/es/labs/linux-rapid-threat-detection-387930)** - Aplica `head` y `tail` al análisis rápido de entradas de registro.

## Resumen

Ahora puedes previsualizar con `head` el principio de archivos y de la salida de órdenes.

1. Utilizar la vista predeterminada de las primeras diez líneas.
2. Seleccionar una cantidad de líneas con `-n`.
3. Seleccionar una cantidad de bytes con `-c` cuando corresponda.
4. Leer desde stdin en una tubería.
5. Controlar los encabezados al mostrar varios archivos.
