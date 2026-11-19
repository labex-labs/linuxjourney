---
lesson_id: "git-repositories"
course_id: "git"
lang: "es"
order_index: 1
title: "Repositorios"
description: "Aprende qué guarda un repositorio de Git y crea uno vacío para un pequeño sitio web."
meta_title: "Repositorios - Git"
meta_description: "Crea un repositorio de Git, localiza el árbol de trabajo y distingue cuándo inicializar un repositorio y cuándo clonarlo."
meta_keywords: "repositorio Git, árbol de trabajo, git init, git clone, DevOps, Linux Journey"
---

Un sitio web empieza con unos cuantos archivos. Git permite registrar cómo eran en distintos momentos. Los archivos del proyecto y su historial forman tu espacio de trabajo local con Git.

## Crear un repositorio

Empieza en un directorio de práctica donde puedas crear una carpeta. Ejecuta una vez los siguientes comandos. El signo de dólar señala el prompt de la shell.

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

La carpeta nueva es el **árbol de trabajo**, donde editarás los archivos del proyecto. Git crea allí el directorio oculto `.git` para guardar el historial y la configuración. El repositorio nuevo aún no tiene cambios guardados. La rama inicial se llama `main`.

:::single-choice{#git-repositories-empty-history} Inicializas un repositorio en una carpeta que ya contiene index.html. ¿Qué ocurre con el historial de ese archivo?

::option[Git guarda de inmediato el archivo en el primer commit.]{#git-repositories-empty-history-b explanation="La inicialización no guarda ningún archivo del proyecto."}
::option[Git puede guardar el archivo en un commit posterior.]{#git-repositories-empty-history-a .correct explanation="Inicializar prepara el repositorio. Guardar una versión es una operación aparte."}
::option[Git mueve el archivo al directorio oculto de Git.]{#git-repositories-empty-history-c explanation="Los archivos del proyecto se quedan en el árbol de trabajo, donde puedes editarlos."}
:::

![Terminal de LabEx con un repositorio de Git recién inicializado y la carpeta de práctica como raíz](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## Reconocer el árbol de trabajo

Usa `git rev-parse --show-toplevel` para mostrar la raíz del repositorio actual. Dentro de la carpeta de práctica, la shell debería mostrar una ruta que termine en `journey-git`. Las subcarpetas del árbol de trabajo pertenecen al mismo repositorio, salvo que alguna contenga un repositorio independiente.

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} Entras en un subdirectorio llamado images dentro de journey-git. ¿Qué directorio debería mostrar Git como raíz?

::option[El directorio journey-git.]{#git-repositories-find-root-b .correct explanation="Git encuentra la raíz del repositorio por encima del directorio actual."}
::option[El subdirectorio images.]{#git-repositories-find-root-a explanation="La raíz pertenece a todo el repositorio, incluso si la shell está en un subdirectorio."}
::option[El directorio oculto .git.]{#git-repositories-find-root-c explanation="El comando muestra la raíz del árbol de trabajo, donde están los archivos del proyecto."}
:::

## Empezar con un historial existente

Usa `git clone` cuando ya exista un repositorio que quieras copiar. Un clon normal crea un nuevo árbol de trabajo local e importa el historial existente. Usa `git init` para empezar a registrar el historial de un proyecto local. En las próximas lecciones seguirás usando `journey-git`.

:::single-choice{#git-repositories-choose-start} Alguien de tu equipo te da la dirección de un repositorio cuyo historial necesitas. ¿Cómo debes empezar?

::option[Crear una carpeta vacía e inicializar un repositorio.]{#git-repositories-choose-start-a explanation="El repositorio nuevo no incluye el historial del otro."}
::option[Copiar solo los archivos visibles del sitio web.]{#git-repositories-choose-start-b explanation="Los archivos visibles representan una versión concreta y no incluyen el historial."}
::option[Clonar el repositorio de tu equipo.]{#git-repositories-choose-start-c .correct explanation="El clon copia el historial compartido y crea un árbol de trabajo local."}
:::

## Resumen

Ya puedes elegir cómo crear un repositorio local de Git.

1. Identificar el árbol de trabajo y el directorio oculto de Git.
2. Localizar la raíz desde un subdirectorio.
3. Inicializar un repositorio para iniciar un historial o clonarlo para conservar uno existente.
