---
index: 13
lang: "es"
title: "tr (Traducir)"
meta_title: "tr (Traducir) - Text-Fu"
meta_description: "Aprende el comando Linux tr con ejemplos para traducir caracteres, eliminar caracteres, comprimir repeticiones, usar clases de caracteres y limpiar texto."
meta_keywords: "comando linux tr, comando tr, tr -d, tr -s, traducir caracteres, eliminar caracteres, clases de caracteres, procesamiento de texto linux"
---

## Lesson Content

El comando `tr`, abreviatura de traducir, es una utilidad de línea de comandos que traduce, elimina o comprime caracteres desde la entrada estándar. Es útil para manipulaciones simples de texto y se usa a menudo con tuberías para procesar la salida de otros comandos.

La sintaxis básica es:

```bash
tr [OPTIONS] SET1 [SET2]
```

A diferencia de herramientas como `sed` o `awk`, `tr` trabaja carácter por carácter. No entiende palabras, columnas o expresiones regulares de la misma manera. Esto lo hace rápido y simple para tareas como cambiar mayúsculas y minúsculas, eliminar dígitos y normalizar espacios repetidos.

### Traducción básica de caracteres

El uso más común de `tr` es sustituir un conjunto de caracteres por otro. Por ejemplo, puedes traducir fácilmente todos los caracteres en minúscula a mayúscula.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

En este ejemplo, canalizamos la salida de `echo` al comando `tr`. El comando `tr` luego tradujo el rango de caracteres `a-z` a los caracteres correspondientes en el rango `A-Z`.

También puedes traducir un carácter a otro:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

Cada carácter en `SET1` se asigna al carácter en la misma posición en `SET2`.

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Aquí, `a` se convierte en `A`, `b` en `B` y `c` en `C`.

### Eliminar caracteres con -d

Otra característica poderosa es la capacidad de eliminar caracteres específicos usando la opción `-d`. Esto es particularmente útil para limpiar texto. Por ejemplo, si quieres eliminar todos los dígitos de una cadena, puedes usar:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Aquí, `tr -d` eliminó cada carácter en el conjunto especificado, desde `0` hasta `9`.

Puedes eliminar signos de puntuación de una cadena usando una clase de caracteres:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

También puedes eliminar caracteres de nueva línea para unir líneas:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

### Comprimir caracteres repetidos

El comando `tr` también puede "comprimir" caracteres repetidos en una sola instancia usando la opción `-s`. Esto es ideal para normalizar texto con espacios en blanco extra.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

En este caso, `tr -s ' '` reemplazó secuencias de múltiples espacios con un solo espacio, haciendo la salida mucho más limpia.

También puedes comprimir saltos de línea repetidos:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

### Uso de clases de caracteres

Las clases de caracteres hacen que los comandos `tr` sean más fáciles de leer y más portables. Las clases comunes incluyen:

- `[:lower:]`: Letras minúsculas.
- `[:upper:]`: Letras mayúsculas.
- `[:digit:]`: Dígitos.
- `[:alpha:]`: Letras.
- `[:alnum:]`: Letras y dígitos.
- `[:space:]`: Caracteres de espacio en blanco.
- `[:punct:]`: Caracteres de puntuación.

Por ejemplo, convierte texto en minúsculas a mayúsculas con clases de caracteres:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

Elimina todo excepto letras y dígitos usando `-c` con `-d`. La opción `-c` significa complemento, o "todo lo que no está en este conjunto."

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

### Combinando eliminar y comprimir

Puedes combinar opciones al limpiar texto. Este ejemplo elimina puntuación y luego comprime espacios repetidos:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Para entrada separada por tabuladores, puedes traducir tabuladores en comas:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

### Opciones comunes de tr

Aquí están las opciones que usarás más a menudo:

- `-d`: Elimina caracteres en `SET1`.
- `-s`: Comprime caracteres repetidos en `SET1`.
- `-c`: Usa el complemento de `SET1`.
- `-t`: Trunca `SET1` a la longitud de `SET2` antes de traducir.

### Preguntas comunes

**¿Por qué tr lee desde una tubería?** `tr` lee desde la entrada estándar, por lo que se usa comúnmente después de comandos como `echo`, `cat`, `printf` u otros comandos que producen texto.

**¿tr reemplaza palabras?** No. `tr` traduce caracteres, no palabras. Usa `sed` cuando necesites reemplazar palabras completas o patrones.

**¿Por qué mi comando tr cambió caracteres uno por uno?** Así es como funciona `tr`. Mapea cada carácter en `SET1` al carácter correspondiente en `SET2`.

**¿Por qué debo poner entre comillas conjuntos como 'a-z'?** Poner entre comillas evita que la shell interprete caracteres especiales antes de que `tr` los reciba.

## Exercise

To put your knowledge into practice, try the following hands-on lab. It will help you reinforce your understanding of character translation and text processing.

1. **[Linux tr Command: Character Translating](https://labex.io/es/labs/linux-linux-tr-command-character-translating-219198)** - Aprende el comando Linux `tr` para transformaciones a nivel de caracteres en flujos de texto. Practicarás traducir caracteres, eliminar caracteres específicos, trabajar con clases de caracteres y comprimir caracteres repetidos.

This lab will help you apply the concepts of text manipulation in real scenarios and build confidence with the `tr` command.

## Quiz Question

¿Qué comando se usa para traducir caracteres? (Por favor responde solo con letras minúsculas en inglés)

## Quiz Answer

tr
