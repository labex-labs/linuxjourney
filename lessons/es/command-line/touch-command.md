---
index: 5
lang: "es"
title: "touch"
meta_title: "touch - Línea de Comandos"
meta_description: "Aprende a usar el comando Linux touch para crear nuevos archivos y actualizar marcas de tiempo. Esta guía para principiantes te ayuda a entender la gestión de archivos."
meta_keywords: "comando touch, crear archivos, tutorial Linux, marcas de tiempo de archivos, Linux para principiantes, guía Linux, comandos básicos"
---

## Lesson Content

Aprendamos cómo crear algunos archivos. Una forma muy sencilla es usar el comando `touch`. `touch` te permite crear nuevos archivos vacíos.

```bash
touch mysuperduperfile
```

¡Y listo, nuevo archivo!

`touch` también se usa para cambiar las marcas de tiempo en archivos y directorios existentes. Pruébalo: haz un `ls -l` en un archivo y anota la marca de tiempo, luego `touch` ese archivo, y actualizará la marca de tiempo.

Hay muchas otras formas de crear archivos que involucran otras cosas como la redirección y los editores de texto, pero llegaremos a eso en el curso de Manipulación de Texto.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión sobre la creación y gestión de objetos del sistema de archivos:

1. **[Comando Linux mkdir: Creación de directorios](https://labex.io/es/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprende a usar el comando `mkdir` en Linux para crear directorios, establecer permisos y organizar tu sistema de archivos. Esto te ayudará a comprender el concepto más amplio de crear nuevos elementos en el sistema de archivos.
2. **[Configuración de una nueva estructura de proyecto](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practica tus habilidades de gestión de directorios de Linux creando una estructura de proyecto específica y navegando a través de ella usando comandos esenciales como `mkdir` y `cd`.

Estos laboratorios te ayudarán a aplicar los conceptos de creación y organización del sistema de archivos en escenarios reales y a generar confianza con los comandos de Linux.

## Quiz Question

¿Cómo se crea un archivo llamado `myfile`?

## Quiz Answer

touch myfile
