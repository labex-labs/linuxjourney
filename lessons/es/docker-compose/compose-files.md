---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "es"
order_index: 1
title: "Archivos de Compose"
description: "Aprende a localizar los servicios, las imágenes, los comandos y los puertos en un archivo de Compose."
meta_title: "Archivos de Compose - Docker Compose"
meta_description: "Aprende a localizar los servicios, las imágenes, los comandos y los puertos en un archivo de Compose."
meta_keywords: "archivos de Compose, servicios, Docker Compose, DevOps, Linux Journey"
---

Puedes arrancar un servidor web y un programa auxiliar con comandos separados. Si vas a repetirlo, un **archivo de Compose** reúne los ajustes necesarios para volver a arrancar los mismos servicios. En este curso usarás Docker con el complemento de Compose, que proporciona el comando `docker compose`.

## Definir dos servicios

Crea una carpeta de prácticas llamada `journey-compose` y guarda allí el ejemplo como `compose.yaml`. Un **servicio** describe cómo debe ejecutar Compose un contenedor. Este archivo define un servidor web y un contenedor de herramientas que se mantiene en ejecución para las comprobaciones posteriores.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

Usa espacios para la sangría. Las claves que aparecen bajo `web` con más sangría pertenecen a ese servicio. El guion bajo `ports` marca el inicio de un elemento de la lista. Los corchetes en `command` también forman una lista, en este caso con el nombre del programa y su argumento.

:::single-choice{#compose-files-service-images} ¿Qué servicio usa la imagen de BusyBox?

::option[El servicio web.]{#compose-files-service-images-a explanation="En la línea de imagen de web aparece nginx."}
::option[El servicio toolbox.]{#compose-files-service-images-c .correct explanation="En el campo image de toolbox aparece busybox:1.36."}
::option[Los dos servicios.]{#compose-files-service-images-b explanation="Cada servicio tiene su propio ajuste de imagen."}
:::

## Leer la configuración del servicio web

El servicio web publica el puerto 80 del contenedor en el puerto 8080 del anfitrión. Una vez que el servicio se inicie, una petición a `http://127.0.0.1:8080` desde el equipo donde se ejecuta Docker puede llegar a Nginx. El contenedor de herramientas no publica ningún puerto. El comando `sleep` lo mantiene activo durante 3600 segundos para la práctica.

:::single-choice{#compose-files-mapping-owner} ¿Qué parte del archivo determina cómo llega a Nginx un navegador del equipo anfitrión de Docker?

::option[El ajuste ports dentro de web.]{#compose-files-mapping-owner-a .correct explanation="Ese ajuste asigna la dirección y el puerto del anfitrión al contenedor web."}
::option[La etiqueta de imagen dentro de toolbox.]{#compose-files-mapping-owner-b explanation="Esa etiqueta selecciona la imagen del contenedor de herramientas."}
::option[El argumento de sleep dentro de toolbox.]{#compose-files-mapping-owner-c explanation="Este argumento indica cuánto tiempo se ejecuta ese programa."}
:::

## Comprobar cómo Compose interpreta el archivo

Ejecuta el comando desde la carpeta que contiene el archivo. Escribe lo que aparece después del símbolo `$` del intérprete. Compose lee `compose.yaml` y muestra la configuración que ha interpretado. Busca las entradas `web` y `toolbox`. Algunos ajustes abreviados pueden aparecer en forma más detallada.

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} El comando muestra dos servicios sin errores. ¿Qué has comprobado?

::option[Los dos contenedores han arrancado.]{#compose-files-config-scope-a explanation="El comando lee y muestra la configuración."}
::option[El navegador ha recibido una respuesta correcta.]{#compose-files-config-scope-c explanation="Puedes probar una petición después de arrancar el servidor."}
::option[Compose puede leer las dos definiciones de servicio.]{#compose-files-config-scope-b .correct explanation="Puedes revisar la configuración interpretada antes de arrancar los servicios."}
:::

## Resumen

Ya puedes reconocer las partes de un archivo de Compose sencillo.

1. Localiza los nombres y las imágenes en services.
2. Relaciona los ajustes de cada servicio con el contenedor que describen.
3. Revisa la configuración interpretada con docker compose config.
