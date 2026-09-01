---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "es"
order_index: 9
title: "Descripción general de DHCP"
description: "Aprende cómo DHCPv4 arrienda direcciones y opciones de red mediante descubrimiento, selección y renovación."
meta_title: "Descripción general de DHCP - Network Basics"
meta_description: "Aprende los fundamentos de DHCP, el protocolo de configuración dinámica de hosts. Esta guía explica cómo asigna direcciones IP, su proceso de cuatro pasos DORA y su función en la configuración de red."
meta_keywords: "DHCP, protocolo de configuración dinámica de host, capa DHCP, dirección IP, redes Linux, proceso DHCP, DORA, configuración de red"
---

El Protocolo de configuración dinámica de hosts proporciona a los clientes una configuración de red arrendada. En DHCPv4 puede incluir una dirección IPv4, una máscara de subred, routers predeterminados, servidores DNS, el tiempo de arrendamiento y otras opciones elegidas por la política local.

## Clientes, servidores y relays

Un servidor DHCP gestiona ámbitos o conjuntos de direcciones y el estado de los arrendamientos. El servidor no tiene que residir en todos los segmentos físicos: un relay DHCP puede reenviar los intercambios de los clientes entre una subred y un servidor centralizado. Las redes que solo utilizan configuración estática pueden no ofrecer DHCP.

DHCP es un protocolo de la capa de aplicación que se transporta sobre UDP. Los servidores DHCPv4 suelen utilizar el puerto UDP 67 y los clientes el puerto 68.

:::single-choice{#dhcp-relay-purpose} ¿Qué permite un relay DHCP?

::option[Que todos los clientes elijan una dirección sin ninguna política.]{#dhcp-client-any-address explanation="El servidor sigue aplicando la política de ámbitos y arrendamientos."}
::option[Que los clientes de otra subred lleguen a un servidor DHCP centralizado.]{#dhcp-central-server .correct explanation="El relay reenvía los intercambios DHCP a través de un límite de enrutamiento e identifica la red del cliente."}
::option[Que los conmutadores Ethernet sustituyan a todos los routers IP.]{#dhcp-switch-router explanation="El relay DHCP no elimina los límites de las redes enrutadas."}
:::

## Intercambio inicial de DHCPv4

El proceso inicial habitual se recuerda como DORA:

1. `DHCPDISCOVER`: un cliente busca servidores disponibles.
2. `DHCPOFFER`: un servidor propone una dirección y opciones.
3. `DHCPREQUEST`: el cliente selecciona y solicita un arrendamiento ofrecido.
4. `DHCPACK`: el servidor seleccionado confirma el arrendamiento y las opciones.

Los detalles de broadcast y unicast varían según el estado del cliente, el uso de relays y las capacidades del servidor. Una oferta todavía no es el arrendamiento final utilizable; la confirmación completa el intercambio normal de selección.

:::single-choice{#dhcp-dora-order} ¿Cuál es el orden inicial normal de DHCPv4?

::option[OFFER, DISCOVER, ACK, REQUEST.]{#dhcp-wrong-order-one explanation="Un cliente descubre antes de que un servidor ofrezca, y solicita antes de recibir la confirmación."}
::option[DISCOVER, OFFER, REQUEST, ACK.]{#dhcp-correct-order .correct explanation="La secuencia busca, propone, selecciona y confirma."}
::option[REQUEST, ACK, DISCOVER, OFFER.]{#dhcp-wrong-order-two explanation="Un cliente nuevo normalmente necesita descubrir y recibir una oferta antes de seleccionar un arrendamiento."}
:::

## Renovación del arrendamiento

Un arrendamiento caduca si no se renueva. Normalmente, el cliente comienza a renovarlo antes de que venza, a menudo contactando primero directamente con el servidor original. Si la renovación no tiene éxito, más adelante amplía el intento de revinculación. Los tiempos exactos los proporciona o deriva el protocolo.

Que una dirección aparezca como asignada dinámicamente no demuestra que su arrendamiento vaya a durar para siempre. Al diagnosticar cambios, registra el arrendamiento activo, su duración, el servidor y las opciones.

:::single-choice{#dhcp-lease-expiration} ¿Qué ocurre con un arrendamiento de dirección DHCP si no se renueva correctamente?

::option[Se convierte en una dirección MAC permanente del hardware.]{#dhcp-lease-mac explanation="Un arrendamiento IP no cambia la identidad de la capa de enlace."}
::option[Finalmente caduca y el cliente debe dejar de tratarlo como válido.]{#dhcp-lease-expires .correct explanation="Los arrendamientos permiten recuperar o cambiar las direcciones y opciones según la política del servidor."}
::option[Convierte al cliente en la raíz DNS autoritativa.]{#dhcp-lease-dns-root explanation="Un arrendamiento DHCP no concede autoridad sobre DNS."}
:::

## Inspeccionar el resultado

Después de que un cliente se configure mediante DHCP, comprueba todo el estado necesario y no solo la dirección:

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

El comando del resolver varía según el sistema. Inspecciona también los datos del arrendamiento y los registros del gestor de red activo. Aún pueden producirse direcciones duplicadas debido a servidores no autorizados, asignaciones estáticas dentro de un conjunto, estados obsoletos o configuraciones manuales; DHCP reduce los errores, pero no puede evitar por sí solo todos los conflictos.

:::single-choice{#dhcp-result-verification} ¿Qué debe comprobarse después de aceptar un arrendamiento DHCP?

::option[Únicamente el nombre que muestra la interfaz.]{#dhcp-interface-name-only explanation="El nombre de una interfaz no demuestra el direccionamiento, el enrutamiento ni la resolución."}
::option[Únicamente si responde el teclado.]{#dhcp-keyboard explanation="La entrada del teclado no está relacionada con la configuración del arrendamiento de red."}
::option[La dirección, las rutas, DNS y los detalles del arrendamiento.]{#dhcp-check-complete-state .correct explanation="Una configuración utilizable depende de varias opciones y del estado que aplican al sistema."}
:::

## DHCPv6 y configuración de IPv6

Los hosts IPv6 pueden utilizar configuración automática de direcciones sin estado, DHCPv6, configuración estática o combinaciones de ellas. DHCPv6 no utiliza el intercambio DORA de IPv4, y la información del router predeterminado suele proceder de los anuncios de router de IPv6, no de DHCPv6.

:::single-choice{#dhcp-ipv6-default-router} ¿Dónde aprende normalmente un host IPv6 la información de su router predeterminado?

::option[De los anuncios de router de IPv6.]{#dhcp-router-advertisement .correct explanation="DHCPv6 puede proporcionar otra configuración, pero los routers se anuncian mediante el descubrimiento de vecinos."}
::option[Del tráiler FCS de Ethernet.]{#dhcp-ipv6-fcs explanation="FCS detecta daños en el enlace y no contiene ninguna configuración de router."}
::option[Únicamente de un DHCPACK de IPv4.]{#dhcp-ipv4-ack explanation="Los mensajes DHCP de IPv4 no configuran el enrutamiento IPv6."}
:::

## Resumen

Ahora puedes explicar cómo DHCPv4 arrienda y renueva la configuración de red de un host.

1. Distingue los servidores DHCP de los relays y las subredes de clientes.
2. Sigue el intercambio DISCOVER, OFFER, REQUEST y ACK.
3. Trata las direcciones y opciones como un estado de arrendamiento con tiempo limitado.
4. Comprueba conjuntamente la dirección, las rutas, DNS y los metadatos del arrendamiento.
5. Mantén el comportamiento de DHCPv4 separado de la configuración automática de IPv6.
