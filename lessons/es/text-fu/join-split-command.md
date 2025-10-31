---
index: 11
lang: "es"
title: "unir y dividir"
meta_title: "unir y dividir - Text-Fu"
meta_description: "Domina el uso de los comandos de Linux join y split. Aprende a unir archivos eficientemente basándote en campos comunes y a dividir archivos grandes en partes más pequeñas. Esta guía cubre qué comando usarías para unir archivos llamados gato, perro, vaca y otros ejemplos prácticos."
meta_keywords: "unir archivos linux, qué comando usarías para unir archivos, comando join linux, comando split linux, manipulación de archivos, línea de comandos, procesamiento de texto"
---

## Lesson Content

En Linux, gestionar y manipular archivos de texto es una tarea común. Dos utilidades potentes para esto son `join` y `split`. El comando `join` fusiona líneas de dos archivos basándose en un campo común, mientras que `split` divide un archivo grande en partes más pequeñas y manejables.

### Unir Archivos por un Campo Común

El comando `join` es una herramienta fundamental cuando necesitas **unir archivos linux**. Por defecto, combina líneas de dos archivos ordenados basándose en un primer campo idéntico.

Por ejemplo, imagina que tienes dos archivos que deseas fusionar:

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

Usando el comando `join`, puedes fusionarlos fácilmente:

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Como puedes ver, los archivos se unieron utilizando el primer campo común (1, 2, 3). Para que `join` funcione correctamente, los campos de unión en ambos archivos deben estar ordenados.

### Especificar Campos de Unión Diferentes

¿Qué pasa si el campo común no es la primera columna? Puedes indicarle a `join` qué campos usar. Considera estos archivos:

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

Aquí, necesitamos unir en el segundo campo de `file1.txt` y el primer campo de `file2.txt`. El comando sería:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

La bandera `-1 2` especifica el campo 2 del primer archivo, y `-2 1` especifica el campo 1 del segundo archivo.

### Dividir Archivos Grandes

El comando `split` hace lo contrario de unir; divide un archivo grande en archivos más pequeños.

```bash
$ split somefile
```

Por defecto, este comando divide `somefile` en nuevos archivos una vez que se alcanza un límite de 1000 líneas. Los archivos de salida se nombran `xaa`, `xab`, y así sucesivamente. Puedes personalizar este comportamiento, por ejemplo, especificando un recuento de líneas diferente con la bandera `-l` o dividiendo por tamaño de archivo con la bandera `-b`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la unión y manipulación de archivos de texto:

1. **[Comando join de Linux: Unión de Archivos](https://labex.io/es/labs/linux-linux-join-command-file-joining-219193)** - Este laboratorio proporciona una introducción directa y práctica al comando `join`, permitiéndote practicar la fusión de líneas de dos archivos de texto ordenados basándose en un campo común, tal como se discutió en la lección.
2. **[Procesamiento de Datos de Empleados](https://labex.io/es/labs/linux-processing-employees-data-388132)** - Aplica tu conocimiento de `join` y otras potentes utilidades de línea de comandos de Linux como `awk` para combinar y procesar datos de múltiples fuentes, simulando un escenario de análisis de datos del mundo real.
3. **[Control de Secuencia y Tubería (Pipeline)](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Mejora tu eficiencia en la línea de comandos y tus habilidades de manipulación de datos aprendiendo a controlar secuencias de ejecución de comandos, utilizar tuberías (pipelines) y aprovechar potentes herramientas de procesamiento de texto, lo que complementa las capacidades de combinación de datos de `join`.

Estos laboratorios te ayudarán a aplicar los conceptos de manipulación de archivos de texto y combinación de datos en escenarios reales y a ganar confianza con las herramientas de línea de comandos de Linux.

## Quiz Question

¿Qué comando usarías para unir archivos llamados `cat`, `dog`, `cow`? Por favor, proporciona el comando completo en inglés. El comando y los nombres de archivo deben estar en minúsculas.

## Quiz Answer

join cat dog cow
