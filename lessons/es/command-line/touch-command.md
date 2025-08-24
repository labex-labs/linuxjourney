---
index: 5
lang: "es"
title: "touch"
meta_title: "touch - Línea de Comandos"
meta_description: "Aprende a usar el comando Linux touch para crear nuevos archivos y actualizar marcas de tiempo. Esta guía amigable para principiantes te ayuda a entender la gestión de archivos."
meta_keywords: "comando touch, crear archivos, tutorial Linux, marcas de tiempo de archivos, Linux para principiantes, guía Linux, comandos básicos"
---

## Lesson Content

Aprendamos a crear algunos archivos. Una forma muy sencilla es usar el comando `touch`. `touch` te permite crear nuevos archivos vacíos.

```bash
touch mysuperduperfile
```

¡Y listo, nuevo archivo!

`touch` también se usa para cambiar las marcas de tiempo en archivos y directorios existentes. Inténtalo: haz un `ls -l` en un archivo y anota la marca de tiempo, luego `touch` ese archivo, y actualizará la marca de tiempo.

Hay muchas otras formas de crear archivos que involucran otras cosas como la redirección y los editores de texto, pero eso lo veremos en el curso de Manipulación de Texto.

## Exercise

1. Crea un archivo nuevo.
2. Anota la marca de tiempo.
3. Toca el archivo y verifica la marca de tiempo una vez más.

Para práctica adicional con la gestión de archivos, explora estos laboratorios interactivos:

- [Linux Directory Navigation](https://labex.io/es/labs/linux-directory-navigation-387844)
- [Setting Up a New Project Structure](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)

## Quiz Question

¿Cómo se crea un archivo llamado `myfile`?

## Quiz Answer

touch myfile
