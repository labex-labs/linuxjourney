---
lesson_id: "ipv6"
course_id: "subnetting"
lang: "es"
order_index: 7
title: "IPv6"
description: "Aprende a interpretar direcciones, prefijos, ámbitos, configuración automática y estado de enrutamiento IPv6 en Linux."
meta_title: "IPv6 - Subnetting"
meta_description: "Guía para principiantes sobre el protocolo IPv6. Aprende por qué se creó, cómo difiere de IPv4 y comprende los fundamentos de su esquema de direccionamiento para las redes Linux modernas."
meta_keywords: "IPv6, IPv4, dirección IP, redes Linux, protocolos de red, protocolo de Internet, agotamiento de direcciones, principiante, tutorial, guía"
---

IPv6 utiliza direcciones de 128 bits y se diseñó para admitir un espacio de direcciones mucho mayor, junto con un comportamiento actualizado de los paquetes y del descubrimiento de vecinos. IPv4 e IPv6 son protocolos independientes; los hosts de pila doble pueden ejecutar ambos durante la transición de las redes.

## Interpretar la notación IPv6

Una dirección IPv6 se escribe como ocho grupos hexadecimales de 16 bits:

```text
2001:0db8:0000:0000:0000:0000:0000:0025
```

Los ceros iniciales de cada grupo pueden omitirse y una secuencia contigua de grupos cero puede comprimirse mediante `::`:

```text
2001:db8::25
```

Solo puede aparecer un `::`, porque de otro modo la cantidad de grupos omitidos sería ambigua. `2001:db8::/32` está reservado para ejemplos de documentación.

:::single-choice{#ipv6-double-colon-rule} ¿Por qué `::` puede aparecer como máximo una vez en una dirección IPv6?

::option[Usar varios marcadores `::` haría ambigua la expansión.]{#ipv6-compression-ambiguity .correct explanation="Un marcador de compresión puede expandirse a la cantidad exacta de grupos necesarios para alcanzar ocho."}
::option[Las direcciones IPv6 solo contienen un bit cero.]{#ipv6-one-zero explanation="Una dirección puede contener muchos bits cero y grupos cero."}
::option[El marcador selecciona el puerto TCP cero.]{#ipv6-port-zero explanation="La compresión de direcciones no está relacionada con los puertos de transporte."}
:::

## Tipos de direcciones y ámbitos

Entre las direcciones e intervalos importantes se encuentran:

- `::1/128`: loopback en el host local.
- `fe80::/10`: unicast link-local; normalmente presente en las interfaces IPv6.
- `2000::/3`: espacio unicast global asignado actualmente.
- `ff00::/8`: multicast.

IPv6 no tiene una dirección de broadcast; multicast y el descubrimiento de vecinos cubren casos de uso que IPv4 suele gestionar mediante broadcast. Un destino link-local puede necesitar una zona de interfaz como `fe80::1%eth0`, porque el mismo prefijo existe en todos los enlaces.

:::single-choice{#ipv6-link-local-scope} ¿Cuál es el ámbito normal de una dirección `fe80::/10`?

::option[Todos los hosts de Internet global.]{#ipv6-global-link-local explanation="Las direcciones unicast globales sirven para el ámbito global enrutado."}
::option[Únicamente un archivo de zona DNS.]{#ipv6-dns-only explanation="Las direcciones link-local se asignan a interfaces y se utilizan en redes."}
::option[Un enlace local.]{#ipv6-one-link .correct explanation="Los routers no reenvían tráfico link-local ordinario entre enlaces."}
:::

## Prefijos y direcciones de interfaces

La notación CIDR de IPv6 utiliza una longitud de prefijo desde `/0` hasta `/128`. Un `/64` es el tamaño estándar para la mayoría de las subredes LAN y admite la configuración automática de direcciones sin estado. Una interfaz puede contener simultáneamente direcciones link-local, globales estables, temporales de privacidad y de otros tipos, cada una con una duración preferida y válida.

:::single-choice{#ipv6-address-multiplicity} ¿Por qué puede mostrar una interfaz varias direcciones IPv6?

::option[IPv6 necesita una dirección para cada dígito hexadecimal.]{#ipv6-one-per-digit explanation="Los dígitos son una representación, no asignaciones distintas de la interfaz."}
::option[Pueden coexistir distintos ámbitos y funciones de privacidad o duración.]{#ipv6-several-roles .correct explanation="Es normal tener una dirección link-local y una o varias direcciones globales o temporales."}
::option[Cada dirección identifica una tarjeta de red física independiente.]{#ipv6-separate-card explanation="Una interfaz puede poseer varias direcciones."}
:::

## Descubrimiento de vecinos y routers

El descubrimiento de vecinos de IPv6 utiliza ICMPv6 para resolver direcciones, detectar direcciones duplicadas, descubrir routers y obtener información de accesibilidad. Los anuncios de router pueden proporcionar prefijos e información del router predeterminado. Los hosts pueden combinar SLAAC con DHCPv6 para otra configuración; DHCPv6 normalmente no proporciona el router predeterminado.

Bloquear todo ICMPv6 rompe funciones esenciales del protocolo. La política del cortafuegos debe permitir los tipos de mensajes necesarios con el ámbito apropiado en lugar de tratar ICMPv6 como opcional.

:::single-choice{#ipv6-default-router-source} ¿Cómo aprende normalmente un host IPv6 un router predeterminado de forma dinámica?

::option[Mediante anuncios de router.]{#ipv6-router-advertisements .correct explanation="El descubrimiento de routers forma parte del descubrimiento de vecinos ICMPv6."}
::option[Mediante una dirección broadcast de Ethernet.]{#ipv6-ethernet-broadcast explanation="IPv6 no utiliza una dirección broadcast IP."}
::option[Mediante el intercambio TCP de tres pasos.]{#ipv6-tcp-handshake explanation="TCP establece el estado de transporte después de que el enrutamiento ya esté disponible."}
:::

## Inspeccionar y probar IPv6

Inspecciona por separado las direcciones, las rutas y los vecinos:

```bash
$ ip -6 address show
$ ip -6 route show
$ ip -6 neighbor show
$ ping -6 -c 3 2001:db8::25
```

Utiliza una dirección de prueba asignada realmente, no la dirección de documentación mostrada. Una aplicación de pila doble puede funcionar mediante IPv4 mientras IPv6 está averiado, o al contrario, así que prueba explícitamente cada familia y sus registros DNS `A` o `AAAA`.

:::single-choice{#ipv6-dual-stack-test} ¿Por qué deben probarse IPv4 e IPv6 por separado en un servicio de pila doble?

::option[Todos los paquetes IPv6 deben convertirse primero en broadcast IPv4.]{#ipv6-becomes-ipv4 explanation="IPv6 e IPv4 nativos son rutas de protocolo distintas."}
::option[Las dos familias pueden tener DNS, rutas, filtros y fallos diferentes.]{#ipv6-independent-paths .correct explanation="Una alternativa satisfactoria puede ocultar que la familia de direcciones preferida está averiada."}
::option[Las herramientas IPv6 no pueden mostrar el estado de las interfaces.]{#ipv6-tools-cannot explanation="Los comandos `ip -6` muestran el estado de las direcciones, las rutas y los vecinos."}
:::

## Resumen

Ahora puedes interpretar y probar el estado habitual de las interfaces y el enrutamiento IPv6.

1. Expande o comprime correctamente los ocho grupos hexadecimales de una dirección.
2. Distingue los ámbitos loopback, link-local, global y multicast.
3. Espera varias direcciones IPv6 y duraciones en una misma interfaz.
4. Conserva el tráfico necesario de descubrimiento de vecinos y anuncios de router.
5. Prueba de forma independiente las rutas IPv4 e IPv6 en servicios de pila doble.
