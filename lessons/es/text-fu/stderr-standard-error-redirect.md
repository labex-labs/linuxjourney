---
index: 3
lang: "es"
title: "stderr (Error Estándar)"
meta_title: "stderr (Error Estándar) - Text-Fu"
meta_description: "Aprenda sobre la redirección de stderr (error estándar) en Linux. Entienda 2>, 2>&1, &> y /dev/null para el manejo de errores en Bash. ¡Mejore sus habilidades de línea de comandos en Linux!"
meta_keywords: "Linux stderr, error estándar, redirección 2>, 2>&1, redirección &>, /dev/null, manejo de errores Bash, tutorial Linux, Linux para principiantes"
---

## Lesson Content

Intentemos algo un poco diferente ahora. Intentemos listar el contenido de un directorio que no existe en su sistema y redirigir la salida al archivo `peanuts.txt` nuevamente.

```bash
ls /fake/directory > peanuts.txt
```

Lo que debería ver es:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Ahora probablemente esté pensando, ¿no debería haberse enviado ese mensaje al archivo? En realidad, hay otra secuencia de E/S en juego aquí llamada error estándar (stderr). Por defecto, stderr también envía su salida a la pantalla; es una secuencia completamente diferente de stdout. Por lo tanto, deberá redirigir su salida de una manera diferente.

Desafortunadamente, el redireccionador no es tan agradable como usar `<` o `>` pero está bastante cerca. Tendremos que usar descriptores de archivo. Un descriptor de archivo es un número no negativo que se utiliza para acceder a un archivo o secuencia. Profundizaremos en esto más adelante, pero por ahora sepa que el descriptor de archivo para stdin, stdout y stderr es 0, 1 y 2 respectivamente.

Así que ahora, si queremos redirigir nuestro stderr al archivo, podemos hacer esto:

```bash
ls /fake/directory 2> peanuts.txt
```

Debería ver solo los mensajes de stderr en `peanuts.txt`.

Ahora, ¿qué pasa si quisiera ver tanto stderr como stdout en el archivo `peanuts.txt`? Es posible hacer esto también con descriptores de archivo:

```bash
ls /fake/directory > peanuts.txt 2>&1
```

Esto envía los resultados de `ls /fake/directory` al archivo `peanuts.txt` y luego redirige stderr a stdout a través de `2>&1`. El orden de las operaciones aquí importa; `2>&1` envía stderr a donde sea que stdout esté apuntando. En este caso, stdout está apuntando a un archivo, por lo que `2>&1` también envía stderr a un archivo. Entonces, si abre ese archivo `peanuts.txt`, debería ver tanto stderr como stdout. En nuestro caso, el comando anterior solo produce stderr.

Hay una forma más corta de redirigir tanto stdout como stderr a un archivo:

```bash
ls /fake/directory &> peanuts.txt
```

Ahora, ¿qué pasa si no quiero nada de esa basura y quiero deshacerme de los mensajes de stderr por completo? Bueno, también puede redirigir la salida a un archivo especial llamado `/dev/null` y descartará cualquier entrada.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la redirección de entrada/salida:

1. **[Redirección de entrada y salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - En este laboratorio, aprenderá a redirigir la entrada y la salida en el shell de Linux. Practicará el control del flujo de datos de los comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) utilizando operadores como >, >>, 2> y el comando tee.

Este laboratorio le ayudará a aplicar los conceptos de redirección de E/S en escenarios reales y a generar confianza en la gestión de flujos de datos en Linux.

## Quiz Question

¿Cuál es el redireccionador para stderr?

## Quiz Answer

2>
