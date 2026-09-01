---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "es"
order_index: 3
title: "Recorrido de un paquete"
description: "Aprende cómo las rutas, el descubrimiento de vecinos, las tramas y los routers transportan un paquete IP a través de una trayectoria."
meta_title: "Recorrido de un paquete - Routing"
meta_description: "Explora el recorrido completo de los datos dentro de una red local y a través de Internet. Aprende cómo colaboran las direcciones IP, las direcciones MAC, ARP y las tablas de enrutamiento."
meta_keywords: "recorrido de paquetes, comunicación de red, ARP, dirección IP, dirección MAC, tabla de enrutamiento, puerta de enlace predeterminada, redes Linux, viaje de paquetes"
---

El recorrido de un paquete es una secuencia de decisiones locales. El host de origen, cada router y el destino aplican sus propios estados de enrutamiento, vecinos, filtrado y protocolos; normalmente, ningún punto final conoce de antemano todas las decisiones internas.

## Enviar a un destino situado en el enlace

Para un destino cubierto por una ruta conectada, el origen selecciona una interfaz y una dirección IP de origen. Después resuelve la dirección de enlace del destino —ARP para IPv4 sobre Ethernet o descubrimiento de vecinos para IPv6— y envía una trama que transporta el paquete IP. Un conmutador puede reenviar la trama sin convertirse en un salto IP.

:::single-choice{#packet-path-switch-hop} ¿Cuenta un conmutador Ethernet ordinario como salto de enrutamiento IP?

::option[No; reenvía tramas locales sin reducir el campo de saltos IP.]{#packet-path-switch-not-hop .correct explanation="Un salto enrutado se produce cuando un router procesa y reenvía el paquete IP."}
::option[Sí; todos los conmutadores sustituyen el destino IP.]{#packet-path-switch-replaces-ip explanation="El reenvío de capa 2 normalmente no reescribe los destinos IP."}
::option[Sí; todos los conectores de los cables también son saltos IP.]{#packet-path-cable-hop explanation="Los componentes físicos no realizan enrutamiento IP."}
:::

## Enviar a través de una puerta de enlace

Para un destino situado fuera del enlace, la ruta seleccionada identifica un router como siguiente salto. El destino IP sigue siendo el punto final remoto, mientras que el destino de la trama local es la dirección de enlace de la puerta de enlace. El host resuelve la puerta de enlace, no el servidor remoto, en su enlace local.

:::single-choice{#packet-path-gateway-mac} ¿Qué dirección MAC se utiliza en la primera trama Ethernet dirigida a un servidor situado fuera del enlace?

::option[La dirección del servidor remoto a través de todas las redes intermedias.]{#packet-path-remote-mac explanation="La dirección de enlace remota no tiene significado en la LAN de origen."}
::option[Un valor calculado a partir del nombre DNS del servidor.]{#packet-path-dns-mac explanation="Los nombres DNS no codifican la dirección MAC del siguiente salto local."}
::option[La dirección de la puerta de enlace local seleccionada.]{#packet-path-local-gateway .correct explanation="La trama se entrega al siguiente salto mientras la cabecera IP se dirige al punto final definitivo."}
:::

## Procesamiento en cada router

Un router elimina el encapsulado de enlace entrante, valida y procesa la cabecera IP, reduce el TTL o Hop Limit, consulta el destino, aplica la política y crea un encapsulado nuevo para el enlace de salida. En IPv4, el procesamiento de la suma de comprobación de la cabecera refleja el cambio del TTL. Si el campo de saltos llega a cero, el router descarta el paquete y puede devolver un mensaje ICMP de tiempo agotado.

:::single-choice{#packet-path-router-change} ¿Qué campo IP cambia en todos los saltos enrutados normales?

::option[El nombre de usuario de la aplicación.]{#packet-path-username explanation="Los routers no necesitan datos de cuentas de aplicaciones para el reenvío básico."}
::option[El TTL de IPv4 o el Hop Limit de IPv6.]{#packet-path-hop-field .correct explanation="Cada router reduce el campo para limitar los bucles de enrutamiento."}
::option[El puerto de transporte de destino en todos los casos.]{#packet-path-port explanation="El enrutamiento ordinario conserva los puntos finales de transporte; NAT puede ser una transformación independiente."}
:::

## Tener en cuenta dispositivos intermedios y MTU

El enrutamiento ordinario conserva las direcciones IP de origen y destino, pero NAT puede reescribirlas y los túneles pueden envolver el paquete original. Los cortafuegos pueden descartar el tráfico silenciosamente o rechazarlo. Las MTU de los enlaces también varían; en ocasiones los routers IPv4 pueden fragmentar paquetes, mientras que los routers IPv6 no fragmentan paquetes reenviados y dependen del descubrimiento de la MTU de la ruta.

:::single-choice{#packet-path-address-change-exception} ¿Cuándo pueden cambiar las direcciones IP de extremo a extremo durante una ruta?

::option[Cuando un conmutador Ethernet aprende una dirección MAC de origen.]{#packet-path-switch-learning-ip explanation="El aprendizaje del conmutador afecta a una tabla de reenvío de enlace, no a las direcciones de los puntos finales IP."}
::option[Cuando una política NAT traduce las cabeceras de los paquetes.]{#packet-path-nat-change .correct explanation="La traducción es una función de un dispositivo intermedio que va más allá del reenvío ordinario de rutas."}
::option[Cuando caduca una entrada de la caché DNS.]{#packet-path-dns-expiry explanation="Los paquetes existentes ya contienen direcciones numéricas."}
:::

## Seguir la ruta de retorno

El destino realiza su propia consulta de ruta para la respuesta. La ruta de retorno puede utilizar routers distintos debido a las políticas de enrutamiento, el equilibrio de carga o los fallos. Los cortafuegos con estado y NAT deben tener en cuenta el flujo observado, por lo que la asimetría puede tener importancia operativa aunque IP la permita.

:::single-choice{#packet-path-return-symmetry} ¿Debe atravesar una respuesta los mismos routers en orden inverso?

::option[Sí, porque IP registra la ruta de salida completa en todos los paquetes.]{#packet-path-records-route explanation="Los paquetes IP ordinarios no contienen obligatoriamente una ruta inversa completa."}
::option[Sí, salvo que el origen y el destino compartan un nombre de host.]{#packet-path-hostname-symmetry explanation="Los nombres no imponen la simetría de las rutas."}
::option[No; cada dirección se enruta de forma independiente.]{#packet-path-independent-return .correct explanation="Las políticas y la topología pueden producir una ruta asimétrica pero válida."}
:::

## Resumen

Ahora puedes seguir el estado cambiante del enlace alrededor de un paquete IP enrutado.

1. Resuelve el host final directamente solo cuando esté en el enlace.
2. Encapsula el tráfico situado fuera del enlace para la puerta de enlace local seleccionada.
3. Sigue la consulta de rutas y el procesamiento del límite de saltos en cada router.
4. Ten en cuenta NAT, el filtrado, los túneles y las restricciones de MTU.
5. Trata la dirección de retorno como una ruta independiente.
