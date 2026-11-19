---
lesson_id: "git-status-command"
course_id: "git"
lang: "es"
order_index: 2
title: "git status"
description: "Aprende a identificar archivos sin seguimiento, preparados y modificados con git status."
meta_title: "git status - Git"
meta_description: "Consulta el árbol de trabajo con git status y comprueba qué cambios has preparado para el siguiente commit."
meta_keywords: "git status, estado de Git, área de preparación, archivos sin seguimiento, DevOps, Linux Journey"
---

Al trabajar en un repositorio, `git status` te indica qué ve Git en el árbol de trabajo y qué has seleccionado para guardar después. Usa el repositorio vacío `journey-git` de la lección anterior.

## Localizar un archivo nuevo

Crea una página pequeña. Después usa el formato abreviado para que la salida resulte fácil de leer.

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

Aquí, `>` escribe en el archivo indicado y reemplaza su contenido si ya existe. Para el archivo nuevo, el estado abreviado muestra `?? index.html`. Git dice que está **sin seguimiento**. El archivo existe, pero todavía no está seleccionado para incluirlo en una versión guardada.

:::single-choice{#git-status-command-untracked-file} Git muestra dos signos de interrogación junto a un archivo nuevo. ¿Qué indica esa marca?

::option[El archivo forma parte de la última versión guardada.]{#git-status-command-untracked-file-a explanation="La última versión guardada no incluye un archivo sin seguimiento."}
::option[El archivo se eliminó del árbol de trabajo.]{#git-status-command-untracked-file-c explanation="Git detecta el archivo en tu árbol de trabajo."}
::option[El archivo existe y aún no se ha seleccionado para la próxima versión.]{#git-status-command-untracked-file-b .correct explanation="Puedes incluir el archivo en el área de preparación."}
:::

![El estado abreviado de Git muestra cómo index.html pasa de estar sin seguimiento a estar preparado](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## Consultar los cambios preparados

Ejecuta `git add` para seleccionar el contenido actual del archivo para la siguiente versión guardada, llamada **commit**. El **área de preparación** contiene esa selección. En la primera columna del estado abreviado aparece ahora una `A`, que indica que el archivo nuevo está preparado.

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} Después de git add, ¿dónde está la versión seleccionada de index.html?

::option[Ya está en un commit nuevo.]{#git-status-command-staged-new-a explanation="Git add prepara el siguiente commit. Aún no lo crea."}
::option[En el área de preparación.]{#git-status-command-staged-new-c .correct explanation="Git seleccionó el contenido que tenía el archivo cuando ejecutaste git add."}
::option[En el repositorio de otra persona.]{#git-status-command-staged-new-b explanation="Este comando cambia únicamente tu área de preparación local."}
:::

## Distinguir dos tipos de cambios

El estado abreviado tiene dos columnas antes del nombre del archivo. La primera indica los cambios preparados. La segunda indica los hechos en el árbol de trabajo después de preparar el archivo. Por ejemplo, `AM index.html` significa que Git preparó un archivo nuevo y que después modificaste la copia de trabajo. Si prefieres ver los detalles por grupos, ejecuta `git status` sin opciones.

:::single-choice{#git-status-command-two-columns} Ves AM junto a index.html. ¿Qué deberías comprobar antes de crear el siguiente commit?

::option[Si la copia preparada incluye la modificación que quieres guardar.]{#git-status-command-two-columns-a .correct explanation="La M de la segunda columna indica que la copia de trabajo tiene un cambio posterior."}
::option[Si el repositorio contiene otro archivo llamado AM.]{#git-status-command-two-columns-b explanation="AM son dos marcas de estado de index.html."}
::option[Si el archivo se ha eliminado del disco.]{#git-status-command-two-columns-c explanation="La M indica una modificación en el árbol de trabajo."}
:::

## Resumen

Ya puedes comprobar qué cambios guardaría Git en el próximo commit.

1. Reconocer un archivo nuevo sin seguimiento.
2. Preparar un archivo con git add.
3. Consultar por separado los cambios preparados y los del árbol de trabajo.
