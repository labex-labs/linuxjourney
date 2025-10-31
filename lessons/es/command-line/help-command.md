---
index: 15
lang: "es"
title: "ayuda"
meta_title: "ayuda - Línea de Comandos"
meta_description: "Descubre cómo usar el comando help de Linux para obtener asistencia rápida en tu terminal. Este tutorial de Bash explica cómo obtener ayuda para comandos integrados del shell y usar la bandera --help para otros programas de Linux."
meta_keywords: "comando help Linux, ayuda Bash, ayuda línea de comandos, comandos Linux, Linux principiantes, tutorial Linux, tutorial Bash, shell integrado, asistencia línea de comandos"
---

## Lesson Content

Cuando trabajas en la línea de comandos de Linux, a menudo necesitarás un recordatorio rápido de cómo funciona un comando o qué opciones acepta. Afortunadamente, Linux proporciona excelentes herramientas para obtener ayuda en la línea de comandos directamente en la terminal.

### El comando 'help' para comandos internos de Bash

Una de las herramientas más directas es `help`, un comando que está integrado directamente en el shell Bash. Está diseñado específicamente para proporcionar información sobre otros comandos internos de Bash. Un comando interno es parte del shell en sí, no un programa separado. Los ejemplos incluyen `echo`, `cd` y `pwd`.

Para usar el **comando help de Linux**, simplemente escribe `help` seguido del nombre del comando interno.

```bash
help echo
```

Esto mostrará un resumen del comando `echo`, su sintaxis y una lista de opciones disponibles. Esta es la forma más rápida de obtener asistencia para funciones específicas del shell.

### La opción --help para programas ejecutables

Para la mayoría de los otros programas ejecutables que no están integrados en el shell, el comando `help` no funcionará. En su lugar, una convención común es proporcionar una opción `--help`. Esta opción indica al programa que imprima un resumen de uso y luego salga.

```bash
ls --help
```

Aunque la mayoría de los desarrolladores se adhieren a este estándar, no es universal. Sin embargo, probar la opción `--help` suele ser el mejor primer paso para encontrar ayuda para un programa desconocido. Es una habilidad fundamental para cualquiera que esté aprendiendo sobre **comandos de Linux**.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Cómo se obtiene ayuda rápida en la línea de comandos para comandos internos de Bash? (Por favor, proporcione el nombre del comando único en inglés y en minúsculas.)

## Quiz Answer

help
