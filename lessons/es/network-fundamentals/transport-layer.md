---
lang: "es"
title: "Capa de Transporte"
description: "Aprenda sobre la capa de transporte en las redes Linux, incluyendo los protocolos TCP/UDP, puertos y segmentación de datos. Comprenda cómo se transfieren los datos de forma fiable."
keywords: "Capa de transporte de Linux, TCP/UDP, puertos de red, segmentación de datos, redes de Linux, tutorial para principiantes, protocolos de red"
---

## Lesson Content

La capa de transporte nos ayuda a transferir nuestros datos de una manera que las redes puedan leerlos. Divide nuestros datos en fragmentos que serán transportados y vueltos a unir en el orden correcto. Estos fragmentos se conocen como segmentos. Los segmentos facilitan el transporte de datos a través de las redes.

### Ports

Aunque sabemos a dónde estamos enviando nuestros datos a través de las direcciones IP, no son lo suficientemente específicas para enviar nuestros datos a ciertos procesos o servicios. Servicios como HTTP utilizan un canal de comunicación a través de puertos. Si queremos enviar datos de páginas web, necesitamos enviarlos a través del puerto HTTP (port 80). Además de formar segmentos, la capa de transporte también adjuntará los puertos de origen y destino al segmento, para que cuando el receptor reciba el paquete final sepa qué puerto usar.

### UDP

Hay dos protocolos de transporte populares: UDP y TCP. Discutiremos brevemente UDP y dedicaremos la mayor parte de nuestro tiempo a TCP, ya que es el más utilizado.

UDP no es un método fiable para transportar datos; de hecho, realmente no le importa si recibes todos tus datos originales. Esto puede sonar terrible, pero tiene sus usos, como para la transmisión de medios. Está bien si pierdes algunos frames; a cambio, obtienes tus datos un poco más rápido.

### TCP

TCP proporciona un flujo de datos fiable y orientado a la conexión. TCP utiliza ports para enviar y recibir datos de los hosts. Una aplicación abre una conexión desde un port en su host a otro port en un host remoto. Para establecer la conexión, utilizamos el TCP handshake.

- El cliente (proceso de conexión) envía un segmento SYN al servidor para solicitar una conexión.
- El servidor envía al cliente un segmento SYN-ACK para acusar recibo de la solicitud de conexión del cliente.
- El cliente envía un ACK al servidor para acusar recibo de la solicitud de conexión del servidor.

Una vez establecida esta conexión, los datos pueden intercambiarse a través de una conexión TCP. Los datos se envían en diferentes segmentos y se rastrean con TCP sequence numbers para que puedan organizarse en el orden correcto cuando se entregan. En nuestro ejemplo de correo electrónico, la capa de transporte adjunta el destination port (25) al source port del source host.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué es un protocolo de transporte fiable?

## Quiz Answer

TCP
