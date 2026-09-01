---
lesson_id: "vim-editing"
course_id: "advanced-text-fu"
lang: "es"
order_index: 7
title: "Edición en Vim"
description: "Aprende cómo Vim combina operadores, movimientos, registros, inserciones y órdenes de deshacer para editar texto."
meta_title: "Edición en Vim - Text-Fu avanzado"
meta_description: "Tutorial de Vim para principiantes sobre órdenes esenciales de edición. Aprende a eliminar, cambiar, copiar y pegar texto para mejorar tu flujo de trabajo."
meta_keywords: "edición Vim, órdenes Vim, editor de texto Linux, tutorial Vim, guía Vim, Vim para principiantes, orden dd, eliminar Vim"
---

Las órdenes de edición de Vim suelen combinar un operador con un movimiento o un objeto de texto. Esta gramática permite aplicar las mismas acciones a caracteres, palabras, líneas y ámbitos mayores. Pulsa `Esc` antes de practicar para volver al modo Normal.

## Combinar un operador con un movimiento

La forma general es:

```text
[count] operator [count] motion
```

Entre los operadores habituales se encuentran:

- `d`: elimina texto.
- `c`: cambia texto y después entra en el modo Insertar.
- `y`: copia texto en un registro (*yank*).

Por ejemplo, `dw` elimina el intervalo cubierto por el movimiento `w`, mientras que `d$` elimina desde el cursor hasta el final de la línea. `2dw` aplica la eliminación a dos movimientos de palabra.

:::single-choice{#vim-edit-operator-motion} En el modo Normal, ¿qué hace `d$`?

::option[Elimina el archivo completo desde el cursor en adelante.]{#vim-edit-delete-file-end explanation="El movimiento con signo de dólar apunta al final de la línea actual, no al final de todo el búfer."}
::option[Elimina desde el cursor hasta el final de la línea.]{#vim-edit-delete-line-end .correct explanation="El operador `d` se aplica al movimiento `$` hacia el final de la línea."}
::option[Se desplaza al final de la línea sin modificar el texto.]{#vim-edit-move-line-end explanation="`$` por sí solo se desplaza, pero la `d` anterior convierte el intervalo cubierto en una eliminación."}
:::

## Editar caracteres y líneas

Algunas órdenes son atajos prácticos:

- `x`: elimina el carácter situado bajo el cursor.
- `dd`: elimina la línea actual como una línea completa.
- `3dd`: elimina tres líneas a partir de la actual.
- `cc`: cambia la línea actual y entra en el modo Insertar.
- `r{char}`: sustituye el carácter bajo el cursor por `{char}`.
- `R`: entra en el modo Reemplazar hasta que se pulsa `Esc`.

Repetir un operador, como en `dd`, hace que actúe por líneas. Una cantidad amplía el número de líneas.

:::single-choice{#vim-edit-delete-three-lines} ¿Qué orden del modo Normal elimina la línea actual y las dos siguientes?

::option[`dd3`]{#vim-edit-dd-three explanation="En esta forma de orden, la cantidad debe ir antes del operador duplicado."}
::option[`3x`]{#vim-edit-three-x explanation="Esto elimina tres caracteres bajo el cursor y después de él, no tres líneas completas."}
::option[`3dd`]{#vim-edit-three-dd .correct explanation="La cantidad se aplica a la orden por líneas `dd` y elimina tres líneas a partir de la actual."}
:::

## Cambiar texto y entrar en el modo Insertar

El operador `c` elimina el texto seleccionado y entra en el modo Insertar para que puedas escribir un reemplazo:

- `ce`: cambia hasta el final de la palabra.
- `c$`: cambia hasta el final de la línea.
- `cc`: cambia toda la línea actual.
- `ciw`: cambia la palabra interior bajo el cursor.
- `caw`: cambia un objeto de texto de palabra, incluido el espacio circundante según lo define Vim.

El comportamiento de `cw` tiene un caso especial histórico y a menudo actúa como `ce`. Los objetos de texto como `iw` pueden expresar con mayor claridad el límite deseado.

:::single-choice{#vim-edit-change-inner-word} ¿Qué orden del modo Normal sustituye la palabra interior bajo el cursor al eliminarla y entrar en el modo Insertar?

::option[`diw`]{#vim-edit-delete-inner-word explanation="Esto elimina la palabra interior, pero permanece en el modo Normal en vez de iniciar el texto de reemplazo."}
::option[`yiw`]{#vim-edit-yank-inner-word explanation="Esto copia la palabra interior sin modificar el búfer ni entrar en el modo Insertar."}
::option[`ciw`]{#vim-edit-change-inner-word-answer .correct explanation="El operador `c` cambia el objeto de texto `iw` y después entra en el modo Insertar."}
:::

## Copiar e insertar texto

Vim denomina **yank** a copiar y **put** a insertar el texto almacenado:

- `yw`: copia el intervalo de un movimiento de palabra.
- `yy`: copia la línea actual.
- `p`: inserta después del cursor si el texto es por caracteres, o debajo de la línea actual si es por líneas.
- `P`: inserta antes del cursor o encima de la línea actual.

Las eliminaciones y los cambios también guardan texto en registros, por lo que un `p` posterior puede insertar el texto eliminado más recientemente en vez de una copia anterior. Los registros con nombre permiten conservar texto específico, pero empieza observando qué ha guardado la última operación.

:::single-choice{#vim-edit-yank-put-line} Después de que `yy` copie la línea actual, ¿qué orden inserta esa línea debajo de la actual?

::option[`p`]{#vim-edit-put-below .correct explanation="Para texto copiado por líneas, la `p` minúscula inserta la línea almacenada debajo de la actual."}
::option[`P`]{#vim-edit-put-above explanation="La `P` mayúscula inserta el texto por líneas encima de la línea actual."}
::option[`u`]{#vim-edit-undo-not-put explanation="La `u` minúscula deshace un cambio; no inserta la línea copiada."}
:::

## Deshacer, rehacer y repetir

En el modo Normal:

- `u`: deshace el cambio más reciente.
- `Ctrl+R`: rehace un cambio deshecho.
- `.`: repite el cambio más reciente en la ubicación actual cuando corresponde.
- `J`: une la línea actual con la siguiente.

El historial de deshacer se aplica a cambios del búfer, no a simples movimientos del cursor. Guarda puntos de control y revisa las ediciones en vez de depender de un historial de deshacer ilimitado o permanente.

:::single-choice{#vim-edit-redo-change} ¿Qué orden del modo Normal rehace un cambio que se acaba de deshacer?

::option[`Ctrl+U`]{#vim-edit-control-u explanation="En el modo Normal, `Ctrl+U` desplaza la vista aproximadamente media pantalla hacia arriba; no rehace."}
::option[`.`]{#vim-edit-dot-repeat explanation="El punto repite el último cambio como una acción nueva en vez de avanzar por el historial de deshacer."}
::option[`Ctrl+R`]{#vim-edit-control-r .correct explanation="Vim usa `Ctrl+R` en el modo Normal para avanzar por el historial de deshacer."}
:::

Para practicar operadores, movimientos y recuperación sobre texto desechable, prueba este laboratorio práctico:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación y edición de archivos, el guardado y la navegación con vi/vim y nano, aplicando eliminaciones, cambios, copias e inserciones de texto.

## Resumen

Ahora puedes componer ediciones de Vim y recuperarte de errores en el modo Normal.

1. Combina operadores con movimientos, objetos de texto y cantidades.
2. Elimina caracteres o líneas completas con el ámbito elegido.
3. Cambia texto y entra en el modo Insertar para reemplazarlo.
4. Copia e inserta texto por caracteres o por líneas.
5. Deshaz, rehace o repite cambios deliberadamente.
