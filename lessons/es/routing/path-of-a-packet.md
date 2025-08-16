---
lang: "es"
title: "Ruta de un Paquete"
description: "Aprenda cómo viaja un paquete dentro y fuera de una red. Comprenda IP, MAC, ARP y tablas de enrutamiento para la comunicación en red. ¡Comience su viaje en redes Linux!"
keywords: "viaje de paquetes, comunicación de red, ARP, dirección IP, dirección MAC, tabla de enrutamiento, redes Linux, guía para principiantes"
---

## Lesson Content

### Veamos cómo viaja un paquete dentro de su red local

1. Primero, la máquina local comparará la dirección IP de destino para ver si está en la misma subred, observando su máscara de subred.
2. Cuando se envían paquetes, necesitan tener una dirección MAC de origen, una dirección MAC de destino, una dirección IP de origen y una dirección IP de destino. En este punto, no conocemos la dirección MAC de destino.
3. Para llegar al host de destino, usamos ARP para transmitir una solicitud en la red local para encontrar la dirección MAC del host de destino.
4. ¡Ahora el paquete puede ser enviado exitosamente!

### Veamos cómo viaja un paquete fuera de su red

1. Primero, la máquina local comparará la dirección IP de destino. Como está fuera de nuestra red, no ve la dirección MAC del host de destino. Y no podemos usar ARP porque la solicitud ARP es una transmisión a hosts conectados localmente.
2. Así que nuestro paquete ahora mira la tabla de enrutamiento. No conoce la dirección IP de destino, por lo que la envía a la puerta de enlace predeterminada (otro router). Así que ahora nuestro paquete contiene nuestra IP de origen, IP de destino y MAC de origen; sin embargo, no tenemos una MAC de destino. Recuerde, las direcciones MAC solo se alcanzan a través de la misma red. Entonces, ¿qué hace? Envía una solicitud ARP para obtener la dirección MAC de la puerta de enlace predeterminada.
3. El router mira el paquete y confirma la dirección MAC de destino, pero no es la dirección IP de destino final, por lo que sigue mirando la tabla de enrutamiento para reenviar el paquete a otra dirección IP que pueda ayudar al paquete a avanzar hacia su destino. Cada vez que el paquete se mueve, elimina las antiguas direcciones MAC de origen y destino y actualiza el paquete con las nuevas direcciones MAC de origen y destino.
4. Una vez que el paquete se reenvía a la misma red, usamos ARP para encontrar la dirección MAC de destino final.
5. Durante este proceso, nuestro paquete no cambia la dirección IP de origen o destino.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cómo encontramos la dirección MAC de una dirección IP?

## Quiz Answer

ARP
