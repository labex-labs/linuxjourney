---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "es"
order_index: 4
title: "Direccionamiento de red"
description: "Aprende cómo las direcciones de enlace, las direcciones IP y los nombres de host identifican distintas partes de la comunicación de red."
meta_title: "Direccionamiento de red - Network Basics"
meta_description: "Descubre los fundamentos del direccionamiento de red. Esta guía explica las direcciones MAC, las direcciones IP y los nombres de host, conceptos esenciales para comprender la comunicación en redes Linux."
meta_keywords: "direccionamiento de red, dirección MAC, dirección IP, nombre de host, identificadores de red, redes Linux, conceptos básicos de redes, principiante, tutorial, guía"
---

La comunicación de red utiliza identificadores distintos en ámbitos diferentes. Las direcciones de la capa de enlace entregan tramas en un enlace local, las direcciones IP permiten la entrega enrutada y los nombres ayudan a las aplicaciones y a las personas a seleccionar servicios.

## Direcciones de la capa de enlace

Una dirección MAC de Ethernet tiene 48 bits y suele escribirse como seis octetos hexadecimales, por ejemplo `00:c4:b5:45:b2:43`. Una dirección de origen identifica una interfaz en el enlace actual, mientras que un destino puede ser unicast, multicast o broadcast.

No se garantiza que las direcciones MAC sean permanentes o globalmente únicas. El software puede asignar una dirección administrada localmente, las interfaces virtuales generan direcciones y las funciones de privacidad de Wi-Fi pueden aleatorizarlas. Normalmente, los routers sustituyen el encapsulado Ethernet en cada salto, por lo que un servidor remoto no recibe la dirección Ethernet de origen del enlace local inicial.

:::single-choice{#network-addressing-mac-scope} ¿Cuál es el ámbito normal de una dirección MAC de Ethernet durante la entrega de paquetes?

::option[El enlace local actual.]{#network-addressing-local-link .correct explanation="Los routers crean un encapsulado nuevo de la capa de enlace para los saltos posteriores."}
::option[Todos los saltos enrutados hasta el servidor final de Internet.]{#network-addressing-all-hops explanation="La trama original no atraviesa los routers sin cambios."}
::option[Únicamente la codificación de texto de la aplicación.]{#network-addressing-text-encoding explanation="Una dirección MAC pertenece al encapsulado de la capa de enlace."}
:::

## Direcciones IP y prefijos

Las direcciones IPv4 tienen 32 bits, o cuatro octetos, mientras que las direcciones IPv6 tienen 128 bits. Una dirección IP se asigna normalmente a una interfaz y se interpreta con una longitud de prefijo como `192.0.2.10/24` o `2001:db8::10/64`. El prefijo identifica cuántos bits iniciales describen la red.

Una interfaz puede tener varias direcciones IP, y una dirección puede cambiar mediante DHCP, direccionamiento de privacidad, conmutación por error o administración. Las direcciones IPv4 privadas pueden reutilizarse en redes distintas; las políticas de enrutamiento público y NAT determinan la accesibilidad externa.

:::single-choice{#network-addressing-ipv4-size} ¿Qué tamaño tiene una dirección IPv4?

::option[32 bits en cuatro octetos.]{#network-addressing-thirty-two .correct explanation="Cada componente decimal mostrado representa ocho bits."}
::option[4 bits en un único dígito hexadecimal.]{#network-addressing-four-bits explanation="Cuatro bits solo representan un dígito hexadecimal."}
::option[128 bits en dieciséis octetos.]{#network-addressing-128-octets explanation="IPv6 tiene 128 bits, no 128 octetos."}
:::

## Nombres de host y resolución de nombres

Un nombre de host es un nombre, no una dirección. La resolución de nombres puede consultar `/etc/hosts`, DNS, sistemas multicast u otras fuentes según la configuración de servicios de nombres de la máquina. Un nombre puede resolverse en varias direcciones y varios nombres pueden hacer referencia a un mismo servicio.

Utiliza la ruta del resolver del sistema cuando compruebes lo que probablemente verá una aplicación:

```bash
$ getent ahosts example.com
```

Las respuestas DNS pueden cambiar o estar en caché, y que la resolución tenga éxito no demuestra que el servicio sea accesible.

:::single-choice{#network-addressing-getent-purpose} ¿Por qué se utiliza `getent ahosts` durante una comprobación de resolución de nombres?

::option[Asigna permanentemente la dirección devuelta a todas las interfaces.]{#network-addressing-getent-assign explanation="El comando consulta bases de datos y no configura interfaces."}
::option[Solicita direcciones a la ruta de servicios de nombres configurada en el sistema.]{#network-addressing-system-resolver .correct explanation="Esta puede incluir archivos locales y DNS según la política de la máquina."}
::option[Garantiza que una aplicación funcione correctamente en todos los hosts devueltos.]{#network-addressing-getent-health explanation="La búsqueda de nombres y la salud de la aplicación son pruebas independientes."}
:::

## Inspeccionar un host Linux

Consulta por separado la configuración de enlace y la configuración IP:

```bash
$ ip -brief link
$ ip -brief address
```

Después, inspecciona las rutas y el estado de los vecinos al diagnosticar la accesibilidad. Nunca deduzcas la interfaz o la dirección de origen correcta solo a partir de su nombre; la selección de rutas, las reglas de política, los espacios de nombres y los túneles pueden cambiar la trayectoria.

:::single-choice{#network-addressing-ip-link-versus-address} ¿Qué vista de comandos se centra en las direcciones IP asignadas?

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="El objeto address muestra las asignaciones IPv4 e IPv6 de las interfaces."}
::option[Únicamente `ip -brief link`.]{#network-addressing-link-only explanation="La vista link se centra en el estado de las interfaces y de la capa de enlace."}
::option[`pwd`]{#network-addressing-pwd explanation="Pwd muestra el directorio de trabajo del shell."}
:::

## Resumen

Ahora puedes distinguir nombres y direcciones según su ámbito de red.

1. Trata las direcciones MAC como identificadores del enlace local que pueden cambiar.
2. Interpreta las direcciones IPv4 e IPv6 junto con sus longitudes de prefijo.
3. Reconoce que las interfaces pueden contener varias direcciones lógicas.
4. Consulta los nombres de host mediante el resolver del sistema configurado.
