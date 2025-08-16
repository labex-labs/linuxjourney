---
lang: "es"
title: "join y split"
description: "Aprenda a usar los comandos 'join' y 'split' de Linux para la manipulación de archivos. Comprenda cómo combinar archivos por campos comunes y dividir archivos grandes de manera eficiente. Obtenga ejemplos prácticos y consejos."
keywords: "comando Linux join, comando Linux split, manipulación de archivos, tutorial de Linux, línea de comandos, Linux para principiantes, guía de Linux"
---

## Lesson Content

El comando `join` le permite unir varios archivos por un campo común:

Supongamos que tengo dos archivos que quiero unir:

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

¿Ves cómo unió mis archivos? Se unen por el primer campo por defecto, y los campos tienen que ser idénticos. Si no lo son, puedes ordenarlos. En este caso, los archivos se unen a través de 1, 2, 3.

¿Cómo uniríamos los siguientes archivos?

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

Para unir este archivo, debe especificar qué campos está uniendo. En este caso, queremos el campo 2 en `file1.txt` y el campo 1 en `file2.txt`, por lo que el comando se vería así:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` se refiere a `file1.txt` y `-2` se refiere a `file2.txt`. Bastante ingenioso. También puede dividir un archivo en diferentes archivos con el comando `split`:

```bash
split somefile
```

Esto lo dividirá en diferentes archivos. Por defecto, los dividirá una vez que alcancen un límite de 1000 líneas. Los archivos se nombran `x**` por defecto.

## Exercise

Join two files with a different number of lines in each file. What happens?

## Quiz Question

¿Qué comando usaría para unir archivos llamados `cat`, `dog`, `cow`?

## Quiz Answer

join cat dog cow
