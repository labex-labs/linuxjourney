---
lesson_id: "ipv4"
course_id: "subnetting"
lang: "es"
order_index: 1
title: "IPv4"
description: "Aprende cómo se relacionan las direcciones IPv4, los prefijos, los ámbitos y la salida de las interfaces Linux."
meta_title: "IPv4 - Subnetting"
meta_description: "Comienza tu recorrido con este tutorial completo sobre direcciones IPv4. Esta guía para principiantes explica la estructura IP y herramientas esenciales de línea de comandos como ip addr."
meta_keywords: "IPv4, dirección IP, linux para principiantes, mejor forma de aprender linux, tutorial completo de linux, curso linux gratuito, redes linux, ifconfig, ip addr"
---

IPv4 proporciona direcciones de origen y destino de 32 bits para los paquetes enrutados. Una dirección tiene significado junto con su prefijo, interfaz, ámbito, política de enrutamiento y duración, no como identificador permanente de todo un dispositivo.

## Notación decimal con puntos

IPv4 se representa como cuatro octetos de ocho bits separados por puntos:

```text
192.0.2.165
```

Cada octeto abarca de 0 a 255, por lo que la dirección completa contiene cuatro bytes. La longitud del prefijo indica cuántos bits iniciales pertenecen al prefijo de red, como en `192.0.2.165/24`.

:::single-choice{#ipv4-address-size}
¿Qué tamaño tiene una dirección IPv4?

::option[32 bits en cuatro octetos.]{#ipv4-thirty-two-bits .correct explanation="Cuatro grupos de ocho bits producen la representación decimal con puntos."}
::option[24 bits en todas las redes.]{#ipv4-always-twenty-four explanation="Un `/24` es una longitud de prefijo, no el tamaño de todas las direcciones IPv4."}
::option[128 bytes separados por dos puntos.]{#ipv4-128-bytes explanation="IPv6 tiene 128 bits y utiliza notación hexadecimal separada por dos puntos."}
:::

## Ámbito y finalidad de las direcciones

No todas las direcciones IPv4 pueden enrutarse globalmente. Entre los ejemplos se encuentran loopback `127.0.0.0/8`, link-local `169.254.0.0/16`, intervalos privados como `10.0.0.0/8` e intervalos de documentación como `192.0.2.0/24`. Las direcciones multicast y de broadcast limitado tienen otras semánticas.

Las direcciones privadas pueden reutilizarse en redes distintas. NAT puede traducirlas para la comunicación externa, pero no es necesario para comunicarse dentro del dominio privado enrutado.

:::single-choice{#ipv4-private-reuse}
¿Por qué puede aparecer `10.0.0.1` en muchas organizaciones?

::option[Todas las instancias identifican el mismo router físico.]{#ipv4-same-router explanation="La dirección tiene significado dentro de cada red y no es globalmente única."}
::option[Los routers IPv4 ignoran el primer octeto.]{#ipv4-ignore-octet explanation="Todos los bits de la dirección participan en la coincidencia de rutas."}
::option[Pertenece a un intervalo de direcciones destinado a reutilizarse en redes privadas.]{#ipv4-private-range .correct explanation="Las redes privadas independientes pueden utilizar las mismas direcciones sin anunciarlas globalmente."}
:::

## Inspeccionar direcciones IPv4 en Linux

Muestra las asignaciones IPv4 con:

```bash
$ ip -4 address show
```

Una línea como esta informa de algo más que la dirección:

```text
inet 192.0.2.165/24 brd 192.0.2.255 scope global dynamic eth0
```

Muestra el prefijo, el broadcast, el ámbito, el indicador de origen dinámico y la interfaz. Otras líneas pueden mostrar las duraciones válida y preferida. Una interfaz puede contener varias direcciones IPv4.

:::single-choice{#ipv4-ip-output-prefix}
¿Qué significa `/24` en `192.0.2.165/24`?

::option[La dirección caduca después de 24 segundos.]{#ipv4-prefix-seconds explanation="La duración se informa por separado."}
::option[Los primeros 24 bits de la dirección forman el prefijo de red.]{#ipv4-prefix-bits .correct explanation="Los ocho bits restantes identifican posiciones dentro de ese prefijo."}
::option[La interfaz corresponde al puerto TCP 24.]{#ipv4-prefix-port explanation="La notación de prefijos CIDR es independiente de los puertos de transporte."}
:::

## Determinar el origen seleccionado

La presencia de una dirección no demuestra que Linux vaya a utilizarla para un destino. Las rutas, las reglas de política, las métricas y la vinculación de la aplicación influyen en la selección del origen. Consulta la decisión de enrutamiento actual:

```bash
$ ip route get 198.51.100.20
```

Interpreta el siguiente salto, la interfaz y el origen seleccionados, y después prueba la ruta real de la aplicación. No modifiques direcciones en una máquina remota sin acceso mediante consola y un plan de reversión.

:::single-choice{#ipv4-route-get-purpose}
¿Qué puede mostrar `ip route get DESTINATION`?

::option[La configuración de todos los routers de la ruta completa de Internet.]{#ipv4-all-router-config explanation="Una consulta local no examina las configuraciones de los dispositivos posteriores."}
::option[La decisión de ruta local, incluidas la interfaz y la dirección de origen preferida.]{#ipv4-route-decision .correct explanation="Evalúa la política de enrutamiento actual del host para el destino proporcionado."}
::option[La contraseña del usuario del destino.]{#ipv4-password explanation="Los comandos de enrutamiento no exponen credenciales de aplicaciones."}
:::

## Resumen

Ahora puedes interpretar una dirección IPv4 como parte del estado de las interfaces y el enrutamiento.

1. Reconoce IPv4 como cuatro octetos que suman 32 bits.
2. Interpreta una dirección junto con su prefijo.
3. Distingue los ámbitos privado, loopback, link-local y otros.
4. Inspecciona las asignaciones y el origen seleccionado para un destino.
