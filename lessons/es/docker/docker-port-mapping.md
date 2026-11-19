---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "es"
order_index: 5
title: "Asignación de puertos"
description: "Aprende a publicar un puerto del contenedor y a encontrar la dirección que debe usar el navegador local."
meta_title: "Asignación de puertos - Docker"
meta_description: "Lee una asignación de puertos de Docker, distingue el puerto del anfitrión del puerto del contenedor y detecta una solicitud enviada al puerto equivocado."
meta_keywords: "asignación de puertos, puertos publicados, docker run -p, puerto del anfitrión, puerto del contenedor"
---

Un servidor web puede estar funcionando dentro de un contenedor y, aun así, tu navegador necesita una forma de llegar a él. Un **puerto** es un número que permite al equipo dirigir las solicitudes de red al servicio adecuado. Docker puede publicar un puerto del anfitrión y reenviar esas solicitudes a un puerto del contenedor.

## Leer una asignación de puertos

En este ejemplo, Nginx acepta solicitudes web en el puerto 80 dentro del contenedor. El contenedor `web` del ejemplo anterior se creó sin publicar ningún puerto. Dale otro nombre al nuevo contenedor y usa `-p` para indicar la asignación al crearlo.

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

Lee `8080:80` como una asignación del **puerto del anfitrión** 8080 al **puerto del contenedor** 80. El navegador se conecta al primero y el servidor recibe la solicitud en el segundo. La dirección `127.0.0.1` vincula la asignación a la dirección de bucle local del anfitrión, la que un equipo usa para comunicarse consigo mismo.

Usa un entorno de práctica privado. En las versiones de Docker Engine anteriores a la 28.0.0, otros equipos del mismo segmento de red local podrían acceder a puertos publicados en localhost. [Publicación de puertos en Docker](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} En `127.0.0.1:9090:80`, ¿a qué puerto debe conectarse un navegador que se ejecuta en el anfitrión de Docker?

::option[Al puerto 9090 del anfitrión.]{#docker-port-mapping-target-outer .correct explanation="La parte central selecciona el puerto del anfitrión al que se conecta el navegador."}
::option[Al puerto 80 del anfitrión.]{#docker-port-mapping-target-inner explanation="El puerto 80 es el destino dentro del contenedor."}
::option[Al puerto 9090 del contenedor.]{#docker-port-mapping-target-wrong-side explanation="En este ejemplo, el servidor recibe la solicitud en el puerto 80 del contenedor."}
:::

## Probar desde el anfitrión

Abre `http://127.0.0.1:8080` en un navegador del equipo en el que Docker publicó el puerto. Si Docker se ejecuta en un equipo remoto, al escribir `127.0.0.1` en tu portátil estarás accediendo al propio portátil. Si practicas en un laboratorio en el navegador, usa el método de acceso que proporciona ese entorno.

:::single-choice{#docker-port-mapping-local-browser} Docker publicó el puerto 8080 en un equipo de laboratorio distinto. ¿Adónde apunta `127.0.0.1` si escribes esa dirección en el navegador de tu portátil?

::option[Al equipo de laboratorio.]{#docker-port-mapping-local-lab explanation="Esa dirección apunta al equipo de laboratorio únicamente si la usas desde el propio equipo de laboratorio."}
::option[Al contenedor web de Docker.]{#docker-port-mapping-local-container explanation="El navegador usa la dirección de su propio equipo. Hace falta una asignación de puertos para reenviar la solicitud a un contenedor."}
::option[A tu portátil.]{#docker-port-mapping-local-laptop .correct explanation="La dirección de bucle local apunta al equipo en el que se ejecuta el navegador."}
:::

## Comprobar qué puerto publicó Docker

La columna `PORTS` de `docker ps` puede mostrar la asignación. La flecha va de la dirección y el puerto del anfitrión al puerto del contenedor. El sufijo `/tcp` indica qué protocolo de red usa esa asignación.

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

Una fila puede mostrar solo `80/tcp`. Si no aparecen la dirección del anfitrión ni la flecha, esa entrada no muestra ningún puerto publicado en el anfitrión.

![Terminal de LabEx con el puerto 8080 del anfitrión redirigido al puerto 80 del contenedor y una respuesta HTTP 200](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

En la captura, la lista está filtrada para mostrar solo `published-web`. La solicitud con `curl` se ejecuta en el anfitrión de Docker y confirma que la dirección publicada responde correctamente.

:::single-choice{#docker-port-mapping-read-listing} Una fila muestra `80/tcp` sin flecha. ¿Qué indica esa entrada?

::option[Docker publicó el puerto 80 en el anfitrión.]{#docker-port-mapping-listing-host explanation="Una asignación publicada muestra un puerto del anfitrión y apunta al puerto del contenedor."}
::option[La entrada muestra un puerto del contenedor sin un puerto publicado en el anfitrión.]{#docker-port-mapping-listing-container .correct explanation="La entrada indica el puerto 80 del contenedor. No tiene dirección del anfitrión ni flecha de reenvío."}
::option[Docker publicó el puerto 8080 en el anfitrión.]{#docker-port-mapping-listing-default explanation="La entrada no contiene ningún puerto del anfitrión. Docker no deduce de ella el puerto 8080."}
:::

## Elegir la dirección que vas a probar

Si la página no se abre, compara la dirección que escribiste con el lado izquierdo de la asignación. El estado `Up` y la flecha indican qué está ejecutando Docker y adónde reenvía las solicitudes. Una solicitud desde el navegador permite comprobar si el servidor devuelve realmente la página.

:::single-choice{#docker-port-mapping-correct-misdirected} En el anfitrión de Docker, pruebas el puerto 8080 y la página no se abre. La fila muestra `127.0.0.1:8081->80/tcp`. ¿Qué deberías probar a continuación?

::option[Abrir `http://127.0.0.1:80`.]{#docker-port-mapping-misdirected-80 explanation="El puerto 80 está en el lado del contenedor."}
::option[Abrir `http://127.0.0.1:8081`.]{#docker-port-mapping-misdirected-8081 .correct explanation="Usa el puerto publicado en el anfitrión que aparece a la izquierda de la flecha."}
::option[Volver a probar `http://127.0.0.1:8080`.]{#docker-port-mapping-misdirected-8080 explanation="El puerto del anfitrión que aparece en la lista es 8081. Si vuelves a usar 8080, no comprobarás esa asignación."}
:::

## Resumen

Ya puedes leer una asignación de puertos y usarla para elegir la dirección del navegador.

1. Distinguir el puerto del anfitrión del puerto del contenedor.
2. Explicar adónde apunta `127.0.0.1`.
3. Reconocer una asignación publicada en la lista de contenedores.
4. Usar el puerto publicado en el anfitrión para probar el servicio.
