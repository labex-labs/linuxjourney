---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "es"
order_index: 5
title: "Navegación en Vim"
description: "Aprende a desplazarte por caracteres, palabras, líneas y posiciones del archivo en el modo Normal de Vim."
meta_title: "Navegación en Vim - Text-Fu avanzado"
meta_description: "Aprende los fundamentos de navegación de Vim con h, j, k y l, además de movimientos por palabras, líneas y posiciones del archivo."
meta_keywords: "navegación Vim, tutorial Vim, Vim Linux, movimiento Vim, fundamentos Vim, Vim para principiantes, editor de texto Linux"
---

Vim proporciona movimientos con el teclado que funcionan en una terminal sin necesidad de ratón. Algunas configuraciones de Vim también admiten el ratón, pero aprender los movimientos permite combinarlos con órdenes de edición.

Pulsa `Esc` antes de practicar para volver al modo Normal.

## Desplazarse por caracteres y líneas de pantalla

Los movimientos fundamentales del modo Normal son:

- `h`: se desplaza un carácter a la izquierda.
- `j`: se desplaza una línea de pantalla hacia abajo.
- `k`: se desplaza una línea de pantalla hacia arriba.
- `l`: se desplaza un carácter a la derecha.

Las teclas de flecha suelen realizar movimientos similares, pero `h`, `j`, `k` y `l` mantienen las manos cerca de otras órdenes. En una línea que se ajusta visualmente, `j` y `k` suelen desplazarse por líneas del archivo; `gj` y `gk` se desplazan por líneas visibles de la pantalla.

:::single-choice{#vim-navigation-down} En el modo Normal, ¿qué tecla desplaza el cursor una línea hacia abajo?

::option[`k`]{#vim-nav-k-up explanation="El movimiento `k` sube una línea."}
::option[`l`]{#vim-nav-l-right explanation="El movimiento `l` avanza un carácter hacia la derecha."}
::option[`j`]{#vim-nav-j-down .correct explanation="El movimiento `j` baja una línea en el modo Normal."}
:::

## Anteponer cantidades a los movimientos

Escribe una cantidad positiva antes de muchos movimientos para repetirlos. Por ejemplo:

```text
5j
3l
```

`5j` baja cinco líneas, mientras que `3l` avanza tres posiciones de caracteres hacia la derecha cuando es posible. Las cantidades también se combinan con órdenes de palabras y edición.

:::single-choice{#vim-navigation-count} ¿Qué hace `4k` en el modo Normal?

::option[Baja cuatro líneas cuando es posible.]{#vim-nav-four-down explanation="El movimiento hacia abajo usa `j`; `k` se desplaza en la dirección opuesta."}
::option[Sube cuatro líneas cuando es posible.]{#vim-nav-four-up .correct explanation="La cantidad `4` repite cuatro veces el movimiento ascendente `k`."}
::option[Elimina cuatro líneas situadas sobre el cursor.]{#vim-nav-delete-four explanation="Un movimiento por sí solo cambia la posición del cursor. Para eliminar se necesitaría un operador como `d`."}
:::

## Desplazarse por palabras

Entre los movimientos útiles por palabras se encuentran:

- `w`: va al principio de la palabra siguiente.
- `b`: va al principio de la palabra actual o anterior.
- `e`: va al final de la palabra actual o siguiente.

Las formas mayúsculas `W`, `B` y `E` usan PALABRAS delimitadas por espacios en blanco y tratan la puntuación de forma diferente. Antepón una cantidad para recorrer varias palabras, como en `3w`.

:::single-choice{#vim-navigation-next-words} ¿Qué orden del modo Normal avanza hasta el principio de la tercera posición de palabra siguiente?

::option[`3w`]{#vim-nav-three-words .correct explanation="La cantidad aplica tres veces el movimiento hacia la palabra siguiente."}
::option[`w3`]{#vim-nav-word-three explanation="En esta forma de orden, las cantidades preceden a los movimientos; colocar `3` después no expresa el desplazamiento solicitado."}
::option[`3b`]{#vim-nav-three-back explanation="El movimiento `b` se dirige hacia principios de palabras anteriores, no hacia delante."}
:::

## Desplazarse dentro de una línea

Estos movimientos apuntan a posiciones de la línea actual:

- `0`: va a la columna cero.
- `^`: va al primer carácter que no sea un espacio en blanco.
- `$`: va al final de la línea.

La diferencia entre `0` y `^` importa en las líneas con sangría.

:::single-choice{#vim-navigation-first-nonblank} ¿Qué movimiento va al primer carácter que no sea un espacio en blanco de una línea con sangría?

::option[`0`]{#vim-nav-column-zero explanation="El cero va a la primera columna, que puede contener espacios de sangría."}
::option[`$`]{#vim-nav-line-end explanation="El movimiento con signo de dólar apunta al final de la línea."}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="El movimiento con circunflejo omite los espacios iniciales y llega al primer carácter que no esté en blanco."}
:::

## Desplazarse por el archivo

Usa estas órdenes del modo Normal para realizar saltos mayores:

- `gg`: va a la primera línea.
- `G`: va a la última línea.
- `42G`: va a la línea 42.
- `Ctrl+F`: avanza aproximadamente una pantalla.
- `Ctrl+B`: retrocede aproximadamente una pantalla.

La orden `:42`, seguida de Intro, es otra forma de saltar a la línea 42.

:::single-choice{#vim-navigation-file-end} ¿Qué orden del modo Normal va a la última línea del búfer?

::option[`gg`]{#vim-nav-first-line explanation="`gg` en minúsculas va a la primera línea, no a la última."}
::option[`$`]{#vim-nav-current-line-end explanation="El movimiento con signo de dólar va al final de la línea actual, no al final del archivo."}
::option[`G`]{#vim-nav-last-line .correct explanation="La `G` mayúscula sin una cantidad salta a la última línea."}
:::

Para practicar la navegación con el teclado mientras editas un archivo desechable, prueba este laboratorio práctico:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación y edición de archivos, el guardado y la navegación con Vim y Nano en un entorno Linux real.

## Resumen

Ahora puedes recorrer un búfer de Vim a varias escalas útiles.

1. Desplázate por caracteres o líneas con `h`, `j`, `k` y `l`.
2. Repite movimientos con un prefijo numérico.
3. Recorre límites de palabras con `w`, `b` y `e`.
4. Apunta al principio, al primer texto o al final de una línea.
5. Salta a posiciones del archivo con `gg`, `G` o un número de línea.
