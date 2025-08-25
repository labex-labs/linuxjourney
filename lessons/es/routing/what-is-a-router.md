---
index: 1
lang: "es"
title: "¿Qué es un router?"
meta_title: "¿Qué es un router? - Enrutamiento"
meta_description: "Aprende qué es un router, cómo funciona y su papel en las redes. Comprende el enrutamiento, los saltos y la entrega de paquetes para principiantes."
meta_keywords: "router, redes, enrutamiento, saltos, conmutación de paquetes, redes Linux, tutorial para principiantes, guía de red"
---

## Lesson Content

Hemos usado el término router antes; con suerte, sabes lo que es, ya que probablemente tengas uno en tu casa. Un router permite que las máquinas de una red se comuniquen entre sí, así como con otras redes. En un router típico, tendrás puertos LAN que permiten que tus máquinas se conecten a la misma red de área local, y también tendrás un puerto de enlace ascendente a internet que te conecta a internet. A veces verás este puerto etiquetado como WAN porque esencialmente te conecta a una red más amplia. Cuando realizamos cualquier tipo de actividad de red, tiene que pasar por el router. El router decide a dónde van nuestros paquetes de red y cuáles entran. Enruta nuestros paquetes entre múltiples redes para ir desde su host de origen hasta su host de destino.

### ¿Cómo funciona un router?

Piensa en el enrutamiento de la misma manera que la entrega de correo. Tenemos una dirección a la que queremos enviar una carta. Cuando la enviamos a la oficina de correos, ellos reciben la carta y ven: "Oh, esto va a California". La pondré en el camión que va a California (honestamente no tengo idea de cómo funciona el sistema postal). La carta luego se envía a San Francisco. Dentro de San Francisco, hay diferentes códigos postales, y luego en esos códigos postales, hay códigos de dirección más pequeños hasta que finalmente, alguien puede entregar tu carta a la dirección que querías. Por otro lado, si ya vivieras en San Francisco y en el mismo código postal, el cartero probablemente sabrá exactamente a dónde tiene que ir la carta sin entregársela a nadie más.

Cuando enrutamos paquetes, utilizan "rutas" de dirección similares, como "para llegar a la red A, envía estos paquetes a la red B". Cuando no tenemos una ruta establecida para eso, tenemos una ruta predeterminada que usarán nuestros paquetes. Estas rutas se establecen en una tabla de enrutamiento que nuestro sistema utiliza para navegar a través de las redes.

### Saltos

A medida que los paquetes se mueven a través de las redes, viajan en saltos. Un salto es cómo medimos aproximadamente la distancia que debe recorrer el paquete para ir del origen al destino. Digamos que tengo dos routers que conectan el host A con el host B; por lo tanto, decimos que hay dos saltos entre el host A y el host B. Cada salto es un dispositivo intermedio, como los routers, por el que debemos pasar.

### ¿Entendiendo la diferencia básica entre Conmutación, Enrutamiento e Inundación?

- **Packet SWITCHING** es básicamente recibir, procesar y reenviar datos al dispositivo de destino.
- **ROUTING** es un proceso de creación de la tabla de enrutamiento para que podamos hacer SWITCHING mejor.
- Antes del enrutamiento, se usaba **FLOODING**. Si un router no sabe por dónde enviar un paquete, entonces cada paquete entrante se envía a través de cada enlace saliente, excepto el que lo recibió.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la conectividad de red y el enrutamiento:

1. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Practica la prueba de la pila TCP/IP local, la identificación de IPs privadas y públicas, y la verificación de la accesibilidad de la red, que son clave para entender cómo un router facilita la comunicación.
2. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprende cómo los comandos `ping` y `arp` te ayudan a observar cómo interactúan las capas de red y de enlace de datos, y cómo la puerta de enlace predeterminada (router) maneja el tráfico remoto.
3. **[Simular la conectividad de la capa de red en Linux](https://labex.io/es/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Usa Docker para simular nodos de red y asignar direcciones IP, luego prueba la conectividad para entender cómo las subredes IP y el enrutamiento rigen la comunicación de red.

Estos laboratorios te ayudarán a aplicar los conceptos de comunicación de red, direccionamiento IP y el papel del enrutamiento en escenarios reales, construyendo confianza con los fundamentos de la red.

## Quiz Question

¿Cómo miden los paquetes la distancia?

## Quiz Answer

Hops
