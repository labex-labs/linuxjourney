---
index: 1
lang: "es"
title: "regex (Expresiones Regulares)"
meta_title: "regex (Expresiones Regulares) - Text-Fu Avanzado"
meta_description: "Aprenda expresiones regulares (regex) para la coincidencia de patrones en Linux. Comprenda la sintaxis de regex como ^, $, ., y [] para la manipulación de texto. ¡Mejore sus habilidades con grep!"
meta_keywords: "expresiones regulares, regex, regex Linux, grep regex, coincidencia de patrones, tutorial regex, comandos Linux, principiante"
---

## Lesson Content

Las expresiones regulares son una herramienta poderosa para la selección basada en patrones. Utilizan notaciones especiales similares a las que ya hemos encontrado, como el comodín `*`.

Repasaremos un par de las expresiones regulares más comunes; estas son casi universales con cualquier lenguaje de programación.

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

### 3. Coincidencia de cualquier carácter individual con

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

El anclaje anterior `^` cuando se usa en un corchete significa cualquier cosa excepto los caracteres dentro del corchete.

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

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de las expresiones regulares y la coincidencia de patrones:

1. **[Buscar texto con grep en Linux](https://labex.io/es/labs/comptia-search-text-with-grep-in-linux-590841)** - En este laboratorio, aprenderá a buscar texto en archivos en un sistema Linux usando el comando `grep`. Realizará búsquedas básicas, mostrará números de línea, usará anclajes como `^` y `$` para hacer coincidir posiciones de línea, y aprovechará expresiones regulares básicas y extendidas para una coincidencia de patrones compleja.
2. **[Procesamiento de texto y expresiones regulares](https://labex.io/es/labs/linux-text-processing-and-regular-expressions-18003)** - Aprenda las potentes herramientas de procesamiento de texto grep, sed y awk. Aprenda a usar expresiones regulares para una manipulación de texto y coincidencia de patrones eficientes en Linux.
3. **[Extracción de correos y números](https://labex.io/es/labs/linux-extracting-mails-and-numbers-17991)** - En este desafío, aprenderá cómo usar grep y expresiones regulares para extraer direcciones de correo electrónico y números de un archivo, demostrando habilidades esenciales de procesamiento de texto en Linux.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con las expresiones regulares y el procesamiento de texto.

## Quiz Question

¿Qué expresión regular usaría para hacer coincidir un solo carácter?

## Quiz Answer

.
