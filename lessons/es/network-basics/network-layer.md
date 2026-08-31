---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "es"
order_index: 7
title: "Capa de red"
description: "Aprende cómo el direccionamiento IP, los prefijos, las tablas de enrutamiento y los límites de saltos mueven paquetes entre redes."
meta_title: "Capa de red - Network Basics"
meta_description: "Explora la capa de red en Linux. Esta guía explica cómo las direcciones IP y las subredes permiten enrutar paquetes para transmitir datos entre redes."
meta_keywords: "capa de red, direcciones IP, subredes, redes Linux, enrutamiento de paquetes, transmisión de datos, modelo OSI, paquete IP"
---

La capa de red proporciona direccionamiento lógico y entrega de paquetes de mejor esfuerzo a través de redes interconectadas. En la suite de protocolos de Internet, IPv4 e IPv6 transportan paquetes mientras los routers eligen el siguiente salto hacia cada destino.

## Paquetes IP

Una cabecera IP incluye las direcciones de origen y destino, además de los campos necesarios para el reenvío y el procesamiento del protocolo. La carga útil suele contener un segmento TCP, un datagrama UDP o un mensaje ICMP. IP no garantiza la llegada, el orden ni la ausencia de duplicados.

:::single-choice{#network-layer-ip-service}
¿Qué servicio de entrega proporciona IP por sí solo?

::option[Confirmaciones garantizadas de las transacciones de las aplicaciones.]{#network-layer-guaranteed-commit explanation="El resultado de una entrega IP no puede demostrar la persistencia en una aplicación."}
::option[Entrega de paquetes de mejor esfuerzo.]{#network-layer-best-effort .correct explanation="Las capas superiores o las aplicaciones añaden la recuperación o el orden que necesiten."}
::option[La reserva permanente de un cable físico.]{#network-layer-cable-reservation explanation="El reenvío de paquetes no reserva una ruta física dedicada."}
:::

## Prefijos y subredes

Una dirección y una longitud de prefijo definen qué bits iniciales forman un prefijo de red. Los hosts utilizan esta información y sus rutas para decidir si un destino está en el enlace o necesita un router como siguiente salto. Una subred es un intervalo de direcciones bajo un prefijo y una política; las subredes no se conectan automáticamente con todas las demás.

:::single-choice{#network-layer-prefix-decision}
¿Qué ayuda a un host a decidir si un destino IPv4 está en el enlace?

::option[La contraseña de la aplicación del destino.]{#network-layer-password explanation="Los datos de autenticación no definen los prefijos de red."}
::option[El color del cable Ethernet.]{#network-layer-cable-color explanation="El aspecto del cable no tiene ningún significado de direccionamiento."}
::option[Sus prefijos configurados y su tabla de enrutamiento.]{#network-layer-prefix-routes .correct explanation="El host compara los destinos con las rutas, incluidos los prefijos conectados."}
:::

## Decisiones de enrutamiento

Linux consulta las políticas y tablas de enrutamiento para seleccionar una interfaz de salida, un siguiente salto y la información de origen preferida. Entre las rutas que cumplen las demás condiciones, normalmente se prefiere el prefijo coincidente más específico. Inspecciona la decisión real para un destino con:

```bash
$ ip route get 203.0.113.10
```

Esta es una consulta de ruta local, no demuestra que todos los routers posteriores tengan una ruta válida ni que el destino acepte tráfico.

:::single-choice{#network-layer-longest-prefix}
¿Qué ruta suele imponerse entre las rutas válidas hacia el mismo destino?

::option[La ruta cuyo nombre de interfaz aparece primero alfabéticamente.]{#network-layer-alphabetical explanation="La ortografía de la interfaz no es la regla de selección."}
::option[La ruta más antigua, independientemente de su prefijo.]{#network-layer-oldest explanation="La antigüedad por sí sola no prevalece sobre la coincidencia de prefijos."}
::option[La ruta con el prefijo coincidente más específico.]{#network-layer-most-specific .correct explanation="La coincidencia del prefijo más largo elige la ruta que abarca el intervalo de direcciones coincidente más estrecho."}
:::

## Límites de saltos y cambios durante el reenvío

Cada paquete IPv4 tiene un TTL y cada paquete IPv6 un Hop Limit. Los routers lo reducen; cuando llega a cero, descartan el paquete y pueden enviar un error ICMP. Esto evita que los bucles de enrutamiento circulen indefinidamente.

Normalmente, los routers conservan las direcciones IP de extremo a extremo, pero NAT, los túneles, los proxies y otros dispositivos intermedios pueden transformar o envolver los paquetes. Las cabeceras de la capa de enlace cambian en cada salto enrutado en cualquier caso.

:::single-choice{#network-layer-hop-limit}
¿Por qué reducen los routers el TTL o Hop Limit?

::option[Para aumentar los permisos de archivo de la aplicación.]{#network-layer-hop-permissions explanation="El recuento de saltos no está relacionado con la autorización del sistema de archivos."}
::option[Para convertir todos los paquetes de IPv4 a IPv6.]{#network-layer-hop-convert explanation="La traducción de protocolos no es la finalidad del campo."}
::option[Para impedir que los paquetes circulen en bucle para siempre.]{#network-layer-prevent-loop .correct explanation="Un número finito de saltos garantiza que un bucle de enrutamiento persistente acabe descartando el paquete."}
:::

## Resumen

Ahora puedes explicar cómo selecciona un host IP el siguiente paso hacia un destino.

1. Trata la entrega IP como de mejor esfuerzo.
2. Usa prefijos y rutas para distinguir destinos en el enlace y enrutados.
3. Aplica la coincidencia del prefijo más largo a la selección de rutas.
4. Reconoce cómo los límites de saltos acotan los bucles de reenvío.
