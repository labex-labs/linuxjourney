---
index: 6
lang: "es"
title: "cut"
meta_title: "cut - Text-Fu"
meta_description: "Aprende a usar el comando `cut` de Linux para extraer texto de archivos. Este tutorial para principiantes cubre el corte por caracteres y campos. ¡Mejora tus habilidades de procesamiento de texto en Linux!"
meta_keywords: "comando cut, procesamiento de texto Linux, extraer texto, tutorial Linux, Linux para principiantes, ejemplos cut, guía Linux"
---

## Lesson Content

Vamos a aprender un par de comandos útiles que puedes usar para procesar texto. Antes de empezar, vamos a crear un archivo con el que trabajaremos. Copia y pega el siguiente comando; una vez que lo hagas, añade un TAB entre "lazy" y "dog" (mantén pulsado Ctrl-v + TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

El primer comando que aprenderemos es el comando `cut`. Extrae porciones de texto de un archivo.

Para extraer contenido por una lista de caracteres:

```bash
cut -c 5 sample.txt
```

Esto muestra el quinto carácter de cada línea del archivo. En este caso, es "q"; ten en cuenta que el espacio también cuenta como un carácter.

Para extraer el contenido por un campo, tendremos que hacer una pequeña modificación:

```bash
cut -f 2 sample.txt
```

El flag `-f` o de campo corta el texto basándose en campos. Por defecto, usa TABs como delimitadores, por lo que todo lo separado por un TAB se considera un campo. Deberías ver "dog" como tu salida.

Puedes combinar el flag de campo con el flag de delimitador para extraer el contenido por un delimitador personalizado:

```bash
cut -f 1 -d ";" sample.txt
```

Esto cambiará el delimitador TAB por un delimitador ";", y como estamos cortando el primer campo, el resultado debería ser "The quick brown".

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del procesamiento de texto con `cut` y otros comandos relacionados:

1. **[Comando cut de Linux: Corte de texto](https://labex.io/es/labs/linux-linux-cut-command-text-cutting-219187)** - Este laboratorio proporciona una introducción directa y práctica al comando `cut`, permitiéndote practicar la extracción de columnas o campos específicos de archivos de texto, tal como se discutió en la lección.
2. **[Procesamiento de texto simple](https://labex.io/es/labs/linux-simple-text-processing-18004)** - Amplía tus habilidades de manipulación de texto utilizando comandos potentes como `tr`, `col`, `join` y `paste` para procesar y analizar datos de texto de manera eficiente.
3. **[Control de secuencia y tuberías](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Mejora tu eficiencia en la línea de comandos aprendiendo a controlar las secuencias de ejecución de comandos, utilizar tuberías y aprovechar herramientas potentes de procesamiento de texto como `cut`, `grep`, `wc`, `sort` y `uniq`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con el procesamiento de texto en Linux.

## Quiz Question

¿Qué comando usarías para obtener el primer carácter de cada línea en un archivo?

## Quiz Answer

cut -c 1
