---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "es"
order_index: 12
title: "Edición en Emacs"
description: "Aprende a mover el punto, activar una región y usar las órdenes del anillo de eliminaciones de Emacs para editar texto."
meta_title: "Edición en Emacs - Text-Fu avanzado"
meta_description: "Domina los fundamentos de edición de Emacs: navegación por texto, regiones, corte, copia y pegado mediante el anillo de eliminaciones."
meta_keywords: "Emacs, tutorial Emacs, órdenes Emacs, editor de texto, editor Linux, navegación Emacs, Emacs para principiantes"
---

Emacs llama **punto** a la posición actual del cursor. Las órdenes de movimiento cambian la posición del punto; las órdenes de edición insertan, eliminan, cortan, copian o pegan texto a su alrededor. En la notación siguiente, `C-` significa Control y `M-` significa Meta, normalmente Alt.

## Desplazarse por caracteres y líneas

Las flechas y otras teclas de navegación de la plataforma pueden funcionar, pero las órdenes estándar de movimiento de Emacs están disponibles tanto en sesiones gráficas como de terminal:

- `C-f`: avanza un carácter.
- `C-b`: retrocede un carácter.
- `C-n`: va a la línea siguiente.
- `C-p`: va a la línea anterior.
- `C-a`: va al principio de la línea.
- `C-e`: va al final de la línea.

:::single-choice{#emacs-edit-next-line}
¿Qué tecla de Emacs lleva el punto a la línea siguiente?

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p` va a la línea anterior, en la dirección opuesta."}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="`C-n`, de `next-line`, desplaza el punto hacia abajo hasta la posición de la línea de pantalla siguiente."}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f` avanza un carácter en vez de ir a la línea siguiente."}
:::

## Desplazarse por palabras y límites del búfer

Las órdenes Meta se desplazan por unidades mayores:

- `M-f`: avanza una palabra.
- `M-b`: retrocede una palabra.
- `M-<`: va al principio del búfer.
- `M->`: va al final del búfer.

En muchos teclados, Alt actúa como Meta. Cuando esa combinación no está disponible, pulsar `Esc` y después la tecla siguiente suele enviar la orden Meta equivalente.

:::single-choice{#emacs-edit-buffer-end}
¿Qué tecla de Emacs lleva el punto al final del búfer?

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e` va al final de la línea actual, no de todo el búfer."}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<` va al principio del búfer."}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->` lleva el punto al final del búfer actual."}
:::

## Definir una región

La **marca** es una posición guardada del búfer. El texto entre el punto y la marca es la **región**. Pulsa `C-SPC`, escrito como `C-space` en parte de la documentación, para ejecutar `set-mark-command`; después mueve el punto para ampliar la región activa.

En una terminal, `C-SPC` puede codificarse como `C-@`. El resaltado depende de la configuración de marca transitoria, pero el punto y la marca siguen definiendo una región.

:::single-choice{#emacs-edit-set-mark}
¿Qué tecla comienza a definir una región al establecer la marca en el punto?

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w` elimina una región ya definida; no es la orden inicial para establecer la marca."}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y` inserta texto del anillo de eliminaciones y no inicia una selección."}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command` coloca la marca; después, el movimiento cambia la región comprendida entre la marca y el punto."}
:::

## Eliminar o copiar una región

Emacs almacena el texto eliminado y copiado en el **anillo de eliminaciones**:

- `C-w`: elimina la región activa y la añade al anillo.
- `M-w`: copia la región activa al anillo sin eliminarla.
- `C-k`: elimina desde el punto hasta el final de la línea; el uso repetido puede incluir el salto de línea.

Esta eliminación conserva el texto para insertarlo posteriormente, a diferencia de una eliminación normal.

:::single-choice{#emacs-edit-copy-region}
¿Qué tecla copia la región activa al anillo de eliminaciones sin quitarla?

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="`kill-ring-save`, asociado a `M-w`, copia la región sin eliminarla."}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w` elimina la región mientras la guarda en el anillo."}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k` elimina texto hacia el final de la línea en vez de copiar sin cambios la región seleccionada."}
:::

## Insertar desde el anillo de eliminaciones

Usa `C-y` para insertar en el punto la entrada más reciente del anillo. Inmediatamente después de la inserción, `M-y` sustituye ese texto por una entrada anterior; repetir `M-y` recorre las entradas.

```text
C-y
M-y
```

Si después de `C-y` se ejecuta otra orden no relacionada, `M-y` deja de tener el mismo contexto para sustituir la inserción.

:::single-choice{#emacs-edit-yank-latest}
¿Qué tecla inserta en el punto la entrada más reciente del anillo de eliminaciones?

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="`yank`, asociado a `C-y`, inserta en el búfer actual el texto más reciente del anillo."}
::option[`M-y`]{#emacs-edit-yank-pop explanation="`M-y` suele sustituir una entrada recién insertada por otra anterior; depende del contexto de inserción precedente."}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d` elimina el carácter posterior al punto y no recupera texto del anillo."}
:::

Practica en `*scratch*` o en un archivo desechable: mueve el punto, establece la marca, copia una región, elimina otra y vuelve a insertar ambas. Guarda únicamente cuando merezca la pena conservar el archivo resultante.

## Resumen

Ahora puedes navegar y reorganizar texto de Emacs mediante el punto, la marca y el anillo de eliminaciones.

1. Desplázate por caracteres o líneas con órdenes Control.
2. Desplázate por palabras o límites del búfer con órdenes Meta.
3. Establece la marca con `C-SPC` para definir una región.
4. Elimina con `C-w` o copia con `M-w`.
5. Inserta con `C-y` y recorre el anillo inmediatamente después con `M-y`.
