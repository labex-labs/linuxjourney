---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "es"
order_index: 3
title: "Modelo TCP/IP"
description: "Aprende cómo cooperan las capas de aplicación, transporte, Internet y enlace en el modelo TCP/IP."
meta_title: "Modelo TCP/IP - Network Basics"
meta_description: "Explora las capas fundamentales del modelo TCP/IP, base de las redes modernas. Aprende sobre las capas de aplicación, transporte, Internet y enlace para trabajar eficazmente con TCP/IP."
meta_keywords: "modelo TCP/IP, capas del modelo tcp ip, redes con tcp ip, capas del protocolo tcp, capas de red, TCP, IP, redes Linux, proyecto de protocolo real"
---

El modelo TCP/IP organiza en capas funcionales los protocolos que utilizan los hosts de Internet. Una forma habitual de cuatro capas incluye Aplicación, Transporte, Internet y Enlace. Algunos modelos didácticos separan el medio físico de la capa de enlace y, por tanto, muestran cinco capas.

## Capa de aplicación

Los protocolos de aplicación definen los mensajes y el comportamiento de servicios como HTTP, DNS, SSH y SMTP. Esta capa también incluye muchas responsabilidades de representación y sesión que el modelo OSI trata por separado.

:::single-choice{#tcpip-http-layer}
¿En qué capa de TCP/IP se clasifica normalmente HTTP?

::option[Internet.]{#tcpip-http-internet explanation="La capa de Internet gestiona el direccionamiento IP y el reenvío de paquetes."}
::option[Enlace.]{#tcpip-http-link explanation="La capa de enlace transporta el tráfico en un medio local."}
::option[Aplicación.]{#tcpip-http-application .correct explanation="HTTP define la semántica de las solicitudes y respuestas de una aplicación."}
:::

## Capa de transporte

Los protocolos de transporte proporcionan comunicación entre los puntos finales de las aplicaciones. TCP ofrece un flujo de bytes fiable y ordenado con control de congestión y de flujo. UDP proporciona datagramas independientes sin las garantías de conexión, orden o retransmisión de TCP. Los números de puerto ayudan a identificar los puntos finales del transporte, pero un número de puerto por sí solo no demuestra qué aplicación está escuchando.

:::single-choice{#tcpip-udp-property}
¿Qué propiedad pertenece a UDP y no a TCP?

::option[Datagramas independientes sin garantías de retransmisión integradas.]{#tcpip-udp-datagrams .correct explanation="Las aplicaciones que utilizan UDP deciden si añaden fiabilidad y de qué manera."}
::option[Entrega garantizada y ordenada de un único flujo de bytes.]{#tcpip-udp-ordered explanation="Esa es una propiedad del servicio TCP, siempre que la conexión tenga éxito."}
::option[Enrutamiento de paquetes entre redes IP distintas.]{#tcpip-udp-routing explanation="El enrutamiento entre redes es una función de la capa de Internet."}
:::

## Capa de Internet

El Protocolo de Internet transporta paquetes mediante direcciones IP de origen y destino. Los routers examinan la información de enrutamiento y reducen los límites de saltos mientras reenvían los paquetes hacia el destino. ICMP comunica información de control y de errores para el funcionamiento de IP. La entrega sigue siendo de mejor esfuerzo; las capas superiores o las aplicaciones se encargan de cualquier recuperación necesaria.

:::single-choice{#tcpip-router-layer}
¿Qué capa proporciona el destino IP que utilizan los routers?

::option[Internet.]{#tcpip-router-internet .correct explanation="La cabecera IP contiene el destino de la capa de red utilizado para el reenvío enrutado."}
::option[Aplicación.]{#tcpip-router-application explanation="Los mensajes de aplicación se transportan dentro de los datos de protocolos de capas inferiores."}
::option[Enlace.]{#tcpip-router-link explanation="Las direcciones de enlace seleccionan el destino de la trama del siguiente salto local."}
:::

## Capa de enlace y encapsulado

La capa de enlace envía un paquete IP a través de un enlace local mediante Ethernet, Wi-Fi, un protocolo punto a punto u otra tecnología. A medida que los datos de la aplicación descienden, cada capa añade la información necesaria para su ámbito. En el receptor, las capas validan y retiran su propio encapsulado antes de entregar los datos hacia arriba.

Las cabeceras de enlace normalmente cambian en cada salto enrutado; las conversaciones de transporte y aplicación son de extremo a extremo salvo que un dispositivo intermedio las termine o transforme.

:::single-choice{#tcpip-link-scope}
¿Cuál es el ámbito normal de una trama de la capa de enlace?

::option[Un enlace o salto local.]{#tcpip-one-link .correct explanation="Un router elimina el encapsulado entrante y crea otro para el siguiente enlace."}
::option[Todas las sesiones de aplicaciones de Internet global.]{#tcpip-global-frame explanation="Las tramas no permanecen sin cambios al atravesar redes enrutadas."}
::option[Únicamente la memoria del proceso de origen.]{#tcpip-process-memory explanation="Las tramas se transmiten a través de un enlace de red."}
:::

## Resumen

Ahora puedes situar funciones habituales de Internet dentro del modelo TCP/IP.

1. Asocia los protocolos de servicio con la capa de aplicación.
2. Distingue los flujos TCP de los datagramas UDP.
3. Sitúa el direccionamiento y el enrutamiento IP en la capa de Internet.
4. Trata el encapsulado de enlace como propio del salto local.
