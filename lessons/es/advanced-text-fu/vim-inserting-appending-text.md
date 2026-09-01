---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "es"
order_index: 6
title: "Insertar y añadir texto en Vim"
description: "Aprende cómo Vim entra en el modo Insertar antes, después, encima o debajo de la posición actual del cursor."
meta_title: "Insertar y añadir texto en Vim - Text-Fu avanzado"
meta_description: "Aprende la diferencia entre insertar y añadir en Vim. Domina órdenes como i, a y o para editar texto y abrir líneas de forma eficiente."
meta_keywords: "Vim añadir, insertar y añadir Vim, Vim agregar línea, edición de texto Vim, órdenes Vim, tutorial Vim, modo Insertar"
---

En el modo Normal, Vim interpreta las teclas como órdenes. El modo Insertar introduce el texto escrito en el búfer. Varias órdenes del modo Normal entran en el modo Insertar en posiciones diferentes, lo que permite comenzar a escribir sin desplazarse por separado.

Pulsa `Esc` para salir del modo Insertar y volver al modo Normal. Si no sabes qué modo está activo, pulsar `Esc` es una forma segura de restablecer el modo Normal, aunque puede cancelar una operación pendiente.

:::single-choice{#vim-insert-return-normal} ¿Qué tecla vuelve normalmente del modo Insertar al modo Normal?

::option[`Esc`]{#vim-insert-escape .correct explanation="Escape termina la inserción actual y devuelve Vim al modo Normal."}
::option[`Enter`]{#vim-insert-enter explanation="Intro inserta un salto de línea y permanece en el modo Insertar."}
::option[`Tab`]{#vim-insert-tab explanation="Tabulador inserta sangría o activa el comportamiento de completado configurado; normalmente no abandona el modo Insertar."}
:::

## Insertar antes o después del cursor

Desde el modo Normal:

- `i`: entra en el modo Insertar antes del cursor.
- `a`: entra en el modo Insertar después del cursor.

Por ejemplo, si el cursor está sobre la `b` de `abc`, `i` comienza antes de `b`, mientras que `a` comienza después. Ambas órdenes cambian de modo; el texto que escribas a continuación realiza la inserción.

:::single-choice{#vim-insert-before-cursor} ¿Qué tecla del modo Normal entra en el modo Insertar inmediatamente antes del cursor?

::option[`a`]{#vim-insert-a-after explanation="La `a` minúscula añade después del cursor en vez de insertar antes."}
::option[`o`]{#vim-insert-o-below explanation="La `o` minúscula abre una línea nueva debajo de la actual antes de entrar en el modo Insertar."}
::option[`i`]{#vim-insert-i-before .correct explanation="La `i` minúscula comienza la inserción en la posición actual del cursor, antes del carácter situado bajo él."}
:::

## Insertar en los límites de una línea

Las órdenes en mayúsculas apuntan a posiciones significativas de la línea actual:

- `I`: entra en el modo Insertar antes del primer carácter que no sea un espacio en blanco.
- `A`: entra en el modo Insertar al final de la línea.

En una línea con sangría, `I` la omite y comienza antes del primer texto que no esté en blanco. Usa `0i` si necesitas específicamente insertar en la columna cero.

:::single-choice{#vim-insert-first-nonblank} ¿Qué orden del modo Normal comienza a insertar antes del primer carácter que no sea un espacio en blanco de la línea actual?

::option[`i`]{#vim-insert-lower-i explanation="La `i` minúscula usa la posición actual del cursor y no apunta primero al texto inicial de la línea."}
::option[`A`]{#vim-insert-capital-a explanation="La `A` mayúscula comienza la inserción al final de la línea actual."}
::option[`I`]{#vim-insert-capital-i .correct explanation="La `I` mayúscula se desplaza al primer carácter que no esté en blanco y entra en el modo Insertar antes de él."}
:::

:::single-choice{#vim-append-line-end} ¿Qué orden del modo Normal va al final de la línea actual y entra en el modo Insertar?

::option[`A`]{#vim-append-capital-a .correct explanation="La `A` mayúscula combina un salto al final de la línea con la entrada en el modo Insertar."}
::option[`$`]{#vim-move-line-end explanation="El movimiento con signo de dólar llega al final de la línea, pero permanece en el modo Normal."}
::option[`a`]{#vim-append-one-position explanation="La `a` minúscula comienza después del cursor actual en vez de saltar al final de la línea."}
:::

## Abrir una línea nueva

Desde el modo Normal:

- `o`: abre una línea nueva debajo de la actual y entra en el modo Insertar.
- `O`: abre una línea nueva encima de la actual y entra en el modo Insertar.

Vim aplica la sangría según la configuración actual y las reglas del tipo de archivo. Una cantidad puede repetir la operación de apertura de línea, pero aprende primero la forma de una sola línea para que la posición resultante del cursor sea predecible.

:::single-choice{#vim-open-line-above} ¿Qué orden del modo Normal abre una línea nueva encima de la actual y entra en el modo Insertar?

::option[`o`]{#vim-open-lower-o explanation="La `o` minúscula abre una línea debajo de la actual."}
::option[`O`]{#vim-open-upper-o .correct explanation="La `O` mayúscula abre una línea nueva encima e inicia allí la inserción."}
::option[`A`]{#vim-open-upper-a explanation="La `A` mayúscula añade al final de la línea existente y no abre una línea nueva encima."}
:::

Para practicar el cambio entre los modos Normal e Insertar, prueba este laboratorio práctico:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación y edición de archivos, el guardado y la navegación con vi/vim y nano para dominar los modos Normal e Insertar de Vim.

## Resumen

Ahora puedes entrar en el modo Insertar en la posición donde debe ir el texto nuevo.

1. Vuelve al modo Normal con `Esc`.
2. Inserta antes o después del cursor con `i` o `a`.
3. Inserta al principio del texto o al final de la línea con `I` o `A`.
4. Abre una línea debajo con `o`.
5. Abre una línea encima con `O`.
