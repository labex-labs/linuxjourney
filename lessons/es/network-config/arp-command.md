---
lesson_id: "arp-command"
course_id: "network-config"
lang: "es"
order_index: 5
title: "arp"
description: "Aprende a inspeccionar e interpretar el estado de la caché de vecinos ARP de IPv4 y de vecinos IPv6 en Linux."
meta_title: "arp - Network Config"
meta_description: "Aprende sobre el comando ARP de Linux y cómo consultar la caché ARP. Comprende la función de ARP en la comunicación de red con esta guía para principiantes."
meta_keywords: "ARP Linux, caché ARP, ip neighbour show, comandos de red, redes Linux, Linux para principiantes, tutorial Linux"
---

Linux almacena en la tabla de vecinos las direcciones de enlace de los siguientes saltos resueltas recientemente. Para IPv4 sobre Ethernet, las entradas se aprenden mediante ARP; IPv6 utiliza el descubrimiento de vecinos. El comando antiguo `arp` solo muestra una parte de este estado, mientras que `ip neighbor` gestiona ambas familias.

## Consultar entradas de vecinos

Inspecciona todas las entradas o las de una interfaz:

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

Una entrada incluye una dirección IP, una dirección de la capa de enlace, un dispositivo y un estado de accesibilidad. La tabla puede estar vacía después del arranque y llenarse a medida que el tráfico necesita siguientes saltos locales.

:::single-choice{#arp-command-modern-view} ¿Qué comando muestra el estado moderno de la tabla de vecinos de Linux?

::option[`pwd neighbor`]{#arp-command-pwd explanation="Pwd muestra el directorio de trabajo del shell."}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="Informa tanto de las entradas derivadas de ARP para IPv4 como de las de descubrimiento de vecinos para IPv6."}
::option[`route --passwords`]{#arp-command-route-passwords explanation="Ninguna inspección de rutas de este tipo debe exponer credenciales."}
:::

## Resolver un vecino IPv4

Cuando falta una correspondencia IPv4 en el enlace, un host difunde una solicitud ARP para preguntar quién posee la dirección de destino. Responde el destino o un router que realice explícitamente proxy ARP. El emisor guarda la correspondencia en caché y transmite la trama que estaba esperando.

Para un destino IP remoto, el host resuelve la dirección de la puerta de enlace seleccionada, no la dirección MAC del host remoto.

:::single-choice{#arp-command-remote-target} ¿Qué vecino IPv4 resuelve un host para un destino situado fuera del enlace?

::option[El servidor remoto final a través de todos los routers.]{#arp-command-final-server explanation="Su dirección MAC no tiene significado en el enlace de origen."}
::option[Todos los servidores DNS indicados en la configuración del resolver.]{#arp-command-all-dns explanation="La resolución de vecinos sigue la ruta seleccionada, no la lista del resolver."}
::option[La puerta de enlace seleccionada que está en el enlace.]{#arp-command-gateway .correct explanation="La trama Ethernet local se dirige al router que reenvía el paquete IP."}
:::

## Interpretar los estados

Entre los estados habituales se encuentran `REACHABLE`, `STALE`, `DELAY`, `PROBE`, `INCOMPLETE` y `FAILED`. `STALE` significa que la confirmación reciente de accesibilidad ha caducado; la dirección en caché aún puede utilizarse mientras la pila realiza las comprobaciones necesarias. `FAILED` indica que la resolución o la detección de accesibilidad no tuvo éxito, pero las causas pueden incluir el enlace, la VLAN, la dirección, la ruta, el filtrado o que el par esté apagado.

:::single-choice{#arp-command-stale-state} ¿Significa `STALE` que se sabe que el vecino es inaccesible?

::option[No; carece de una confirmación reciente y puede comprobarse al utilizarlo.]{#arp-command-stale-probe .correct explanation="El estado no equivale a `FAILED`."}
::option[Sí, y la entrada no puede volver a usarse nunca.]{#arp-command-stale-dead explanation="Las entradas obsoletas siguen siendo candidatas y pueden cambiar después de las comprobaciones de accesibilidad."}
::option[Sí, porque su registro DNS ha caducado.]{#arp-command-stale-dns explanation="El estado de los vecinos y la caché DNS son aspectos independientes."}
:::

## Cambiar el estado de los vecinos con cuidado

Las entradas estáticas y el vaciado de la caché modifican el estado y pueden interrumpir el tráfico activo u ocultar las pruebas originales. Captura primero las rutas, los contadores de paquetes y el estado de los vecinos actuales. Es preferible realizar una prueba dirigida y una captura de paquetes en una red de pruebas autorizada antes de vaciar toda una interfaz.

ARP no dispone de autenticación integrada, por lo que las direcciones duplicadas o las respuestas falsificadas pueden contaminar las correspondencias. Las protecciones de los conmutadores, la segmentación, la supervisión y la autenticación de capas superiores ayudan a reducir el impacto.

:::single-choice{#arp-command-flush-first} ¿Por qué no debes empezar un diagnóstico vaciando toda la tabla de vecinos?

::option[Las entradas de vecinos solo se almacenan en servidores raíz DNS.]{#arp-command-neighbors-dns explanation="La pila de red local las mantiene."}
::option[Un vaciado elimina permanentemente el hardware de la interfaz.]{#arp-command-flush-hardware explanation="Elimina entradas de la caché, no dispositivos físicos."}
::option[Modifica las pruebas y puede interrumpir siguientes saltos que sí funcionaban.]{#arp-command-flush-disrupts .correct explanation="La inspección de solo lectura y las pruebas dirigidas conservan el estado necesario para diagnosticar la causa."}
:::

## Resumen

Ahora puedes inspeccionar la resolución de vecinos sin tratar todos los estados de la caché como fallos.

1. Usa `ip neighbor` para consultar el estado de IPv4 e IPv6.
2. Resuelve el destino directamente solo cuando esté en el enlace.
3. Resuelve una puerta de enlace para el tráfico IP dirigido fuera del enlace.
4. Conserva las pruebas de la caché antes de realizar cambios de estado dirigidos.
