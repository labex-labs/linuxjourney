---
index: 10
lang: "es"
title: "Expandir y desexpandir"
meta_title: "Expandir y desexpandir - Text-Fu"
meta_description: "Domina el formato de texto en Linux con nuestra guía sobre los comandos expand y unexpand. Aprende a convertir tabulaciones a espacios y espacios a tabulaciones para diseños de archivo consistentes."
meta_keywords: "comando expand, comando unexpand, tabulaciones Linux, espacios Linux, formato de texto, tutorial Linux, Linux principiantes, guía Linux"
---

## Lesson Content

El espaciado inconsistente puede hacer que los archivos de texto sean difíciles de leer. Si bien las tabulaciones están destinadas a crear sangría uniforme, su ancho de visualización puede variar entre diferentes editores y sistemas. Esto puede alterar el formato y la alineación del texto. Afortunadamente, Linux proporciona herramientas sencillas para gestionar esto convirtiendo entre tabulaciones y espacios. Esta guía de Linux para principiantes le guiará a través del proceso.

### Convertir Tabulaciones a Espacios con el Comando expand

Cuando necesite asegurar un espaciado consistente, puede convertir las tabulaciones en un número estándar de espacios usando el comando `expand`. Este comando lee un archivo y reemplaza cada carácter de tabulación con un conjunto de caracteres de espacio, imprimiendo el resultado en la salida estándar.

```bash
expand sample.txt
```

Por defecto, el `comando expand` convierte cada tabulación en 8 espacios. Esta simple utilidad es una herramienta poderosa para mejorar el formato del texto.

### Guardar la Salida Convertida

El comando `expand` solo imprime el texto convertido en su terminal. Para guardar los cambios, debe redirigir la salida a un nuevo archivo.

```bash
expand sample.txt > result.txt
```

Este comando toma la salida de `expand sample.txt` y la escribe en `result.txt`, dándole un nuevo archivo con espacios en lugar de tabulaciones.

### Convertir Espacios a Tabulaciones con el Comando unexpand

La operación inversa, convertir espacios de nuevo en tabulaciones, es manejada por el comando `unexpand`. Esto puede ser útil para reducir el tamaño del archivo o adherirse a estándares de codificación que requieren tabulaciones.

```bash
unexpand -a result.txt
```

Por defecto, `unexpand` solo convierte los espacios iniciales en cada línea. La opción `-a` le indica al `comando unexpand` que convierta todas las instancias de 8 espacios en una tabulación, no solo aquellas al principio de una línea, proporcionando un control más completo sobre sus espacios y tabulaciones de Linux.

## Exercise

Para dominar la manipulación de texto y la redirección en Linux, la práctica es clave. Los siguientes laboratorios prácticos ayudarán a reforzar su comprensión:

1. **[Redirección de Entrada y Salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practique el control del flujo de datos desde comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como `>` y `>>`.
2. **[Procesamiento Simple de Texto](https://labex.io/es/labs/linux-simple-text-processing-18004)** - Aprenda a usar comandos potentes como `tr`, `col`, `join` y `paste` para manipular y analizar datos de texto de manera eficiente, mejorando sus habilidades de línea de comandos para el procesamiento de datos.
3. **[Procesamiento de Texto y Expresiones Regulares](https://labex.io/es/labs/linux-text-processing-and-regular-expressions-18003)** - Aprenda las potentes herramientas de procesamiento de texto `grep`, `sed` y `awk`, y use expresiones regulares para una manipulación de texto y coincidencia de patrones eficientes en Linux.

Completar estos laboratorios le ayudará a aplicar los conceptos de transformación de texto y manipulación de archivos en escenarios del mundo real, aumentando su confianza con las herramientas esenciales de la línea de comandos de Linux.

## Quiz Question

¿Qué comando se utiliza para convertir tabulaciones en espacios? (Por favor, responda usando el nombre del comando en inglés en minúsculas.)

## Quiz Answer

expand
