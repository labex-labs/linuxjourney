---
index: 4
lang: "es"
title: "pipe y tee"
meta_title: "pipe y tee - Text-Fu"
meta_description: "Aprende los pipes de Linux y el comando tee para un flujo de datos eficiente en la línea de comandos. Comprende stdout, stdin y la salida de archivos. ¡Mejora tus habilidades en Linux!"
meta_keywords: "pipe de Linux, comando tee, tutorial de Linux, stdout, stdin, Linux para principiantes, línea de comandos, guía de Linux"
---

## Lesson Content

Vamos a meternos en algo de "fontanería" ahora, no literalmente, pero algo parecido. Intentemos un comando:

```bash
ls -la /etc
```

Deberías ver una lista muy larga de elementos; en realidad, es un poco difícil de leer. En lugar de redirigir esta salida a un archivo, ¿no sería bueno si pudiéramos ver la salida directamente en otro comando como `less`? ¡Pues podemos!

```bash
ls -la /etc | less
```

El operador pipe `|`, representado por una barra vertical, nos permite obtener el `stdout` de un comando y convertirlo en el `stdin` para otro proceso. En este caso, tomamos el `stdout` de `ls -la /etc` y luego lo _canalizamos_ al comando `less`. El comando pipe es extremadamente útil y seguiremos usándolo por toda la eternidad.

Bueno, ¿qué pasa si quiero escribir la salida de mi comando en dos flujos diferentes? Eso es posible con el comando `tee`:

```bash
ls | tee peanuts.txt
```

Deberías ver la salida de `ls` en tu pantalla, y si abres el archivo `peanuts.txt`, ¡deberías ver la misma información!

## Exercise

Try the following commands:

```bash
ls | tee peanuts.txt banan.txt
```

## Quiz Question

¿Qué tecla representa el operador pipe?

## Quiz Answer

|
