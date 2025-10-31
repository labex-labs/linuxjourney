---
index: 1
lang: "es"
title: "stdout (Salida Estándar)"
meta_title: "stdout (Salida Estándar) - Text-Fu"
meta_description: "Comienza tu viaje para aprender Linux dominando la salida estándar (stdout) y la redirección de E/S. Esta lección cubre cómo redirigir la salida de comandos a archivos usando los operadores > y >>, una habilidad fundamental para cualquier usuario de Linux."
meta_keywords: "Linux, aprender linux, stdout, redirección E/S, salida estándar, redirigir salida, bash, scripting shell, comandos Linux, tutorial Linux"
---

## Lesson Content

A medida que continúas aprendiendo Linux, has visto cómo los comandos producen salida. Esto nos lleva al importante tema de las transmisiones de E/S (entrada/salida), específicamente la salida estándar o **stdout**. Exploremos este concepto ejecutando el siguiente comando:

```bash
echo Hola Mundo > cacahuetes.txt
```

Después de ejecutar esto, encontrarás un nuevo archivo llamado `cacahuetes.txt` en tu directorio actual. Si ves su contenido, verás el texto "Hola Mundo". Analicemos lo que sucedió.

### Entendiendo la Salida Estándar (stdout)

Primero, considera el comando sin el carácter especial:

```bash
echo Hola Mundo
```

Por defecto, muchos comandos envían sus resultados a **stdout**, que es la pantalla de tu terminal. Por eso `echo Hola Mundo` muestra el texto directamente en tu shell. Los procesos utilizan transmisiones de E/S para recibir entrada (entrada estándar o stdin) y enviar salida. La redirección de E/S nos permite cambiar este comportamiento predeterminado, dándonos un mayor control sobre nuestros datos.

### Redirección de stdout con >

El carácter `>` es un operador de redirección. Intercepta los datos que se dirigen a **stdout** y los envía a un nuevo destino.

```bash
>
```

En nuestro ejemplo, envía la salida de `echo Hola Mundo` a un archivo en lugar de a la pantalla. Si el archivo no existe, se creará. **Ten cuidado**, ya que si el archivo ya existe, este operador sobrescribirá completamente su contenido.

### Anexar stdout con >>

¿Qué pasa si quieres añadir contenido a un archivo sin borrar su contenido? Para eso, usamos el operador `>>`.

```bash
echo Hola Mundo >> cacahuetes.txt
```

Este operador anexa la salida al final del archivo especificado. Si el archivo no existe previamente, se creará, al igual que el operador `>`.
Manejar la redirección de **stdout** es un paso fundamental en tu camino en Linux.

## Exercise

Para solidificar tu comprensión de la redirección de E/S, prueba este laboratorio práctico:

1. **[Redirección de Entrada y Salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practica el control del flujo de datos desde comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como `>`, `>>`, `2>`, y el comando `tee`.

Este laboratorio te ayudará a aplicar estos conceptos en escenarios del mundo real y a ganar confianza con la redirección de E/S.

## Quiz Question

¿Qué redireccionador usas para anexar salida a un archivo?

## Quiz Answer

`>>`
