---
index: 15
lang: "es"
title: "wc y nl"
meta_title: "wc y nl - Text-Fu"
meta_description: "Aprenda los comandos wc y nl de Linux. Comprenda el conteo de palabras, la numeración de líneas y el análisis de archivos. ¡Mejore sus habilidades de línea de comandos de Linux hoy mismo!"
meta_keywords: "comando wc, comando nl, conteo de palabras Linux, números de línea Linux, análisis de archivos, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

El comando `wc` (word count) muestra el recuento total de palabras en un archivo.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Muestra el número de líneas, el número de palabras y el número de bytes, respectivamente.

Para ver solo el recuento de un campo determinado, use las opciones `-l`, `-w` o `-c`, respectivamente.

```bash
$ wc -l /etc/passwd
96
```

Otro comando que puede usar para verificar el recuento de líneas en un archivo es el comando `nl` (number lines).

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del conteo de texto y la numeración de líneas en Linux:

1. **[Comando wc de Linux: Conteo de texto](https://labex.io/es/labs/linux-linux-wc-command-text-counting-219200)** - Practique el conteo de palabras, líneas y caracteres en archivos de texto usando el comando `wc`.
2. **[Comando nl de Linux: Numeración de líneas](https://labex.io/es/labs/linux-linux-nl-command-line-numbering-210988)** - Aprenda a numerar líneas en archivos de texto con el comando `nl`.
3. **[Conteo y Ordenación de Palabras](https://labex.io/es/labs/linux-word-count-and-sorting-388125)** - Aplique su conocimiento de `wc` para contar líneas, palabras y caracteres, y combínelo con la ordenación para tareas prácticas de análisis de texto.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con el procesamiento de texto en Linux.

## Quiz Question

¿Qué comando usaría para obtener el número total de palabras en un archivo y solo las palabras?

## Quiz Answer

wc -w
