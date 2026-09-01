---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "es"
order_index: 17
title: "whatis"
description: "Aprende a obtener descripciones concisas de las páginas del manual y a interpretar sus números de sección."
meta_title: "whatis - Línea de Comandos"
meta_description: "Aprende el comando whatis de Linux con ejemplos para obtener descripciones de comandos en una línea desde las páginas man y entender múltiples secciones del manual."
meta_keywords: "comando whatis, linux whatis, descripción de comando linux, resumen página man, ayuda línea de comandos, apropos"
---

Cuando reconoces el nombre de una orden, pero has olvidado para qué sirve, `whatis` puede ofrecer un recordatorio breve procedente de la base de datos de páginas del manual.

## Consulta de un nombre exacto

Usar `whatis` es sencillo. Escribe `whatis` seguido del comando sobre el que quieres saber.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

La salida es una descripción, no una lista de opciones ni ejemplos. Utiliza `man cat` o `cat --help` cuando necesites más detalles.

:::single-choice{#describe-known-command} Conoces el nombre `cat` y quieres su descripción de una línea en el manual. ¿Qué orden debes ejecutar?

::option[`man cat`]{#manual-cat explanation="`man cat` abre la página completa del manual. Proporciona más información que el recordatorio de una línea solicitado."}
::option[`apropos cat`]{#apropos-cat explanation="`apropos` busca una palabra clave en las descripciones y puede devolver muchos temas relacionados. Es más amplio que una consulta por nombre exacto."}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis` consulta el nombre exacto del tema y muestra su descripción concisa procedente de la base de datos del manual."}
:::

## Lectura de los números de sección

La descripción que proporciona `whatis` proviene de la sección `NAME` de la página del manual del comando. Si un nombre tiene varias páginas del manual en diferentes secciones, `whatis` puede mostrar más de una línea.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

El número entre paréntesis es la sección del manual. Aquí, `passwd(1)` describe la orden de usuario y `passwd(5)`, un formato de archivo. Puedes abrirlas explícitamente con `man 1 passwd` o `man 5 passwd`.

:::single-choice{#interpret-whatis-section} En la salida `passwd (5) - the password file`, ¿qué identifica `(5)`?

::option[La quinta opción que acepta la orden `passwd`.]{#fifth-option explanation="El número no es la posición de una opción. Las opciones se documentan dentro de la página del manual elegida."}
::option[La sección del manual que contiene la página del formato de archivo.]{#section-five .correct explanation="La sección 5 se utiliza para formatos de archivo y convenciones, por lo que `passwd(5)` hace referencia a esa sección."}
::option[Cinco páginas del manual que comparten el nombre `passwd`.]{#five-pages explanation="Pueden existir varios resultados, pero el valor entre paréntesis identifica una sección, no una cantidad de páginas."}
:::

## Elección entre whatis, man y apropos

- `whatis ls`: Muestra una descripción en una línea para un nombre de comando exacto.
- `man ls`: Abre la página completa del manual.
- `apropos keyword`: Busca en las descripciones de las páginas man una palabra clave.

Por ejemplo:

```bash
$ apropos password
```

Utiliza `apropos` cuando conoces la tarea, pero no el nombre de la orden. Utiliza `whatis` cuando ya conoces el nombre.

:::single-choice{#search-by-purpose} No conoces el nombre de una orden, pero quieres buscar la palabra clave `password` en las descripciones del manual. ¿Qué orden sirve para esta tarea?

::option[`apropos password`]{#apropos-password .correct explanation="`apropos` busca la palabra clave en los nombres y descripciones de las páginas del manual, lo que ayuda a descubrir temas pertinentes."}
::option[`whatis password`]{#exact-password explanation="`whatis` busca un tema exacto del manual llamado `password`. No es la interfaz general de búsqueda por palabras clave."}
::option[`man password`]{#manual-password explanation="`man` intenta abrir una página con ese nombre de tema. No realiza la búsqueda solicitada en las descripciones."}
:::

## Cuando no aparece ninguna descripción

Si `whatis` informa de que no hay nada apropiado, quizá el tema no tenga instalada una página del manual o la base de datos esté desactualizada. Este resultado no demuestra que no exista un ejecutable, alias, función u orden integrada con ese nombre. Utiliza `type NAME` para ver cómo resuelve Bash el nombre y elige después la fuente de ayuda adecuada.

:::single-choice{#whatis-versus-type} `whatis deploy` no encuentra ninguna descripción del manual. ¿Qué orden comprueba si Bash resuelve `deploy` como alias, función, orden integrada o ejecutable?

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="Cambiar la consulta de la base de datos del manual no muestra todos los alias, funciones, órdenes integradas y resoluciones de rutas de Bash."}
::option[`man 5 deploy`]{#manual-five-deploy explanation="Esta orden intenta abrir una página de la sección 5. No determina cómo resuelve Bash el nombre de la orden."}
::option[`type deploy`]{#resolve-deploy .correct explanation="La orden `type` de Bash informa de cómo resuelve la shell actual un nombre, exista o no una descripción instalada en el manual."}
:::

## Resumen

Ahora puedes obtener e interpretar descripciones concisas de la base de datos del manual.

1. Consultar un tema exacto con `whatis`.
2. Leer la sección del manual indicada entre paréntesis.
3. Utilizar `man` cuando necesites la página completa.
4. Utilizar `apropos` cuando conozcas una palabra clave en vez de un nombre.
