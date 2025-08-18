---
lang: "es"
title: "stdout (Salida Estándar)"
meta_title: "stdout (Salida Estándar) - Text-Fu"
meta_description: "Aprende sobre stdout y la redirección de E/S en Linux. Entiende cómo redirigir la salida de comandos a archivos usando los operadores > y >>. ¡Comienza tu viaje en Linux hoy mismo!"
meta_keywords: "Linux stdout, redirección de E/S, comandos de Linux, redirigir salida, tutorial de Linux, Linux para principiantes, guía de Linux, scripting de shell"
---

## Lesson Content

A estas alturas, ya nos hemos familiarizado con muchos comandos y su salida, y eso nos lleva a nuestro siguiente tema: los flujos de E/S (entrada/salida). Ejecutemos el siguiente comando y luego discutiremos cómo funciona.

```bash
echo Hello World > peanuts.txt
```

¿Qué acaba de pasar? Bueno, revisa el directorio donde ejecutaste ese comando y, ¡sorpresa!, deberías ver un archivo llamado `peanuts.txt`. Mira dentro de ese archivo y deberías ver el texto "Hello World". Muchas cosas acaban de suceder en un solo comando, así que vamos a desglosarlo.

Primero, desglosemos la primera parte:

```bash
echo Hello World
```

Sabemos que esto imprime "Hello World" en la pantalla, pero ¿cómo? Los procesos utilizan flujos de E/S para recibir entrada y devolver salida. Por defecto, el comando `echo` toma la entrada (entrada estándar o stdin) del teclado y devuelve la salida (salida estándar o stdout) a la pantalla. Por eso, cuando escribes `echo Hello World` en tu shell, obtienes "Hello World" en la pantalla. Sin embargo, la redirección de E/S nos permite cambiar este comportamiento predeterminado, dándonos mayor flexibilidad de archivos.

Pasemos a la siguiente parte del comando:

```bash
>
```

El `>` es un operador de redirección que nos permite cambiar a dónde va la salida estándar. Nos permite enviar la salida de `echo Hello World` a un archivo en lugar de a la pantalla. Si el archivo no existe, lo creará por nosotros. Sin embargo, si ya existe, lo sobrescribirá (puedes añadir un flag de shell para evitar esto, dependiendo del shell que estés usando).

¡Y así es básicamente como funciona la redirección de stdout!

Bueno, digamos que no quería sobrescribir mi `peanuts.txt`. Afortunadamente, también hay un operador de redirección para eso: `>>`.

```bash
echo Hello World >> peanuts.txt
```

Esto añadirá "Hello World" al final del archivo `peanuts.txt`. Si el archivo no existe, lo creará por nosotros, ¡al igual que el redireccionador `>`!

## Exercise

Try a couple of commands:

```bash
ls -l /var/log > myoutput.txt
echo Hello World > rm
> somefile.txt
```

## Quiz Question

¿Qué redireccionador usas para añadir salida a un archivo?

## Quiz Answer

> >
