---
lesson_id: "help-command"
course_id: "command-line"
lang: "es"
order_index: 15
title: "help"
description: "Aprende a elegir entre la ayuda integrada, la salida de uso de un programa o las páginas del manual para consultar una orden."
meta_title: "help - Línea de Comandos"
meta_description: "Aprende cómo obtener ayuda en la línea de comandos de Linux con Bash help, salida --help, páginas man y type para comandos internos y externos."
meta_keywords: "comando help linux, ayuda bash, ayuda línea de comandos, --help, comando interno shell, comando man, comando type"
---

No necesitas memorizar todas las opciones de cada orden. Bash y muchos programas instalados pueden explicar su sintaxis directamente en la terminal, pero la fuente de ayuda adecuada depende del tipo de orden que utilices.

## Ayuda para órdenes integradas de Bash

Bash proporciona la orden integrada `help` para las órdenes implementadas por la propia shell. Algunos ejemplos son `cd`, `history` y `type`.

Para usar `help`, escríbelo seguido del nombre del comando interno.

```bash
$ help echo
```

La salida describe la sintaxis y el comportamiento de la orden integrada. Ejecutar `help` sin argumentos enumera las órdenes para las que Bash dispone de ayuda.

:::single-choice{#help-for-bash-cd}
¿Qué orden muestra la entrada de ayuda de Bash para su orden integrada `cd`?

::option[`cd --help`]{#cd-help-option explanation="Algunas órdenes integradas pueden reconocer opciones, pero la interfaz de documentación específica de Bash es `help` seguida del nombre de la orden."}
::option[`help cd`]{#help-cd .correct explanation="La orden integrada `help` de Bash busca la documentación de la orden integrada indicada, en este caso `cd`."}
::option[`type cd`]{#type-cd explanation="`type` explica cómo resuelve Bash el nombre `cd`. Identifica la orden, pero no muestra su entrada de ayuda completa."}
:::

## Solicitud del resumen de uso de un programa

Para la mayoría de los otros programas ejecutables que no están integrados en el shell, el comando `help` no funcionará. En cambio, una convención común es proporcionar una opción `--help`. Esta opción indica al programa que imprima un resumen de uso y luego termine.

```bash
$ ls --help
```

Aunque la mayoría de los desarrolladores siguen este estándar, no es universal. Probar `--help` suele ser un buen primer paso para un programa desconocido.

:::single-choice{#quick-ls-usage}
¿Qué orden suele mostrar un resumen rápido de uso proporcionado por el programa externo `ls`?

::option[`help ls`]{#bash-help-ls explanation="`help` de Bash documenta órdenes integradas. En un sistema habitual no proporciona la página de uso del programa externo `ls`."}
::option[`ls --help`]{#ls-help .correct explanation="GNU `ls` sigue la convención habitual de `--help` y muestra su uso y sus opciones."}
::option[`type --help ls`]{#type-help-ls explanation="Esta orden pregunta a la orden integrada `type` por sus propias opciones, no pide a `ls` que explique su uso."}
:::

## Cómo averiguar la resolución de un nombre en Bash

Si no estás seguro de si un comando es un interno de Bash o un programa externo, usa `type`.

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

El resultado exacto puede variar según los alias, funciones, programas instalados y el valor de `PATH`. Utiliza `type -a NAME` si quieres que Bash muestre todas las resoluciones conocidas, no solo la primera que usaría.

:::single-choice{#identify-command-resolution}
No sabes si `deploy` es un alias, una función, una orden integrada o un ejecutable. ¿Qué orden de Bash comprueba cómo se resuelve el nombre?

::option[`type deploy`]{#type-deploy .correct explanation="La orden integrada `type` informa de cómo interpreta Bash el nombre en el entorno actual de la shell."}
::option[`help deploy`]{#help-deploy explanation="`help` busca documentación de órdenes integradas de Bash. En general no identifica alias, funciones y archivos externos."}
::option[`deploy --help`]{#deploy-help explanation="Esta opción intenta ejecutar la orden y depende de que esta admita la opción. No explica primero cómo resolvió Bash el nombre."}
:::

## Elección del nivel de detalle

- Usa `help COMMAND` para comandos internos de Bash como `cd`, `echo` y `history`.
- Usa `COMMAND --help` para un resumen rápido de muchos comandos externos.
- Usa `man COMMAND` para páginas de manual detalladas.
- Usa `whatis COMMAND` para una descripción de una línea.

Las próximas lecciones examinan con más detalle las páginas del manual y las descripciones de una sola línea.

:::single-choice{#choose-detailed-manual}
Necesitas documentación detallada de la orden externa `ls`, no solo un resumen breve de uso. ¿Qué orden debes probar?

::option[`man ls`]{#man-ls .correct explanation="`man ls` abre la página del manual instalada, que normalmente describe con más detalle la sintaxis, las opciones y el comportamiento."}
::option[`whatis ls`]{#whatis-ls explanation="`whatis` está diseñado para mostrar descripciones concisas de las páginas del manual. No proporciona la documentación detallada solicitada."}
::option[`type ls`]{#type-ls explanation="`type` informa de cómo resuelve Bash el nombre `ls`. No muestra el manual detallado del programa."}
:::

## Resumen

Ahora puedes elegir una fuente de ayuda según cómo resuelva Bash una orden.

1. Utilizar `help` para las órdenes integradas de Bash.
2. Probar `--help` para obtener un resumen rápido de uso de un programa.
3. Inspeccionar la resolución de nombres con `type`.
4. Abrir documentación detallada con `man`.
