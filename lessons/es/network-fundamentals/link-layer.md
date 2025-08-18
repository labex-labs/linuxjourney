---
lang: "es"
title: "Capa de Enlace"
meta_description: "Aprende sobre la Link Layer en TCP/IP, cómo ARP resuelve las direcciones MAC y el recorrido de los paquetes. Comprende los fundamentos de la red con este tutorial de redes de Linux."
meta_keywords: "Link Layer, ARP, TCP/IP, MAC address, fundamentos de red, redes Linux, principiante, tutorial"
---

## Lesson Content

En la parte inferior del modelo TCP/IP se encuentra la Link Layer. Esta capa es específica del hardware.

En la capa de enlace, nuestro paquete se encapsula una vez más en algo llamado frame. El encabezado del frame adjunta las direcciones MAC de origen y destino de nuestros hosts, sumas de verificación y separadores de paquetes para que el receptor pueda saber cuándo termina un paquete.

Afortunadamente, estamos en la misma red, por lo que nuestro paquete no tendrá que viajar muy lejos. Primero, la capa de enlace adjunta mi dirección MAC de origen al encabezado del frame, pero también necesita saber la dirección MAC de Patty. ¿Cómo lo sabe, y cómo la encuentro si no está en Internet? ¡Usamos ARP!

### ARP (Address Resolution Protocol)

ARP encuentra la dirección MAC asociada con una dirección IP. ARP se utiliza dentro de la misma red. Si Patty no estuviera en la misma red, usaríamos un sistema de enrutamiento para determinar el siguiente router que recibiría el paquete, y una vez que estuviéramos en la misma red, podríamos usar ARP.

Una vez que estamos en la misma red, los sistemas primero usan la tabla de búsqueda ARP que almacena información sobre qué direcciones IP están asociadas con qué dirección MAC. Si el valor no está allí, entonces se usa ARP. Luego, el sistema enviará un mensaje de difusión a la red usando el protocolo ARP para averiguar qué host tiene la IP 10.10.1.4. Un mensaje de difusión es un mensaje especial que se envía a todos los hosts en una red (acertadamente llamado así por enviar una difusión). Cualquier máquina con la dirección IP solicitada responderá con un paquete ARP que contiene la dirección IP y la dirección MAC.

Ahora que tenemos todos los datos necesarios que necesitamos —dirección IP y direcciones MAC— nuestra capa de enlace reenvía este frame a través de nuestra network interface card, hacia el siguiente dispositivo, y encuentra la red de Patty. Este paso es un poco más complejo de lo que acabo de explicar, pero discutiremos más detalles en el curso de Routing.

Y ahí está: un recorrido de paquete simple (o no tan simple) a través de la capa TCP/IP. Ten en cuenta que los paquetes no viajan de forma unidireccional como esta. ¡Ni siquiera hemos llegado a la red de Patty todavía! Al viajar a través de redes, requiere pasar por el modelo TCP/IP al menos dos veces antes de que se envíe o reciba cualquier dato. En realidad, la forma en que se ve este paquete sería algo como esto:

### Packet Traversal

1. Pete sends Patty an email: this data gets sent to the transport layer.
2. The transport layer encapsulates the data into a TCP or UDP header to form a segment. The segment attaches the destination and source TCP or UDP port, then the segment is sent to the network layer.
3. The network layer encapsulates the TCP segment inside an IP packet; it attaches the source and destination IP address. Then it routes the packet to the link layer.
4. The packet then reaches Pete's physical hardware and gets encapsulated in a frame. The source and destination MAC addresses get added to the frame.
5. Patty receives this data frame through her physical layer and checks each frame for data integrity, then de-encapsulates the frame contents and sends the IP packet to the network layer.
6. The network layer reads the packet to find the source and destination IP that was previously attached. It checks if its IP is the same as the destination IP, which it is! It de-encapsulates the packet and sends the segment to the transport layer.
7. The transport layer de-encapsulates the segments, checks the TCP or UDP port numbers, and makes a connection to the application layer based on those port numbers.
8. The application layer receives the data from the transport layer on the port that was specified and presents it to Patty in the form of the final email message.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué se utiliza para encontrar la dirección MAC en la misma red?

## Quiz Answer

ARP
