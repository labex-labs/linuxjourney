---
index: 7
lang: "es"
title: "Edición Vim"
meta_title: "Edición Vim - Text-Fu Avanzado"
meta_description: "Aprende los conceptos básicos de edición de Vim: elimina, cambia, copia y pega texto de manera eficiente. Domina los comandos esenciales de Vim para principiantes y mejora tus habilidades de edición de texto en Linux."
meta_keywords: "edición Vim, comandos Vim, editor de texto Linux, tutorial Vim, guía Vim, Vim para principiantes, comando dd, eliminar Vim"
---

## Lesson Content

La edición en Vim se realiza desde el modo Normal utilizando operadores y movimientos. Puedes eliminar, cambiar, copiar (yank), pegar (put) y reemplazar texto de manera eficiente.

- Presiona `Esc` para asegurarte de estar en modo Normal antes de usar estos comandos.

Eliminar (operador `d`):

- `x` – elimina el carácter bajo el cursor
- `dw` – elimina desde el cursor hasta el inicio de la siguiente palabra
- `d$` – elimina desde el cursor hasta el final de la línea
- `dd` – elimina la línea actual
- Se aplican los conteos: `3dd` elimina tres líneas; `2dw` elimina dos palabras

Cambios (operador `c`, elimina y luego entra en modo Insertar):

- `cw` – cambia la palabra desde el cursor
- `c$` – cambia hasta el final de la línea
- `cc` – cambia toda la línea

Yank y Put (copiar/pegar):

- `yw` – copia la palabra
- `yy` – copia la línea actual
- `p` – pega después del cursor o debajo de la línea
- `P` – pega antes del cursor o encima de la línea

Reemplazar y otras ediciones útiles:

- `r{char}` – reemplaza el carácter bajo el cursor con `{char}`
- `R` – entra en modo Reemplazar para sobrescribir texto
- `J` – une la línea actual con la siguiente línea
- `.` – repite el último cambio

Combina operadores con movimientos para mayor potencia: `d}` elimina hasta el siguiente párrafo; `caw` cambia "una palabra" (palabra bajo el cursor incluyendo el espacio circundante).

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de la edición de texto en Vim:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/es/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación de archivos, la edición de texto, el guardado de archivos y la navegación con vi/vim y nano. Este laboratorio te ayudará a dominar los comandos de edición fundamentales discutidos, como eliminar, cambiar, copiar y pegar texto.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a generar confianza con la edición de texto en Linux.

## Quiz Question

¿Qué comando elimina la línea actual en Vim?

## Quiz Answer

dd
