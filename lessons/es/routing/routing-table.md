---
lesson_id: "routing-table"
course_id: "routing"
lang: "es"
order_index: 2
title: "Tabla de enrutamiento"
description: "Aprende a interpretar rutas de Linux e inspeccionar la ruta seleccionada para un destino."
meta_title: "Tabla de enrutamiento - Routing"
meta_description: "Guía para comprender la tabla de enrutamiento de Linux. Aprende a interpretar la salida del comando route, incluidos destino, gateway, genmask y la interfaz eth0. Domina los fundamentos de las rutas Linux."
meta_keywords: "tabla de enrutamiento linux, tabla de rutas linux, genmask, eth0, comando route, enrutamiento de red, enrutamiento IP, destino, puerta de enlace, máscara de subred, redes linux"
---

El estado de enrutamiento de Linux determina qué siguiente salto, interfaz y origen son válidos para un destino IP. La vista antigua `route -n` aún se encuentra, pero `ip route` expone de forma más directa los conceptos modernos de enrutamiento del kernel.

## Interpretar rutas IPv4

Una salida de ejemplo puede tener este aspecto:

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

La ruta conectada `/24` envía los destinos coincidentes directamente por `eth0`. La ruta predeterminada utiliza la puerta de enlace del siguiente salto `192.168.224.2`. `proto` describe cómo se instaló la ruta, `src` es un origen preferido para el tráfico coincidente y una métrica ayuda a ordenar rutas comparables en los demás aspectos.

:::single-choice{#routing-table-via-meaning} ¿Qué indica `via 192.168.224.2`?

::option[La única aplicación autorizada para utilizar la ruta.]{#routing-table-application explanation="La autorización de aplicaciones no está codificada mediante la palabra clave `via`."}
::option[La puerta de enlace del siguiente salto de la ruta.]{#routing-table-next-hop .correct explanation="El paquete se encapsula para ese router situado en el enlace, pero conserva su destino IP."}
::option[El punto de montaje del sistema de archivos de la ruta.]{#routing-table-mount explanation="Las entradas de enrutamiento se ocupan del reenvío de red, no de los sistemas de archivos."}
:::

## Rutas conectadas y predeterminadas

Una ruta con `scope link` y sin un siguiente salto `via` trata el prefijo como directamente accesible en la interfaz. Una ruta predeterminada coincide con todas las direcciones, pero pierde frente a cualquier ruta válida más específica.

:::single-choice{#routing-table-connected-route} ¿Cómo se llega normalmente a un destino conectado con `scope link`?

::option[A través de la puerta de enlace predeterminada incluso cuando coincide una ruta conectada.]{#routing-table-connected-default explanation="El prefijo conectado es más específico y no tiene un operando de puerta de enlace."}
::option[Convirtiendo el destino en un servidor DNS.]{#routing-table-connected-dns explanation="El servicio de nombres no forma parte de una ruta IP ya seleccionada."}
::option[Directamente mediante la interfaz indicada después de resolver el vecino.]{#routing-table-direct .correct explanation="El host resuelve la dirección del destino en el enlace y encapsula el tráfico localmente."}
:::

## Longitud del prefijo y métrica

La selección de rutas tiene en cuenta las reglas de política y elige el prefijo válido más largo. Las métricas ordenan las rutas dentro de conjuntos comparables apropiados; una ruta predeterminada con una métrica baja no prevalece sobre un `/24` coincidente solo porque su número sea menor.

:::single-choice{#routing-table-prefix-before-default} ¿Qué ruta suele coincidir de forma más específica con `192.168.224.50`?

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="El prefijo coincidente de 24 bits es el más largo de las rutas mostradas."}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="La ruta predeterminada tiene una longitud de prefijo de cero."}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="Esta abarca la dirección, pero fija menos bits que `/24`."}
:::

## Reglas de política y varias tablas

Linux puede consultar varias tablas de enrutamiento según las políticas de `ip rule`, basadas en el origen, la marca, la interfaz u otros selectores. Por tanto, consultar solo la tabla principal puede no mostrar la ruta real:

```bash
$ ip rule show
$ ip route show table all
```

Los espacios de nombres de red y las VRF también pueden contener estados independientes. Realiza la inspección en el mismo contexto que el proceso afectado.

:::single-choice{#routing-table-policy-limit} ¿Por qué puede que `ip route show` por sí solo no explique la ruta de una aplicación?

::option[Las reglas de política u otro espacio de nombres de red pueden seleccionar un estado de enrutamiento distinto.]{#routing-table-policy-context .correct explanation="La consulta efectiva depende de los atributos del paquete y del contexto de red del proceso."}
::option[Las tablas de enrutamiento de Linux no contienen prefijos de destino.]{#routing-table-no-prefixes explanation="Los prefijos de destino son claves fundamentales de las rutas."}
::option[Las aplicaciones nunca envían paquetes IP.]{#routing-table-apps-never explanation="El tráfico de las aplicaciones se transporta mediante protocolos de red y transporte."}
:::

## Consultar una ruta efectiva

Pide al kernel que evalúe un destino y un origen opcional:

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

El resultado predice la consulta local en ese momento. No envía una prueba ni demuestra la accesibilidad de vecinos, elementos posteriores, cortafuegos o aplicaciones.

:::single-choice{#routing-table-route-get-limit} ¿Qué no hace `ip route get`?

::option[Mostrar la interfaz local y el siguiente salto elegidos.]{#routing-table-get-does-interface explanation="Esos son campos principales del resultado de la consulta."}
::option[Evaluar la política actual de rutas locales para un destino.]{#routing-table-get-does-policy explanation="El comando realiza una consulta de rutas del kernel."}
::option[Demostrar que la entrega tiene éxito a través de todos los saltos posteriores.]{#routing-table-get-not-probe .correct explanation="Es una consulta de decisión local, no una prueba de red de extremo a extremo."}
:::

## Resumen

Ahora puedes interpretar entradas de enrutamiento de Linux y consultar la decisión local efectiva.

1. Distingue las rutas conectadas de las rutas que pasan por una puerta de enlace.
2. Interpreta los campos de prefijo, interfaz, protocolo, origen y métrica.
3. Aplica la coincidencia del prefijo más largo antes de comparar las métricas pertinentes.
4. Ten en cuenta las tablas de políticas, los espacios de nombres y las VRF.
5. Trata `ip route get` como una consulta, no como una prueba de accesibilidad.
