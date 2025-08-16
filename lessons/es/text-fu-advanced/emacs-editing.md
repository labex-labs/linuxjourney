---
lang: "es"
title: "Edición en Emacs"
description: "Aprende los conceptos básicos de edición en Emacs: navega por el texto, corta y pega de manera eficiente. Esta guía para principiantes te ayuda a dominar los comandos esenciales de Emacs para Linux."
keywords: "Emacs, tutorial de Emacs, comandos de Emacs, editor de texto, editor de Linux, navegación en Emacs, Emacs para principiantes, guía de Emacs"
---

## Lesson Content

### Text Navigation

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

Con la navegación de texto, tus botones de texto habituales funcionan como deberían: Home, End, Page Up, Page Down y las teclas de flecha, etc.

### Cutting and Pasting

Para cortar (`kill`) o pegar (`yank`) en Emacs, primero necesitarás poder seleccionar texto. Para seleccionar texto, mueve el cursor a donde quieras cortar o pegar y presiona `C-space key`. Luego puedes usar las teclas de navegación para seleccionar el texto que desees. Ahora puedes cortar y pegar así:

```
C-w: cut
C-y: yank
```

## Exercise

Experimenta con la navegación de texto.

## Quiz Question

¿Cómo te mueves al final del buffer?

## Quiz Answer

M->
