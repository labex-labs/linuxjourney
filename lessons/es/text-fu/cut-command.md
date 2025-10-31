---
index: 6
lang: "es"
title: "cortar"
meta_title: "cortar - Text-Fu"
meta_description: "Aprenda a usar el comando Linux `cut` para extraer secciones específicas de texto de archivos. Esta guía cubre el corte por carácter y campo (`cut f`), incluido cómo cortar f con delimitadores personalizados. Perfecto para dominar el procesamiento de texto en Linux."
meta_keywords: "comando cut, procesamiento de texto Linux, extraer texto, cut f, cómo usar cut f, tutorial Linux, ejemplos de cut, guía Linux, corte por campo"
---

## Lesson Content

Vamos a aprender un par de comandos útiles para procesar texto. Antes de empezar, creemos un archivo con el que trabajar. Copia y pega el siguiente comando. Después de pegar, deberás añadir un carácter TAB literal entre "lazy" y "dog" (a menudo puedes hacerlo presionando Ctrl-v y luego TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

El primer comando que exploraremos es `cut`, que extrae porciones de texto de un archivo.

### Cortar por Carácter

Puedes extraer contenido basado en la posición del carácter usando la opción `-c`.

```bash
cut -c 5 sample.txt
```

Este comando muestra el 5º carácter de cada línea del archivo. En nuestro caso, la salida es "q". Ten en cuenta que los espacios también cuentan como caracteres.

### Cortar por Campo con cut f

Una característica más potente es cortar por campos. La sintaxis `cut f`, usando la opción `-f`, te permite extraer texto basado en la posición del campo. Por defecto, `cut` utiliza el carácter TAB como delimitador, lo que significa que todo lo separado por un TAB se considera un campo distinto.

Veamos cómo cortar f basado en campos:

```bash
cut -f 2 sample.txt
```

Dado que insertamos un TAB entre "lazy" y "dog", este comando trata a "dog" como el segundo campo. Tu salida debería ser "dog".

### Usar Delimitadores Personalizados

También puedes combinar la opción de campo con la opción de delimitador (`-d`) para especificar un delimitador personalizado. Esto es útil cuando trabajas con archivos que usan caracteres como comas o punto y coma para separar datos.

```bash
cut -f 1 -d ";" sample.txt
```

Este comando cambia el delimitador de TAB a punto y coma (";"). Como estamos cortando el primer campo (`-f 1`), el resultado será "The quick brown".

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del procesamiento de texto con `cut` y otros comandos relacionados:

1. **[Comando cut de Linux: Corte de Texto](https://labex.io/es/labs/linux-linux-cut-command-text-cutting-219187)** - Este laboratorio proporciona una introducción práctica y directa al comando `cut`, permitiéndote practicar la extracción de columnas o campos específicos de archivos de texto, tal como se discutió en la lección.
2. **[Procesamiento Simple de Texto](https://labex.io/es/labs/linux-simple-text-processing-18004)** - Expande tus habilidades de manipulación de texto utilizando comandos potentes como `tr`, `col`, `join` y `paste` para procesar y analizar datos de texto de manera eficiente.
3. **[Control de Secuencia y Tubería (Pipeline)](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Mejora tu eficiencia en la línea de comandos aprendiendo a controlar secuencias de ejecución de comandos, utilizar tuberías (pipelines) y aprovechar herramientas potentes de procesamiento de texto como `cut`, `grep`, `wc`, `sort` y `uniq`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con el procesamiento de texto en Linux.

## Quiz Question

¿Qué comando usarías para obtener el primer carácter de cada línea de un archivo?

## Quiz Answer

cut -c 1
