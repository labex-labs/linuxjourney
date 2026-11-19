---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "es"
order_index: 3
title: "docker run"
description: "Aprende cómo Docker crea e inicia contenedores a partir de imágenes con docker run."
meta_title: "docker run - Docker"
meta_description: "Lee un comando docker run, elige un nombre para el contenedor y distingue una tarea breve en primer plano de un servidor que corre en segundo plano."
meta_keywords: "docker run, ejecutar un contenedor, nombres de contenedores, primer plano, segundo plano"
---

Tienes la imagen de un servidor web. Para poner en marcha el servidor, usa `docker run` para crear e iniciar un contenedor a partir de esa imagen. Empieza con un comando que termine rápido para ver cuándo recuperas el control de la terminal.

## Ejecutar una tarea breve

BusyBox es una imagen pequeña con comandos básicos de Linux. En el ejemplo, `echo` imprime un mensaje. Escribe la referencia de la imagen antes del comando que quieres ejecutar dentro del contenedor. Docker suele descargar la imagen si no está disponible. El símbolo `$` marca el prompt de la terminal. Si Docker necesita descargar la imagen primero, puede mostrar mensajes de descarga antes de la línea del ejemplo.

```text
$ docker run busybox:1.36 echo Hello
Hello
```

Verás el resultado en la terminal. Cuando `echo` termina, el contenedor se detiene y vuelve a aparecer el prompt.

:::single-choice{#docker-run-command-short-task} ¿Qué se ejecuta dentro del contenedor en este ejemplo?

::option[`busybox:1.36` como un comando de shell.]{#docker-run-command-short-image explanation="BusyBox es la imagen que aporta las herramientas. El comando va después de la referencia."}
::option[`echo Hello` con las herramientas de la imagen.]{#docker-run-command-short-echo .correct explanation="Después de la referencia de la imagen se indica el comando echo y el texto que debe imprimir."}
::option[`docker run` como un segundo comando de Docker.]{#docker-run-command-short-docker explanation="Ejecutas docker run en tu terminal. Este comando inicia la tarea dentro del contenedor."}
:::

## Dar un nombre al contenedor

Escribe `--name` antes de la referencia de la imagen para darle al contenedor un nombre que puedas reconocer más adelante. En este comando, el contenedor de la tarea breve se llama `report`.

```bash
$ docker run --name report busybox:1.36 echo Ready
```

Un contenedor conserva su nombre aunque se detenga. En el mismo entorno de Docker, elige un nombre libre antes de crear otro contenedor.

:::single-choice{#docker-run-command-name-choice} Report ya terminó, pero el contenedor sigue existiendo. ¿Qué puedes cambiar para crear otro contenedor con la misma imagen?

::option[Usar otro nombre de contenedor y mantener la referencia de la imagen.]{#docker-run-command-name-new .correct explanation="Con un nombre libre, Docker puede crear otro contenedor a partir de la misma imagen."}
::option[Cambiar la etiqueta de la imagen y mantener el nombre del contenedor.]{#docker-run-command-name-change-tag explanation="El contenedor original conserva el nombre aunque elijas otra imagen."}
::option[Cambiar el mensaje y mantener el nombre del contenedor.]{#docker-run-command-name-change-message explanation="El mensaje es la entrada de echo. Cambiarlo no deja libre el nombre report."}
:::

## Iniciar un servidor en segundo plano

Las imágenes pueden incluir un comando predeterminado. La imagen `nginx:alpine` arranca un servidor web cuando no indicas ningún comando después de la referencia. Añade `-d` para ejecutar el contenedor **en segundo plano** y recuperar el prompt mientras el servidor sigue funcionando.

```bash
$ docker run -d --name web nginx:alpine
```

Docker imprime un ID de contenedor, un identificador largo para el contenedor que acaba de iniciar. En la siguiente lección comprobarás si el servidor sigue en marcha.

![Terminal de LabEx con Hello y Ready de tareas breves de Docker y el ID de un servidor iniciado en segundo plano](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

Las tareas breves imprimen sus mensajes en la terminal. El servidor en segundo plano devuelve un ID de contenedor.

:::single-choice{#docker-run-command-detach-meaning} Docker imprime un ID y vuelve a aparecer el prompt. ¿Qué puedes hacer en este modo?

::option[Usar la terminal solo después de que el servidor se detenga.]{#docker-run-command-detach-wait explanation="El modo en segundo plano te devuelve el prompt mientras el servidor sigue funcionando."}
::option[Omitir el inicio del servidor y dejar preparada la imagen.]{#docker-run-command-detach-skip explanation="Docker también inicia el contenedor en segundo plano."}
::option[Usar la terminal mientras el servidor está en marcha.]{#docker-run-command-detach-continue .correct explanation="Después de iniciar el contenedor, Docker te devuelve el control de la terminal."}
:::

## Reconocer un contenedor nuevo

Cada vez que `docker run` se ejecuta correctamente, crea un contenedor. Si vuelves a usar la imagen del servidor con un nombre libre, Docker crea un segundo contenedor. El primero conserva su nombre y su estado.

:::single-choice{#docker-run-command-second-instance} Web está en marcha. ¿Qué hace `docker run -d --name demo nginx:alpine` si demo está libre?

::option[Cambia el nombre del contenedor web a demo.]{#docker-run-command-second-rename explanation="Docker run crea un contenedor. El contenedor original web conserva su nombre."}
::option[Añade demo como otra etiqueta de la imagen.]{#docker-run-command-second-tag explanation="La opción asigna un nombre al contenedor. La referencia de la imagen sigue siendo nginx:alpine."}
::option[Inicia otro contenedor llamado demo.]{#docker-run-command-second-new .correct explanation="Docker crea un contenedor nuevo a partir de esa imagen y le asigna el nombre demo."}
:::

Para practicar cómo iniciar un contenedor y observar su salida, prueba [Tu primer laboratorio de Docker](https://labex.io/labs/docker-your-first-docker-lab-92719).

## Resumen

Ya puedes leer un comando docker run y prever qué creará Docker.

1. Identificar la imagen y el comando opcional que se ejecuta en el contenedor.
2. Usar `--name` para reconocer un contenedor más adelante.
3. Describir qué ocurre cuando termina una tarea breve.
4. Usar `-d` para recuperar el prompt mientras un servidor sigue en marcha.
