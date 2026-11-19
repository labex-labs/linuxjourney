---
lesson_id: "git-commits"
course_id: "git"
lang: "es"
order_index: 4
title: "Commits"
description: "Aprende a guardar los cambios preparados en un commit y a localizarlo en el historial de Git."
meta_title: "Commits - Git"
meta_description: "Guarda el contenido del área de preparación, añade un mensaje e identifica el commit en el historial."
meta_keywords: "commits, Git, área de preparación, git commit, git log, DevOps, Linux Journey"
---

Un **commit** guarda los archivos seleccionados en el área de preparación. También registra un mensaje, los datos del autor y la relación con los commits anteriores. El identificador que asigna Git permite localizar ese punto exacto del historial.

## Configurar una identidad para el repositorio de práctica

Git registra un nombre y un correo con cada commit. Configura valores de ejemplo que solo se apliquen a este repositorio. Esos datos quedan en el historial y no te dan acceso a ningún servicio remoto.

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

Usa el repositorio de práctica con `index.html` preparado. Si quieres comprobar qué archivos entrarán en el commit, ejecuta `git status`.

:::single-choice{#git-commits-identity-scope} ¿Qué hace aquí la opción --local?

::option[Inicia sesión en un servicio de alojamiento compartido.]{#git-commits-identity-scope-b explanation="El nombre y el correo son metadatos del commit. La autenticación en un servicio remoto es un paso distinto."}
::option[Configura los datos del autor para este repositorio.]{#git-commits-identity-scope-a .correct explanation="La configuración local se aplica al repositorio actual."}
::option[Cambia el autor de todos los commits existentes.]{#git-commits-identity-scope-c explanation="La configuración se usa en los commits posteriores."}
:::

## Guardar la versión seleccionada

Ejecuta `git commit` después de preparar la versión que quieres guardar. Con `-m` puedes indicar el mensaje en la línea de comandos.

```bash
$ git commit -m "Set the homepage heading"
```

Un commit guarda la versión preparada de un archivo. Si vuelves a editar el árbol de trabajo después de prepararlo, ese cambio se queda fuera del commit hasta que vuelvas a preparar el archivo.

:::single-choice{#git-commits-staged-snapshot} Preparaste Welcome y luego escribiste Hi en el archivo sin volver a prepararlo. ¿Qué encabezado se incluirá en el commit?

::option[Welcome, porque esa fue la versión preparada.]{#git-commits-staged-snapshot-c .correct explanation="Git lee el contenido preparado al guardar el commit."}
::option[Hi, porque es el texto más reciente que hay en el disco.]{#git-commits-staged-snapshot-a explanation="La copia de trabajo más reciente puede ser distinta de la preparada."}
::option[Los dos, porque Git guarda automáticamente cada cambio.]{#git-commits-staged-snapshot-b explanation="El contenido preparado incluye una sola versión seleccionada del archivo."}
:::

## Leer un historial abreviado

Usa `git log --oneline` para ver el historial en formato breve. Cada línea comienza con un identificador de commit abreviado seguido de su mensaje. Tu identificador será distinto del ejemplo.

```text
$ git log --oneline
a12c345 Set the homepage heading
```

Usa el identificador para referirte a un commit concreto, ya que varios commits pueden tener el mismo mensaje. La salida suele empezar por el más reciente de la rama actual.

:::single-choice{#git-commits-identify-snapshot} Dos commits tienen el mensaje Set the homepage heading. ¿Cómo distingues las dos versiones que guardaron?

::option[Por el mensaje que comparten.]{#git-commits-identify-snapshot-a explanation="El mismo texto puede aparecer en varios commits."}
::option[Por el nombre del archivo afectado por los dos cambios.]{#git-commits-identify-snapshot-c explanation="El mismo archivo puede formar parte de muchos commits."}
::option[Por el identificador del commit.]{#git-commits-identify-snapshot-b .correct explanation="Cada identificador permite referirse a una entrada concreta."}
:::

Para practicar la preparación de archivos y la creación de commits en una terminal del navegador, prueba [Tu primer laboratorio de Git](https://labex.io/tutorials/git-your-first-git-lab-92739).

## Resumen

Ya puedes guardar el trabajo preparado y localizarlo en el historial.

1. Configurar una identidad para los commits en un repositorio de práctica.
2. Guardar la versión preparada con un mensaje claro.
3. Identificar un commit en el historial abreviado.
