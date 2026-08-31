---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "es"
order_index: 15
title: "wc y nl"
description: "Aprende a contar líneas, palabras, bytes o caracteres con wc y a numerar líneas con nl."
meta_title: "wc y nl - Text-Fu"
meta_description: "Domina las órdenes wc y nl en este tutorial de Linux. Aprende a contar palabras, añadir números de línea y realizar análisis básicos de archivos."
meta_keywords: "orden wc, orden nl, recuento de palabras Linux, contar palabras archivo Linux, números de línea Linux, análisis de archivos, procesamiento de texto Linux"
---

La orden `wc` cuenta propiedades de los flujos de texto, mientras que `nl` escribe la entrada con números de línea generados. Ambas leen archivos o la entrada estándar y envían sus resultados a la salida estándar.

## Interpretar la salida predeterminada de wc

Sin una opción de recuento, `wc` imprime la cantidad de caracteres de nueva línea, palabras y bytes, seguida del nombre de archivo cuando se ha proporcionado uno:

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

De izquierda a derecha:

1. `2` caracteres de nueva línea, indicados como líneas.
2. `3` palabras delimitadas por espacios en blanco.
3. `15` bytes en este ejemplo ASCII.

Una última línea de texto sin un salto de línea final no se cuenta con `wc -l`, porque esta opción cuenta caracteres de nueva línea, no las líneas percibidas visualmente.

:::single-choice{#wc-default-columns}
En la salida predeterminada de `wc file.txt`, ¿qué representan los tres primeros números?

::option[Líneas, palabras y bytes, en ese orden.]{#wc-lines-words-bytes .correct explanation="La salida predeterminada de `wc` muestra el recuento de saltos de línea, palabras y bytes antes del nombre de archivo."}
::option[Bytes, palabras y líneas, en ese orden.]{#wc-bytes-words-lines explanation="Son las mismas medidas en un orden incorrecto. El recuento de líneas aparece primero."}
::option[Archivos, caracteres y párrafos, en ese orden.]{#wc-files-characters-paragraphs explanation="Las columnas predeterminadas no cuentan archivos ni párrafos, y la tercera medida predeterminada son bytes."}
:::

## Solicitar un único recuento

Selecciona únicamente la medida que necesites:

- `-l`: cuenta caracteres de nueva línea.
- `-w`: cuenta palabras.
- `-c`: cuenta bytes.
- `-m`: cuenta caracteres según la configuración regional actual.

Por ejemplo:

```bash
$ wc -w colors.txt
3 colors.txt
```

Los recuentos de bytes y caracteres son iguales para texto ASCII, pero pueden diferir con codificaciones multibyte como UTF-8. Cuando se usa la entrada estándar sin un operando de nombre de archivo, `wc` suele omitir la etiqueta del nombre:

```bash
$ printf 'one two\n' | wc -w
2
```

:::single-choice{#wc-word-count-only}
¿Qué orden muestra únicamente el recuento de palabras de `essay.txt`?

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="La opción `-l` muestra caracteres de nueva línea, no palabras."}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="La opción `-w` selecciona la medida de recuento de palabras."}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="La opción `-c` muestra bytes, no palabras delimitadas por espacios en blanco."}
:::

:::single-choice{#wc-characters-not-bytes}
¿Qué opción pide a `wc` que cuente caracteres en vez de bytes con la configuración regional actual?

::option[`-m`]{#wc-character-option .correct explanation="La opción `-m` muestra caracteres, que pueden diferir de los bytes en texto multibyte."}
::option[`-c`]{#wc-byte-option explanation="La opción `-c` muestra bytes. Un carácter puede ocupar varios bytes en codificaciones como UTF-8."}
::option[`-w`]{#wc-word-option explanation="La opción `-w` cuenta palabras, no caracteres ni bytes."}
:::

Cuando se indican varios archivos, `wc` imprime un resultado por archivo y una línea `total`. En GNU, `wc -L` muestra la anchura máxima de visualización de una línea de entrada.

## Numerar líneas no vacías con nl

De forma predeterminada, `nl` numera las líneas no vacías del cuerpo lógico de su entrada. Supón que `notes.txt` contiene una segunda línea vacía:

```text
alpha

beta
```

La línea vacía se conserva, pero no recibe ningún número:

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

`nl` escribe una salida numerada; no modifica `notes.txt`.

:::single-choice{#nl-default-blank-lines}
¿Cómo trata `nl notes.txt` las líneas vacías del cuerpo de forma predeterminada?

::option[Omite por completo cada línea vacía de la salida.]{#nl-omit-blank explanation="La línea vacía permanece en la salida, pero no se le asigna un número de forma predeterminada."}
::option[Las conserva sin números de línea.]{#nl-preserve-unnumbered .correct explanation="El estilo predeterminado del cuerpo numera las líneas no vacías y deja pasar las vacías sin numerarlas."}
::option[Las numera en la misma secuencia que las líneas no vacías.]{#nl-number-blank-default explanation="Numerar todas las líneas del cuerpo requiere otro estilo, como `-ba`."}
:::

## Numerar todas las líneas

Usa `-ba` para seleccionar el estilo de numeración del cuerpo `a`, que numera todas las líneas:

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

Otras opciones controlan el formato. Por ejemplo, `-w 3` establece la anchura del campo numérico y `-s ': '` cambia el separador posterior al número.

:::single-choice{#nl-number-all-lines}
¿Qué orden numera todas las líneas del cuerpo de `notes.txt`, incluidas las vacías?

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="Esto cambia la anchura del campo numérico, pero conserva la regla predeterminada de numerar líneas no vacías."}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="La opción `-b` elige el estilo del cuerpo y el estilo `a` numera todas las líneas."}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="Esto imprime un recuento de caracteres de nueva línea y no reproduce el archivo con números de línea."}
:::

Para practicar el recuento y la numeración de texto, prueba estos laboratorios prácticos:

1. **[Orden wc de Linux: recuento de texto](https://labex.io/labs/linux-linux-wc-command-text-counting-219200)** - Practica cómo contar palabras, líneas y caracteres en archivos de texto con `wc`.
2. **[Orden nl de Linux: numeración de líneas](https://labex.io/labs/linux-linux-nl-command-line-numbering-210988)** - Aprende a numerar líneas de archivos de texto con `nl`.
3. **[Recuento de palabras y ordenación](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Aplica tus conocimientos de `wc` para contar líneas, palabras y caracteres, y combínalo con la ordenación en tareas prácticas de análisis de texto.

## Resumen

Ahora puedes medir flujos de texto y añadir números de línea visibles sin editar el origen.

1. Interpreta las columnas predeterminadas de líneas, palabras y bytes de `wc`.
2. Selecciona un recuento con `-l`, `-w`, `-c` o `-m`.
3. Distingue los recuentos de bytes de los de caracteres.
4. Numera líneas no vacías con el comportamiento predeterminado de `nl`.
5. Numera también las líneas vacías con `nl -ba`.
