---
index: 5
lang: "es"
title: "touch"
meta_title: "touch - Command Line"
meta_description: "Aprende a usar el comando Linux touch para crear nuevos archivos y actualizar las marcas de tiempo. Esta guía para principiantes te ayuda a entender la gestión de archivos."
meta_keywords: "comando touch, crear archivos, tutorial de Linux, marcas de tiempo de archivos, Linux para principiantes, guía de Linux, comandos básicos"
---

## Lesson Content

Aprendamos cómo crear algunos archivos. Una forma muy sencilla es usar el comando `touch`. `touch` te permite crear nuevos archivos vacíos.

```bash
touch mysuperduperfile
```

¡Y listo, nuevo archivo!

`touch` también se usa para cambiar las marcas de tiempo en archivos y directorios existentes. Inténtalo: haz un `ls -l` en un archivo y anota la marca de tiempo, luego `touch` ese archivo, y actualizará la marca de tiempo.

Hay muchas otras formas de crear archivos que involucran otras cosas como la redirección y los editores de texto, pero llegaremos a eso en el curso de Manipulación de Texto.

## Exercise

1. Crea un archivo nuevo.
2. Anota la marca de tiempo.
3. Toca el archivo y verifica la marca de tiempo una vez más.

## Quiz Question

¿Cómo se crea un archivo llamado `myfile`?

## Quiz Answer

touch myfile
