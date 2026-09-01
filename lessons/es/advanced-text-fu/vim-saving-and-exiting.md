---
lesson_id: "vim-saving-and-exiting"
course_id: "advanced-text-fu"
lang: "es"
order_index: 8
title: "Guardar y salir de Vim"
description: "Aprende a guardar, salir, guardar con otro nombre o descartar deliberadamente los cambios de un búfer de Vim."
meta_title: "Guardar y salir de Vim - Text-Fu avanzado"
meta_description: "Aprende a guardar en Vim con :w y a guardar y salir con :wq, :x o ZZ. Descubre también cómo descartar cambios de forma deliberada."
meta_keywords: "cómo guardar Vim, vi guardar y salir, cómo guardar y salir Vim, guardar archivo Vim, salir Vim, órdenes Vim"
---

Guardar y salir son operaciones distintas en Vim. Antes de introducir una orden Ex, pulsa `Esc` para volver al modo Normal, escribe `:`, introduce la orden y pulsa Intro. Lee el estado o el mensaje de error de Vim antes de dar por hecho que se ha guardado correctamente.

## Guardar el búfer actual

Usa `:w` para escribir el búfer actual en su archivo asociado sin cerrar la ventana:

```vim
:w
```

El guardado puede fallar porque el búfer no tenga nombre de archivo, el directorio no permita escribir, el sistema de archivos esté lleno u otra condición impida la operación. Comprueba el mensaje que muestra Vim.

Usa `:w copy.txt` para escribir el búfer actual en otra ruta y mantener el nombre existente del búfer. Usa `:saveas copy.txt` cuando el búfer deba adoptar la ruta nueva.

:::single-choice{#vim-save-without-quit} ¿Qué orden de Vim escribe el búfer actual en su archivo asociado sin salir?

::option[`:q`]{#vim-save-q explanation="`:q` solicita salir y no guarda un búfer modificado."}
::option[`:w`]{#vim-save-w .correct explanation="La orden `:write` guarda el búfer actual y deja abierta la ventana de edición."}
::option[`:q!`]{#vim-save-q-force explanation="`:q!` descarta los cambios sin guardar y sale; no los guarda."}
:::

## Salir de un búfer sin modificar

Usa `:q` para cerrar la ventana actual cuando hacerlo no descarte cambios sin guardar del búfer:

```vim
:q
```

Si el búfer actual está modificado y sus cambios se perderían, Vim suele negarse y mostrar una advertencia. Esta protección permite guardar o reconsiderar la acción.

:::single-choice{#vim-quit-clean-buffer} ¿Qué orden cierra la ventana actual de Vim cuando no se perderán cambios sin guardar?

::option[`:w`]{#vim-quit-w explanation="Esto guarda el búfer, pero deja abierta la ventana actual."}
::option[`:q`]{#vim-quit-q .correct explanation="La orden normal de salida cierra la ventana cuando las protecciones de Vim para búferes modificados lo permiten."}
::option[`u`]{#vim-quit-u explanation="La `u` del modo Normal deshace un cambio y no cierra la ventana del editor."}
:::

## Descartar cambios sin guardar

Usa `:q!` únicamente cuando quieras cerrar deliberadamente la ventana actual y abandonar cambios que de otro modo impedirían salir:

```vim
:q!
```

El signo de exclamación ignora la advertencia sobre cambios sin guardar. Esos cambios del búfer no se escriben, así que comprueba que sean realmente prescindibles antes de pulsar Intro.

:::single-choice{#vim-quit-discard-changes} El búfer actual tiene cambios que deliberadamente no quieres guardar. ¿Qué orden cierra la ventana actual y los descarta?

::option[`:q`]{#vim-discard-plain-q explanation="`:q` sin más suele negarse cuando salir implicaría perder cambios de un búfer modificado."}
::option[`:wq`]{#vim-discard-wq explanation="`:wq` guarda los cambios antes de salir, lo contrario de descartarlos."}
::option[`:q!`]{#vim-discard-q-force .correct explanation="El signo de exclamación ignora la advertencia de modificación y cierra sin escribir los cambios sin guardar."}
:::

## Guardar y salir conjuntamente

Usa `:wq` cuando el búfer deba guardarse y la ventana actual deba cerrarse después de un guardado correcto:

```vim
:wq
```

Si el guardado falla, Vim no completa la salida solicitada. Resuelve el error en vez de dar por hecho que los datos llegaron al disco.

:::single-choice{#vim-write-and-quit} ¿Qué orden escribe el búfer actual y después cierra la ventana actual si el guardado tiene éxito?

::option[`:wq`]{#vim-save-wq .correct explanation="Esto combina un guardado con una salida, y la salida depende de que se guarde correctamente."}
::option[`:q!`]{#vim-save-force-quit explanation="Esto sale descartando los cambios en vez de guardarlos."}
::option[`:w copy.txt`]{#vim-save-copy explanation="Esto escribe en otra ruta, pero mantiene abierta la ventana de edición."}
:::

## Usar :x y ZZ

`:x` escribe el búfer solo si está modificado y después sale. En el modo Normal, `ZZ` en mayúsculas realiza el mismo comportamiento de guardar si se ha modificado y salir:

```vim
:x
```

```text
ZZ
```

Esto difiere sutilmente de `:wq`, que solicita un guardado incluso cuando el búfer no ha cambiado. `ZQ` en mayúsculas es la forma correspondiente del modo Normal para salir sin guardar, similar a `:q!`.

:::single-choice{#vim-write-if-modified-quit} ¿Qué orden del modo Normal guarda únicamente si el búfer está modificado y después sale?

::option[`ZZ`]{#vim-save-zz .correct explanation="`ZZ` en mayúsculas realiza el comportamiento de guardar si se ha modificado y salir asociado a `:x`."}
::option[`zz`]{#vim-center-screen explanation="`zz` en minúsculas vuelve a centrar la línea actual en la ventana; no guarda ni sale."}
::option[`ZQ`]{#vim-quit-zq explanation="`ZQ` en mayúsculas sale sin guardar, por lo que descarta los cambios sin guardar en vez de conservarlos."}
:::

Cuando intervienen varias ventanas o búferes, una orden puede cerrar únicamente la ventana actual. Órdenes como `:qa`, `:wqa` y `:qa!` actúan sobre varias ventanas, pero revisa todos los búferes modificados antes de usar una orden forzada para todas ellas.

Para practicar cómo guardar y salir con un archivo desechable, prueba este laboratorio práctico:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación y edición de archivos, el guardado y la navegación con Vim y Nano, incluidas las operaciones básicas para guardar y salir.

## Resumen

Ahora puedes elegir una orden de salida de Vim que refleje tu intención respecto a los datos sin guardar.

1. Guarda sin salir con `:w`.
2. Sal con seguridad mediante `:q` cuando no se perderán cambios.
3. Descarta cambios deliberadamente con `:q!`.
4. Guarda y sal con `:wq`.
5. Usa `:x` o `ZZ` para guardar solo si se ha modificado.
