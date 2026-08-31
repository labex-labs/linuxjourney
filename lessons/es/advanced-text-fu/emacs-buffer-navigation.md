---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "es"
order_index: 11
title: "Navegación por búferes de Emacs"
description: "Aprende a cambiar y eliminar búferes de Emacs, así como a dividir, seleccionar y cerrar ventanas de visualización."
meta_title: "Navegación por búferes de Emacs - Text-Fu avanzado"
meta_description: "Guía para cambiar entre búferes, dividir y seleccionar ventanas y gestionar el espacio de trabajo con órdenes esenciales de Emacs."
meta_keywords: "navegación Emacs, cambiar búfer Emacs, gestión de búferes Emacs, órdenes Emacs, C-x b, C-x k, C-x 2, editor de texto"
---

Un búfer de Emacs contiene texto o estado del editor, mientras que una ventana muestra un búfer. Un búfer puede existir sin estar visible y varias ventanas pueden mostrar el mismo búfer. Gestionar un objeto no gestiona automáticamente el otro.

## Cambiar de búfer

Usa `C-x b`, que ejecuta `switch-to-buffer`, para seleccionar por nombre un búfer en la ventana actual:

```text
C-x b
```

El minibúfer ofrece completado para los nombres existentes. Introducir un nombre nuevo puede crear un búfer sin archivo con ese nombre; no visita una ruta de archivo.

De forma predeterminada, `C-x Right` ejecuta `next-buffer` y `C-x Left` ejecuta `previous-buffer`, recorriendo los búferes en la ventana seleccionada.

:::single-choice{#emacs-switch-buffer-key}
¿Qué secuencia de teclas solicita el nombre de un búfer para mostrarlo en la ventana actual?

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="Esto solicita una ruta de archivo y la visita, una operación distinta de elegir un búfer existente por su nombre."}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer` lee el nombre de un búfer y lo muestra en la ventana seleccionada."}
::option[`C-x k`]{#emacs-buffer-kill explanation="Esto solicita eliminar un búfer en vez de cambiar la ventana seleccionada a otro."}
:::

## Dividir la ventana seleccionada

Usa `C-x 2` para dividir la ventana seleccionada en una ventana superior y otra inferior:

```text
C-x 2
```

Usa `C-x 3` para dividirla en ventanas izquierda y derecha:

```text
C-x 3
```

La ventana nueva muestra inicialmente un búfer, a menudo el mismo. Puedes cambiar de búfer independientemente en cada ventana.

:::single-choice{#emacs-split-side-by-side}
¿Qué secuencia de teclas divide la ventana seleccionada de Emacs en ventanas izquierda y derecha?

::option[`C-x 1`]{#emacs-window-one explanation="Esto elimina las demás ventanas y convierte la seleccionada en la única de su marco."}
::option[`C-x 2`]{#emacs-window-below explanation="Esto crea ventanas superior e inferior, no una división lado a lado."}
::option[`C-x 3`]{#emacs-window-right .correct explanation="`split-window-right`, asociado a `C-x 3`, crea ventanas izquierda y derecha."}
:::

## Seleccionar y cerrar ventanas

Usa `C-x o`, que ejecuta `other-window`, para seleccionar la ventana siguiente:

```text
C-x o
```

Usa estas órdenes para eliminar ventanas de visualización:

- `C-x 0`: elimina la ventana seleccionada.
- `C-x 1`: elimina las demás ventanas del marco actual.

Eliminar una ventana suele dejar activo el búfer que mostraba. Puedes volver a mostrarlo en otra ventana.

:::single-choice{#emacs-select-other-window}
¿Qué secuencia de teclas traslada el punto y el foco del teclado a otra ventana de Emacs?

::option[`C-x 0`]{#emacs-delete-selected-window explanation="Esto elimina la ventana seleccionada en vez de trasladar el foco a otra."}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window` cambia la selección a otra ventana del marco."}
::option[`C-x b`]{#emacs-switch-in-window explanation="Esto cambia el búfer que muestra la ventana actual, no la ventana seleccionada."}
:::

:::single-choice{#emacs-keep-one-window}
¿Qué secuencia de teclas conserva la ventana seleccionada y elimina las demás ventanas de su marco?

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows` convierte la ventana seleccionada en la única del marco."}
::option[`C-x 0`]{#emacs-delete-current-window explanation="Esto elimina la propia ventana seleccionada en vez de conservarla."}
::option[`C-x 2`]{#emacs-add-lower-window explanation="Esto añade otra ventana en lugar de reducir el marco a una sola."}
:::

## Eliminar un búfer

Usa `C-x k`, que ejecuta `kill-buffer`, para solicitar un búfer que se deba eliminar de Emacs:

```text
C-x k
```

El búfer actual es la opción predeterminada. Si un búfer asociado a un archivo tiene cambios sin guardar, Emacs muestra una advertencia antes de eliminarlo. Lee la solicitud; eliminar un búfer modificado puede descartar ediciones.

Eliminar un búfer es distinto de eliminar una ventana. Emacs sustituye un búfer eliminado en cualquier ventana que lo mostrase, mientras que eliminar una ventana puede dejar intacto su búfer.

:::single-choice{#emacs-kill-buffer-key}
¿Qué secuencia de teclas solicita eliminar un búfer de Emacs?

::option[`C-x 0`]{#emacs-kill-window-only explanation="Esto elimina una ventana de visualización, pero normalmente deja activo el búfer."}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer` elimina el búfer seleccionado de Emacs después de cualquier confirmación necesaria por modificaciones."}
::option[`C-x b`]{#emacs-kill-switch explanation="Esto cambia la ventana actual a un búfer con nombre y no lo elimina."}
:::

Practica estas órdenes con `*scratch*` y búferes desechables. Antes de eliminar un búfer asociado a un archivo, comprueba si su indicador de modificación muestra trabajo sin guardar.

## Resumen

Ahora puedes gestionar lo que Emacs almacena y lo que muestra cada ventana.

1. Cambia de búfer en la ventana seleccionada con `C-x b`.
2. Divide debajo con `C-x 2` o a la derecha con `C-x 3`.
3. Selecciona otra ventana con `C-x o`.
4. Elimina ventanas de visualización con `C-x 0` o `C-x 1`.
5. Elimina un búfer con `C-x k` solo después de revisar los cambios sin guardar.
