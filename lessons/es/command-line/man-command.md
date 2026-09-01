---
lesson_id: "man-command"
course_id: "command-line"
lang: "es"
order_index: 16
title: "man"
description: "Aprende a abrir, recorrer, buscar y seleccionar secciones de las páginas del manual instaladas."
meta_title: "man - Línea de Comandos"
meta_description: "Aprende el comando man de Linux con ejemplos para leer páginas de manual, buscar dentro de páginas man, entender secciones y encontrar opciones de comandos."
meta_keywords: "comando man, páginas man linux, manual de comandos, man ls, secciones man, buscar en página man, ayuda línea de comandos"
---

Muchas órdenes, interfaces, archivos de configuración y herramientas de administración de Linux disponen de documentación de referencia instalada denominada páginas del manual o páginas man. La orden `man` busca y muestra esas páginas.

## Apertura de una página del manual

Para ver el manual de cualquier comando, usa `man` seguido del nombre del comando. Por ejemplo, para leer el manual de `ls`, escribe:

```bash
$ man ls
```

Las páginas suelen incluir una sinopsis, una descripción, opciones, archivos relacionados y referencias cruzadas, aunque las secciones exactas varían.

:::single-choice{#open-ls-manual} ¿Qué orden abre la página del manual instalada para `ls`?

::option[`help ls`]{#help-ls explanation="`help` de Bash documenta órdenes integradas y normalmente no abre la página del manual del programa externo `ls`."}
::option[`man ls`]{#manual-ls-page .correct explanation="`man` busca el tema `ls` en la base de datos del manual y muestra la página coincidente."}
::option[`ls --help`]{#ls-usage explanation="Esta orden pide a `ls` su propio resumen de uso. No abre la página del manual instalada."}
:::

## Navegación y búsqueda en una página

Las páginas man son particularmente útiles para entender las opciones de un comando. Por ejemplo, si has visto `ls -l` y quieres saber qué significa `-l`, abre `man ls` y busca `-l`.

En muchos sistemas, `man` muestra las páginas mediante un paginador como `less`. Mientras una página esté abierta, puedes desplazarte con las flechas o las teclas de página y usar estos controles:

- Presiona `/` y escribe un término para buscar hacia adelante.
- Presiona `n` para saltar a la siguiente coincidencia.
- Presiona `N` para saltar a la coincidencia anterior.
- Presiona `q` para salir.

El paginador puede variar según el sistema o el entorno, así que estas teclas no están garantizadas en todos los casos. Los controles anteriores corresponden a la configuración habitual con `less`.

:::single-choice{#search-man-page} Con una página man abierta en `less`, ¿qué inicia una búsqueda hacia delante de `--recursive`?

::option[Escribir `?--recursive` y pulsar Enter.]{#backward-man-search explanation="El signo de interrogación inicia una búsqueda hacia atrás. Busca en la dirección opuesta a la solicitada."}
::option[Escribir `/--recursive` y pulsar Enter.]{#forward-man-search .correct explanation="Una barra inicia una búsqueda hacia delante en `less` y Enter envía el patrón."}
::option[Escribir `n--recursive` y pulsar Enter.]{#repeat-man-search explanation="La tecla `n` repite una búsqueda existente. No introduce de esta forma un patrón de búsqueda nuevo."}
:::

:::single-choice{#leave-man-page} Con una página man abierta en el paginador habitual, ¿qué tecla devuelve el control a la shell?

::option[`G`]{#man-page-end explanation="La `G` mayúscula lleva al final de la página en `less`. No cierra el paginador."}
::option[`n`]{#next-man-match explanation="La tecla `n` repite la búsqueda más reciente. La página del manual permanece abierta."}
::option[`q`]{#quit-man .correct explanation="La tecla `q` cierra el paginador habitual y devuelve el control a la shell."}
:::

## Selección de una sección del manual

Las páginas manual están organizadas en secciones numeradas. Las secciones comunes incluyen:

- `1`: Comandos de usuario.
- `2`: Llamadas al sistema.
- `3`: Funciones de biblioteca.
- `5`: Formatos de archivo.
- `8`: Comandos de administración del sistema.

A veces el mismo nombre existe en más de una sección. Puedes especificar el número de sección:

```bash
$ man 5 passwd
$ man 1 passwd
```

La primera orden abre la página del formato de archivo `passwd` en la sección 5. La segunda abre la página de la orden de usuario en la sección 1. Las referencias como `passwd(5)` utilizan la misma notación `topic(section)`.

:::single-choice{#open-passwd-file-format} ¿Qué orden abre la página de la sección 5 que documenta el formato del archivo `passwd`?

::option[`man passwd 5`]{#section-after-topic explanation="En esta forma de la orden, el selector de sección debe aparecer antes del tema. Este orden no solicita `passwd(5)`."}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="Al colocar la sección `5` antes de `passwd`, se selecciona específicamente la página del formato de archivo."}
::option[`man 1 passwd`]{#passwd-command-page explanation="La sección 1 contiene órdenes de usuario, por lo que selecciona la página de la orden `passwd`, no la del formato de archivo."}
:::

## Cuando falta una página

No todos los nombres de órdenes tienen una página del manual independiente instalada. Si `man` indica que no existe ninguna entrada:

- Ejecuta `type NAME` para averiguar cómo resuelve Bash el nombre.
- Utiliza `help NAME` si es una orden integrada de Bash.
- Prueba `NAME --help` si un programa externo admite esa convención.
- Comprueba si tu distribución ofrece un paquete de documentación independiente.

:::single-choice{#missing-builtin-manual} `type cd` indica que `cd` es una orden integrada de Bash y no hay una página man independiente. ¿Qué orden debes probar a continuación?

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis` resume entradas de la base de datos del manual. No puede proporcionar una página independiente inexistente para la orden integrada."}
::option[`file cd`]{#file-cd-name explanation="`file` clasifica objetos del sistema de archivos, pero aquí `cd` se resuelve como una orden integrada, no como una ruta."}
::option[`help cd`]{#builtin-cd-help .correct explanation="La orden integrada `help` de Bash proporciona la documentación propia de la shell para `cd`."}
:::

## Resumen

Ahora puedes localizar y recorrer la documentación instalada del manual.

1. Abrir una página por el nombre del tema.
2. Buscar y desplazarte por una página en el paginador habitual.
3. Salir del paginador y volver a la shell.
4. Seleccionar una sección numerada del manual.
5. Elegir otra fuente de ayuda cuando una página no esté disponible.
