---
index: 2
lang: "es"
title: "stdin (Entrada Estándar)"
meta_title: "stdin (Entrada Estándar) - Text-Fu"
meta_description: "Aprende sobre la redirección de stdin (entrada estándar) en Linux. Comprende cómo usar el operador '<' con archivos y comandos. Explora ejemplos prácticos y mejora tus habilidades de línea de comandos de Linux."
meta_keywords: "stdin, entrada estándar, redirección Linux, operador <, tutorial Linux, línea de comandos, principiante, guía"
---

## Lesson Content

En nuestra lección anterior, aprendimos que tenemos diferentes flujos de stdout que podemos usar, como un archivo o la pantalla. Bueno, también hay diferentes flujos de entrada estándar (stdin) que podemos usar. Sabemos que tenemos stdin de dispositivos como el teclado, pero también podemos usar archivos, la salida de otros procesos y la terminal. Veamos un ejemplo.

Usemos el archivo `peanuts.txt` de la lección anterior para este ejemplo. Recuerda, tenía el texto "Hello World" en él.

```bash
cat < peanuts.txt > banana.txt
```

Así como teníamos `>` para la redirección de stdout, podemos usar `<` para la redirección de stdin.

Normalmente, en el comando `cat`, se le envía un archivo y ese archivo se convierte en el stdin. En este caso, redirigimos `peanuts.txt` para que fuera nuestro stdin. Luego, la salida de `cat peanuts.txt`, que sería "Hello World", se redirige a otro archivo llamado `banana.txt`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la redirección de entrada y salida en Linux:

1. **[Redirección de entrada y salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practica el control del flujo de datos de los comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como >, >>, 2> y el comando tee.
2. **[Redirección de flujo de datos](https://labex.io/es/labs/linux-data-stream-redirection-17995)** - Aprende el arte de la redirección de flujos en Linux. Manipula los flujos de entrada, salida y error estándar, combina salidas y utiliza /dev/null para operaciones avanzadas de archivos.
3. **[Control de secuencia y tuberías](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Aprende a controlar las secuencias de ejecución de comandos y a utilizar las tuberías (pipelines), que son fundamentales para dirigir la salida de un comando como entrada para otro.

Estos laboratorios te ayudarán a aplicar los conceptos de redirección de entrada y salida en escenarios reales y a ganar confianza con la escritura de scripts de shell y la manipulación de datos.

## Quiz Question

¿Qué redireccionador utilizas para redirigir stdin?

## Quiz Answer

<
