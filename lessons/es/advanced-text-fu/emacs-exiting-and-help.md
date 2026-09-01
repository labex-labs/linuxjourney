---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "es"
order_index: 13
title: "Salir de Emacs y usar la ayuda"
description: "Aprende a salir de Emacs con seguridad, cancelar órdenes pendientes, consultar temas de ayuda y deshacer cambios."
meta_title: "Salir de Emacs y usar la ayuda - Text-Fu avanzado"
meta_description: "Aprende a salir de Emacs, acceder a su ayuda contextual, cancelar órdenes pendientes y deshacer cambios en el búfer."
meta_keywords: "salir Emacs, ayuda Emacs, deshacer Emacs, tutorial Emacs, editor de texto Linux, guía para principiantes"
---

Emacs proporciona ayuda contextual para teclas, funciones, variables y modos activos. También protege los búferes modificados asociados a archivos al salir, lo que permite decidir si se guarda o rechaza cada escritura.

## Salir de Emacs

Usa `C-x C-c`, que ejecuta `save-buffers-kill-terminal`, para solicitar el cierre de la sesión de Emacs o de la conexión de terminal:

```text
C-x C-c
```

Emacs comprueba los búferes modificados relevantes asociados a archivos y pregunta si deben guardarse. Lee cada nombre de búfer y responde deliberadamente. También puede preguntar por procesos activos. Cancela la salida si necesitas revisar el trabajo antes de decidir.

En un flujo con `emacsclient` o un servidor de Emacs, el comportamiento exacto del marco y del servidor puede variar, pero las preguntas sobre búferes modificados siguen mereciendo atención.

:::single-choice{#emacs-exit-key} ¿Qué secuencia de teclas solicita una salida normal de Emacs y comprueba los búferes modificados?

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="Esto elimina un búfer seleccionado y no solicita cerrar la sesión de Emacs."}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="Esto cancela una orden o solicitud pendiente en vez de cerrar Emacs."}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="Esto ejecuta el flujo normal para comprobar los búferes, guardarlos y salir, incluidas las preguntas por trabajo relevante sin guardar."}
:::

## Abrir el selector de ayuda

El prefijo estándar de ayuda es `C-h`. Usa `C-h C-h`, que ejecuta la ayuda sobre la ayuda, para mostrar orientación sobre las órdenes disponibles:

```text
C-h C-h
```

La segunda tecla elige el tipo de ayuda que necesitas.

:::single-choice{#emacs-help-for-help} ¿Qué secuencia de teclas explica cómo usar el sistema de ayuda de Emacs?

::option[`C-h C-h`]{#emacs-help-help .correct explanation="El prefijo de ayuda seguido de otro `C-h` abre ayuda sobre el propio selector de ayuda."}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="Esta no es la secuencia de ayuda sobre la ayuda presentada aquí."}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="Esto abre directamente el tutorial en vez de explicar el menú general de ayuda."}
:::

## Describir teclas y el estado del editor

Entre las órdenes de ayuda útiles se encuentran:

- `C-h k KEY`: describe lo que ejecuta una secuencia de teclas.
- `C-h f FUNCTION`: describe una función de Emacs Lisp.
- `C-h v VARIABLE`: describe una variable de Emacs Lisp.
- `C-h m`: describe los modos principal y secundarios actuales.
- `C-h t`: abre el tutorial interactivo.

Por ejemplo, escribe `C-h k C-x C-s` para ver la documentación de la asociación que guarda el búfer.

:::single-choice{#emacs-describe-key} Quieres saber qué hace `C-x C-s`. ¿Qué prefijo de ayuda debes introducir antes de esa secuencia?

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key` espera una secuencia de teclas y explica la orden asociada a ella."}
::option[`C-h f`]{#emacs-describe-function explanation="Esto solicita el nombre de una función en vez de leer una secuencia de teclas para identificar su asociación."}
::option[`C-h v`]{#emacs-describe-variable explanation="Esto solicita el nombre de una variable y no examina una asociación de teclas."}
:::

## Cancelar una orden pendiente

Usa `C-g`, asociado a `keyboard-quit`, cuando estés atrapado en una solicitud, una secuencia de teclas parcialmente introducida, una búsqueda incremental u otra orden que quieras cancelar:

```text
C-g
```

No deshace cambios del búfer que ya hayan ocurrido ni sale de Emacs. Detiene la interacción actual y devuelve el control a la edición normal cuando es posible.

:::single-choice{#emacs-cancel-pending-command} ¿Qué tecla cancela normalmente la solicitud u orden pendiente actual de Emacs?

::option[`C-x C-c`]{#emacs-cancel-exit explanation="Esto inicia el flujo de salida de Emacs en vez de limitarse a cancelar la solicitud actual."}
::option[`C-y`]{#emacs-cancel-yank explanation="Esto inserta texto del anillo de eliminaciones y no cancela una orden."}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit` interrumpe la interacción de la orden actual y devuelve el control a Emacs."}
:::

## Deshacer cambios del búfer

Usa `C-/`, `C-_` o `C-x u` para invocar deshacer en configuraciones habituales de Emacs:

```text
C-/
```

Las órdenes repetidas de deshacer retroceden por los cambios recientes del búfer. El movimiento del cursor por sí solo no suele ser un cambio del búfer. Las versiones y configuraciones de Emacs pueden ofrecer `undo-redo` y herramientas de historial más avanzadas; usa `C-h k` sobre tus asociaciones reales de deshacer y rehacer para verificar el comportamiento local.

:::single-choice{#emacs-undo-change} ¿Qué secuencia de teclas es una asociación estándar para deshacer un cambio reciente de un búfer de Emacs?

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/` es una asociación estándar para deshacer, junto con `C-_` y `C-x u` en configuraciones habituales."}
::option[`C-x C-s`]{#emacs-undo-save explanation="Esto guarda el búfer actual en vez de recorrer su historial de deshacer."}
::option[`C-w`]{#emacs-undo-kill explanation="Esto elimina la región activa y crea otro cambio en vez de deshacer uno."}
:::

Practica abriendo `*scratch*`, realizando un cambio desechable, usando deshacer, consultando con `C-h k` una tecla desconocida y cancelando una solicitud del minibúfer con `C-g` antes de salir normalmente.

## Resumen

Ahora puedes recuperar ayuda y salir de Emacs sin ignorar trabajo sin guardar.

1. Sal mediante las comprobaciones de búferes modificados con `C-x C-c`.
2. Abre la ayuda sobre la ayuda con `C-h C-h`.
3. Describe teclas, funciones, variables o modos activos.
4. Cancela una orden pendiente con `C-g`.
5. Deshaz cambios recientes del búfer con una asociación local verificada.
