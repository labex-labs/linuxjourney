---
index: 11
lang: "es"
title: "join y split"
meta_title: "join y split - Text-Fu"
meta_description: "Aprende a usar los comandos 'join' y 'split' de Linux para la manipulación de archivos. Comprende cómo combinar archivos por campos comunes y dividir archivos grandes de manera eficiente. Obtén ejemplos prácticos y consejos."
meta_keywords: "comando join de Linux, comando split de Linux, manipulación de archivos, tutorial de Linux, línea de comandos, Linux para principiantes, guía de Linux"
---

## Lesson Content

El comando `join` te permite unir múltiples archivos por un campo común:

Digamos que tengo dos archivos que quiero unir:

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

¿Ves cómo unió mis archivos? Se unen por el primer campo por defecto, y los campos tienen que ser idénticos. Si no lo son, puedes ordenarlos. En este caso, los archivos se unen a través de 1, 2, 3.

¿Cómo uniríamos los siguientes archivos?

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

Para unir este archivo, necesitas especificar qué campos estás uniendo. En este caso, queremos el campo 2 en `file1.txt` y el campo 1 en `file2.txt`, por lo que el comando se vería así:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` se refiere a `file1.txt` y `-2` se refiere a `file2.txt`. Bastante ingenioso. También puedes dividir un archivo en diferentes archivos con el comando `split`:

```bash
split somefile
```

Esto lo dividirá en diferentes archivos. Por defecto, los dividirá una vez que alcancen un límite de 1000 líneas. Los archivos se nombran `x**` por defecto.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de cómo unir y manipular archivos de texto:

1. **[Comando Linux join: Unión de archivos](https://labex.io/es/labs/linux-linux-join-command-file-joining-219193)** - Este laboratorio proporciona una introducción directa y práctica al comando `join`, permitiéndote practicar la fusión de líneas de dos archivos de texto ordenados basándose en un campo común, tal como se discutió en la lección.
2. **[Procesamiento de datos de empleados](https://labex.io/es/labs/linux-processing-employees-data-388132)** - Aplica tus conocimientos de `join` y otras potentes utilidades de línea de comandos de Linux como `awk` para combinar y procesar datos de múltiples fuentes, simulando un escenario de análisis de datos del mundo real.
3. **[Control de secuencia y tuberías](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Mejora tu eficiencia en la línea de comandos y tus habilidades de manipulación de datos aprendiendo a controlar las secuencias de ejecución de comandos, utilizar tuberías y aprovechar potentes herramientas de procesamiento de texto, lo que complementa las capacidades de combinación de datos de `join`.

Estos laboratorios te ayudarán a aplicar los conceptos de manipulación de archivos de texto y combinación de datos en escenarios reales y a ganar confianza con las herramientas de línea de comandos de Linux.

## Quiz Question

¿Qué comando usarías para unir archivos llamados `cat`, `dog`, `cow`?

## Quiz Answer

join cat dog cow
