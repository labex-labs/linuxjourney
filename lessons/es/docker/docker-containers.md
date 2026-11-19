---
lesson_id: "docker-containers"
course_id: "docker"
lang: "es"
order_index: 1
title: "Contenedores"
description: "Descubre qué se ejecuta dentro de un contenedor de Docker y cómo se relaciona con el equipo que ejecuta Docker."
meta_title: "Contenedores - Docker"
meta_description: "Entiende qué es un contenedor a partir de un pequeño servidor web y descubre qué cambia cuando se inicia o se detiene su programa principal."
meta_keywords: "contenedores de Docker, contenedores básicos, equipo anfitrión, procesos, servidor web"
---

Un navegador abre una página que le envía un servidor web que funciona en Docker. ¿Dónde se ejecuta ese servidor? ¿Qué pasa con la página si se detiene? Empecemos por el programa que responde al navegador.

## Un programa dentro de un contenedor

Un **servidor web** es un programa que responde a solicitudes de páginas. Imagina que el navegador y un pequeño servidor web llamado `web` están en el mismo equipo. Docker ejecuta el servidor en un **contenedor**, que le da al programa su propia vista de los archivos y de otros recursos. El curso incluye ejemplos ya preparados, así que puedes seguirlo sin instalar Docker.

:::single-choice{#docker-containers-page-request} Cuando el navegador solicita una página, ¿qué le devuelve el contenido?

::option[El servidor web que se ejecuta en el contenedor.]{#docker-containers-page-server .correct explanation="El programa del servidor recibe la solicitud y devuelve la página."}
::option[Los archivos que indican cómo iniciar el contenedor.]{#docker-containers-page-files explanation="Esos archivos definen la configuración. La solicitud la atiende un programa en ejecución."}
::option[La lista de contenedores de Docker en el equipo.]{#docker-containers-page-list explanation="La lista indica qué está ejecutando Docker. No sirve páginas web."}
:::

## El contenedor y su anfitrión

El equipo que ejecuta los contenedores se llama **anfitrión**. Cuando Docker ejecuta contenedores Linux en un sistema Linux, los programas se ejecutan como procesos de ese equipo. Un **proceso** es un programa en ejecución. Aunque varios contenedores compartan el anfitrión, cada uno puede ver solo un conjunto limitado de recursos. En Docker Desktop, los contenedores Linux se ejecutan en una máquina virtual Linux que gestiona Docker.

:::single-choice{#docker-containers-shared-host} Dos contenedores Linux se ejecutan en el mismo anfitrión Linux. ¿Qué puedes deducir?

::option[Sus programas tienen que ver los mismos archivos.]{#docker-containers-host-shared-files explanation="Cada contenedor puede tener su propia vista de los archivos del anfitrión."}
::option[Sus programas pueden ejecutarse como procesos independientes en ese equipo.]{#docker-containers-host-separate-processes .correct explanation="En un mismo anfitrión pueden ejecutarse programas en contenedores distintos."}
::option[Cada contenedor tiene que iniciar otra máquina Linux.]{#docker-containers-host-separate-machines explanation="Los contenedores Linux pueden ejecutarse como procesos en un mismo anfitrión, sin una máquina distinta para cada uno."}
:::

## Partir de una imagen

Docker crea un contenedor a partir de una **imagen**, un paquete que incluye el programa y los archivos que necesita. Puedes usar la misma imagen de servidor web para crear `web` y `demo`. Al arrancar, cada contenedor ejecuta el mismo programa del servidor en un proceso propio. Puedes detener cualquiera de los dos por separado.

:::single-choice{#docker-containers-two-from-image} Detienes demo mientras web sigue en ejecución. ¿Qué le ocurre a web?

::option[Se pone en pausa hasta que vuelvas a iniciar demo.]{#docker-containers-two-paused explanation="Cada contenedor ejecuta su propio programa. En este ejemplo, detener demo no interrumpe web."}
::option[Hay que volver a crearlo a partir de la imagen.]{#docker-containers-two-recreate explanation="El contenedor web se creó por separado y puede seguir en ejecución."}
::option[Sigue funcionando en su propio contenedor.]{#docker-containers-two-independent .correct explanation="Los dos contenedores parten de la misma imagen, pero funcionan de forma independiente."}
:::

## Comprobar el servicio antes y después de detenerlo

Supón que tu navegador ya puede enviar solicitudes a `web`. Antes de detenerlo, el navegador recibe la página. Después, si haces una solicitud nueva, ese servidor ya no devuelve la página. La imagen sigue disponible para crear otro contenedor. Para servir la página, el programa tiene que estar en marcha y el navegador debe poder conectarse. En otra lección verás cómo conectar el navegador con un contenedor.

:::single-choice{#docker-containers-stopped-server} La imagen sigue disponible, pero web está detenido. ¿Qué necesita web para volver a responder?

::option[Su programa servidor tiene que volver a ejecutarse.]{#docker-containers-stopped-program .correct explanation="La imagen proporciona los archivos. Para atender nuevas solicitudes, hace falta un servidor en ejecución."}
::option[La imagen necesita otro nombre para poder servir páginas.]{#docker-containers-stopped-rename explanation="Cambiar el nombre de la imagen no vuelve a poner en marcha el servidor."}
::option[El navegador necesita otra copia de la imagen del servidor.]{#docker-containers-stopped-browser-image explanation="El navegador envía solicitudes. El programa servidor se ejecuta dentro del contenedor."}
:::

![Terminal de LabEx con una respuesta HTTP 200 antes de detener el contenedor y un fallo de conexión después](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

En este ejemplo de LabEx, un contenedor llamado `page-demo` sirve la página. La primera solicitud con `curl` recibe HTTP 200. Una vez detenido el contenedor, una nueva solicitud falla. Curl muestra `000` porque no ha recibido ninguna respuesta HTTP.

## Resumen

Ya puedes explicar cómo un contenedor ejecuta un programa en un equipo anfitrión.

1. Identificar qué programa responde a una solicitud del navegador.
2. Explicar cómo varios contenedores pueden compartir un mismo equipo.
3. Describir cómo una imagen puede servir para crear varios contenedores.
4. Hacer una nueva solicitud para comprobar si un servidor que antes era accesible sigue respondiendo.
