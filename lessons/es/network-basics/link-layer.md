---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "es"
order_index: 8
title: "Capa de enlace"
description: "Aprende cómo las tramas Ethernet, el descubrimiento de vecinos, los conmutadores y los routers entregan paquetes en un enlace local."
meta_title: "Capa de enlace - Network Basics"
meta_description: "Explora los fundamentos de la capa de enlace de TCP/IP. Aprende cómo se construye una cabecera de enlace, cómo ARP resuelve direcciones IP en direcciones MAC y cómo atraviesa un paquete una red local."
meta_keywords: "capa de enlace, cabecera de capa de enlace, ARP, TCP/IP, dirección MAC, fundamentos de redes, redes Linux, recorrido de paquetes, protocolo de resolución de direcciones"
---

La capa de enlace transporta paquetes de la capa de red a través de un medio local o un enlace virtual. Ethernet y Wi-Fi utilizan detalles de encapsulado distintos, pero ambos proporcionan entrega local por debajo de IP.

## Tramas Ethernet

Una trama Ethernet contiene direcciones MAC de destino y origen, un campo EtherType o de longitud, una carga útil y un tráiler con una secuencia de comprobación de trama. La transmisión física también utiliza un preámbulo y un delimitador de inicio. La secuencia de comprobación detecta daños en el enlace; no repara una trama dañada ni la protege criptográficamente.

:::single-choice{#link-layer-fcs-purpose}
¿Para qué se utiliza la secuencia de comprobación de una trama Ethernet?

::option[Para detectar daños en la trama dentro del enlace.]{#link-layer-detect-corruption .correct explanation="Un receptor puede descartar una trama que no supere la comprobación de integridad."}
::option[Para cifrar la carga útil en todos los saltos enrutados.]{#link-layer-fcs-encryption explanation="FCS es un código de detección de errores, no cifrado ni autenticación."}
::option[Para seleccionar una aplicación mediante un puerto TCP.]{#link-layer-fcs-port explanation="Los puertos de transporte se llevan dentro de la carga útil IP."}
:::

## Conmutadores y entrega local

Un conmutador Ethernet aprende qué direcciones MAC de origen aparecen en sus puertos y reenvía las tramas unicast conocidas hacia el puerto del destino aprendido. El tráfico broadcast y parte del tráfico de destino desconocido se inunda dentro del dominio de difusión. Las VLAN pueden dividir un mismo sistema de conmutación en dominios lógicos de enlace independientes.

:::single-choice{#link-layer-switch-learning}
¿Qué información aprende normalmente un conmutador Ethernet de las tramas?

::option[Las contraseñas de las aplicaciones y las cookies HTTP.]{#link-layer-switch-passwords explanation="Una tabla básica de reenvío utiliza direcciones de enlace, no credenciales de aplicaciones."}
::option[La tabla completa de enrutamiento de Internet de todos los routers.]{#link-layer-switch-routing-table explanation="La conmutación de capa 2 y el intercambio global de rutas son funciones distintas."}
::option[Las direcciones MAC de origen asociadas a los puertos del conmutador.]{#link-layer-switch-source .correct explanation="Este aprendizaje construye la tabla de reenvío utilizada posteriormente para el tráfico unicast conocido."}
:::

## Resolver la dirección del siguiente salto

Para IPv4 sobre Ethernet, el Protocolo de resolución de direcciones relaciona una dirección IPv4 del siguiente salto en el enlace con una dirección MAC. El host consulta primero su caché de vecinos. Si es necesario, difunde una solicitud ARP y responde el propietario o un proxy autorizado.

Para un destino IP fuera del enlace, el host resuelve la dirección MAC de la puerta de enlace predeterminada o seleccionada, no la dirección MAC del destino remoto. IPv6 utiliza el descubrimiento de vecinos sobre ICMPv6 en lugar de ARP.

:::single-choice{#link-layer-remote-destination-mac}
¿Qué dirección MAC utiliza un host para un destino IPv4 situado fuera del enlace?

::option[La dirección MAC del router seleccionado como siguiente salto.]{#link-layer-gateway-mac .correct explanation="El paquete IP sigue dirigido al host remoto, mientras que la trama local se dirige al router."}
::option[La dirección MAC del servidor remoto a través de todos los routers.]{#link-layer-remote-mac explanation="Las direcciones MAC son identificadores del enlace local y no se transportan de extremo a extremo."}
::option[Una dirección MAC derivada del puerto TCP de destino.]{#link-layer-port-mac explanation="Los puertos de transporte no determinan las direcciones de enlace."}
:::

## Inspeccionar el estado de los vecinos

Consulta las entradas ARP de IPv4 y de descubrimiento de vecinos de IPv6 con:

```bash
$ ip neighbor show
```

Estados como `REACHABLE`, `STALE`, `DELAY`, `PROBE` y `FAILED` describen el proceso de detección de inaccesibilidad de vecinos. `STALE` no significa averiado; indica que la confirmación de accesibilidad en caché ya no es reciente y puede comprobarse al utilizarla.

:::single-choice{#link-layer-stale-neighbor}
¿Qué indica una entrada de vecino con estado `STALE`?

::option[El cortafuegos bloquea permanentemente al vecino.]{#link-layer-stale-blocked explanation="El estado no describe la política del cortafuegos."}
::option[La dirección MAC se ha escrito en el disco como copia de seguridad.]{#link-layer-stale-backup explanation="El estado de los vecinos es información operativa en caché."}
::option[La correspondencia en caché no tiene una confirmación reciente de accesibilidad.]{#link-layer-stale-confirmation .correct explanation="La pila aún puede utilizarla y realizar la detección de accesibilidad cuando sea necesario."}
:::

## Encapsulado a través de un router

El emisor coloca un paquete IP dentro de una trama dirigida al siguiente salto. El router valida y retira la trama entrante, procesa la cabecera IP, selecciona una ruta de salida y construye una trama nueva para ese enlace. El receptor deshace el encapsulado y entrega la carga útil de transporte al socket correspondiente.

:::single-choice{#link-layer-router-reframing}
¿Qué permanece igual durante el reenvío ordinario mientras cambia el encapsulado Ethernet en un router?

::option[El destino IP, salvo que lo cambie un dispositivo intermedio como NAT.]{#link-layer-ip-destination .correct explanation="Los routers ordinarios reenvían hacia el destino IP final mientras sustituyen las tramas locales de cada salto."}
::option[La secuencia de comprobación de la trama entrante.]{#link-layer-same-fcs explanation="Una trama de salida nueva recibe su propio valor de integridad del enlace."}
::option[La dirección MAC de destino en todos los enlaces.]{#link-layer-same-mac explanation="Cada enlace utiliza la dirección de enlace apropiada para su siguiente salto."}
:::

## Resumen

Ahora puedes seguir un paquete IP durante un paso de entrega en un enlace local.

1. Identifica los campos principales de una trama Ethernet y su tráiler de integridad.
2. Explica cómo aprende un conmutador las ubicaciones de reenvío locales.
3. Resuelve un siguiente salto IPv4 con ARP y vecinos IPv6 con NDP.
4. Interpreta el estado de la caché de vecinos sin afirmar indebidamente que existe un fallo.
5. Reconoce que los routers reconstruyen las tramas para cada enlace de salida.
