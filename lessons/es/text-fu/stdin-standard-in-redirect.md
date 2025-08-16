---
title: "stdin (Entrada Estándar)"
description: "Aprende sobre la redirección de stdin (entrada estándar) en Linux. Comprende cómo usar el operador '<' con archivos y comandos. Explora ejemplos prácticos y mejora tus habilidades en la línea de comandos de Linux."
keywords: "stdin, entrada estándar, redirección de Linux, operador <, tutorial de Linux, línea de comandos, principiante, guía"
---

## Lesson Content

En nuestra lección anterior, aprendimos que tenemos diferentes flujos de stdout que podemos usar, como un archivo o la pantalla. Bueno, también hay diferentes flujos de entrada estándar (stdin) que podemos usar. Sabemos que tenemos stdin de dispositivos como el teclado, pero también podemos usar archivos, la salida de otros procesos y la terminal. Veamos un ejemplo.

Usemos el archivo `peanuts.txt` de la lección anterior para este ejemplo. Recuerda, contenía el texto "Hello World".

```bash
cat < peanuts.txt > banana.txt
```

Así como teníamos `>` para la redirección de stdout, podemos usar `<` para la redirección de stdin.

Normalmente, en el comando `cat`, le envías un archivo y ese archivo se convierte en el stdin. En este caso, redirigimos `peanuts.txt` para que fuera nuestro stdin. Luego, la salida de `cat peanuts.txt`, que sería "Hello World", se redirige a otro archivo llamado `banana.txt`.

## Exercise

Prueba un par de comandos:

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

¿Qué redirigidor usas para redirigir stdin?

## Quiz Answer

<
