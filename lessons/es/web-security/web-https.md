---
lesson_id: "web-https"
course_id: "web-security"
lang: "es"
order_index: 2
title: "HTTPS"
description: "Aprende a identificar qué parte de una petición web protege HTTPS."
meta_title: "HTTPS - Seguridad web"
meta_description: "Aprende a identificar qué parte de una petición web protege HTTPS."
meta_keywords: "HTTPS, seguridad web, ciberseguridad, Linux Journey"
---

HTTP define los mensajes que intercambian un navegador y un servidor. HTTPS envía esos mismos mensajes mediante **TLS**, un protocolo que protege la conexión y ayuda al navegador a verificar la identidad del servidor.

## Identificar la conexión protegida

Imagina que un navegador se conecta a `https://site.example`. Después de establecer la conexión TLS, el navegador y el servidor pueden intercambiar mensajes HTTP cifrados. Quien observe ese tramo de la red no puede leer el cuerpo HTTP directamente ni modificarlo sin que se detecte.

```text
Browser  ===== HTTPS connection =====  Website server
```

El navegador aún debe validar la identidad que presenta el servidor.

:::single-choice{#web-https-protected-hop} ¿Qué protege HTTPS en este caso sencillo?

::option[La página después de que el navegador ya la haya mostrado.]{#web-https-protected-hop-b explanation="El navegador lee la página después de descifrar la respuesta."}
::option[Todas las copias de seguridad que guarda el sitio web.]{#web-https-protected-hop-c explanation="Las copias de seguridad requieren su propia protección."}
::option[Los mensajes HTTP que viajan por la conexión protegida.]{#web-https-protected-hop-a .correct explanation="TLS protege los mensajes en tránsito entre los dos extremos de la conexión."}
:::

## Interpretar una ruta con varios tramos

Un proxy puede recibir una petición del navegador y reenviarla a otro servidor. Si la conexión TLS termina en el proxy, este puede leer la petición antes de reenviarla. La siguiente conexión necesita su propia protección. Comprueba cada tramo de la ruta.

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

En este diagrama, la conexión externa usa TLS. La conexión interna usa HTTP sin cifrar.

:::single-choice{#web-https-inner-hop} ¿Qué tramo necesita un cambio propio para quedar protegido con TLS?

::option[Del navegador al proxy.]{#web-https-inner-hop-a explanation="Ese tramo ya usa HTTPS en el diagrama."}
::option[Del proxy al servidor interno.]{#web-https-inner-hop-b .correct explanation="El tramo interno del diagrama usa HTTP sin cifrar."}
::option[Una pestaña del navegador que nunca solicita el sitio.]{#web-https-inner-hop-c explanation="Esa pestaña no tiene ninguna conexión en el diagrama."}
:::

## Comprobar los permisos de la aplicación

Una conexión segura y válida aporta confianza en la identidad del servidor y protege los mensajes en tránsito. La aplicación aún debe decidir qué cuenta puede leer una página o cambiar un ajuste. Aunque una página privada use TLS con una configuración robusta, sigue necesitando una política de acceso en la aplicación.

:::single-choice{#web-https-access-vs-transport} ¿Qué debe comprobar el servicio antes de devolver la página privada de una cuenta?

::option[Si la cuenta autenticada tiene permiso para leer esa página.]{#web-https-access-vs-transport-c .correct explanation="La autorización en la aplicación controla a qué puede acceder la cuenta."}
::option[Solo si se está usando TLS.]{#web-https-access-vs-transport-a explanation="HTTPS protege el intercambio. El servicio aún necesita decidir si permite el acceso."}
::option[Solo si el certificado cubre el nombre del equipo solicitado.]{#web-https-access-vs-transport-b explanation="El certificado ayuda a verificar la identidad del servidor. La aplicación sigue controlando el acceso a las páginas privadas."}
:::

## Resumen

Ya puedes explicar qué protege HTTPS a lo largo de la ruta de una petición web.

1. Identifica dónde empieza y termina TLS.
2. Comprueba cada tramo si un proxy reenvía la petición.
3. Reconoce por qué la aplicación sigue necesitando controles de acceso.
