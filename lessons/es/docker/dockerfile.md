---
lesson_id: "dockerfile"
course_id: "docker"
lang: "es"
order_index: 7
title: "Dockerfile"
description: "Aprende cómo un Dockerfile combina una página y una imagen base para crear una imagen de servidor web reutilizable."
meta_title: "Dockerfile - Docker"
meta_description: "Lee FROM, COPY y CMD en un Dockerfile pequeño y distingue la construcción de una imagen de la ejecución de un contenedor."
meta_keywords: "Dockerfile, construcción de imágenes, FROM, COPY, CMD, contexto de construcción"
---

Ya has iniciado un contenedor con una imagen de servidor web existente. Para servir tu propia página, puedes construir una imagen que ya la contenga. Un **Dockerfile** es un archivo de texto con las instrucciones para construir esa imagen.

## Partir de una imagen base

Una **imagen base** proporciona los programas y archivos de partida. El siguiente Dockerfile parte de la imagen de Nginx, añade una página e indica qué comando debe usar el contenedor por defecto. Guarda el Dockerfile y un archivo llamado `index.html` en la misma carpeta de práctica. Para la página basta con una línea como `<h1>Hello from Docker</h1>`.

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine` parte de la imagen indicada, que ya incluye el programa Nginx. Docker la usa durante la construcción de la nueva imagen.

:::single-choice{#dockerfile-base-image-purpose} ¿Qué línea proporciona Nginx antes de añadir tu página?

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY añade la página. Usa el servidor que proporciona la imagen base."}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM selecciona la imagen de partida, que ya trae el servidor."}
::option[La línea que empieza por `CMD`.]{#dockerfile-base-image-cmd explanation="CMD fija el comando de inicio predeterminado. El programa del servidor viene de la imagen base."}
:::

## Añadir un archivo

`COPY` lee `index.html` de los archivos que proporcionas para la construcción. Escribe la página en la ruta indicada a la derecha, que es donde esta versión de la imagen de Nginx busca su página predeterminada. Si después editas la página local, vuelve a construir la imagen para incorporar el cambio.

:::single-choice{#dockerfile-copy-after-edit} Después de construir la imagen, has cambiado el encabezado de index.html en tu equipo. ¿Cómo incorporas ese cambio a una imagen nueva?

::option[Iniciar otro contenedor con la imagen existente.]{#dockerfile-copy-edit-run explanation="Ese contenedor arranca con la página que ya estaba empaquetada en la imagen."}
::option[Cambiar solo el nombre del contenedor existente.]{#dockerfile-copy-edit-rename explanation="El nombre del contenedor no cambia los archivos de la imagen."}
::option[Volver a construir la imagen con la página actualizada.]{#dockerfile-copy-edit-rebuild .correct explanation="Al construirla, COPY lee el archivo local actualizado y lo incluye en la imagen nueva."}
:::

## Definir el comando de inicio

`CMD` fija el comando predeterminado para los contenedores nuevos. En el ejemplo, indica a Nginx que siga ejecutándose en primer plano dentro del contenedor. Docker puede ejecutar el contenedor en segundo plano respecto de tu terminal si usas `docker run -d`.

:::single-choice{#dockerfile-cmd-start-time} ¿Cuándo se ejecuta el comando de CMD en el ejemplo?

::option[Cuando un contenedor se inicia con su comando predeterminado.]{#dockerfile-cmd-when-start .correct explanation="Docker usa el comando predeterminado de la imagen al iniciar el contenedor."}
::option[Mientras Docker copia la página en la imagen.]{#dockerfile-cmd-when-copy explanation="COPY añade la página durante la construcción. En ese momento no se inicia el servidor."}
::option[Cuando Docker termina de escribir la imagen.]{#dockerfile-cmd-when-build explanation="La construcción registra el comando de inicio para usarlo después."}
:::

## Construir la imagen e iniciar el contenedor

Ejecuta la construcción desde la carpeta que contiene los dos archivos. La opción `-t` asigna la referencia `journey-web:1` a la imagen. El punto final indica a Docker que use el directorio actual como origen de los archivos de construcción.

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

El segundo comando inicia un contenedor. Si el puerto 8082 está disponible, puedes abrir `http://127.0.0.1:8082` en un navegador del anfitrión de Docker para ver tu página.

:::single-choice{#dockerfile-build-versus-run} La construcción se completó y todavía no ejecutaste el segundo comando. ¿Qué está listo?

::option[La imagen existe y puedes usarla para crear un contenedor.]{#dockerfile-build-ready-image .correct explanation="El primer comando produjo la imagen. El siguiente la usa para iniciar un contenedor."}
::option[El contenedor con ese nombre ya sirve tu página.]{#dockerfile-build-ready-container explanation="El servidor se inicia cuando arrancas el contenedor a partir de la imagen."}
::option[Docker ya publicó el puerto de acceso para la imagen.]{#dockerfile-build-ready-port explanation="La asignación de puertos es una opción de docker run. La construcción no configura esa conexión."}
:::

![Terminal de LabEx con la construcción de la imagen, el inicio del contenedor y la respuesta HTML de la página personalizada](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

La última solicitud recupera la página que se incluyó durante la construcción. En tu entorno pueden variar los mensajes de progreso y los ID de las imágenes.

## Resumen

Ya puedes leer un Dockerfile pequeño y seguir el proceso desde una página local hasta un servidor en ejecución.

1. Identificar la imagen base que indica `FROM`.
2. Explicar de dónde lee `COPY` un archivo y dónde lo escribe.
3. Reconocer `CMD` como el comando de inicio predeterminado del contenedor.
4. Construir una imagen e iniciar un contenedor a partir de ella.
