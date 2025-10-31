---
index: 8
lang: "es"
title: "Guardar y Salir en Vim"
meta_title: "Guardar y Salir en Vim - Dominio Avanzado de Texto"
meta_description: "Aprenda a guardar en el editor Vim usando comandos como :w. Domine cómo guardar y salir con :wq o ZZ. Esta guía cubre los comandos esenciales de linux wq y vi escribir y salir para una gestión eficiente de archivos en Vim."
meta_keywords: "vim cómo guardar, linux wq, vi escribir y salir, vim cómo guardar y salir, cómo guardar en el editor vim, guardar archivo vim, salir de vim, comandos de vim"
---

## Lesson Content

Después de terminar de editar un archivo, el siguiente paso es guardar los cambios y salir del editor. Vim proporciona varios comandos para este propósito, cada uno con una función específica. Todos estos comandos se ejecutan en el modo de línea de comandos, al que se accede presionando `:`.

### Cómo Guardar en el Editor Vim

Para guardar los cambios que has realizado en un archivo sin salir, utilizas el comando de escritura (write). Esta es la respuesta fundamental a la pregunta "vim cómo guardar".

- `:w` - Escribe (guarda) el estado actual del archivo en el disco.

### Salir de Vim

Si deseas salir del editor, tienes un par de opciones dependiendo de si quieres guardar tus cambios o no.

- `:q` - Sale del editor. Este comando solo funciona si no tienes cambios sin guardar.
- `:q!` - Sale del editor y descarta cualquier cambio no guardado. Esto es útil cuando has cometido errores y deseas revertir a la última versión guardada del archivo.

### Vim Cómo Guardar y Salir

Combinar el guardado y la salida es un flujo de trabajo muy común. El comando `linux wq` es un elemento básico para muchos desarrolladores que trabajan en la línea de comandos.

- `:wq` - Este comando primero escribe (guarda) el archivo y luego sale. Es una acción combinada para mayor eficiencia. Muchos usuarios buscan `vi escribir y salir` (vi write and quit), y este comando funciona tanto para Vi como para Vim.
- `ZZ` - Este es un atajo equivalente a `:wq`. Guarda el archivo si ha sido modificado y luego sale. Es un carácter menos para escribir y uno de los favoritos entre los usuarios experimentados de Vim.

### Deshacer y Rehacer Cambios

Mientras editas, es posible que necesites revertir una acción o volver a aplicarla. Estos comandos se utilizan en el modo Normal (presiona `Esc` para entrar).

- `u` - Deshace tu última acción.
- `Ctrl-r` - Rehace la última acción que deshiciste.

Dominar estos comandos básicos es el primer paso hacia la competencia en Vim. A medida que te sientas más cómodo, descubrirás que estas operaciones se vuelven instintivas. Para funciones más avanzadas, la documentación oficial de Vim es un recurso excelente.

## Exercise

Para dominar estos comandos, la práctica directa es esencial. El siguiente laboratorio proporciona un escenario del mundo real para ayudarte a reforzar tus habilidades de edición de texto en Vim.

1. **[Editar Archivos de Texto en Linux con Vim y Nano](https://labex.io/es/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación de archivos, la edición de texto, el guardado de archivos y la navegación tanto con Vim como con Nano. Este laboratorio solidificará tu comprensión de las operaciones básicas de Vim, incluido cómo guardar y salir.

Completar este laboratorio te ayudará a aplicar estos conceptos y a ganar confianza con la edición de texto en un entorno Linux.

## Quiz Question

¿Cómo sales de Vim sin guardar tus cambios? Por favor, proporciona el comando exacto en inglés, prestando atención a las mayúsculas y los caracteres especiales.

## Quiz Answer

:q
