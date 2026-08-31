---
lesson_id: "less-command"
course_id: "command-line"
lang: "es"
order_index: 8
title: "less"
description: "Aprende a navegar, buscar y seguir interactivamente archivos de texto largos con `less`."
meta_title: "less - Línea de Comandos"
meta_description: "Aprende el comando less de Linux con ejemplos para ver archivos grandes, desplazarte, buscar, saltar a líneas, seguir logs y salir de less."
meta_keywords: "comando less, linux less, ver archivo grande linux, buscar en less, salir de less, less -N, less +F, visor de texto linux"
---

Cuando un archivo de texto es demasiado largo para una sola pantalla, `less` permite leerlo sin enviar todo el contenido de golpe por la terminal. Su nombre inspiró la vieja broma de Unix «less is more», ya que `more` es otro paginador.

## Apertura de un archivo

Para empezar a ver un archivo, usa `less` seguido del nombre del archivo.

```bash
$ less /home/pete/Documents/text1
```

Mientras `less` está activo, las pulsaciones controlan el paginador en vez de iniciar órdenes normales de la shell. Volverás a la shell al salir del paginador.

:::single-choice{#open-long-file}
¿Qué orden abre `/var/log/syslog` en un paginador interactivo?

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less` abre el archivo en un paginador para que puedas desplazarte, buscar y volver a la shell al salir."}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat` envía todo el archivo a la salida estándar de una sola vez. No proporciona controles interactivos de paginación."}
::option[`file /var/log/syslog`]{#classify-log explanation="`file` informa del tipo de contenido probable. No abre el registro para leerlo de forma interactiva."}
:::

## Navegación en less

Puedes usar varias teclas para moverte por el documento:

- Usa `Up`, `Down`, `Page Up` y `Page Down` para desplazarte por líneas o pantallas.
- Pulsa `g` para ir al principio.
- Pulsa `G` para ir al final.
- Pulsa `u` para subir media pantalla o `d` para bajar media pantalla.
- Pulsa `h` para abrir la ayuda integrada.

:::single-choice{#jump-to-file-end}
¿Qué tecla lleva directamente al final de un archivo en `less`?

::option[`g`]{#lowercase-g explanation="La `g` minúscula lleva al principio del archivo. Su variante en mayúscula se desplaza en la dirección opuesta."}
::option[`G`]{#uppercase-g .correct explanation="La `G` mayúscula lleva al final de la entrada. La orden distingue entre mayúsculas y minúsculas."}
::option[`h`]{#help-key explanation="La tecla `h` abre la ayuda del paginador. No lleva al final del archivo."}
:::

## Búsqueda en less

Una característica poderosa de `less` es su capacidad para buscar texto. Escribe `/` seguido del texto que quieres encontrar y luego presiona Enter.

- `/search_term`: busca hacia adelante `search_term`.
- `?search_term`: busca hacia atrás `search_term`.
- `n`: Repite la búsqueda en la misma dirección.
- `N`: Repite la búsqueda en la dirección opuesta.

:::single-choice{#repeat-search-direction}
Después de buscar `error` hacia delante, ¿qué tecla repite la búsqueda en la misma dirección?

::option[`n`]{#same-search .correct explanation="La `n` minúscula repite la búsqueda más reciente en su dirección original. En este caso, esa dirección es hacia delante."}
::option[`N`]{#opposite-search explanation="La `N` mayúscula repite la búsqueda más reciente en la dirección opuesta. Después de una búsqueda hacia delante, recorre las coincidencias hacia atrás."}
::option[`g`]{#search-to-start explanation="La tecla `g` lleva al principio de la entrada. No repite una búsqueda."}
:::

## Salida de less

Cuando termines de ver el archivo, necesitas saber cómo `salir de less` y volver a tu línea de comandos.

Pulsa `q` para salir de `less` y volver al prompt de la shell.

:::single-choice{#quit-less}
¿Qué tecla sale de `less` y vuelve a la shell?

::option[`q`]{#less-quit .correct explanation="La orden `q` cierra el paginador y restaura el prompt de la shell."}
::option[`h`]{#less-help explanation="La tecla `h` abre la ayuda dentro de `less`. No vuelve directamente a la shell."}
::option[`G`]{#less-end explanation="La `G` mayúscula lleva al final de la entrada. El paginador permanece abierto."}
:::

## Inicio de less con opciones

Puedes iniciar `less` con opciones:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: Mostrar números de línea.
- `+G`: Abrir al final del archivo.
- `+F`: Seguir nuevo contenido a medida que se agrega, similar a `tail -f`.

Mientras sigues un archivo con `+F`, presiona `Ctrl-C` para dejar de seguir y volver a la navegación normal, luego presiona `q` para salir.

Utiliza `-i` para que las búsquedas no distingan mayúsculas salvo que el patrón contenga una letra mayúscula, o `-I` para ignorarlas siempre.

También puedes enviar la salida de una orden a `less` mediante una tubería:

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log}
¿Qué orden abre `/var/log/syslog` y sigue el contenido nuevo a medida que llega?

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="La orden inicial `+F` activa el modo de seguimiento, por lo que `less` muestra el contenido nuevo que se añade al registro."}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="La orden inicial `+G` abre el archivo al final, pero no continúa siguiendo el contenido que llegue después."}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="La opción `-N` muestra números de línea. No activa el seguimiento continuo."}
:::

Para practicar la paginación, las búsquedas y la lectura de texto del sistema, prueba estos laboratorios:

1. **[Orden less de Linux: paginación de archivos](https://labex.io/es/labs/linux-linux-less-command-file-paging-214301)** - Aprende a consultar y recorrer archivos de texto con `less`, incluidas las búsquedas, la numeración de líneas y la coincidencia de patrones.
2. **[Visualización de registros y archivos de configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practica el uso de `cat`, `more` y `less` para consultar registros y archivos de configuración.

## Resumen

Ahora puedes utilizar `less` para inspeccionar archivos largos sin inundar la terminal.

1. Abrir un archivo o la salida canalizada de una orden en el paginador.
2. Desplazarte a partes concretas de la entrada.
3. Buscar hacia delante o atrás y repetir una búsqueda.
4. Mostrar números de línea o seguir contenido que crece.
5. Salir de forma segura y volver a la shell.
