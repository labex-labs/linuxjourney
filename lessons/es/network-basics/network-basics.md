---
lesson_id: "network-basics"
course_id: "network-basics"
lang: "es"
order_index: 1
title: "Conceptos básicos de redes"
description: "Aprende cómo los hosts, enlaces, conmutadores, routers y paquetes forman redes locales y de área amplia."
meta_title: "Conceptos básicos de redes - Network Basics"
meta_description: "Descubre la mejor forma de aprender Linux comenzando por los conceptos básicos de redes. Esta guía explica componentes como WAN, LAN, routers y hosts para principiantes."
meta_keywords: "básicos red, básicos linux, mejor forma aprender linux, fundamentos linux, WAN, LAN, WLAN, tutorial redes, guía networking"
---

Una red conecta interfaces para que las aplicaciones de distintos hosts puedan intercambiar datos. Comprender qué dispositivo, dirección y enlace gestiona cada parte de la ruta facilita la interpretación de los comandos de Linux que veremos más adelante.

## Hosts e interfaces

Un host es un punto final o sistema conectado a una red, como un portátil, un servidor, un teléfono o una máquina virtual. Un mismo host puede tener varias interfaces: Ethernet, Wi-Fi, loopback, túneles, puentes o adaptadores virtuales. Cada interfaz puede tener una configuración de la capa de enlace y de la capa de red apropiada para su tecnología.

Inspecciona las interfaces y direcciones de un host Linux con:

```bash
$ ip address show
```

Que una interfaz esté presente o administrativamente activa no demuestra que haya conectividad de extremo a extremo.

:::single-choice{#network-basics-host-interface}
¿Qué es una interfaz de red?

::option[Una copia permanente de todos los paquetes de Internet.]{#network-basics-interface-copy explanation="Una interfaz transmite y recibe tráfico; no es un archivo global de paquetes."}
::option[El punto de conexión de un host a una red o un enlace virtual.]{#network-basics-interface-attachment .correct explanation="Un host puede tener varias interfaces físicas o virtuales con configuraciones independientes."}
::option[Un alias legible de una factura del proveedor de Internet.]{#network-basics-interface-invoice explanation="Las etiquetas de facturación no están relacionadas con las conexiones de red de un host."}
:::

## Redes locales

Una red de área local, o LAN, abarca un entorno limitado como una vivienda, una oficina o un segmento de un centro de datos. Los conmutadores Ethernet reenvían tramas entre puertos de un enlace local. Una red LAN inalámbrica, o WLAN, utiliza tecnología de enlace inalámbrico. Las interfaces cableadas e inalámbricas pueden seguir perteneciendo a la misma subred IP cuando un puente o un punto de acceso las une.

:::single-choice{#network-basics-wlan-relationship}
¿Qué relación tiene una WLAN con una LAN?

::option[Una WLAN siempre es un Internet global independiente.]{#network-basics-wlan-global explanation="Es una red local que utiliza tecnología de enlace inalámbrico."}
::option[Una WLAN es una partición de disco que utilizan los routers.]{#network-basics-wlan-disk explanation="El término describe redes, no la disposición del almacenamiento."}
::option[Una WLAN es una modalidad inalámbrica de red de área local.]{#network-basics-wlan-local .correct explanation="Los enlaces inalámbricos y cableados pueden incluso unirse mediante un puente en un único dominio de difusión local."}
:::

## Routers y redes más amplias

Un router reenvía paquetes de la capa de red entre redes IP según su tabla de enrutamiento. Un dispositivo doméstico suele combinar enrutamiento, conmutación, acceso Wi-Fi, cortafuegos, NAT y DHCP, pero siguen siendo funciones distintas.

Una red de área amplia, o WAN, abarca límites geográficos o administrativos mayores. Un proveedor de servicios de Internet puede conectar la red de un cliente con otras redes, pero «WAN» no significa simplemente todos los dispositivos situados fuera de una vivienda.

:::single-choice{#network-basics-router-role}
¿Cuál es la función que define a un router?

::option[Reenviar paquetes entre redes de la capa de red.]{#network-basics-forward-networks .correct explanation="El enrutamiento selecciona los siguientes saltos a través de los límites de las redes IP."}
::option[Almacenar obligatoriamente todos los archivos de los usuarios como copia de seguridad.]{#network-basics-router-backup explanation="La conservación de archivos no es la función que define el enrutamiento."}
::option[Traducir todos los nombres de host sin consultar DNS.]{#network-basics-router-hostnames explanation="La resolución de nombres y el reenvío de paquetes son funciones independientes."}
:::

## Paquetes, tramas y flujos

Las aplicaciones producen datos que las capas de protocolos dividen y encapsulan para transmitirlos. IP transporta paquetes entre redes; un enlace local lleva cada paquete dentro de una trama específica de su tecnología. Normalmente, los routers sustituyen el encapsulado de la capa de enlace en cada salto mientras siguen reenviando el paquete IP.

Una conversación puede incluir muchos paquetes en ambas direcciones. Las pérdidas, los cambios de orden, la fragmentación, las retransmisiones y los cambios de ruta hacen que un único paquete capturado rara vez describa toda la transacción de una aplicación.

:::single-choice{#network-basics-router-frame}
¿Qué ocurre normalmente con el encapsulado de la capa de enlace en el salto de un router?

::option[El router elimina el encapsulado entrante y crea otro para el siguiente enlace.]{#network-basics-reframe .correct explanation="El paquete IP reenviado se transporta en una trama nueva de la capa de enlace apropiada para la interfaz de salida."}
::option[La misma trama Ethernet atraviesa todo Internet sin cambiar.]{#network-basics-same-frame explanation="Las tramas están limitadas a sus enlaces y se sustituyen en los saltos enrutados."}
::option[La aplicación elimina permanentemente las direcciones IP.]{#network-basics-delete-ip explanation="El enrutamiento depende de las direcciones de la capa de red."}
:::

## Resumen

Ahora puedes describir los componentes principales de una ruta de red básica.

1. Distingue los hosts de sus interfaces físicas y virtuales.
2. Reconoce las modalidades cableadas e inalámbricas de las redes locales.
3. Separa el enrutamiento de las demás funciones de un dispositivo doméstico combinado.
4. Distingue las tramas de enlace de los paquetes IP enrutados.
