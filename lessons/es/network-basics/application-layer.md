---
lesson_id: "application-layer"
course_id: "network-basics"
lang: "es"
order_index: 5
title: "Capa de aplicación"
description: "Aprende cómo los protocolos de aplicación definen los mensajes, el estado, los nombres y el comportamiento de seguridad de los servicios."
meta_title: "Capa de aplicación - Network Basics"
meta_description: "Explora la capa de aplicación, la capa superior del modelo TCP/IP. Aprende qué es un protocolo de aplicación, consulta un ejemplo con SMTP y comprende cómo se preparan los datos para la comunicación de red."
meta_keywords: "capa de aplicación, la capa de aplicación, protocolo de capa de aplicación, ejemplo de protocolo de aplicación, cabecera de aplicación, modelo TCP/IP, SMTP, protocolos de red"
---

La capa de aplicación de TCP/IP contiene los protocolos que utilizan las aplicaciones para solicitar y proporcionar servicios de red. Abarca muchas funciones que la terminología OSI separa en las capas de aplicación, presentación y sesión.

## Mensajes y semántica de los protocolos

Un protocolo de aplicación define cómo interpretan los pares los mensajes y el estado. HTTP define solicitudes, respuestas, métodos, códigos de estado y campos. DNS define consultas y registros de recursos. SMTP define comandos y respuestas para transferir correo.

No todos los protocolos de aplicación añaden una «cabecera de aplicación» fija. Algunos utilizan campos de texto, otros registros binarios, otros varios formatos anidados y algunos transportan una secuencia continua de mensajes a través de una única conexión de transporte.

:::single-choice{#application-layer-protocol-role}
¿Qué define principalmente un protocolo de aplicación?

::option[El significado y las reglas de intercambio de los mensajes de un servicio.]{#application-layer-message-semantics .correct explanation="Los pares necesitan una sintaxis, una semántica y un comportamiento de estado compartidos para interoperar."}
::option[El voltaje de todos los cables Ethernet.]{#application-layer-voltage explanation="La señalización física pertenece a tecnologías de capas inferiores."}
::option[La ruta que elige de forma independiente cada router de Internet.]{#application-layer-router-choice explanation="Las decisiones de enrutamiento pertenecen al comportamiento de la capa de red."}
:::

## Clientes, servidores y pares

Un cliente inicia una solicitud o conexión con un servicio; un servidor escucha o la acepta de otra forma. Son funciones dentro de una interacción, no categorías permanentes de dispositivos. Un mismo host puede ser cliente de DNS y servidor de SSH al mismo tiempo, y algunos protocolos utilizan funciones entre pares.

:::single-choice{#application-layer-client-role}
¿Qué convierte a un programa en el cliente de un intercambio típico de solicitud y respuesta?

::option[Inicia una solicitud al servicio.]{#application-layer-client-initiates .correct explanation="Cliente y servidor describen funciones de interacción que un host puede realizar simultáneamente para servicios distintos."}
::option[Debe ejecutarse en un portátil y no en un servidor.]{#application-layer-client-laptop explanation="La categoría del hardware no determina la función en el protocolo."}
::option[Posee el prefijo IP de destino.]{#application-layer-client-prefix explanation="La propiedad de la red no está relacionada con iniciar una solicitud de aplicación."}
:::

## Nombres, puertos y selección de servicios

Una aplicación puede resolver el nombre de un servicio en una o varias direcciones IP y elegir un punto final de transporte. Los puertos conocidos proporcionan valores predeterminados, no pruebas inmutables de un protocolo. HTTP suele usar el puerto TCP 80 y HTTPS el puerto TCP 443, pero cualquiera puede ejecutarse en otro lugar. SMTP utiliza distintos puertos y políticas para la retransmisión y el envío de mensajes.

:::single-choice{#application-layer-port-limit}
¿Qué demuestra por sí solo un puerto TCP 443 abierto?

::option[Que un proceso ha aceptado un punto final TCP allí, pero aún debe comprobarse su comportamiento de aplicación.]{#application-layer-port-endpoint .correct explanation="El intercambio del protocolo y la validación de TLS proporcionan pruebas más sólidas en la capa de aplicación."}
::option[Que el servicio es sin duda una aplicación HTTPS configurada correctamente.]{#application-layer-port-proves-https explanation="Un número de puerto no valida el comportamiento del protocolo, la identidad ni la salud."}
::option[Que DNS no puede devolver una dirección IPv6.]{#application-layer-port-dns explanation="Los puertos de transporte no restringen las familias de registros DNS."}
:::

## Seguridad y pruebas de extremo a extremo

TLS puede proporcionar confidencialidad, integridad y autenticación de la identidad del par cuando la validación del certificado y el nombre del punto final son correctos. No autoriza automáticamente todas las acciones de la aplicación. Comprueba el mismo nombre, familia de direcciones, puerto, protocolo, credenciales y solicitud que utiliza el cliente real.

Por ejemplo, un diagnóstico de HTTPS puede comprobar por separado la resolución, la conexión TCP, el certificado y el nombre TLS, la respuesta HTTP y el contenido de la aplicación. El éxito en un paso acota el problema, pero no demuestra que todos los pasos posteriores funcionen.

:::single-choice{#application-layer-tls-limit}
¿Qué establece una validación satisfactoria del certificado TLS?

::option[Que todos los usuarios están autorizados para todos los recursos.]{#application-layer-tls-all-users explanation="La autenticación del transporte no sustituye la política de acceso de la aplicación."}
::option[La identidad del par para el nombre validado y un canal seguro autenticado.]{#application-layer-tls-identity .correct explanation="La autorización de la aplicación y la corrección del contenido aún necesitan sus propias comprobaciones."}
::option[Que ningún router podrá descartar nunca un paquete posterior.]{#application-layer-tls-routing explanation="TLS no puede garantizar la entrega futura por la red."}
:::

## Resumen

Ahora puedes describir el comportamiento de la capa de aplicación más allá de un número de puerto o un nombre de programa.

1. Identifica la sintaxis, la semántica y el estado del protocolo como aspectos de la aplicación.
2. Trata cliente y servidor como funciones dentro de un intercambio.
3. Usa los puertos como convenciones de puntos finales, no como prueba de un protocolo.
4. Comprueba de extremo a extremo los nombres, la seguridad y las respuestas de la aplicación.
