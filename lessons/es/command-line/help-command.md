---
index: 15
lang: "es"
title: "help"
meta_title: "help - Línea de Comandos"
meta_description: "Aprende cómo obtener ayuda en la línea de comandos de Linux con Bash help, salida --help, páginas man y type para comandos internos y externos."
meta_keywords: "comando help linux, ayuda bash, ayuda línea de comandos, --help, comando interno shell, comando man, comando type"
---

## Lesson Content

Cuando trabajas en la línea de comandos de Linux, a menudo necesitarás un recordatorio rápido de cómo funciona un comando o qué opciones acepta. Linux proporciona varias herramientas de ayuda directamente en el terminal.

### El comando 'help' para comandos internos de Bash

Una de las herramientas más directas es `help`, un comando que está integrado directamente en el shell Bash. Está diseñado específicamente para proporcionar información sobre otros comandos internos de Bash. Un comando interno es parte del propio shell, no un programa separado. Ejemplos incluyen `echo`, `cd` y `pwd`.

Para usar `help`, escríbelo seguido del nombre del comando interno.

```bash
$ help echo
```

Esto mostrará un resumen del comando `echo`, su sintaxis y una lista de opciones disponibles. Esta es la forma más rápida de obtener asistencia para funciones específicas del shell.

### La opción --help para programas ejecutables

Para la mayoría de los otros programas ejecutables que no están integrados en el shell, el comando `help` no funcionará. En cambio, una convención común es proporcionar una opción `--help`. Esta opción indica al programa que imprima un resumen de uso y luego termine.

```bash
$ ls --help
```

Aunque la mayoría de los desarrolladores siguen este estándar, no es universal. Probar `--help` suele ser un buen primer paso para un programa desconocido.

### Encontrar el tipo de comando

Si no estás seguro de si un comando es un interno de Bash o un programa externo, usa `type`.

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

Esto te ayuda a elegir entre `help cd`, `ls --help` o `man ls`.

### Elegir la herramienta de ayuda adecuada

- Usa `help COMMAND` para comandos internos de Bash como `cd`, `echo` y `history`.
- Usa `COMMAND --help` para un resumen rápido de muchos comandos externos.
- Usa `man COMMAND` para páginas de manual detalladas.
- Usa `whatis COMMAND` para una descripción de una línea.

### Preguntas comunes

**¿Por qué no funciona help ls?** `ls` suele ser un programa externo, no un comando interno de Bash. Prueba `ls --help` o `man ls`.

**¿Por qué no funciona --help para todos los comandos?** Es una convención, no una regla estricta.

**¿Cuál es la forma más rápida de consultar un comando?** Prueba `COMMAND --help` para comandos externos y `help COMMAND` para comandos internos de Bash.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

How do you get quick command-line help for built-in Bash commands? (Please provide the single command name in English and in lowercase.)

## Quiz Answer

help
