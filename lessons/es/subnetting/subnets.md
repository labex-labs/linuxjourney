---
lesson_id: "subnets"
course_id: "subnetting"
lang: "es"
order_index: 2
title: "Subredes"
description: "Aprende cómo los prefijos definen subredes IPv4 e influyen en la entrega en el enlace, el enrutamiento y las políticas."
meta_title: "Subredes - Subnetting"
meta_description: "Domina los fundamentos de las subredes y máscaras de Linux. Esta guía explica los prefijos de red y cómo gestionar la segmentación en un entorno Linux."
meta_keywords: "subred linux, subredes linux, máscara de subred linux, división en subredes, subredes, máscara de subred, prefijo de red, redes Linux, dirección IP"
---

Una subred es un intervalo de direcciones IP definido por un prefijo de red. Los hosts de una subred suelen estar en el mismo enlace local, pero la proximidad física no constituye la definición: las VLAN, los túneles, las redes superpuestas y los enlaces enrutados pueden cambiar la topología.

## Prefijos y máscaras

IPv4 puede expresar un prefijo de 24 bits como `/24` o mediante la máscara `255.255.255.0`. En binario, una máscara de subred convencional válida contiene unos contiguos seguidos de ceros:

```text
11111111.11111111.11111111.00000000
```

Para la dirección `192.168.1.8/24`, el prefijo de red es `192.168.1.0/24`. Algunos contextos comprenden `192.168.1.0/255.255.255.0`, pero la notación de prefijo CIDR es la forma compacta estándar.

:::single-choice{#subnets-mask-24}
¿Qué máscara decimal con puntos corresponde a `/24`?

::option[`255.255.255.0`]{#subnets-mask-correct .correct explanation="Tres octetos completos contienen 24 bits uno iniciales."}
::option[`255.255.0.255`]{#subnets-noncontiguous explanation="Esta máscara tiene bits de red no contiguos y no es la máscara convencional `/24`."}
::option[`0.0.0.24`]{#subnets-prefix-as-octet explanation="Una longitud de prefijo no se coloca en el último octeto de la máscara."}
:::

## Decidir si un destino está en el enlace

Linux instala rutas conectadas a partir de las direcciones y prefijos de las interfaces. Compara un destino con las rutas válidas en lugar de limitarse a comparar los tres primeros octetos decimales. En límites que no coinciden con octetos, como `/20`, la división se produce dentro de un octeto.

Inspecciona las rutas conectadas y la decisión para una dirección:

```bash
$ ip route show
$ ip route get 192.168.1.50
```

:::single-choice{#subnets-on-link-decision}
¿Cómo determina un host Linux si debe enviar directamente o a través de un router?

::option[Siempre supone que las direcciones terminadas en `.1` son locales.]{#subnets-dot-one explanation="Las convenciones de números de host no sustituyen los prefijos y las rutas configurados."}
::option[Consulta los prefijos y la política de enrutamiento.]{#subnets-route-policy .correct explanation="La ruta seleccionada identifica si el destino está en el enlace y qué interfaz o siguiente salto utilizar."}
::option[Pide a la aplicación de destino una máscara de subred después de conectarse.]{#subnets-ask-application explanation="La selección de ruta debe producirse antes de ese intercambio de la aplicación."}
:::

## Enrutamiento entre subredes

Un router con interfaces y rutas apropiadas puede reenviar tráfico entre subredes. Una puerta de enlace predeterminada es simplemente un siguiente salto elegido por una ruta predeterminada; no tiene por qué utilizar la primera dirección disponible ni terminar en `.1`.

La separación en subredes crea un lugar donde aplicar políticas de enrutamiento y filtrado, pero no constituye automáticamente un límite de seguridad. Si se permite el reenvío sin una política restrictiva, los hosts de distintas subredes aún pueden comunicarse.

:::single-choice{#subnets-security-boundary}
¿Crear dos subredes bloquea automáticamente el tráfico entre ellas?

::option[Sí, porque los routers no pueden conectar prefijos distintos.]{#subnets-never-route explanation="Conectar prefijos es la función principal del enrutamiento."}
::option[No; las políticas de enrutamiento y filtrado determinan el tráfico permitido.]{#subnets-policy-required .correct explanation="La segmentación permite aplicar políticas, pero no las define por sí sola."}
::option[Sí, salvo que ambas utilicen la dirección de host `.1`.]{#subnets-dot-one-security explanation="Una convención de números de host no controla el reenvío."}
:::

## Motivos para crear subredes

La división en subredes puede organizar la asignación de direcciones, limitar el ámbito de broadcast de la capa de enlace, separar dominios de fallo y proporcionar límites para las políticas. También puede añadir complejidad de enrutamiento, cortafuegos, DHCP, supervisión y documentación. Diseña los prefijos en función de los requisitos reales de escala, crecimiento, redundancia y seguridad, no suponiendo que una red más pequeña siempre sea más rápida.

:::single-choice{#subnets-design-tradeoff}
¿Cuál es una verdadera contrapartida de dividir en subredes?

::option[Los dominios de broadcast más pequeños no requieren enrutamiento ni documentación.]{#subnets-no-complexity explanation="Más límites suelen exigir gestionar más rutas, políticas, direcciones y servicios."}
::option[La segmentación puede mejorar la organización y, a la vez, aumentar la complejidad de las políticas.]{#subnets-tradeoff .correct explanation="Los límites de las subredes pueden ayudar al control, pero añaden estado operativo que debe mantenerse."}
::option[Todas las subredes garantizan la misma latencia hacia Internet.]{#subnets-equal-latency explanation="Las condiciones de la ruta y de la carga de trabajo determinan la latencia."}
:::

## Resumen

Ahora puedes relacionar un prefijo IPv4 con la entrega local y las políticas de enrutamiento.

1. Expresa máscaras contiguas mediante longitudes de prefijo CIDR.
2. Calcula el prefijo de red a partir de los bits de la dirección y la máscara.
3. Usa las rutas para determinar la entrega en el enlace o mediante un siguiente salto.
4. Trata el aislamiento por subredes como una oportunidad para aplicar políticas, no como una garantía.
