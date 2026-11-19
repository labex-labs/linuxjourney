---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "es"
order_index: 5
title: "Sesiones y cookies"
description: "Aprende cómo una cookie vincula las peticiones del navegador a una sesión web."
meta_title: "Sesiones y cookies - Seguridad web"
meta_description: "Aprende cómo una cookie vincula las peticiones del navegador a una sesión web."
meta_keywords: "sesiones y cookies, seguridad web, ciberseguridad, Linux Journey"
---

Después de iniciar sesión, el navegador suele enviar más peticiones. Una **sesión** permite a la aplicación asociar esas peticiones con la cuenta que inició sesión. Un método habitual usa un identificador corto guardado en una cookie del navegador.

## Seguir el recorrido de una cookie

Estos ejemplos están abreviados. La respuesta envía una cookie llamada `session` con un token ficticio para ilustrar el intercambio.

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

El navegador puede incluir la cookie en una petición posterior que cumpla las reglas de la cookie.

```http
Cookie: session=sample-token
```

El servidor usa el token para buscar la sesión que creó antes.

:::single-choice{#web-sessions-and-cookies-direction} ¿Qué cabecera devuelve el valor de la cookie en una petición que cumple las reglas?

::option[Set-Cookie.]{#web-sessions-and-cookies-direction-a explanation="El servidor envía esta cabecera en la respuesta para establecer la cookie."}
::option[Content-Type.]{#web-sessions-and-cookies-direction-c explanation="Esa cabecera describe el formato del cuerpo del mensaje."}
::option[Cookie.]{#web-sessions-and-cookies-direction-b .correct explanation="El navegador incluye esta cabecera en la petición cuando se cumplen las reglas."}
:::

## Interpretar los atributos

`Secure` limita el envío habitual de la cookie a HTTPS. `HttpOnly` impide que los scripts de la página lean la cookie mediante la API habitual de cookies. `SameSite` controla cuándo el navegador incluye la cookie en peticiones iniciadas desde otro sitio. Cada ajuste controla un aspecto distinto del comportamiento del navegador.

:::single-choice{#web-sessions-and-cookies-secure-attribute} ¿Qué atributo indica al navegador que limite el envío de la cookie a HTTPS?

::option[HttpOnly.]{#web-sessions-and-cookies-secure-attribute-b explanation="Restringe el acceso a la cookie desde los scripts de la página."}
::option[Secure.]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="Este atributo controla el transporte protegido que usa la cookie."}
::option[El nombre session.]{#web-sessions-and-cookies-secure-attribute-c explanation="El nombre de la cookie es una etiqueta que elige la aplicación."}
:::

## Cerrar una sesión

Cuando un usuario cierra sesión, el servicio puede invalidar la sesión en el servidor y pedir al navegador que elimine la cookie que guardó. Es importante invalidarla en el servidor porque el navegador aún puede conservar durante un tiempo el valor antiguo. Trata todo token de sesión real como una credencial y evita incluirlo en capturas de pantalla o registros compartidos.

:::single-choice{#web-sessions-and-cookies-after-sign-out} ¿Qué debe ocurrir si un token de una sesión invalidada vuelve a llegar al servidor?

::option[El servidor debe tratar la petición como no autenticada.]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="La sesión asociada a ese valor ya no es válida en el servidor."}
::option[El servidor debe restaurar la sesión antigua automáticamente.]{#web-sessions-and-cookies-after-sign-out-a explanation="La sesión anterior ya terminó."}
::option[El servidor debe aceptarlo porque la cookie aún tiene un nombre.]{#web-sessions-and-cookies-after-sign-out-b explanation="El nombre de una cookie no hace válido su valor."}
:::

## Resumen

Ya puedes seguir una cookie de sesión entre un navegador y un servicio.

1. Identifica la cabecera que establece la cookie y la que la devuelve.
2. Explica para qué sirven los atributos habituales de las cookies.
3. Describe cómo termina una sesión cuando se invalida en el servidor.
