---
lang: "es"
title: "¿Qué es un router?"
meta_description: "Aprende qué es un router, cómo funciona y su papel en las redes. Comprende el enrutamiento, los saltos y la entrega de paquetes para principiantes."
meta_keywords: "router, redes, enrutamiento, saltos, conmutación de paquetes, redes Linux, tutorial para principiantes, guía de red"
---

## Lesson Content

Ya hemos usado el término router antes; con suerte, sabes lo que es, ya que probablemente tengas uno en tu casa. Un router permite que las máquinas de una red se comuniquen entre sí, así como con otras redes. En un router típico, tendrás puertos LAN que permiten que tus máquinas se conecten a la misma red de área local, y también tendrás un puerto de enlace ascendente a internet que te conecta a internet. A veces verás este puerto etiquetado como WAN porque esencialmente te conecta a una red más amplia. Cuando realizamos cualquier tipo de actividad de red, tiene que pasar por el router. El router decide a dónde van nuestros paquetes de red y cuáles entran. Enruta nuestros paquetes entre múltiples redes para ir desde su host de origen hasta su host de destino.

### ¿Cómo funciona un router?

Piensa en el enrutamiento de la misma manera que la entrega de correo. Tenemos una dirección a la que queremos enviar una carta. Cuando la enviamos a la oficina de correos, ellos toman la carta y ven: "Oh, esto va a California". La pondré en el camión que va a California (honestamente no tengo idea de cómo funciona el sistema postal). La carta luego se envía a San Francisco. Dentro de San Francisco, hay diferentes códigos postales, y luego en esos códigos postales, hay códigos de dirección más pequeños hasta que finalmente, alguien puede entregar tu carta a la dirección que querías. Por otro lado, si ya vivieras en San Francisco y en el mismo código postal, el cartero probablemente sabrá exactamente a dónde tiene que ir la carta sin entregársela a nadie más.

Cuando enrutamos paquetes, utilizan "rutas" de dirección similares, como "para llegar a la red A, envía estos paquetes a la red B". Cuando no tenemos una ruta establecida para eso, tenemos una ruta predeterminada que usarán nuestros paquetes. Estas rutas se establecen en una tabla de enrutamiento que nuestro sistema utiliza para navegar a través de las redes.

### Hops

A medida que los paquetes se mueven a través de las redes, viajan en hops. Un hop es cómo medimos aproximadamente la distancia que el paquete debe recorrer para ir desde el origen hasta el destino. Digamos que tengo dos routers que conectan el host A con el host B; por lo tanto, decimos que hay dos hops entre el host A y el host B. Cada hop es un dispositivo intermedio, como los routers, por el que debemos pasar.

### Understanding the basic difference between Switching, Routing & Flooding?

- **Packet SWITCHING** is basically receiving, processing, and forwarding data to the destination device.
- **ROUTING** is a process of creating the routing table so that we can do SWITCHING better.
- Before routing, **FLOODING** was used. If a router doesn't know which way to send a packet, then every incoming packet is sent through every outgoing link except the one it arrived on.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cómo miden la distancia los paquetes?

## Quiz Answer

Hops
