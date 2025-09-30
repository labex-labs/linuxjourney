---
index: 8
lang: "es"
title: "Capa de Enlace"
meta_title: "Capa de Enlace - Fundamentos de Red"
meta_description: "Aprenda sobre la Capa de Enlace en TCP/IP, cómo ARP resuelve las direcciones MAC y el recorrido de paquetes. Comprenda los fundamentos de la red con este tutorial de redes de Linux."
meta_keywords: "Capa de Enlace, ARP, TCP/IP, dirección MAC, fundamentos de red, redes Linux, principiante, tutorial"
---

## Lesson Content

En la parte inferior del modelo TCP/IP se encuentra la Capa de Enlace. Esta capa es específica del hardware.

En la capa de enlace, nuestro paquete se encapsula una vez más en algo llamado trama. El encabezado de la trama adjunta las direcciones MAC de origen y destino de nuestros hosts, sumas de verificación y separadores de paquetes para que el receptor pueda saber cuándo termina un paquete.

Afortunadamente, estamos en la misma red, por lo que nuestro paquete no tendrá que viajar muy lejos. Primero, la capa de enlace adjunta mi dirección MAC de origen al encabezado de la trama, pero también necesita saber la dirección MAC de Patty. ¿Cómo lo sabe, y cómo lo encuentro ya que no está en Internet? ¡Usamos ARP!

### ARP (Protocolo de Resolución de Direcciones)

ARP encuentra la dirección MAC asociada con una dirección IP. ARP se utiliza dentro de la misma red. Si Patty no estuviera en la misma red, usaríamos un sistema de enrutamiento para determinar el siguiente enrutador que recibiría el paquete, y una vez que estuviéramos en la misma red, podríamos usar ARP.

Una vez que estamos en la misma red, los sistemas primero usan la tabla de búsqueda ARP que almacena información sobre qué direcciones IP están asociadas con qué dirección MAC. Si el valor no está allí, entonces se usa ARP. Luego, el sistema enviará un mensaje de difusión a la red usando el protocolo ARP para averiguar qué host tiene la IP 10.10.1.4. Un mensaje de difusión es un mensaje especial que se envía a todos los hosts en una red (acertadamente llamado así por enviar una difusión). Cualquier máquina con la dirección IP solicitada responderá con un paquete ARP que contiene la dirección IP y la dirección MAC.

Ahora que tenemos todos los datos necesarios (dirección IP y direcciones MAC), nuestra capa de enlace reenvía esta trama a través de nuestra tarjeta de interfaz de red, hacia el siguiente dispositivo, y encuentra la red de Patty. Este paso es un poco más complejo de lo que acabo de explicar, pero discutiremos más detalles en el curso de Enrutamiento.

Y ahí está: un recorrido de paquete simple (o no tan simple) a través de la capa TCP/IP. Tenga en cuenta que los paquetes no viajan de forma unidireccional como esta. ¡Ni siquiera hemos llegado a la red de Patty todavía! Al viajar a través de redes, requiere pasar por el modelo TCP/IP al menos dos veces antes de que se envíe o reciba cualquier dato. En realidad, la forma en que se vería este paquete sería algo como esto:

### Recorrido de Paquetes

1. Pete le envía un correo electrónico a Patty: estos datos se envían a la capa de transporte.
2. La capa de transporte encapsula los datos en un encabezado TCP o UDP para formar un segmento. El segmento adjunta el puerto TCP o UDP de destino y origen, luego el segmento se envía a la capa de red.
3. La capa de red encapsula el segmento TCP dentro de un paquete IP; adjunta la dirección IP de origen y destino. Luego enruta el paquete a la capa de enlace.
4. El paquete luego llega al hardware físico de Pete y se encapsula en una trama. Las direcciones MAC de origen y destino se agregan a la trama.
5. Patty recibe esta trama de datos a través de su capa física y verifica cada trama en busca de integridad de datos, luego desencapsula el contenido de la trama y envía el paquete IP a la capa de red.
6. La capa de red lee el paquete para encontrar la IP de origen y destino que se adjuntó previamente. ¡Verifica si su IP es la misma que la IP de destino, lo cual es cierto! Desencapsula el paquete y envía el segmento a la capa de transporte.
7. La capa de transporte desencapsula los segmentos, verifica los números de puerto TCP o UDP y establece una conexión con la capa de aplicación basándose en esos números de puerto.
8. La capa de aplicación recibe los datos de la capa de transporte en el puerto que se especificó y se los presenta a Patty en forma del mensaje de correo electrónico final.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la Capa de Enlace, las direcciones MAC y ARP:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones MAC, en un sistema Linux.
2. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda cómo los comandos `ping` y `arp` trabajan juntos para resolver direcciones IP a direcciones MAC y comprender las interacciones de la capa de red.
3. **[Analizar tramas Ethernet con tcpdump en Linux](https://labex.io/es/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Obtenga experiencia práctica capturando e inspeccionando tramas Ethernet, incluidas las direcciones MAC, para comprender las comunicaciones de red de bajo nivel.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con los fundamentos de la red en la Capa de Enlace.

## Quiz Question

¿Qué se utiliza para encontrar la dirección MAC en la misma red?

## Quiz Answer

ARP
