---
index: 10
lang: "es"
title: "expand y unexpand"
meta_title: "expand y unexpand - Text-Fu"
meta_description: "Aprenda a convertir tabulaciones a espacios con el comando `expand` y espacios a tabulaciones con `unexpand`. Mejore el formato de archivos de texto con este tutorial de Linux."
meta_keywords: "comando expand, comando unexpand, tabulaciones Linux, espacios Linux, formato de texto, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

En nuestra lección sobre el comando `cut`, teníamos nuestro archivo `sample.txt` que contenía una tabulación. Normalmente, las tabulaciones suelen mostrar una diferencia notable, pero algunos archivos de texto no la muestran lo suficientemente bien. Tener tabulaciones en un archivo de texto puede no proporcionar el espaciado deseado. Para cambiar sus tabulaciones a espacios, use el comando `expand`.

```bash
expand sample.txt
```

El comando anterior imprimirá la salida con cada tabulación convertida en un grupo de espacios. Para guardar esta salida en un archivo, use la redirección de salida como se muestra a continuación.

```bash
expand sample.txt > result.txt
```

Opuesto a `expand`, podemos convertir cada grupo de espacios de nuevo a una tabulación con el comando `unexpand`:

```bash
unexpand -a result.txt
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la manipulación y redirección de texto en Linux:

1. **[Redirección de entrada y salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practique el control del flujo de datos de los comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como `>` y `>>`.
2. **[Procesamiento de texto simple](https://labex.io/es/labs/linux-simple-text-processing-18004)** - Aprenda a usar comandos potentes como `tr`, `col`, `join` y `paste` para manipular y analizar datos de texto de manera eficiente, mejorando sus habilidades de línea de comandos para el procesamiento de datos.
3. **[Procesamiento de texto y expresiones regulares](https://labex.io/es/labs/linux-text-processing-and-regular-expressions-18003)** - Aprenda las potentes herramientas de procesamiento de texto `grep`, `sed` y `awk`, y use expresiones regulares para una manipulación de texto y coincidencia de patrones eficientes en Linux.

Estos laboratorios le ayudarán a aplicar los conceptos de transformación de texto y manipulación de archivos en escenarios reales y a generar confianza con las herramientas de línea de comandos de Linux.

## Quiz Question

¿Qué comando se utiliza para convertir tabulaciones en espacios?

## Quiz Answer

expand
