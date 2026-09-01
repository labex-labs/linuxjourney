---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "es"
order_index: 4
title: "Patrones de búsqueda de Vim"
description: "Aprende a buscar hacia delante o hacia atrás en Vim y a repetir, refinar o borrar las coincidencias de patrones."
meta_title: "Patrones de búsqueda de Vim - Text-Fu avanzado"
meta_description: "Aprende a buscar hacia delante y hacia atrás en Vim mediante patrones, y a recorrer rápidamente los resultados con n y N."
meta_keywords: "búsqueda Vim, órdenes Vim, editor de texto Linux, tutorial Vim, guía Vim, patrones de búsqueda"
---

Vim busca patrones desde la posición actual del cursor. Empieza en el modo Normal, introduce una búsqueda hacia delante o hacia atrás y después repite las coincidencias sin volver a escribir el patrón.

## Buscar hacia delante

En el modo Normal, escribe `/`, introduce un patrón y pulsa Intro. Vim se desplaza a la siguiente coincidencia posterior al cursor:

```vim
/pretty
```

Las búsquedas usan la sintaxis de expresiones regulares de Vim, por lo que caracteres como `.`, `*`, `[` y `\` pueden tener un significado especial. Usa `\V` al principio cuando el resto del patrón deba tratarse como «muy no mágico», o escapa deliberadamente los caracteres especiales.

:::single-choice{#vim-search-forward-key} Desde el modo Normal, ¿qué orden inicia una búsqueda hacia delante de `pretty`?

::option[`?pretty` seguido de Intro]{#vim-backward-pretty explanation="Un signo de interrogación inicia una búsqueda hacia atrás desde la posición actual del cursor."}
::option[`/pretty` seguido de Intro]{#vim-forward-pretty .correct explanation="Una barra inicia una búsqueda hacia delante e Intro envía el patrón."}
::option[`:pretty` seguido de Intro]{#vim-command-pretty explanation="Los dos puntos entran en el modo de línea de órdenes para una orden Ex; `pretty` no inicia así una búsqueda."}
:::

## Buscar hacia atrás

Escribe `?`, introduce un patrón y pulsa Intro para desplazarte a la coincidencia anterior al cursor:

```vim
?pretty
```

Esto no significa necesariamente «la última coincidencia del archivo». El resultado depende de la posición actual del cursor. Con la opción predeterminada `wrapscan` de Vim, una búsqueda puede continuar al principio o al final; `:set nowrapscan` desactiva ese recorrido circular.

:::single-choice{#vim-search-backward-key} ¿Qué prefijo de búsqueda del modo Normal busca texto anterior al cursor?

::option[`/`]{#vim-slash-forward explanation="Una barra busca hacia delante desde el cursor, no hacia el texto anterior."}
::option[`?`]{#vim-question-backward .correct explanation="Un signo de interrogación inicia una búsqueda de patrones hacia atrás desde la posición actual del cursor."}
::option[`:`]{#vim-colon-command explanation="Los dos puntos inician una línea de órdenes Ex. No son el prefijo de búsqueda hacia atrás."}
:::

## Repetir una búsqueda

Después de cualquier tipo de búsqueda:

- Pulsa `n` para repetir en la dirección original de la búsqueda.
- Pulsa `N` para repetir en la dirección contraria.

Por tanto, después de `/pretty`, `n` avanza y `N` retrocede. Después de `?pretty`, `n` retrocede y `N` avanza.

:::single-choice{#vim-repeat-backward-search} Después de ejecutar `?error`, ¿qué tecla repite la búsqueda en la misma dirección hacia atrás?

::option[`n`]{#vim-same-question-search .correct explanation="La `n` minúscula repite la búsqueda más reciente en su dirección original, que en este caso es hacia atrás."}
::option[`N`]{#vim-opposite-question-search explanation="La `N` mayúscula invierte la dirección original, por lo que avanzaría después de una búsqueda con `?`."}
::option[`/`]{#vim-new-forward-search explanation="Una barra inicia una nueva búsqueda hacia delante y espera un patrón en vez de repetir el anterior."}
:::

## Buscar la palabra bajo el cursor

En el modo Normal, coloca el cursor sobre una palabra y usa:

- `*` para buscar esa palabra completa hacia delante.
- `#` para buscar esa palabra completa hacia atrás.

Estas órdenes establecen el patrón de búsqueda más reciente, por lo que `n` y `N` pueden continuar a partir de él.

:::single-choice{#vim-current-word-forward} ¿Qué tecla del modo Normal busca hacia delante la palabra completa situada bajo el cursor?

::option[`#`]{#vim-hash-current-word explanation="La tecla de almohadilla busca hacia atrás la palabra situada bajo el cursor."}
::option[`*`]{#vim-star-current-word .correct explanation="La orden con asterisco crea un patrón de palabra completa a partir de la palabra bajo el cursor y busca hacia delante."}
::option[`n`]{#vim-repeat-current-pattern explanation="La tecla `n` repite una búsqueda existente; no crea primero un patrón a partir de la palabra actual."}
:::

## Controlar mayúsculas y resaltado

Las opciones de Vim pueden cambiar el comportamiento de las mayúsculas:

- `:set ignorecase` hace que las búsquedas ignoren mayúsculas y minúsculas.
- `:set smartcase` restablece la distinción cuando el patrón incluye una mayúscula y también está activado `ignorecase`.
- `\c` dentro de un patrón obliga a esa búsqueda a ignorar mayúsculas y minúsculas.
- `\C` obliga a esa búsqueda a distinguirlas.

Por ejemplo, `/\cerror` coincide con `error`, `Error` y `ERROR` independientemente de las opciones actuales de mayúsculas.

Cuando está activado el resaltado de búsquedas, `:nohlsearch` borra los resaltados visibles actuales sin eliminar el patrón de búsqueda. La siguiente búsqueda o repetición puede volver a resaltar coincidencias.

:::single-choice{#vim-force-case-insensitive} ¿Qué patrón obliga a una búsqueda concreta de Vim de `error` a ignorar mayúsculas y minúsculas sin importar las opciones actuales?

::option[`/\Cerror`]{#vim-pattern-match-case explanation="La `\C` mayúscula obliga a distinguir mayúsculas y minúsculas, el comportamiento contrario."}
::option[`/:error`]{#vim-pattern-colon-error explanation="En este patrón, los dos puntos son un carácter literal y no seleccionan el tratamiento de mayúsculas."}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="El átomo `\c` hace que esa búsqueda no distinga mayúsculas y minúsculas, por lo que pueden coincidir variantes de capitalización."}
:::

Para practicar la navegación y las búsquedas de Vim en un archivo controlado, prueba este laboratorio práctico:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación, edición, guardado y navegación de archivos de texto con Vim y Nano.

## Resumen

Ahora puedes buscar en un búfer de Vim y desplazarte de forma predecible entre coincidencias.

1. Inicia búsquedas hacia delante con `/` y hacia atrás con `?`.
2. Repite en la misma dirección con `n` o en la contraria con `N`.
3. Busca la palabra completa bajo el cursor con `*` o `#`.
4. Controla las mayúsculas para un patrón o mediante opciones.
5. Borra los resaltados sin perder el patrón de búsqueda actual.
