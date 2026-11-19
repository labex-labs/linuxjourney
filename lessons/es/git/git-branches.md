---
lesson_id: "git-branches"
course_id: "git"
lang: "es"
order_index: 5
title: "Ramas"
description: "Aprende a usar ramas para trabajar por separado y a incorporar un cambio a main mediante una fusión."
meta_title: "Ramas - Git"
meta_description: "Crea una rama local, guarda un cambio en ella y usa git merge para incorporarlo a main."
meta_keywords: "ramas de Git, git switch, git merge, avance rápido, DevOps, Linux Journey"
---

Una **rama** es un nombre que apunta a un commit. Cuando creas un commit en la rama actual, el nombre pasa a apuntar al nuevo commit. Las demás ramas mantienen su posición hasta que las actualizas.

## Empezar una línea de trabajo aparte

En el repositorio de práctica, parte de `main`, crea una rama llamada `health-page` y cámbiate a ella. La opción `-c` de `git switch` significa que se va a crear la rama.

```bash
$ git switch -c health-page
```

Al principio, ambas ramas apuntan al mismo commit. Usa `git branch --show-current` para ver cuál avanzará cuando hagas el próximo commit.

:::single-choice{#git-branches-start-pointer} Justo después de git switch -c health-page, ¿a qué commit apunta la rama nueva?

::option[A un commit vacío que creó el comando.]{#git-branches-start-pointer-a explanation="El comando crea un nombre que apunta a un commit ya existente."}
::option[A un commit del repositorio de otra persona.]{#git-branches-start-pointer-c explanation="Este comando crea una rama local en el repositorio actual."}
::option[Al commit del que partiste.]{#git-branches-start-pointer-b .correct explanation="Al principio las dos ramas apuntan a la misma versión."}
:::

## Guardar un cambio en la rama

Añade un archivo de estado de una línea y guarda el cambio mientras `health-page` sea la rama actual.

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

Imagina que el commit de la portada es A y el de la página de estado es B.

```text
A (main) --- B (health-page)
```

Solo `health-page` avanzó hasta B. Si vuelves a `main` con el árbol de trabajo limpio, los archivos vuelven al estado de A.

:::single-choice{#git-branches-branch-snapshot} Antes de la fusión, ¿qué rama contiene el commit de la página de estado?

::option[Las dos, porque comparten repositorio.]{#git-branches-branch-snapshot-a explanation="Las ramas de un repositorio pueden apuntar a versiones distintas."}
::option[Solo health-page.]{#git-branches-branch-snapshot-c .correct explanation="Esa era la rama actual cuando se creó el commit B."}
::option[Solo main, porque partiste de ahí.]{#git-branches-branch-snapshot-b explanation="Main no avanzó al hacer el commit en health-page."}
:::

## Incorporar el cambio a main

Cámbiate a la rama que debe recibir el cambio e indica en el comando desde qué rama quieres incorporarlo.

```bash
$ git switch main
$ git merge health-page
```

Aquí, `main` no tiene commits propios después de A. Git puede moverla directamente a B mediante un **avance rápido**. Si cada rama tiene commits nuevos, puede ser necesario combinar los cambios. Lee el resultado antes de dar la fusión por terminada.

:::single-choice{#git-branches-merge-direction} Quieres que main reciba el cambio de health-page. ¿Cómo debes ejecutar la fusión?

::option[En main, indicando health-page como origen.]{#git-branches-merge-direction-a .correct explanation="El resultado de la fusión se aplica a la rama actual."}
::option[En health-page, indicando main como origen.]{#git-branches-merge-direction-b explanation="Ese comando actualizaría health-page."}
::option[En una rama nueva que no usa ninguna de las partes.]{#git-branches-merge-direction-c explanation="Main mantendrá su posición hasta que reciba el cambio."}
:::

## Resumen

Ya puedes seguir un cambio desde una rama local hasta main.

1. Crear una rama que apunte al commit actual.
2. Guardar un cambio en la rama prevista.
3. Incorporar el cambio a la rama que debe recibirlo.
