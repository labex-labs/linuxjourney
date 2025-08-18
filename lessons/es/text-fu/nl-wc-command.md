---
lang: "es"
title: "wc y nl"
meta_description: "Aprenda los comandos de Linux wc y nl. Comprenda el recuento de palabras, la numeración de líneas y el análisis de archivos. ¡Mejore sus habilidades de línea de comandos de Linux hoy mismo!"
meta_keywords: "comando wc, comando nl, recuento de palabras en Linux, números de línea en Linux, análisis de archivos, tutorial de Linux, Linux para principiantes, guía de Linux"
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

¿Cómo obtendría el recuento total de líneas usando el comando `nl` sin buscar en toda la salida? Sugerencia: Use algunos de los otros comandos que aprendió en este curso.

## Quiz Question

¿Qué comando usaría para obtener el número total de palabras en un archivo y solo las palabras?

## Quiz Answer

wc -w
