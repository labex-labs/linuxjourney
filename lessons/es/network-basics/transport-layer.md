---
index: 6
lang: "es"
title: "Capa de Transporte"
meta_title: "Capa de Transporte - Conceptos Básicos de Redes"
meta_description: "Aprenda sobre la capa de transporte en redes Linux, incluyendo protocolos TCP/UDP, puertos y segmentación de datos. Comprenda cómo se transfieren los datos de forma fiable."
meta_keywords: "Capa de Transporte Linux, TCP/UDP, puertos de red, segmentación de datos, redes Linux, tutorial para principiantes, protocolos de red"
---

## Lesson Content

La capa de transporte nos ayuda a transferir nuestros datos de una manera que las redes puedan leerlos. Divide nuestros datos en fragmentos que serán transportados y vueltos a unir en el orden correcto. Estos fragmentos se conocen como segmentos. Los segmentos facilitan el transporte de datos a través de las redes.

### Puertos

Aunque sabemos a dónde enviamos nuestros datos a través de direcciones IP, no son lo suficientemente específicas para enviar nuestros datos a ciertos procesos o servicios. Servicios como HTTP utilizan un canal de comunicación a través de puertos. Si queremos enviar datos de páginas web, necesitamos enviarlos a través del puerto HTTP (puerto 80). Además de formar segmentos, la capa de transporte también adjuntará los puertos de origen y destino al segmento, para que cuando el receptor reciba el paquete final sepa qué puerto usar.

### UDP

Hay dos protocolos de transporte populares: UDP y TCP. Discutiremos brevemente UDP y dedicaremos la mayor parte de nuestro tiempo a TCP, ya que es el más utilizado.

UDP no es un método fiable para transportar datos; de hecho, realmente no le importa si recibes todos tus datos originales. Esto puede sonar terrible, pero tiene sus usos, como para la transmisión de medios. Está bien si pierdes algunos fotogramas; a cambio, obtienes tus datos un poco más rápido.

### TCP

TCP proporciona un flujo de datos fiable y orientado a la conexión. TCP utiliza puertos para enviar y recibir datos de los hosts. Una aplicación abre una conexión desde un puerto en su host a otro puerto en un host remoto. Para establecer la conexión, utilizamos el "handshake" de TCP.

- El cliente (proceso de conexión) envía un segmento SYN al servidor para solicitar una conexión.
- El servidor envía al cliente un segmento SYN-ACK para reconocer la solicitud de conexión del cliente.
- El cliente envía un ACK al servidor para reconocer la solicitud de conexión del servidor.

Una vez establecida esta conexión, los datos pueden intercambiarse a través de una conexión TCP. Los datos se envían en diferentes segmentos y se rastrean con números de secuencia TCP para que puedan organizarse en el orden correcto cuando se entregan. En nuestro ejemplo de correo electrónico, la capa de transporte adjunta el puerto de destino (25) al puerto de origen del host de origen.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Cuál es un protocolo de transporte fiable?

## Quiz Answer

TCP
