---
index: 6
lang: "es"
title: "Insertar y Añadir Texto en Vim"
meta_title: "Insertar y Añadir Texto en Vim - Dominio Avanzado de Texto"
meta_description: "Aprende la diferencia entre los modos de inserción y adición de Vim. Domina comandos como 'i', 'a' y 'o' para editar texto eficientemente, añadir contenido y agregar líneas en Vim."
meta_keywords: "vim añadir, añadir vs insertar vim, vim insertar vs añadir, vim agregar línea, edición de texto vim, comandos vim, tutorial vim, modo inserción, modo añadir"
---

## Lesson Content

En Vim, trabajarás principalmente en dos modos: el modo Normal para ejecutar comandos y el modo Insertar para escribir texto. Para cambiar del modo Insertar de vuelta al modo Normal, simplemente presiona la tecla `Esc`.

Existen varios comandos para entrar en el modo Insertar, cada uno colocando el cursor en una posición inicial diferente para la entrada de texto.

### Comandos Básicos de Inserción

La forma más fundamental de empezar a escribir es con el comando `i`.

- `i` – **i**nserta texto antes de la posición actual del cursor.

Este comando te cambia al modo Insertar, permitiéndote escribir directamente en el archivo.

### Vim Append vs Insert

Un punto común de comparación es **vim append vs insert** (añadir vs insertar en Vim). Aunque ambos entran en el modo Insertar, sus puntos de partida difieren con respecto al cursor. Comprender la distinción **vim insert vs append** es clave para un movimiento y edición eficientes.

- `a` – **a**ñade texto después de la posición actual del cursor.
- `I` – **I**nserta texto al principio de la línea actual.
- `A` – **A**ñade texto al final de la línea actual.

Usar `a` en lugar de `i` te ahorra una pulsación de tecla (mover el cursor un espacio a la derecha antes de insertar). De manera similar, `A` es un atajo potente para empezar a escribir inmediatamente al final de una línea. Dominar los comandos de **vim append** (añadir en Vim) es un paso significativo para mejorar tu velocidad de edición.

### Cómo Vim Add Line (Añadir Línea en Vim)

Cuando necesites añadir nuevas líneas de texto, no tienes que presionar Enter manualmente al final de una línea. Vim proporciona comandos dedicados para abrir líneas y entrar inmediatamente en el modo Insertar.

- `o` – **o**bre una nueva línea debajo de la línea actual y entra en el modo Insertar.
- `O` – **O**bre una nueva línea encima de la línea actual y entra en el modo Insertar.

Estos comandos son extremadamente útiles cuando necesitas rápidamente **vim add line** (añadir línea en Vim) mientras codificas o escribes.

Consejo: Puedes anteponer un número a estos comandos para repetirlos. Por ejemplo, escribir `3o` en el modo Normal abrirá tres nuevas líneas en blanco debajo de la actual y te colocará en el modo Insertar en la primera de estas nuevas líneas.

## Exercise

La práctica es esencial para dominar Vim. El siguiente laboratorio proporciona un entorno práctico para reforzar tu comprensión de las capacidades de edición de texto de Vim.

1.  **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/es/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación de archivos, la edición de texto, el guardado de archivos y la navegación con vi/vim y nano. Este laboratorio te ayudará a dominar las habilidades fundamentales del uso de los modos Normal e Insertar de Vim.

Aplicar estos conceptos en escenarios reales te ayudará a ganar confianza con la edición de texto en Linux usando Vim.

## Quiz Question

Qué tecla entra en modo Insertar antes del cursor? Por favor, responde con una sola letra minúscula en inglés.

## Quiz Answer

i
