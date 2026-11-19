---
lesson_id: "git-diff-command"
course_id: "git"
lang: "es"
order_index: 3
title: "git diff"
description: "Aprende a comparar el archivo del árbol de trabajo con su versión preparada mediante git diff."
meta_title: "git diff - Git"
meta_description: "Consulta las líneas que cambiaron y revisa los cambios preparados antes de guardarlos en un commit."
meta_keywords: "git diff, árbol de trabajo, área de preparación, diferencias, DevOps, Linux Journey"
---

El estado indica qué archivos cambiaron. Para ver las líneas concretas, usa `git diff`. En este ejemplo, la versión preparada de `index.html` ya contiene el encabezado Hello de la lección anterior.

## Comparar un archivo con su copia preparada

Cambia el encabezado del archivo de práctica y compara la copia de trabajo con la versión preparada.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

`--` separa las opciones de la ruta que quieres inspeccionar. En la salida, la línea que empieza por `-` corresponde a la versión anterior. La que empieza por `+` muestra el reemplazo. Las dos líneas de abajo son la parte de la diferencia que describe este cambio.

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} ¿Qué encabezado contiene ahora la copia de trabajo?

::option[Welcome.]{#git-diff-command-changed-heading-b .correct explanation="En esta comparación, el signo más indica el texto nuevo del árbol de trabajo."}
::option[Hello.]{#git-diff-command-changed-heading-a explanation="La línea del signo menos muestra el texto anterior del área de preparación."}
::option[Los dos encabezados.]{#git-diff-command-changed-heading-c explanation="Son dos versiones de la misma línea, antes y después del cambio."}
:::

## Comparar el área de preparación con el historial

Usa `git diff --staged -- index.html` para comparar la versión preparada con el último commit. Antes del primer commit, Git parte de un estado vacío. Aquí, esa salida muestra el encabezado Hello como una adición. A la vez, `git diff` sin más opciones muestra el cambio posterior a Welcome.

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} ¿Qué comando te permite ver qué versión entraría en un commit ahora mismo?

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="Compara el archivo de trabajo actual con la versión preparada."}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="El estado indica dónde hay cambios, sin mostrar las líneas modificadas."}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="Compara lo que has seleccionado con la última versión guardada."}
:::

![Terminal de LabEx comparando el encabezado Welcome del árbol de trabajo con el encabezado Hello preparado](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## Entender una salida vacía

Vuelve a añadir el archivo actual para actualizar la copia preparada.

```bash
$ git add index.html
$ git diff -- index.html
```

Ahora `git diff` puede no mostrar nada porque el archivo de trabajo y la copia preparada coinciden. Usa la comparación del área de preparación para ver el cambio que aún falta guardar. Git tampoco incluye los archivos sin seguimiento en estas comparaciones habituales. Si no sabes en qué estado está un cambio, consulta primero el estado.

:::single-choice{#git-diff-command-empty-diff} Ejecutas git diff sin opciones y no aparece nada justo después de preparar el cambio. ¿Dónde puedes ver todavía la diferencia respecto al historial?

::option[Ejecutando por segunda vez git diff sin opciones.]{#git-diff-command-empty-diff-a explanation="Repetir la misma comparación vuelve a comparar dos copias iguales."}
::option[Con git diff --staged.]{#git-diff-command-empty-diff-c .correct explanation="Así se compara la versión preparada con el historial."}
::option[Solo después de crear un commit.]{#git-diff-command-empty-diff-b explanation="Puedes revisar el contenido previsto del commit antes de guardarlo."}
:::

## Resumen

Ya puedes elegir una comparación que responda a tu pregunta.

1. Leer las líneas eliminadas y añadidas en una comparación.
2. Comparar el archivo de trabajo con el área de preparación.
3. Revisar los cambios preparados antes de crear un commit.
