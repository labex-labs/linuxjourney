---
index: 7
lang: "es"
title: "Edición en Vim"
meta_title: "Edición en Vim - Text-Fu Avanzado"
meta_description: "Aprende los conceptos básicos de edición en Vim: eliminar, cambiar, copiar y pegar texto de manera eficiente. Domina los comandos esenciales de Vim para principiantes y mejora tus habilidades de edición de texto en Linux."
meta_keywords: "edición Vim, comandos Vim, editor de texto Linux, tutorial Vim, guía Vim, Vim para principiantes, comando dd, eliminar en Vim"
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

Cambios (operador `c`, elimina y luego entra en modo Insert):

- `cw` – cambia la palabra desde el cursor
- `c$` – cambia hasta el final de la línea
- `cc` – cambia toda la línea

Yank y Put (copiar/pegar):

- `yw` – yank word
- `yy` – yank the current line
- `p` – put (pegar) después del cursor o debajo de la línea
- `P` – put (pegar) antes del cursor o encima de la línea

Reemplazar y otras ediciones útiles:

- `r{char}` – reemplaza el carácter bajo el cursor con `{char}`
- `R` – entra en modo Replace para sobrescribir texto
- `J` – une la línea actual con la siguiente línea
- `.` – repite el último cambio

Combina operadores con movimientos para mayor potencia: `d}` elimina hasta el siguiente párrafo; `caw` cambia “a word” (palabra bajo el cursor incluyendo el espacio circundante).

## Exercise

Open a file with `vim [file]` and try: `dw`, `cw`, `yy` then `p`, `dd`, `J`, and `.` to repeat a change.

## Quiz Question

¿Qué comando elimina la línea actual en Vim?

## Quiz Answer

dd
