---
index: 8
lang: "es"
title: "Capa de Enlace"
meta_title: "Capa de Enlace - Fundamentos de Red"
meta_description: "Explore los fundamentos de la capa de enlace de TCP/IP. Aprenda cómo se construye la cabecera de la capa de enlace, cómo ARP resuelve direcciones IP a direcciones MAC y el proceso de recorrido de paquetes en una red local."
meta_keywords: "capa de enlace, cabecera de capa de enlace, ARP, TCP/IP, dirección MAC, fundamentos de red, redes Linux, recorrido de paquetes, protocolo de resolución de direcciones"
---

## Lesson Content

La **Capa de Enlace** es la capa fundamental del modelo TCP/IP, responsable de las comunicaciones en el segmento de red local. Esta capa es específica del hardware, ya que trata directamente con las tarjetas de interfaz de red y el direccionamiento físico.

### Tramas y la Cabecera de la Capa de Enlace

En la **capa de enlace**, el paquete de la capa de red se encapsula en una estructura llamada trama. Una parte crucial de este proceso es la adición de la **cabecera de la capa de enlace**. Esta cabecera contiene las direcciones MAC de origen y destino de los hosts, sumas de verificación para la detección de errores y separadores de paquetes, que permiten al dispositivo receptor identificar dónde termina una trama y comienza la siguiente.

Para construir la **cabecera de la capa de enlace**, el sistema necesita tanto las direcciones MAC de origen como las de destino. Si bien se conoce la dirección MAC de origen, se debe descubrir la dirección MAC de destino para una IP en la misma red local. Aquí es donde entra en juego el Protocolo de Resolución de Direcciones (ARP).

### ARP (Protocolo de Resolución de Direcciones)

ARP es un protocolo de la **capa de enlace** que se utiliza para encontrar la dirección MAC asociada con una dirección IP específica dentro de la misma red. Si el host de destino estuviera en una red diferente, el paquete se enviaría a una puerta de enlace predeterminada (router), y ARP se utilizaría para encontrar la dirección MAC del router.

Los sistemas consultan primero su tabla de búsqueda ARP, que almacena en caché las asignaciones conocidas de IP a dirección MAC. Si la dirección requerida no está en la caché, el sistema transmite una solicitud ARP a toda la red. Este mensaje especial pregunta qué host tiene una dirección IP específica, por ejemplo, 10.10.1.4. El host con esa dirección IP enviará una respuesta ARP que contiene su dirección IP y MAC.

Con todas las direcciones IP y MAC necesarias, la **capa de enlace** ahora puede reenviar la trama a través de la tarjeta de interfaz de red. El viaje de un paquete es un proceso de varios pasos de encapsulación y desencapsulación a medida que se mueve hacia arriba y hacia abajo en la pila TCP/IP tanto en el extremo de envío como en el de recepción.

### Recorrido del Paquete

Aquí hay un desglose paso a paso de cómo viaja un paquete desde un remitente (Pete) hasta un receptor (Patty):

1. Pete envía un correo electrónico a Patty. Estos datos se envían a la capa de transporte.
2. La capa de transporte encapsula los datos en una cabecera TCP o UDP para formar un segmento. Adjunta los puertos de destino y origen y luego envía el segmento a la capa de red.
3. La capa de red encapsula el segmento dentro de un paquete IP y adjunta las direcciones IP de origen y destino. Luego enruta el paquete a la **capa de enlace**.
4. El paquete llega a la **capa de enlace**, donde se encapsula en una trama. Se añade la **cabecera de la capa de enlace**, que contiene las direcciones MAC de origen y destino.
5. Patty recibe esta trama de datos a través de su capa física, comprueba la integridad de los datos de la trama, luego la desencapsula y envía el paquete IP a su capa de red.
6. La capa de red lee el paquete para encontrar las direcciones IP de origen y destino. Confirma que la IP de destino coincide con la suya, desencapsula el paquete y envía el segmento a la capa de transporte.
7. La capa de transporte desencapsula el segmento, comprueba los números de puerto TCP o UDP y establece una conexión con la capa de aplicación basándose en esos puertos.
8. La capa de aplicación recibe los datos de la capa de transporte en el puerto especificado y se los presenta a Patty como el mensaje de correo electrónico final.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la Capa de Enlace, las direcciones MAC y ARP:

1. **[Identificar Direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones MAC, en un sistema Linux.
2. **[Explorar la Interacción de la Capa de Red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda cómo funcionan juntos los comandos `ping` y `arp` para resolver direcciones IP a direcciones MAC y comprender las interacciones de la capa de red.
3. **[Analizar Tramas Ethernet con tcpdump en Linux](https://labex.io/es/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Obtenga experiencia práctica capturando e inspeccionando tramas Ethernet, incluidas las direcciones MAC, para comprender las comunicaciones de red de bajo nivel.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con los fundamentos de red en la Capa de Enlace.

## Quiz Question

¿Qué protocolo se utiliza para encontrar la dirección MAC de un host en la misma red local? (Por favor, responda con el acrónimo en inglés en mayúsculas).

## Quiz Answer

ARP
