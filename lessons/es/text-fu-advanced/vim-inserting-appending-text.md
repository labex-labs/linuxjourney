---
title: "Vim: Insertar y Añadir Texto"
description: "Aprende los modos de inserción y adición de Vim. Entiende los comandos 'i', 'a', 'I', 'A', 'o', 'O' para una edición de texto eficiente. ¡Mejora tus habilidades con Vim ahora!"
keywords: "modo de inserción Vim, añadir en Vim, comandos Vim, tutorial Vim, editor de texto Linux, Vim para principiantes, guía Vim, Vim 'i' 'a'"
---

## Lesson Content

Vim tiene dos modos principales que usarás a menudo: el modo Normal (para comandos) y el modo Insertar (para escribir texto).

- Presiona `Esc` para volver al modo Normal en cualquier momento.

Entra en el modo Insertar de diferentes maneras, dependiendo de dónde quieras escribir:

- `i` – inserta antes del cursor
- `a` – añade después del cursor
- `I` – inserta al principio de la línea actual
- `A` – añade al final de la línea actual
- `o` – abre una nueva línea debajo de la línea actual y comienza a insertar
- `O` – abre una nueva línea encima de la línea actual y comienza a insertar

Consejo: Puedes prefijar estos comandos con un número. Por ejemplo, `3o` abre tres nuevas líneas debajo.

Cuando hayas terminado de insertar texto, presiona `Esc` para volver al modo Normal.

## Exercise

Open any text file with `vim [file]` and try: `i`, `a`, `I`, `A`, `o`, `O`, then press `Esc` after each to return to Normal mode.

## Quiz Question

¿Qué tecla entra en el modo Insertar antes del cursor?

## Quiz Answer

i
