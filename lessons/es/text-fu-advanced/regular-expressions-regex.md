---
lang: "es"
title: "regex (Expresiones Regulares)"
meta_title: "regex (Expresiones Regulares) - Text-Fu Avanzado"
meta_description: "Aprende expresiones regulares (regex) para la coincidencia de patrones en Linux. Comprende la sintaxis de regex como ^, $, ., y [] para la manipulación de texto. ¡Mejora tus habilidades con grep!"
meta_keywords: "expresiones regulares, regex, regex de Linux, grep regex, coincidencia de patrones, tutorial de regex, comandos de Linux, principiante"
---

## Lesson Content

Las expresiones regulares son una herramienta poderosa para la selección basada en patrones. Utilizan notaciones especiales similares a las que ya hemos encontrado, como el comodín `*`.

Repasaremos un par de las expresiones regulares más comunes; estas son casi universales en cualquier lenguaje de programación.

Usaremos esta frase como nuestra cadena de prueba:

```plaintext
sally sells seashells
by the seashore
```

### 1. Inicio de una línea con ^

```plaintext
^by
would match the line "by the seashore"
```

### 2. Fin de una línea con $

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. Coincidencia de cualquier carácter único con

```plaintext
b.
would match by
```

### 4. Notación de corchetes con [] y ()

Esto puede ser un poco complicado. Los corchetes nos permiten especificar caracteres encontrados dentro del corchete.

```plaintext
d[iou]g
would match: dig, dog, dug
```

La etiqueta de anclaje anterior `^` cuando se usa en un corchete significa cualquier cosa excepto los caracteres dentro del corchete.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

Los corchetes también pueden usar rangos para aumentar la cantidad de caracteres que desea usar.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

Sin embargo, tenga cuidado, ya que los corchetes distinguen entre mayúsculas y minúsculas:

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

Y esas son algunas expresiones regulares básicas.

## Exercise

Intenta combinar expresiones regulares con `grep` y busca en algunos archivos.

```bash
grep [regular expression here] [file]
```

## Quiz Question

¿Qué expresión regular usarías para hacer coincidir un solo carácter?

## Quiz Answer

.
