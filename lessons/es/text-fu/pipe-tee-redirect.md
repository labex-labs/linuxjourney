---
index: 4
lang: "es"
title: "tubería y tee"
meta_title: "tubería y tee - Text-Fu"
meta_description: "Aprende las tuberías de Linux y el comando tee para un flujo de datos eficiente en la línea de comandos. Comprende stdout, stdin y la salida de archivos. ¡Mejora tus habilidades en Linux!"
meta_keywords: "tubería Linux, comando tee, tutorial Linux, stdout, stdin, Linux para principiantes, línea de comandos, guía Linux"
---

## Lesson Content

Vamos a meternos en algo de "fontanería" ahora, bueno, no realmente, pero algo así. Probemos un comando:

```bash
ls -la /etc
```

Deberías ver una lista muy larga de elementos; en realidad, es un poco difícil de leer. En lugar de redirigir esta salida a un archivo, ¿no sería genial si pudiéramos ver la salida en otro comando como `less`? ¡Pues podemos!

```bash
ls -la /etc | less
```

El operador de tubería `|`, representado por una barra vertical, nos permite obtener la `stdout` de un comando y convertirla en la `stdin` para otro proceso. En este caso, tomamos la `stdout` de `ls -la /etc` y luego la _canalizamos_ al comando `less`. El comando pipe es extremadamente útil, y seguiremos usándolo por toda la eternidad.

Bueno, ¿y si quisiera escribir la salida de mi comando en dos flujos diferentes? Eso es posible con el comando `tee`:

```bash
ls | tee peanuts.txt
```

Deberías ver la salida de `ls` en tu pantalla, y si abres el archivo `peanuts.txt`, ¡deberías ver la misma información!

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la redirección de entrada/salida y las tuberías:

1. **[Redirección de entrada y salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practica el control del flujo de datos de los comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como `>`, `>>`, `2>` y el comando `tee`.
2. **[Control de secuencia y tubería](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Aprende a controlar las secuencias de ejecución de comandos, utilizar tuberías y aprovechar potentes herramientas de procesamiento de texto como `cut`, `grep`, `wc`, `sort` y `uniq`.
3. **[Redirección de flujo de datos](https://labex.io/es/labs/linux-data-stream-redirection-17995)** - Aprende el arte de la redirección de flujos en Linux, incluyendo la manipulación de los flujos de entrada, salida y error estándar, la combinación de salidas y la utilización de `/dev/null`.

Estos laboratorios te ayudarán a aplicar los conceptos de tuberías y redirección en escenarios reales y a desarrollar confianza con la manipulación de datos en la línea de comandos.

## Quiz Question

¿Qué tecla representa el operador de tubería?

## Quiz Answer

|
