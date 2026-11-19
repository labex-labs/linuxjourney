---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "es"
order_index: 1
title: "Peticiones y respuestas HTTP"
description: "Aprende a interpretar el método, la ruta, el estado y el tipo de contenido de un intercambio HTTP."
meta_title: "Peticiones y respuestas HTTP - Seguridad web"
meta_description: "Aprende a interpretar el método, la ruta, el estado y el tipo de contenido de un intercambio HTTP."
meta_keywords: "peticiones y respuestas HTTP, seguridad web, ciberseguridad, Linux Journey"
---

Un navegador u otro cliente pide algo a un servidor web mediante una **petición HTTP**. El servidor devuelve una **respuesta HTTP**. Al leer los dos mensajes, puedes saber qué pidió el cliente y qué devolvió el servidor.

## Leer la petición

Esta es una petición breve de HTTP/1.1. `GET` es el método e indica la acción que pide el cliente. `/health` es la ruta. La cabecera `Host` identifica el sitio web al que se dirige el cliente.

```http
GET /health HTTP/1.1
Host: site.example
```

Una **cabecera** es un valor con nombre que aporta información sobre el mensaje. El método y la ruta aparecen en la primera línea de la petición.

:::single-choice{#web-http-requests-responses-request-path} ¿Qué le pide el cliente al servidor?

::option[Un archivo llamado HTTP/1.1.]{#web-http-requests-responses-request-path-b explanation="Ese campo indica la versión del protocolo."}
::option[El recurso en /health.]{#web-http-requests-responses-request-path-a .correct explanation="La ruta aparece después de GET en la primera línea."}
::option[Un recurso en /site.example.]{#web-http-requests-responses-request-path-c explanation="La cabecera Host identifica el sitio web. La ruta aparece en la primera línea."}
:::

## Leer una respuesta

En un directorio de prácticas vacío, crea una página e inicia un servidor HTTP de Python en la dirección de bucle local. La redirección escribe la página. Deja el servidor en marcha en ese terminal hasta que termine la petición y luego usa Ctrl+C para detenerlo.

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

Desde un segundo terminal del mismo equipo, ejecuta `curl -i`. La opción incluye las cabeceras de respuesta antes del contenido.

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

La primera línea de la respuesta incluye un **código de estado**. Un código `200` indica que esta petición se completó correctamente. Una línea en blanco separa las cabeceras del cuerpo. `Content-Type` indica al cliente cómo interpretar el cuerpo, por ejemplo, como texto sin formato.

:::single-choice{#web-http-requests-responses-response-parts} ¿Qué parte ayuda al cliente a decidir cómo mostrar el contenido?

::option[La cabecera Content-Type de la respuesta.]{#web-http-requests-responses-response-parts-b .correct explanation="Indica el tipo de contenido del cuerpo de la respuesta."}
::option[El nombre del equipo en la petición original.]{#web-http-requests-responses-response-parts-a explanation="Ese nombre identifica el sitio con el que se puso en contacto el cliente."}
::option[Solo la ruta.]{#web-http-requests-responses-response-parts-c explanation="La ruta identifica el recurso, pero no especifica el formato devuelto."}
:::

![Respuesta HTTP registrada en LabEx con estado 200, un tipo de contenido de texto y ready como cuerpo](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## Comparar dos resultados

Una respuesta `404` indica que el servidor no encontró el recurso solicitado o no revela su existencia. Un sitio puede devolver 200 en una ruta y 404 en otra. Usa el método y la ruta exactos para comparar resultados.

:::single-choice{#web-http-requests-responses-health-scope} Una petición a /health recibe 200. ¿Qué puedes concluir sobre /welcome?

::option[/welcome también devolvió 200.]{#web-http-requests-responses-health-scope-a explanation="El ejemplo comprobó otra ruta."}
::option[No se pudo contactar con el equipo.]{#web-http-requests-responses-health-scope-b explanation="El servidor respondió a la comprobación de estado."}
::option[Debes solicitar /welcome para saber qué devuelve.]{#web-http-requests-responses-health-scope-c .correct explanation="Las dos rutas pueden responder de distinta manera."}
:::

Para practicar la comprobación de cabeceras de respuesta y de conectividad, prueba [Cómo comprobar la conectividad de un servidor con curl en Linux](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082).

## Resumen

Ya puedes interpretar las partes principales de un intercambio HTTP sencillo.

1. Identifica el método, la ruta y el nombre del equipo en una petición.
2. Lee el estado y el tipo de contenido en una respuesta.
3. Describe el resultado de la petición concreta que se hizo.
