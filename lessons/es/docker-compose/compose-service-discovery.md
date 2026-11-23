---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "es"
order_index: 3
title: "Descubrimiento de servicios"
description: "Aprende cómo se conectan los servicios de Compose por nombre y cómo se accede desde el anfitrión a través de un puerto publicado."
meta_title: "Descubrimiento de servicios - Docker Compose"
meta_description: "Aprende cómo se conectan los servicios de Compose por nombre y cómo se accede desde el anfitrión a través de un puerto publicado."
meta_keywords: "descubrimiento de servicios, red de Compose, Docker Compose, DevOps, Linux Journey"
---

Un navegador del equipo anfitrión de Docker llega al servicio web por su dirección publicada. Otro contenedor del mismo proyecto sigue una ruta diferente. Compose suele conectar los servicios del proyecto a una misma red, donde pueden encontrarse por el nombre del servicio.

## Solicitar la página desde el contenedor de herramientas

Vuelve a la carpeta de prácticas que contiene `compose.yaml`. Si el contenedor de herramientas se detuvo desde la lección anterior, vuelve a iniciarlo con `docker compose start toolbox`. Con los dos servicios en marcha, usa `docker compose exec` para ejecutar un comando en el contenedor de herramientas que ya existe. El comando `wget` de BusyBox solicita una página. La opción `-q` oculta los mensajes de progreso y `-O -` escribe la página en el terminal.

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

La opción `-T` impide que se asigne un terminal interactivo. La URL indica el nombre del servicio web y su puerto dentro del contenedor. Si la petición funciona, verás el HTML de la página de Nginx.

:::single-choice{#compose-service-discovery-sibling-url} ¿Qué dirección debe usar otro servicio de la misma red de Compose para llegar al contenedor web?

::option[`http://web:80/`]{#compose-service-discovery-sibling-url-c .correct explanation="En la red compartida, web se resuelve al servicio deseado. El puerto 80 llega al programa que está escuchando."}
::option[`http://127.0.0.1:8080/`]{#compose-service-discovery-sibling-url-a explanation="La dirección de bucle local apunta al entorno de red del propio servicio que hace la petición."}
::option[`http://web:8080/`]{#compose-service-discovery-sibling-url-b explanation="En este ejemplo, el programa web escucha en el puerto 80 dentro de la red."}
:::

![HTML devuelto en el contenedor de herramientas después de solicitar el servicio web por nombre](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## Elegir una dirección desde el anfitrión

En el equipo anfitrión de Docker, abre `http://127.0.0.1:8080/` si conservaste la asignación original. Si cambiaste el puerto del anfitrión en la lección anterior, usa ese puerto en la dirección del navegador. El contenedor de herramientas sigue usando `http://web:80/` porque se conecta dentro de la red de Compose, donde está disponible el nombre de servicio `web`.

:::single-choice{#compose-service-discovery-host-url} Supón que cambias el puerto del anfitrión a 8081. ¿Qué dirección del ejemplo debes cambiar también?

::option[La URL que usa el contenedor de herramientas, con web y el puerto 80.]{#compose-service-discovery-host-url-b explanation="Esta conexión sigue llegando directamente al puerto en el que escucha el contenedor web."}
::option[Las dos direcciones del ejemplo.]{#compose-service-discovery-host-url-c explanation="Solo ha cambiado el puerto del lado del anfitrión."}
::option[La dirección que usa el navegador del anfitrión.]{#compose-service-discovery-host-url-a .correct explanation="El navegador se conecta por el nuevo puerto publicado en el anfitrión."}
:::

## Mantener un nombre de servicio estable

Al reemplazar un contenedor, su dirección de red puede cambiar. El nombre del servicio de Compose permanece igual. Un cliente puede volver a resolver el nombre y conectarse de nuevo. Las conexiones abiertas con el contenedor anterior pueden interrumpirse.

:::single-choice{#compose-service-discovery-replacement} El contenedor web volvió a crearse y ahora tiene otra dirección. ¿Qué puede usar el contenedor de herramientas en su próxima petición?

::option[La dirección antigua copiada del contenedor.]{#compose-service-discovery-replacement-a explanation="Un contenedor nuevo puede recibir otra dirección de red."}
::option[El mismo nombre de servicio web y puerto del contenedor.]{#compose-service-discovery-replacement-b .correct explanation="El nombre puede resolverse al contenedor actual dentro de la red del proyecto."}
::option[El nombre del propio contenedor de herramientas.]{#compose-service-discovery-replacement-c explanation="Ese otro nombre identifica el servicio que realiza la petición."}
:::

## Resumen

Ya puedes elegir una dirección según el lugar desde el que sale la petición.

1. Dentro de la red del proyecto, usa el nombre del servicio y el puerto del contenedor.
2. Para el navegador del anfitrión, usa una dirección publicada.
3. Vuelve a resolver el nombre del servicio cuando se reemplace un contenedor.
