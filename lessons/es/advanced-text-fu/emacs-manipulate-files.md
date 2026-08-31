---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "es"
order_index: 10
title: "Manipular archivos en Emacs"
description: "Aprende a visitar, guardar, renombrar, volver a cargar y revisar búferes asociados a archivos en Emacs."
meta_title: "Manipular archivos en Emacs - Text-Fu avanzado"
meta_description: "Aprende a abrir, guardar y guardar como en Emacs mediante C-x C-f, C-x C-s y C-x C-w, y a revisar varios búferes modificados."
meta_keywords: "Emacs, guardar archivo Emacs, abrir archivo Emacs, tutorial Emacs, órdenes Linux, Emacs para principiantes, guía Emacs"
---

Emacs visita archivos en búferes. La edición modifica primero el búfer; guardar escribe su contenido actual en la ruta asociada. Lee los mensajes del minibúfer porque los permisos, los cambios conflictivos en disco u otros errores pueden impedir la escritura.

## Visitar un archivo

Usa `C-x C-f`, que ejecuta `find-file`, introduce una ruta en el minibúfer y pulsa Intro:

```text
C-x C-f
```

Emacs abre un archivo existente y legible en un búfer, o prepara un búfer nuevo que visita un archivo cuando la ruta no existe. En el segundo caso, no existe ningún archivo en disco hasta que se guarda correctamente.

Puedes usar el completado con Tabulador mientras introduces una ruta. Visitar un directorio suele abrir Dired, el editor de directorios de Emacs, en vez de tratarlo como un archivo de texto.

:::single-choice{#emacs-find-file-key}
¿Qué secuencia de teclas de Emacs solicita una ruta y la visita?

::option[`C-x C-s`]{#emacs-file-save explanation="Esto guarda el búfer actual asociado a un archivo y no solicita visitar otra ruta."}
::option[`C-x C-c`]{#emacs-file-exit explanation="Esto inicia la salida de Emacs en vez de abrir un archivo."}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="Esto ejecuta `find-file` y solicita en el minibúfer la ruta que se debe visitar."}
:::

:::single-choice{#emacs-find-missing-file}
Cuando `C-x C-f` visita una ruta que no existe, ¿cuándo se crea normalmente el archivo en disco?

::option[Únicamente después de guardar correctamente el búfer nuevo.]{#emacs-file-created-on-save .correct explanation="El búfer puede contener ediciones antes de que exista un archivo, y el guardado realiza la creación."}
::option[Inmediatamente después de introducir la ruta.]{#emacs-file-created-immediately explanation="Emacs crea primero un búfer asociado a la ruta nueva; la creación en disco se aplaza."}
::option[Únicamente después de cerrar el propio Emacs.]{#emacs-file-created-on-exit explanation="Al salir se puede solicitar guardar, pero la creación del archivo depende de un guardado correcto y no necesariamente del cierre de Emacs."}
:::

## Guardar el búfer actual

Usa `C-x C-s`, que ejecuta `save-buffer`, para guardar el búfer actual asociado a un archivo:

```text
C-x C-s
```

Si el búfer no tiene un nombre de archivo asociado, Emacs solicita uno. Una escritura correcta elimina el indicador de modificación del búfer; un fallo conserva en él los datos sin guardar y muestra un error.

:::single-choice{#emacs-save-current-buffer}
¿Qué secuencia de teclas guarda el búfer actual asociado a un archivo?

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s` ejecuta `save-buffer` para el búfer actual."}
::option[`C-x C-w`]{#emacs-write-file-key explanation="Esto solicita otro nombre de archivo y cambia el archivo que visita el búfer."}
::option[`C-x s`]{#emacs-save-some-key explanation="Esto revisa varios búferes asociados a archivos y pregunta si deben guardarse, en vez de actuar solo sobre el actual."}
:::

## Escribir con otro nombre

Usa `C-x C-w`, que ejecuta `write-file`, para solicitar una ruta, escribir allí el búfer y hacer que este visite el archivo nuevo:

```text
C-x C-w
```

Este es el comportamiento «Guardar como» de Emacs. Difiere de limitarse a escribir una copia separada mientras se continúa visitando la ruta original.

:::single-choice{#emacs-write-file-as}
¿Qué secuencia de teclas realiza la operación habitual «Guardar como» para el búfer actual?

::option[`C-x C-f`]{#emacs-find-file-other explanation="Esto visita un archivo y puede cambiar a otro búfer; no es «Guardar como» para el búfer actual."}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="Esto solicita eliminar un búfer y puede preguntar por cambios sin guardar; no guarda con otro nombre."}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file` escribe en la ruta elegida y hace que el búfer visite ese archivo."}
:::

## Revisar varios búferes modificados

Usa `C-x s`, que ejecuta `save-some-buffers`, para examinar los búferes modificados asociados a archivos:

```text
C-x s
```

Emacs suele preguntar si debe guardar cada búfer modificado que cumple los requisitos. Lee el nombre del búfer y responde deliberadamente; no es un atajo incondicional para guardarlos todos.

:::single-choice{#emacs-save-some-buffers}
¿Qué hace normalmente `C-x s`?

::option[Pregunta si se deben guardar los búferes modificados asociados a archivos.]{#emacs-prompt-save-some .correct explanation="`save-some-buffers` revisa los búferes modificados que cumplen los requisitos y pregunta cuáles deben escribirse."}
::option[Guarda todos los búferes silenciosamente sin mostrar sus nombres.]{#emacs-silent-save-all explanation="La orden interactiva normal pregunta en vez de escribir incondicionalmente todos los búferes."}
::option[Cierra todos los búferes después de guardar el actual.]{#emacs-close-all-buffers explanation="La orden se ocupa de guardar varios búferes y normalmente no los cierra."}
:::

## Volver a cargar desde el disco

Si un archivo ha cambiado en disco y quieres descartar deliberadamente el contenido actual del búfer, ejecuta `M-x revert-buffer` y revisa la solicitud de confirmación. Volver a cargar puede destruir ediciones sin guardar del búfer, así que úsalo solo después de confirmar qué origen debe prevalecer.

Para comparar antes de decidir, guarda una copia separada o usa herramientas de control de versiones y diferencias. No trates las operaciones de recarga como inofensivas cuando el búfer esté modificado.

## Resumen

Ahora puedes gestionar búferes asociados a archivos sin confundir visitas y escrituras.

1. Visita una ruta con `C-x C-f`.
2. Crea un archivo inexistente únicamente al guardar su búfer.
3. Guarda el búfer actual con `C-x C-s`.
4. Guarda con un nuevo nombre visitado mediante `C-x C-w`.
5. Revisa varios búferes modificados con `C-x s`.
