---
index: 15
lang: "es"
title: "wc y nl"
meta_title: "wc y nl - Text-Fu"
meta_description: "Domina los comandos wc y nl en este tutorial de Linux. Aprende a realizar un conteo de palabras en Linux, añadir números de línea a archivos y realizar análisis básicos de archivos. Una guía perfecta para principiantes para mejorar sus habilidades en la línea de comandos."
meta_keywords: "comando wc, comando nl, conteo de palabras Linux, contar palabras en archivo Linux, números de línea Linux, comando nl Linux, análisis de archivos, procesamiento de texto Linux, línea de comandos Linux, tutorial de Linux para principiantes"
---

## Lesson Content

En Linux, analizar archivos de texto es una tarea común. Dos utilidades fundamentales para esto son `wc` y `nl`, que le ayudan a contar contenido y numerar líneas, respectivamente.

### Contar con el comando wc

El comando `wc` (word count o conteo de palabras) es una herramienta potente para el análisis básico de archivos. Cuando se ejecuta en un archivo, proporciona un resumen de su contenido.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

La salida muestra tres números seguidos del nombre del archivo. De izquierda a derecha, estos números representan:

1.  El número de líneas.
2.  El número de palabras (el conteo de palabras en Linux).
3.  El número de bytes.

### Obtener conteos específicos

A menudo, solo necesita una pieza de información. Puede usar opciones para mostrar un conteo específico en lugar de los tres.

- `-l`: Muestra solo el conteo de líneas.
- `-w`: Muestra solo el conteo de palabras.
- `-c`: Muestra solo el conteo de bytes.

Por ejemplo, para ver solo el número de líneas en el archivo `/etc/passwd`, usaría:

```bash
$ wc -l /etc/passwd
96
```

### Numerar líneas con el comando nl

Otro comando útil para inspeccionar archivos es `nl` (number lines o numerar líneas). Como su nombre indica, lee un archivo y muestra su contenido con números de línea añadidos al principio de cada línea. Esto es especialmente útil para revisar scripts o archivos de configuración.

Considere un archivo llamado `file1.txt` con el siguiente contenido:

```plaintext
i
like
turtles
```

Usando el comando `nl`, puede añadir fácilmente números de línea en Linux:

```bash
$ nl file1.txt
     1	i
     2	like
     3	turtles
```

Tanto `wc` como `nl` son comandos esenciales para el procesamiento de texto cotidiano en la línea de comandos de Linux.

## Exercise

Para dominar estos comandos, la práctica es clave. Intente estos ejercicios para solidificar sus habilidades en el conteo de texto y la numeración de líneas en Linux:

1.  **[Comando wc de Linux: Conteo de texto](https://labex.io/es/labs/linux-linux-wc-command-text-counting-219200)** - Practique el conteo de palabras, líneas y caracteres en archivos de texto usando el comando `wc`.
2.  **[Comando nl de Linux: Numeración de líneas](https://labex.io/es/labs/linux-linux-nl-command-line-numbering-210988)** - Aprenda a numerar líneas en archivos de texto con el comando `nl`.
3.  **[Conteo de palabras y ordenación](https://labex.io/es/labs/linux-word-count-and-sorting-388125)** - Aplique su conocimiento de `wc` para contar líneas, palabras y caracteres, y combínelo con la ordenación para tareas prácticas de análisis de texto.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios del mundo real y a ganar confianza con el procesamiento de texto en Linux.

## Quiz Question

¿Qué comando y opción usaría para mostrar solo el conteo total de palabras de un archivo? Por favor, responda usando solo el comando y su opción en inglés. La respuesta distingue entre mayúsculas y minúsculas.

## Quiz Answer

wc -w
