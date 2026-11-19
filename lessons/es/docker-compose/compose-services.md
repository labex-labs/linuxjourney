---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "es"
order_index: 2
title: "Servicios de Compose"
description: "Aprende a iniciar servicios de Compose y a comprobar el estado de sus contenedores."
meta_title: "Servicios de Compose - Docker Compose"
meta_description: "Aprende a iniciar servicios de Compose y a comprobar el estado de sus contenedores."
meta_keywords: "servicios de Compose, estado de contenedores, Docker Compose, DevOps, Linux Journey"
---

Usa el archivo `compose.yaml` de la lección anterior, con `web` y `toolbox`. Los dos servicios pertenecen a un mismo **proyecto** de Compose, es decir, al conjunto de recursos que se administran juntos con esta configuración. Ejecuta los comandos desde la carpeta de prácticas.

## Iniciar el proyecto

Si el puerto 8080 está ocupado, elige un puerto libre del anfitrión en `compose.yaml`. Por ejemplo, el contenedor `published-web` del curso de Docker usa el puerto 8080 mientras se ejecuta. Puedes dejarlo en marcha y usar `127.0.0.1:8081:80` para Compose si el puerto 8081 está libre. Mantén el puerto 80 del lado del contenedor y usa el puerto que hayas elegido al hacer peticiones posteriores desde el navegador.

Usa `docker compose up -d` para iniciar los servicios en segundo plano. Compose crea los recursos necesarios del proyecto y usa los ajustes de cada servicio para crear o actualizar los contenedores.

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} Ejecutas up -d desde esta carpeta de prácticas. ¿Qué ajustes determinan lo que se inicia?

::option[Todas las imágenes disponibles en el anfitrión de Docker.]{#compose-services-project-start-a explanation="El anfitrión puede tener imágenes de otros proyectos."}
::option[Todos los contenedores que estén detenidos.]{#compose-services-project-start-c explanation="Compose trabaja con el proyecto que le pediste iniciar."}
::option[Los servicios del archivo de Compose seleccionado.]{#compose-services-project-start-b .correct explanation="En este ejemplo, Compose usa las definiciones de web y toolbox."}
:::

## Consultar la lista de servicios

Usa `docker compose ps` para revisar este proyecto. La columna de servicios muestra los nombres del archivo YAML. Docker también asigna un nombre a cada contenedor, que puede incluir el nombre del proyecto.

```bash
$ docker compose ps
```

Busca `web` y `toolbox` y revisa su estado. Un contenedor en ejecución indica que el programa está activo en el momento de la comprobación. Para verificar la respuesta web, haz una petición aparte desde el navegador.

:::single-choice{#compose-services-compose-list} Compose indica que web está en ejecución. ¿Qué comprobación directa confirma que devuelve la página esperada?

::option[Contar los servicios que muestra config.]{#compose-services-compose-list-b explanation="El número de servicios no aporta información sobre la respuesta web."}
::option[Solicitar la dirección web publicada.]{#compose-services-compose-list-a .correct explanation="La petición comprueba si el servidor entrega la página."}
::option[Consultar el nombre de otro contenedor.]{#compose-services-compose-list-c explanation="El nombre identifica un contenedor concreto y no comprueba su servicio."}
:::

![Estado de Compose con los servicios web y toolbox en ejecución y el puerto 8080 del anfitrión](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

La captura usa el puerto original del anfitrión, el 8080. Si elegiste otro, busca ese número en el lado del anfitrión de la asignación.

## Comprobar un servicio detenido

El contenedor de herramientas es temporal. Si completa la espera o lo detienes, añade `-a` para que la lista de Compose incluya los contenedores detenidos. El comando de ejemplo detiene el contenedor de herramientas de este proyecto de prácticas y deja en marcha el servicio web. Vuelve a iniciar el contenedor de herramientas cuando quieras continuar.

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} ¿Dónde debes buscar toolbox después de detenerlo?

::option[En la salida de docker compose ps -a para este proyecto.]{#compose-services-stopped-service-c .correct explanation="La opción incluye los contenedores detenidos del proyecto."}
::option[Solo en la lista de imágenes.]{#compose-services-stopped-service-a explanation="Al detener el programa, el contenedor sigue disponible para que lo revises."}
::option[En la lista de contenedores de otro proyecto.]{#compose-services-stopped-service-b explanation="Toolbox pertenece a este proyecto."}
:::

Para practicar más con contenedores y Compose, consulta [las prácticas con comandos de Docker](https://labex.io/courses/docker-command-labs).

## Resumen

Ya puedes usar un archivo de Compose para iniciar y revisar un grupo de servicios.

1. Inicia los servicios del proyecto seleccionado.
2. Localiza el nombre del servicio y consulta su estado actual.
3. Incluye los servicios detenidos cuando revises un proyecto.
