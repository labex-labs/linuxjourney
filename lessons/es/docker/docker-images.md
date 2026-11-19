---
lesson_id: "docker-images"
course_id: "docker"
lang: "es"
order_index: 2
title: "Imágenes"
description: "Aprende a leer una referencia de imagen y a comprobar si esa imagen está disponible en el entorno local."
meta_title: "Imágenes - Docker"
meta_description: "Lee los nombres y las etiquetas de imágenes Docker, conoce los registros y las descargas, y distingue la lista de imágenes de la de contenedores."
meta_keywords: "imágenes de Docker, etiquetas de imagen, registro de imágenes, docker pull, docker image ls"
---

Una imagen de Docker reúne un programa, sus archivos y su configuración predeterminada. Docker usa ese paquete para crear un contenedor. En esta lección aprenderás a leer los nombres de las imágenes y a saber cuáles tiene ya Docker.

## Leer el nombre y la etiqueta de una imagen

En `nginx:alpine`, `nginx` es el nombre de la imagen y `alpine` es la **etiqueta**, que permite seleccionar una versión o variante concreta. Aquí selecciona una variante basada en Alpine Linux. Los dos puntos separan el nombre de la etiqueta. `nginx:alpine` y `nginx:latest` son referencias distintas al mismo nombre de imagen.

:::single-choice{#docker-images-read-reference} En `busybox:1.36`, ¿qué parte es la etiqueta?

::option[`busybox`]{#docker-images-reference-name explanation="BusyBox es el nombre que aparece antes de los dos puntos."}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="La referencia completa incluye el nombre y la etiqueta de la imagen."}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="El texto después de los dos puntos es la etiqueta que selecciona la imagen."}
:::

## Elegir una etiqueta

Si omites la etiqueta de una referencia como `nginx`, Docker usa `latest`. Es un nombre establecido por convención. Quien publica la imagen decide a cuál apunta la etiqueta y puede cambiarla más adelante. Con `nginx:alpine` indicas qué variante quieres, aunque la imagen asociada con esa etiqueta también puede actualizarse.

:::single-choice{#docker-images-default-tag} Una persona usa `nginx` sin indicar una etiqueta y supone que Docker ha elegido la versión más reciente. ¿Qué ha seleccionado realmente la referencia?

::option[La imagen a la que apunta la etiqueta latest.]{#docker-images-default-latest .correct explanation="Al omitir la etiqueta se usa latest. Quien publica la imagen decide adónde apunta."}
::option[La imagen de Nginx publicada más recientemente.]{#docker-images-default-newest explanation="Docker usa la etiqueta llamada latest. No ordena las imágenes por fecha de publicación."}
::option[La imagen de Nginx más pequeña que haya disponible.]{#docker-images-default-smallest explanation="El tamaño no determina la etiqueta predeterminada. Indica por su nombre la variante que quieras."}
:::

## Descargar una imagen

Un **registro** almacena imágenes y las ofrece para su descarga. Para referencias como `nginx:alpine`, Docker usa Docker Hub de forma predeterminada. Para descargar una imagen al entorno de Docker al que estás conectado, usa `docker pull`. A esa descarga también se le llama hacer un **pull** de la imagen.

```bash
$ docker pull nginx:alpine
```

Si el comando termina correctamente, la imagen queda disponible en ese entorno. Iniciar un contenedor es otra operación. En los ejemplos de terminal, `$` indica el prompt.

:::single-choice{#docker-images-pull-result} La descarga de una imagen termina correctamente. ¿Qué ha hecho Docker?

::option[Ha iniciado un contenedor que responde a solicitudes web.]{#docker-images-pull-started explanation="El contenedor se inicia al ejecutarlo. La descarga solo deja disponible la imagen."}
::option[Ha dejado la imagen disponible en ese entorno.]{#docker-images-pull-available .correct explanation="Ya puedes usar la imagen descargada como punto de partida para un contenedor."}
::option[Ha subido una copia de la imagen al registro.]{#docker-images-pull-uploaded explanation="El comando pull transfiere la imagen desde el registro al almacenamiento local de Docker."}
:::

## Consultar las imágenes locales

Usa `docker image ls` para ver las imágenes que ya están disponibles. El ejemplo solo muestra las columnas con el nombre y la etiqueta. Docker llama `REPOSITORY` a la columna del nombre de la imagen.

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

La primera fila muestra `nginx:alpine`. Esta tabla indica qué imágenes están presentes. El estado de los contenedores creados a partir de ellas se consulta en otra lista.

![Terminal de LabEx con docker pull y las columnas REPOSITORY y TAG de docker image ls](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

En esta captura, la lista está filtrada para mostrar solo las dos referencias de la lección.

:::single-choice{#docker-images-local-list} ¿Qué referencia aparece como disponible en esta salida?

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="La fila de busybox muestra la etiqueta 1.36. En el ejemplo no aparece busybox con la etiqueta latest."}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="Combina busybox de la columna REPOSITORY con 1.36 de la columna TAG."}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="Toma el nombre y la etiqueta de una misma fila. Aquí 1.36 pertenece a la fila de busybox."}
:::

## Resumen

Ya puedes leer una referencia de imagen y comprobar si aparece en la lista local.

1. Identificar el nombre y la etiqueta en una referencia de imagen.
2. Explicar qué ocurre al omitir la etiqueta.
3. Usar `docker pull` para descargar una imagen desde un registro.
4. Leer las columnas de nombre y etiqueta de `docker image ls`.
