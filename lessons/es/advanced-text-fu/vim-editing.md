---
index: 7
lang: "es"
title: "Edición en Vim"
meta_title: "Edición en Vim - Trucos de Texto Avanzados"
meta_description: "Un tutorial de Vim para principiantes sobre comandos de edición esenciales. Aprende a borrar, cambiar, copiar (yank) y pegar texto en el editor de texto Vim para mejorar tu flujo de trabajo en Linux."
meta_keywords: "edición Vim, comandos Vim, editor de texto Linux, tutorial Vim, guía Vim, Vim para principiantes, comando dd, borrar en Vim"
---

## Lesson Content

Editar texto en Vim es una característica potente que se basa en combinar operadores y movimientos desde el modo Normal. Este enfoque le permite eliminar, cambiar, copiar (yank) y pegar (put) texto de manera eficiente. Antes de ejecutar cualquier comando, presione `Esc` para asegurarse de estar en el modo Normal.

### Entendiendo los Operadores y Movimientos de Vim

El núcleo de la edición en Vim es la fórmula: `operador + movimiento`. Un operador es una acción (como `d` para eliminar), y un movimiento es un desplazamiento (como `w` para palabra). Por ejemplo, `dw` combina el operador de eliminar con el movimiento de palabra para borrar una palabra. También puede usar contadores para repetir una acción, como `2dw` para eliminar dos palabras.

### Eliminar Texto en Vim

El operador de eliminación es `d`. Es uno de los comandos de Vim más comunes para la manipulación de texto.

- `x` – Elimina el carácter directamente bajo el cursor.
- `dw` – Elimina desde el cursor hasta el principio de la siguiente palabra.
- `d$` – Elimina desde el cursor hasta el final de la línea actual.
- `dd` – El comando `dd` elimina la línea actual completa.
- `3dd` – Elimina tres líneas, comenzando desde la línea actual.

### Cambiar Texto

El operador de cambio, `c`, funciona de manera similar a eliminar, pero lo coloca en el modo Insertar después de realizar la acción. Esto es útil para reemplazar texto.

- `cw` – Cambia el texto desde el cursor hasta el final de la palabra.
- `c$` – Cambia el texto desde el cursor hasta el final de la línea.
- `cc` – Cambia la línea actual completa.

### Copiar y Pegar en Vim

En Vim, copiar se denomina "yankear" (operador `y`), y pegar se denomina "poner" (put).

- `yw` – Yankea (copia) una palabra.
- `yy` – Yankea la línea actual completa.
- `p` – Pone (pega) el texto yankeado después del cursor o en la línea inferior.
- `P` – Pone el texto antes del cursor o en la línea superior.

### Otros Comandos de Edición Útiles

Esta guía de Vim no estaría completa sin algunos otros comandos prácticos.

- `r{char}` – Reemplaza el carácter único bajo el cursor con el carácter especificado.
- `R` – Entra en el modo Reemplazar, permitiéndole sobrescribir texto continuamente hasta que presione `Esc`.
- `J` – Une la línea actual con la siguiente.
- `.` – Repite el último cambio que realizó, un comando muy potente y eficiente.

Combinar operadores con diferentes movimientos desbloquea todo el potencial de este editor de texto de Linux. Por ejemplo, `d}` elimina hasta el siguiente párrafo, y `caw` cambia "una palabra" (la palabra bajo el cursor incluyendo cualquier espacio circundante).

## Exercise

Para poner en práctica sus conocimientos, recomendamos el siguiente laboratorio práctico. Le ayudará a dominar los comandos de edición fundamentales discutidos en este tutorial de Vim.

1.  **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/es/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practique la creación de archivos, la edición de texto, el guardado de archivos y la navegación con vi/vim y nano. Este laboratorio le ayudará a aplicar conceptos como eliminar, cambiar, yanquear y poner texto en escenarios reales.

## Quiz Question

Which command deletes the current line in Vim? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

dd
