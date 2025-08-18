---
lang: "es"
title: "Modelo TCP/IP"
meta_description: "Aprenda sobre las capas del modelo TCP/IP: Aplicación, Transporte, Red y Enlace. Comprenda cómo viajan los datos a través de las redes. ¡Comience su viaje en redes Linux!"
meta_keywords: "modelo TCP/IP, conceptos básicos de redes, redes Linux, TCP, IP, tutorial para principiantes, capas de red, guía"
---

## Lesson Content

El modelo OSI dio origen a lo que finalmente se convirtió en el modelo TCP/IP, y este modelo es en realidad la base de Internet. Es la implementación real de la red. El modelo TCP/IP utiliza el conjunto de protocolos TCP/IP, al que comúnmente nos referimos como TCP/IP. Estos protocolos trabajan juntos para especificar cómo se deben recopilar, direccionar, transmitir y enrutar los datos a través de una red. Usando el modelo TCP/IP, podemos ver cómo se utilizan estos protocolos para mostrar el desglose de cómo un paquete viaja a través de la red.

### Application Layer

La capa superior del modelo TCP/IP. Determina cómo los programas de su computadora (como su navegador web) interactúan con los servicios de la capa de transporte para ver los datos que se envían o reciben.

Esta capa utiliza:

- HTTP (Hypertext Transfer Protocol) - utilizado para páginas web en Internet.
- SMTP (Simple Mail Transfer Protocol) - transmisión de correo electrónico.

### Transport Layer

Cómo se transmitirán los datos, incluye la verificación de los puertos correctos, la integridad de los datos y, básicamente, la entrega de nuestros paquetes.

Esta capa utiliza:

- TCP (Transmission Control Protocol) - entrega de datos confiable
- UDP (User Datagram Protocol) - entrega de datos no confiable

### Network Layer

Esta capa especifica cómo mover paquetes entre hosts y a través de redes.

Esta capa utiliza:

- IP (Internet Protocol) - Ayuda a enrutar paquetes de una máquina a otra.
- ICMP (Internet Control Message Protocol) - Ayuda a decirnos qué está sucediendo, como mensajes de error e información de depuración.

### Link Layer

Esta capa especifica cómo enviar datos a través de una pieza física de hardware, como datos que viajan a través de Ethernet, fibra, etc.

Las listas anteriores de protocolos que utiliza cada capa no son exhaustivas, y encontrará muchos otros protocolos que entran en juego.

En las siguientes lecciones, profundizaremos en cada una de estas capas y discutiremos cómo nuestro paquete atraviesa la red a los ojos del modelo TCP/IP (hay muchas perspectivas sobre cómo un paquete viaja a través de las redes; no las veremos todas, pero tenga en cuenta que existen).

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuál es la capa superior del modelo TCP/IP?

## Quiz Answer

Application
