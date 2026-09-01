---
lesson_id: "classless-interdomain-routing-cidr"
course_id: "subnetting"
lang: "es"
order_index: 5
title: "CIDR"
description: "Aprende cómo los prefijos CIDR representan intervalos de direcciones, límites de subred y rutas agregadas."
meta_title: "CIDR - Subnetting"
meta_description: "Guía sobre la notación CIDR. Aprende el formato CIDR, cómo dividir en subredes y cómo calcular hosts para una red, también en un servidor Ubuntu. Domina el direccionamiento IP con CIDR."
meta_keywords: "CIDR, subredes CIDR, formato CIDR, máscara de subred, direccionamiento IP, cidr subred servidor ubuntu, cidr subred ubuntu, prefijo de red, redes Linux"
---

El enrutamiento entre dominios sin clases representa un intervalo de direcciones mediante una longitud de prefijo en lugar de depender de las clases históricas de direcciones. CIDR permite asignaciones de tamaño variable, división en subredes y agregación de rutas para IPv4 e IPv6.

## Interpretar la notación de prefijos

En `10.42.3.17/24`, los primeros 24 bits son el prefijo de red y quedan ocho bits para las posiciones dentro del intervalo. La red canónica es `10.42.3.0/24`; la dirección de host proporcionada aún puede escribirse con el prefijo al configurar una interfaz.

:::single-choice{#cidr-prefix-meaning} ¿Qué especifica `/24` en un valor CIDR de IPv4?

::option[Veinticuatro bits iniciales de prefijo de red.]{#cidr-24-prefix-bits .correct explanation="Los ocho bits restantes de los 32 de IPv4 varían dentro del prefijo."}
::option[Veinticuatro direcciones utilizables en todas las subredes.]{#cidr-24-addresses explanation="Un `/24` contiene 256 valores de dirección totales."}
::option[El puerto TCP de destino de la red.]{#cidr-24-port explanation="CIDR y los puertos de transporte son independientes."}
:::

## Calcular el tamaño del intervalo

El prefijo IPv4 `/23` deja nueve bits de host y, por tanto, abarca `2^9 = 512` direcciones totales. El prefijo alineado `123.12.24.0/23` abarca:

```text
first: 123.12.24.0
last:  123.12.25.255
```

En el uso tradicional con broadcast, la primera es la dirección de red y la última es el broadcast dirigido. No apliques ciegamente el atajo de «restar dos» hosts utilizables a los enlaces punto a punto `/31` o a las rutas de host `/32`.

:::single-choice{#cidr-23-total} ¿Cuántas direcciones IPv4 totales contiene un `/23`?

::option[512]{#cidr-total-512 .correct explanation="Nueve bits variables crean 2^9 combinaciones."}
::option[23]{#cidr-total-23 explanation="El número del prefijo cuenta bits fijos, no direcciones."}
::option[510]{#cidr-total-510 explanation="Esa es una cantidad tradicional utilizable después de los extremos especiales, no el tamaño total del intervalo."}
:::

## Comprobar la alineación

Un prefijo debe comenzar en su límite binario. Un `/23` avanza en bloques de dos en el tercer octeto cuando los octetos anteriores son fijos, por lo que `123.12.24.0/23` está alineado, mientras que `123.12.25.0/23` se canoniza al mismo intervalo `123.12.24.0/23`.

:::single-choice{#cidr-canonical-25} ¿Cuál es la red `/23` canónica que contiene `123.12.25.0`?

::option[Únicamente `123.12.25.0/23`, que comienza en 25.]{#cidr-25-unaligned explanation="El último bit del prefijo agrupa los valores del tercer octeto en pares alineados."}
::option[`123.12.0.0/23`]{#cidr-third-zero explanation="Esto describe otro intervalo `/23`."}
::option[`123.12.24.0/23`]{#cidr-24-canonical .correct explanation="Los valores 24 y 25 del tercer octeto comparten el mismo prefijo alineado de 23 bits."}
:::

## Agregar rutas

CIDR permite anunciar un único agregado para varios prefijos contiguos, del mismo tamaño y correctamente alineados. Por ejemplo, `192.0.2.0/25` y `192.0.2.128/25` se combinan en `192.0.2.0/24`. La agregación solo es segura cuando el router anunciante puede llegar correctamente a todo el agregado o dispone de políticas para impedir bucles y agujeros negros.

:::single-choice{#cidr-aggregate-two-25s} ¿Qué agregado abarca ambas mitades de `192.0.2.0/24`?

::option[`192.0.2.0/26`]{#cidr-aggregate-26 explanation="Un `/26` solo abarca 64 direcciones, menos que cualquiera de las mitades."}
::option[`192.0.3.0/25`]{#cidr-aggregate-other explanation="Esto queda fuera del intervalo de direcciones indicado."}
::option[`192.0.2.0/24`]{#cidr-aggregate-24 .correct explanation="Los dos intervalos `/25` contiguos y alineados solo difieren en el bit siguiente y comparten el prefijo `/24`."}
:::

## Enrutamiento por el prefijo más largo

Cuando las rutas se solapan, el reenvío suele seleccionar la ruta válida con el prefijo coincidente más largo. Una ruta `/24` es más específica que un `/16` que la contiene, mientras que una ruta predeterminada `/0` solo se impone cuando no gana ninguna ruta válida más específica.

:::single-choice{#cidr-route-specificity} Para el destino `10.42.3.8`, ¿qué ruta válida es más específica?

::option[`10.42.3.0/24`]{#cidr-route-24 .correct explanation="La coincidencia de 24 bits es más larga y, por tanto, más específica que `/8`."}
::option[`10.0.0.0/8`]{#cidr-route-8 explanation="Esta ruta coincide, pero fija menos bits del destino."}
::option[`0.0.0.0/0`]{#cidr-default explanation="La ruta predeterminada es el prefijo IPv4 menos específico posible."}
:::

## Resumen

Ahora puedes utilizar la notación CIDR tanto para intervalos de direcciones como para seleccionar rutas.

1. Interpreta el valor tras la barra como una cantidad de bits iniciales de prefijo.
2. Calcula el tamaño total del intervalo a partir de los bits restantes.
3. Canoniza un prefijo a su límite de red alineado.
4. Agrega únicamente intervalos contiguos y alineados cuya accesibilidad sea válida.
5. Durante una consulta de ruta, prefiere el prefijo válido más largo.
