---
lesson_id: "git-remotes"
course_id: "git"
lang: "es"
order_index: 6
title: "Repositorios remotos"
description: "Aprende cómo un remoto de Git conecta repositorios y distingue entre traer y enviar cambios."
meta_title: "Repositorios remotos - Git"
meta_description: "Configura un repositorio desnudo local como remoto, envía un commit y comprueba qué se actualiza al traer cambios."
meta_keywords: "remotos de Git, git remote, git fetch, git push, DevOps, Linux Journey"
---

Un **remoto** es una dirección con nombre que tu repositorio local de Git puede usar para ponerse en contacto con otro repositorio. El otro repositorio puede estar en un servicio de alojamiento o en una carpeta del mismo equipo. Esta práctica usa una carpeta local separada, así que puedes hacerla sin una cuenta en un servicio de alojamiento.

## Añadir una dirección

Desde el repositorio de práctica, crea un **repositorio desnudo** aparte. Un repositorio desnudo guarda el historial y las referencias, pero carece de árbol de trabajo. Puede recibir commits de tu espacio de trabajo. Para empezar desde cero, necesitas que el directorio `journey-remote.git` todavía no esté en uso.

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

El nombre `origin` se usa por convención. En la lista de remotos puedes ver a qué dirección corresponde.

:::single-choice{#git-remotes-add-address} Ejecutaste git remote add y apareció origin en la lista. ¿Qué hizo Git?

::option[Guardó un nombre para el otro repositorio.]{#git-remotes-add-address-b .correct explanation="En los próximos comandos puedes referirte a esa dirección como origin."}
::option[Subió todos los commits locales.]{#git-remotes-add-address-a explanation="Añadir un remoto registra la dirección. Para subir los commits se usa push."}
::option[Clonó otro árbol de trabajo en el proyecto.]{#git-remotes-add-address-c explanation="El árbol de trabajo existente sigue en el mismo sitio."}
:::

## Enviar una rama

Usa `git push` para enviar commits locales y pedir al remoto que actualice su rama. La opción `-u` registra esa rama remota como la rama de seguimiento, o upstream, que Git asocia a la rama local para comandos posteriores.

```bash
$ git push -u origin main
```

Esta operación solo envía a la carpeta de práctica separada. Un remoto compartido puede pedir autorización y rechazar cambios. Comprueba su respuesta antes de dar el envío por correcto.

:::single-choice{#git-remotes-push-direction} ¿Qué comando envía un commit nuevo de tu main local a este remoto?

::option[git fetch origin]{#git-remotes-push-direction-b explanation="Fetch obtiene información del remoto y la trae al repositorio local."}
::option[git remote -v]{#git-remotes-push-direction-c explanation="Este comando muestra qué dirección usa origin."}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="Push transfiere los commits que necesita el remoto y solicita que actualice la rama."}
:::

## Traer cambios

Usa `git fetch origin` para actualizar tu vista local del historial remoto. Git usa una **rama de seguimiento remoto** como `origin/main` para recordar el último estado que obtuvo. Puedes consultarla con `git log --oneline origin/main`. Fetch por sí solo deja el árbol de trabajo en la rama local actual.

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} Después de fetch, origin/main avanzó, pero tu main local no. ¿Qué afirmación encaja?

::option[Fetch sobrescribió los archivos que estabas editando.]{#git-remotes-after-fetch-a explanation="Fetch actualiza el registro local del estado de la rama remota."}
::option[Git conoció el cambio remoto. Integrarlo es un paso aparte.]{#git-remotes-after-fetch-c .correct explanation="Tu rama local puede quedarse donde estaba mientras avanza origin/main."}
::option[Tu push actualizó el remoto durante fetch.]{#git-remotes-after-fetch-b explanation="Fetch recibe información del remoto."}
:::

## Resumen

Ya puedes distinguir a qué repositorio afecta un comando de Git.

1. Añadir y consultar la dirección de un remoto.
2. Enviar una rama e identificar la rama que sigue.
3. Traer el historial remoto sin cambiar los archivos que tienes abiertos en el árbol de trabajo.
