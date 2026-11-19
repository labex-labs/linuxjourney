---
lesson_id: "git-revert-command"
course_id: "git"
lang: "es"
order_index: 8
title: "git revert"
description: "Aprende cómo git revert registra la reversión de un cambio y conserva el commit original."
meta_title: "git revert - Git"
meta_description: "Crea un commit que deshaga un cambio compartido y verifica el resultado en los archivos y el historial."
meta_keywords: "git revert, deshacer un cambio, historial de Git, DevOps, Linux Journey"
---

Incluso un cambio que ya has compartido se puede deshacer. Usa `git revert` para aplicar el cambio inverso en un commit nuevo. El historial conserva tanto el cambio original como la decisión de deshacerlo.

## Encontrar el cambio que quieres deshacer

En el repositorio de práctica, `main` contiene los commits de la portada y de la página de estado. Usa el historial abreviado para identificar la entrada más reciente. Los identificadores de abajo son ilustrativos.

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD` se refiere al commit que tienes activo. Confirma que es el cambio que quieres deshacer. Usa `git status` para verificar que el árbol de trabajo esté limpio.

:::single-choice{#git-revert-command-newest-commit} ¿Qué cambio desharía una reversión de HEAD en este ejemplo?

::option[El cambio anterior en el encabezado de la portada.]{#git-revert-command-newest-commit-b explanation="El cambio del encabezado corresponde al commit anterior."}
::option[Los dos cambios en una sola operación.]{#git-revert-command-newest-commit-c explanation="Aquí HEAD se refiere a un solo commit. La reversión se aplica a ese commit."}
::option[La incorporación de la página de estado.]{#git-revert-command-newest-commit-a .correct explanation="HEAD apunta a la entrada más reciente que aparece en esta rama."}
:::

## Guardar la reversión

Con el repositorio de práctica limpio, revierte el commit de la página de estado. Esto cambia archivos del árbol de trabajo y crea un commit. Usa `--no-edit` para conservar el mensaje de reversión que propone Git.

```bash
$ git revert --no-edit HEAD
```

En el ejemplo se elimina el archivo de la página de estado porque el commit original lo añadió. Si un cambio posterior tocó las mismas líneas, Git puede detenerse y pedirte que resuelvas el conflicto. Consulta el estado antes de continuar.

:::single-choice{#git-revert-command-undo-effect} ¿Qué cambio de archivo deberías ver si la reversión del ejemplo funciona?

::option[Se borran tanto la portada como la página de estado.]{#git-revert-command-undo-effect-a explanation="El commit anterior de la portada sigue vigente."}
::option[Se elimina el archivo de la página de estado.]{#git-revert-command-undo-effect-b .correct explanation="La reversión deshace la incorporación de ese archivo en el commit seleccionado."}
::option[Se incorpora la página de estado por segunda vez.]{#git-revert-command-undo-effect-c explanation="Revert aplica el cambio inverso. No repite la incorporación."}
:::

![Historial de Git con el nuevo commit de reversión y el commit original de la página de estado](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## Verificar el historial después de la reversión

Ejecuta `git log --oneline` de nuevo. Debería aparecer una entrada de reversión encima del commit original de la página de estado. Con `git status --short` puedes ver si quedan cambios locales. El nuevo commit se puede revisar y compartir igual que los demás.

:::single-choice{#git-revert-command-history-after-revert} ¿Qué debería seguir apareciendo debajo de la entrada de reversión?

::option[El commit original de la página de estado.]{#git-revert-command-history-after-revert-c .correct explanation="El par deja constancia tanto del cambio como de su reversión."}
::option[Solo el primer commit del encabezado.]{#git-revert-command-history-after-revert-a explanation="El commit original de la página de estado sigue en el historial."}
::option[Ningún commit.]{#git-revert-command-history-after-revert-b explanation="La reversión añade un commit y conserva el historial de la rama."}
:::

## Conservar los demás cambios

Supón que en el historial hay tres cambios independientes. Primero se añadió la página de estado y después se corrigió una errata en la portada. Ambos cambios se compartieron. Si reviertes el commit que añadió la página de estado, puedes quitar el archivo y conservar la corrección independiente. Lee el historial y los archivos afectados antes de elegir un commit.

:::single-choice{#git-revert-command-final-application} ¿Qué comprobación demuestra que la reversión respetó los cambios que querías conservar?

::option[El commit que añadió la página de estado desapareció del historial.]{#git-revert-command-final-application-b explanation="Una reversión conserva la entrada original."}
::option[La corrección de la errata también desapareció de la portada.]{#git-revert-command-final-application-c explanation="La corrección era un cambio aparte y debería conservarse."}
::option[El archivo de estado ya no está, la portada conserva la corrección y el historial muestra la reversión.]{#git-revert-command-final-application-a .correct explanation="Estas comprobaciones abarcan el cambio deshecho, la corrección independiente y la nueva entrada en el historial."}
:::

## Resumen

Ya puedes deshacer un cambio guardado y dejar constancia del cambio original y su reversión.

1. Identificar el commit exacto que quieres revertir.
2. Revertir el cambio con el árbol de trabajo limpio.
3. Verificar ambas entradas en el historial.
