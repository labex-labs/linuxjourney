---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "es"
order_index: 6
title: "Dependencias entre servicios"
description: "Aprende a distinguir el orden de arranque de las dependencias de la disponibilidad para responder a peticiones."
meta_title: "Dependencias entre servicios - Docker Compose"
meta_description: "Aprende a distinguir el orden de arranque de las dependencias de la disponibilidad para responder a peticiones."
meta_keywords: "dependencias entre servicios, comprobación de estado, arranque, Docker Compose, DevOps, Linux Journey"
---

Un programa que necesita un servidor web puede hacer su primera petición demasiado pronto, aunque ambos se inicien en el orden correcto. Una **comprobación de estado** es una prueba breve que ejecuta Docker para comprobar si un servicio puede cumplir una función concreta, como responder a una petición HTTP.

## Elegir cómo comprobar si el servicio está listo

En este ejemplo independiente, la comprobación se ejecuta en el contenedor web y solicita la página local. Si tiene éxito, Docker puede comprobar que el servidor responde desde ese punto.

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

Guarda este ejemplo como `compose.health.yaml` en la misma carpeta de prácticas. La comprobación se ejecuta a intervalos y cada intento tiene un límite de tiempo. Se comprueba una respuesta local dentro del contenedor web.

:::single-choice{#compose-service-dependencies-check-location} ¿Dónde se ejecuta wget para esta comprobación de estado?

::option[En el contenedor web.]{#compose-service-dependencies-check-location-c .correct explanation="Se accede a la URL de bucle local desde el contenedor web."}
::option[En el navegador del anfitrión.]{#compose-service-dependencies-check-location-a explanation="Docker ejecuta el comando según lo indicado en la definición del servicio web."}
::option[En el contenedor de herramientas.]{#compose-service-dependencies-check-location-b explanation="La comprobación está definida en web."}
:::

## Esperar a que esté lista la dependencia

La condición `service_healthy` hace que Compose espere a que la comprobación de estado sea satisfactoria antes de arrancar el contenedor de herramientas que depende del servidor. Si solo se indica el orden de arranque, el contenedor dependiente puede iniciarse en cuanto se ejecute el servidor, incluso antes de que logre responder a una petición.

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

Comprueba que la fila de web muestra que el servicio está en buen estado y que el contenedor de herramientas está en ejecución.

:::single-choice{#compose-service-dependencies-ready-condition} El proceso web arrancó, pero la petición local sigue fallando. ¿Qué condición debe retrasar el inicio del contenedor de herramientas?

::option[Solo el orden de arranque.]{#compose-service-dependencies-ready-condition-b explanation="Aunque web arranque primero, puede tardar en responder."}
::option[El modo en segundo plano.]{#compose-service-dependencies-ready-condition-c explanation="Este modo determina cómo espera el terminal. Por sí solo no comprueba si el servicio está listo."}
::option[La condición service_healthy.]{#compose-service-dependencies-ready-condition-a .correct explanation="Esta condición hace que Compose espere el resultado de la comprobación."}
:::

![Estado de Compose con el servicio web en buen estado y el contenedor de herramientas en ejecución](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## Responder a un fallo posterior

Una condición de arranque de Compose determina cuándo se inicia un servicio dependiente. Un servicio que estaba en buen estado puede dejar de responder más tarde. El cliente debe poder gestionar una petición fallida y volver a conectarse cuando la dependencia se recupere. Consulta el estado del servicio y haz una petición directa para comprobar cómo se comporta ahora.

:::single-choice{#compose-service-dependencies-later-failure} Una petición falla una hora después de arrancar los dos servicios. ¿Qué te ayuda a entender el fallo?

::option[Solo el orden de arranque original.]{#compose-service-dependencies-later-failure-a explanation="Ese dato indica lo que pasó al inicio."}
::option[El resultado actual de la comprobación y una petición desde el servicio dependiente.]{#compose-service-dependencies-later-failure-b .correct explanation="Así puedes comprobar el estado actual del servicio y la ruta de conexión del cliente."}
::option[El número de imágenes en la caché de Docker.]{#compose-service-dependencies-later-failure-c explanation="Las imágenes disponibles apenas aportan información sobre la respuesta de un servicio en ejecución."}
:::

## Comprobar desde dos puntos distintos

Una comprobación de estado local satisfactoria indica a qué puede acceder el contenedor web desde dentro. El contenedor de herramientas sigue necesitando la red del proyecto y una dirección que le permita llegar al servicio. Comprueba por separado el estado y la respuesta a una petición desde el contenedor de herramientas.

:::single-choice{#compose-service-dependencies-final-application} La comprobación está en verde, pero falla una petición desde el contenedor de herramientas. ¿Qué comparación ayuda a localizar el problema?

::option[Consultar solo la hora de arranque original.]{#compose-service-dependencies-final-application-b explanation="Ese dato no indica qué rutas funcionan ahora."}
::option[Dar ambas peticiones por correctas porque el estado de web está en verde.]{#compose-service-dependencies-final-application-c explanation="La comprobación solo aporta información desde un punto de la red."}
::option[Comparar la misma petición desde dentro de web y desde el contenedor de herramientas hacia web.]{#compose-service-dependencies-final-application-a .correct explanation="Así comparas la disponibilidad dentro del servicio con la ruta que usa el contenedor dependiente."}
:::

## Resumen

Ya puedes usar una comprobación para determinar si una dependencia está lista.

1. Identifica qué observa realmente la comprobación de estado.
2. Usa una condición de disponibilidad si el orden de arranque no basta.
3. Comprueba el comportamiento actual si un servicio falla más tarde.
