---
index: 12
lang: "es"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "Aprende a usar el comando sort de Linux para ordenar archivos de texto. Descubre opciones como la ordenación inversa y numérica. ¡Mejora tus habilidades en la línea de comandos de Linux!"
meta_keywords: "comando sort de Linux, sort -r, sort -n, tutorial de Linux, línea de comandos, Linux para principiantes, guía de sort"
---

## Lesson Content

El comando `sort` es útil para ordenar líneas.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

También puedes hacer un orden inverso:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

Y también ordenar por valor numérico:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del comando `sort` y el procesamiento de texto:

1. **[Comando sort de Linux: Ordenación de texto](https://labex.io/es/labs/linux-linux-sort-command-text-sorting-219196)** - Este laboratorio proporciona una introducción directa al comando `sort`, permitiéndote practicar la ordenación de líneas de archivos de texto de varias maneras, incluyendo orden ascendente y descendente.
2. **[Conteo de palabras y ordenación](https://labex.io/es/labs/linux-word-count-and-sorting-388125)** - En este desafío, aplicarás tus conocimientos de ordenación junto con el conteo de palabras para analizar datos de texto, ayudándote a encontrar patrones frecuentes y ordenar datos de manera eficiente.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con la manipulación y ordenación de texto en Linux.

## Quiz Question

¿Qué bandera usas para realizar una ordenación inversa?

## Quiz Answer

-r
