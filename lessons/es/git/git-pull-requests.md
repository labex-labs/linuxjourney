---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "es"
order_index: 7
title: "Pull requests"
description: "Aprende a leer un pull request y a determinar qué cubren la revisión y las comprobaciones automáticas."
meta_title: "Pull requests - Git"
meta_description: "Identifica las ramas de un pull request, revisa qué archivos cambian y comprueba a qué commit corresponden los resultados automáticos."
meta_keywords: "pull request, PR, Git, revisión de código, DevOps, Linux Journey"
---

Un **pull request**, o PR, propone incorporar los cambios de una rama a otra. Git registra los commits y las ramas. El servicio de alojamiento añade la página de revisión, la conversación y las comprobaciones.

## Leer el origen y el destino

Supón que alguien del equipo propone una página de estado. En la página de revisión aparece `health-page → main`. La rama de origen, también llamada **head**, contiene el trabajo propuesto. La rama de destino, también llamada **base**, es la que lo recibiría.

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

En este punto, la página de revisión describe un cambio propuesto. La rama de destino lo recibe al fusionar el PR.

:::single-choice{#git-pull-requests-pr-direction} ¿Qué rama recibe la página de estado cuando se fusiona el PR?

::option[Una rama con el identificador del commit como nombre.]{#git-pull-requests-pr-direction-a explanation="El identificador señala una versión guardada. No indica cuál es la rama de destino."}
::option[Main.]{#git-pull-requests-pr-direction-b .correct explanation="La rama de destino es main, así que recibe el cambio revisado."}
::option[Health-page.]{#git-pull-requests-pr-direction-c explanation="Health-page es la rama de origen, que aporta el cambio."}
:::

## Revisar las diferencias

Abre la vista de archivos modificados y lee las diferencias con respecto a la rama de destino del PR. Añadir una línea a `health.txt` encaja con una página de estado sencilla. Si la revisión también muestra un cambio en `index.html`, comprueba si ese cambio pertenece a la misma propuesta. Revisa los archivos que aparecen realmente en el PR.

:::single-choice{#git-pull-requests-unexpected-file} Un PR titulado Add a health page también modifica la portada. ¿Dónde puedes comprobar el cambio exacto?

::option[En la comparación de los archivos modificados.]{#git-pull-requests-unexpected-file-a .correct explanation="La comparación muestra qué líneas cambia la propuesta."}
::option[Solo en el título.]{#git-pull-requests-unexpected-file-b explanation="El título resume la intención y puede omitir detalles."}
::option[En el nombre de la rama.]{#git-pull-requests-unexpected-file-c explanation="El nombre de la rama designa una línea de trabajo. No describe cada cambio."}
:::

## Leer las comprobaciones automáticas

Un servicio de alojamiento puede ejecutar una prueba cuando cambia un PR. Busca el commit o la revisión que cubre el resultado. Si alguien envía otro commit después de que pasen las comprobaciones, confirma que se ejecutaron las comprobaciones exigidas para la revisión nueva. Un resultado correcto significa que pasaron las comprobaciones que sí se ejecutaron.

:::single-choice{#git-pull-requests-changed-revision} Una prueba pasó para 3ab4501. El PR ahora apunta a 78ac900. ¿Qué debes comprobar antes de confiar en el resultado?

::option[Si estaba bien escrito el mensaje del commit original.]{#git-pull-requests-changed-revision-a explanation="El mensaje no indica si se probó el commit más reciente."}
::option[Si el PR conserva el mismo título.]{#git-pull-requests-changed-revision-b explanation="El título puede seguir siendo el mismo aunque cambie el código."}
::option[Si se ejecutaron las comprobaciones para la revisión actualizada.]{#git-pull-requests-changed-revision-c .correct explanation="El resultado anterior correspondía a otra revisión."}
:::

## Resumen

Ya puedes saber qué propone un pull request y qué pruebas respaldan su fusión.

1. Localizar las ramas de origen y de destino.
2. Verificar los cambios propuestos en la vista de archivos modificados.
3. Comprobar qué revisión cubre un resultado automatizado.
