---
index: 13
lang: "es"
title: "tr (Traducir)"
meta_title: "tr (Traducir) - Text-Fu"
meta_description: "Domina el comando tr de Linux para la traducción y eliminación de caracteres. Esta guía cubre cómo trtraducir caracteres, usar opciones como linux tr -d para eliminar caracteres, y proporciona ejemplos prácticos para la manipulación de texto."
meta_keywords: "tr, comando tr, trtraducir, linux tr -d, tr -d linux, traducir caracteres, eliminar caracteres, procesamiento de texto, comando Linux"
---

## Lesson Content

El comando `tr`, abreviatura de translate (traducir), es una utilidad de línea de comandos en Linux que traduce o elimina caracteres de la entrada estándar. Es una herramienta útil para la manipulación simple de texto y se utiliza a menudo con tuberías (pipes) para procesar la salida de otros comandos. La funcionalidad `trtranslate` es una parte central del procesamiento de texto.

### Traducción Básica de Caracteres

El uso más común de `tr` es sustituir un conjunto de caracteres por otro. Por ejemplo, puedes traducir fácilmente todos los caracteres en minúsculas a mayúsculas.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

En este ejemplo, canalizamos (`piped`) la salida de `echo` al comando `tr`. Luego, el comando `tr` tradujo el rango de caracteres `a-z` a los caracteres correspondientes en el rango `A-Z`.

### Eliminación de Caracteres con -d

Otra característica potente es la capacidad de eliminar caracteres específicos usando la opción `-d` (delete/eliminar). Esto es particularmente útil para limpiar texto. Por ejemplo, si deseas eliminar todos los dígitos de una cadena, puedes usar `linux tr -d`.

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Aquí, el comando `tr -d` eliminó cada carácter del conjunto especificado ('0' a '9') del flujo de entrada. Este es un patrón común para los usuarios de `tr -d linux`.

### Comprimir Caracteres Repetidos

El comando `tr` también puede "comprimir" (squeeze) caracteres repetidos en una sola instancia usando la opción `-s` (squeeze/comprimir). Esto es excelente para normalizar texto con espacios en blanco adicionales.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

En este caso, `tr -s ' '` reemplazó secuencias de múltiples espacios con un solo espacio, haciendo la salida mucho más limpia.

## Exercise

Para poner en práctica tus conocimientos, prueba el siguiente laboratorio práctico. Te ayudará a reforzar tu comprensión de la traducción de caracteres y el procesamiento de texto.

1. **[Comando Linux tr: Traducción de Caracteres](https://labex.io/es/labs/linux-linux-tr-command-character-translating-219198)** - Aprende el comando Linux `tr` para transformaciones a nivel de carácter en flujos de texto. Practicarás la traducción de caracteres, la eliminación de caracteres específicos, el trabajo con clases de caracteres y la compresión de caracteres repetidos.

Este laboratorio te ayudará a aplicar los conceptos de manipulación de texto en escenarios reales y a ganar confianza con el comando `tr`.

## Quiz Question

Qué comando se utiliza para traducir caracteres? (Por favor, responda solo con letras inglesas en minúsculas)

## Quiz Answer

tr
