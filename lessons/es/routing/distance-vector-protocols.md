---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "es"
order_index: 5
title: "Protocolos de vector de distancia"
description: "Aprende cómo los protocolos de vector de distancia derivan rutas de los anuncios de sus vecinos y limitan los bucles."
meta_title: "Protocolos de vector de distancia - Routing"
meta_description: "Guía para principiantes sobre los protocolos de vector de distancia. Este tutorial explica cómo protocolos como RIP utilizan la cantidad de saltos para determinar rutas y cuáles son sus limitaciones."
meta_keywords: "protocolos de vector de distancia, enrutamiento de red, RIP, protocolo de información de enrutamiento, cantidad de saltos, redes Linux, guía para principiantes, tutorial"
---

El enrutamiento por vector de distancia indica a los vecinos qué destinos son accesibles y una métrica que describe la distancia. Un router combina el anuncio de un vecino con el coste para llegar a él y así deriva su propia ruta candidata.

## Aprender mediante los vecinos

Si el router A anuncia una distancia de tres hasta un prefijo y el router B llega a A con un coste de uno, B puede derivar una distancia de cuatro a través de A. La información describe una dirección y una métrica, no un mapa completo de la topología, por lo que este enfoque a veces se denomina enrutamiento por rumores.

:::single-choice{#distance-vector-derived-distance}
Si un vecino anuncia la métrica 3 y el coste del enlace es 1, ¿qué métrica se deriva a través de él?

::option[2]{#distance-vector-two explanation="El coste del enlace se suma, no se resta."}
::option[31]{#distance-vector-thirty-one explanation="Los valores son métricas, no dígitos decimales que deban concatenarse."}
::option[4]{#distance-vector-four .correct explanation="La distancia del vecino y el coste del enlace local se combinan para formar la ruta candidata."}
:::

## Bucles y cuenta hasta el infinito

Después de un fallo, los vecinos pueden anunciarse por error una ruta mutuamente y aumentar su métrica de forma gradual. Los protocolos mitigan este problema mediante valores finitos de infinito, horizonte dividido, envenenamiento de rutas, inversa envenenada, actualizaciones activadas y temporizadores. Estos mecanismos reducen el problema, pero no convierten todos los cambios de topología en una convergencia instantánea.

:::single-choice{#distance-vector-split-horizon}
¿Qué pretende reducir el horizonte dividido?

::option[La cantidad de bits de todas las direcciones IPv4.]{#distance-vector-ip-bits explanation="El tamaño de una dirección IPv4 es fijo e independiente de las actualizaciones de enrutamiento."}
::option[La sobrecarga de cifrado de las cargas útiles de las aplicaciones.]{#distance-vector-encryption explanation="La técnica se ocupa de la dirección de los anuncios de rutas."}
::option[Anunciar una ruta aprendida de vuelta hacia el vecino del que procedía.]{#distance-vector-no-return .correct explanation="Suprimir esa dirección ayuda a evitar bucles sencillos de realimentación."}
:::

## Métricas y límites de RIP

RIP utiliza la cantidad de saltos. Una ruta con métrica 16 es inaccesible, por lo que la mayor métrica utilizable es 15. Esto limita el crecimiento de los bucles, pero también el diámetro de la red. Una cantidad menor de saltos no significa necesariamente menor latencia o más ancho de banda.

RIPv2 utiliza actualizaciones periódicas y activadas, y admite información CIDR. Suele enviar las actualizaciones mediante multicast en lugar de difundir una tabla completa en todas las circunstancias. La autenticación y el filtrado aún requieren una configuración deliberada.

:::single-choice{#distance-vector-rip-infinity}
¿Qué representa la métrica 16 de RIP?

::option[La ruta más rápida con dieciséis enlaces paralelos.]{#distance-vector-fastest-16 explanation="RIP trata el valor como inaccesible."}
::option[Infinito, lo que significa que el destino es inaccesible.]{#distance-vector-unreachable .correct explanation="RIP limita las rutas utilizables a 15 saltos."}
::option[Una ruta aprendida de BGP.]{#distance-vector-bgp-route explanation="El número tiene un significado específico de RIP."}
:::

## Evaluar una ruta aprendida

Comprueba el estado del vecino, los prefijos recibidos y anunciados, la métrica, el siguiente salto, la instalación de la ruta y la accesibilidad del plano de datos. Una ruta puede ser válida dentro de RIP, pero perder frente a otra fuente de rutas debido a la política local de preferencias.

:::single-choice{#distance-vector-fewest-hop-limit}
¿Por qué puede rendir mal la ruta de RIP con menos saltos?

::option[La cantidad de saltos no representa el ancho de banda, la latencia, las pérdidas ni la congestión de los enlaces.]{#distance-vector-hop-limited .correct explanation="Una ruta con más saltos puede tener mejores enlaces y rendimiento para la aplicación."}
::option[RIP siempre elige la ruta con más saltos.]{#distance-vector-most-hops explanation="Su métrica prefiere cantidades menores de saltos utilizables."}
::option[La cantidad de saltos se mide en bytes de espacio en disco.]{#distance-vector-disk-bytes explanation="Cuenta transiciones enrutadas, no almacenamiento."}
:::

## Resumen

Ahora puedes explicar tanto la sencillez como las limitaciones del enrutamiento por vector de distancia.

1. Deriva una distancia candidata del anuncio de un vecino.
2. Reconoce el comportamiento de los bucles y la cuenta hasta el infinito.
3. Explica el límite utilizable de 15 saltos de RIP y la métrica 16.
4. Comprueba por separado la instalación de la ruta y el resultado del plano de datos.
