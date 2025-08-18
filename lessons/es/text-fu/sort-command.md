---
lang: "es"
title: "sort"
meta_description: "Aprende a usar el comando sort de Linux para ordenar archivos de texto. Descubre opciones como el orden inverso y numérico. ¡Mejora tus habilidades en la línea de comandos de Linux!"
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

El verdadero poder de `sort` reside en su capacidad para combinarse con otros comandos. Prueba el siguiente comando y observa qué sucede:

```bash
ls /etc | sort -rn
```

## Quiz Question

¿Qué bandera utilizas para realizar un orden inverso?

## Quiz Answer

-r
