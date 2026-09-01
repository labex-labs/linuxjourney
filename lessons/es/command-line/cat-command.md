---
lesson_id: "cat-command"
course_id: "command-line"
lang: "es"
order_index: 7
title: "cat"
description: "Aprende a mostrar, concatenar y redirigir de forma segura el contenido de archivos con la orden `cat`."
meta_title: "cat - Línea de Comandos"
meta_description: "Aprende el comando cat de Linux con ejemplos para ver archivos, concatenar archivos, numerar líneas, crear archivos y usar redirección de forma segura."
meta_keywords: "comando linux cat, comando cat, ver archivo linux, concatenar archivos, cat -n, cat -b, redirección cat, linux cat"
---

Después de aprender a identificar archivos, el siguiente paso es leer su contenido. La orden `cat` muestra archivos y une su contenido; su nombre es una abreviatura de «concatenate» (concatenar).

## Visualización del contenido de archivos

El uso más básico del comando `cat` es mostrar el contenido de un solo archivo directamente en tu terminal.

```bash
$ cat myfile.txt
```

La orden escribe todo el archivo en la salida estándar. Funciona bien con textos cortos, pero un archivo largo puede desplazarse demasiado rápido por la pantalla.

:::single-choice{#display-short-file} ¿Qué orden muestra todo el contenido de `myfile.txt` en la terminal?

::option[`file myfile.txt`]{#classify-myfile explanation="`file` informa del tipo probable del archivo. No imprime todo el texto que contiene."}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch` actualiza las marcas de tiempo o crea un archivo ausente. No muestra el contenido del archivo."}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat` lee `myfile.txt` y escribe su contenido en la salida estándar, que en este caso es la terminal."}
:::

## Concatenación de archivos

Fiel a su nombre, `cat` puede combinar, o concatenar, múltiples archivos y mostrar su salida combinada. Lee los archivos en el orden en que se proporcionan y los imprime secuencialmente.

```bash
$ cat dogfile birdfile
```

Este comando mostrará primero el contenido de `dogfile`, seguido inmediatamente por el contenido de `birdfile`.

Para guardar la salida combinada en un nuevo archivo, usa la redirección:

```bash
$ cat dogfile birdfile > animals
```

La shell crea `animals` o lo trunca antes de ejecutar `cat`, y después envía allí la salida combinada. No utilices uno de los archivos de entrada como destino, pues podría vaciarse antes de que `cat` lo lea.

:::single-choice{#combine-files-in-order} ¿Qué orden escribe `part1` seguido de `part2` en un archivo nuevo o sustituido llamado `whole`?

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="La redirección tiene un único destino y las demás palabras se convierten en operandos de `cat`. Esta orden no expresa las entradas ni el orden solicitados."}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat` emite los dos archivos en el orden indicado y `>` redirige esa salida combinada a `whole`."}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="Esta orden escribe las mismas dos entradas en `whole`, pero lee `part2` antes que `part1`. El orden de los operandos controla el de la salida."}
:::

## Lectura de la entrada de la terminal en un archivo

También puedes usar `cat` con el operador de redirección de salida (`>`) para crear archivos nuevos. Esta es una forma rápida de escribir texto en un archivo directamente desde tu terminal.

```bash
$ cat > newfile.txt
```

Después de ejecutar la orden, escribe el texto deseado. Pulsa `Ctrl+D` para enviar una señal de fin de archivo y volver a la shell. Ten cuidado: si `newfile.txt` ya existe, `>` trunca su contenido anterior.

Para agregar texto a un archivo en lugar de sobrescribirlo, usa `>>`.

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input} Quieres escribir más texto al final de un `notes.txt` existente. ¿Qué orden inicia la operación sin truncar el archivo?

::option[`cat > notes.txt`]{#overwrite-notes explanation="Un solo `>` redirige la entrada después de truncar el destino. Se perdería el texto existente en `notes.txt`."}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="El operador `>>` abre el destino para añadir contenido, por lo que el texto leído por `cat` se coloca después del contenido existente."}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="Usar el mismo archivo como entrada y como destino de `>` puede truncarlo antes de que `cat` lo lea. No es una operación segura para añadir contenido."}
:::

## Formato de la salida

El comando `cat` tiene varias opciones para modificar su comportamiento.

- `-n`: Numera todas las líneas de salida, comenzando desde 1.
- `-b`: Numera solo las líneas de salida que no están vacías.
- `-s`: Comprime múltiples líneas en blanco en una sola línea en blanco.
- `-A`: Muestra caracteres no imprimibles, tabulaciones y finales de línea.

Ejemplos:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines} ¿Qué orden numera únicamente las líneas no vacías de la salida de `notes.txt`?

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="La opción `-b` numera las líneas no vacías y deja sin numerar las líneas vacías."}
::option[`cat -n notes.txt`]{#number-all-lines explanation="La opción `-n` numera todas las líneas, incluidas las vacías. No cumple la condición de numerar solo las que contienen texto."}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="La opción `-s` reduce varias líneas vacías seguidas a una. No añade números de línea."}
:::

## Elección de un visor para archivos largos

Usa `cat` para archivos cortos. Para archivos largos, usa `less` para poder desplazarte, buscar y salir sin saturar tu terminal.

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file} ¿Qué orden resulta más adecuada para leer de forma interactiva un archivo de registro largo?

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less` permite desplazarse, buscar y salir de forma controlada, por lo que es apropiado para leer interactivamente archivos largos."}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat` escribe todo el registro de una vez en la terminal. Un archivo largo podría desplazarse antes de que puedas examinarlo."}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch` modifica marcas de tiempo y puede necesitar permisos. No es una orden para leer el registro."}
:::

Para practicar cómo mostrar y combinar contenido, prueba estos laboratorios:

1. **[Orden cat de Linux: concatenar archivos](https://labex.io/es/labs/linux-linux-cat-command-file-concatenating-210986)** - Aprende a usar `cat` para visualizar, concatenar y manipular archivos de texto de forma eficaz.
2. **[Visualización de registros y archivos de configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practica con órdenes como `cat` para consultar archivos de texto, incluidos registros y configuraciones del sistema.

## Resumen

Ahora puedes utilizar `cat` para mostrar y combinar contenido eligiendo una redirección segura.

1. Mostrar todo el contenido de un archivo corto.
2. Concatenar archivos en el orden elegido.
3. Sustituir o añadir contenido a un destino de forma deliberada.
4. Numerar o simplificar las líneas de salida.
5. Elegir `less` cuando resulte más apropiada una lectura interactiva.
