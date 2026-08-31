---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "es"
order_index: 3
title: "traceroute"
description: "Aprende cómo traceroute descubre los saltos que responden y cómo interpretar huecos, tiempos y variaciones de ruta."
meta_title: "traceroute - Resolución de problemas"
meta_description: "Domina la orden traceroute de Linux para rastrear rutas de red y diagnosticar problemas de conectividad. Aprende cómo utiliza TTL para descubrir el camino hacia un destino."
meta_keywords: "traceroute, traceroute Linux, redes Linux, resolución de problemas de red, TTL, enrutamiento de paquetes, órdenes Linux, principiantes, tutorial"
---

`traceroute` envía pruebas con valores crecientes de TTL de IPv4 o Hop Limit de IPv6. Los routers donde el valor caduca pueden devolver mensajes Time Exceeded, lo que revela algunos puntos de la ruta de ida que responden.

## Cómo funciona el descubrimiento de saltos

Las pruebas comienzan con un límite de un salto y lo incrementan. El primer router reduce el valor a cero y puede devolver un error ICMP. Un límite de dos llega al segundo router antes de caducar, y el proceso continúa hasta que el destino responde o se alcanza el máximo.

:::single-choice{#traceroute-expiring-field}
¿Qué campo hace que las pruebas sucesivas caduquen en routers posteriores?

::option[El TTL de la caché DNS del nombre de destino.]{#traceroute-dns-ttl explanation="La duración del registro DNS no controla los saltos de reenvío de los paquetes."}
::option[La dirección MAC Ethernet de origen.]{#traceroute-source-mac explanation="Las direcciones de enlace no transportan un contador de saltos de extremo a extremo."}
::option[El TTL de IPv4 o Hop Limit de IPv6.]{#traceroute-hop-field .correct explanation="Aumentar este contador limitado de reenvíos revela los saltos enrutados que responden."}
:::

## Métodos de prueba

El traceroute tradicional de Linux suele enviar pruebas UDP a puertos de destino altos. El destino puede señalar el final mediante ICMP Port Unreachable. Otras opciones utilizan pruebas ICMP Echo o TCP SYN, que pueden atravesar el filtrado de manera distinta:

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

Los privilegios y las opciones disponibles varían. Utiliza métodos autorizados para el destino y anota el método al comparar resultados.

:::single-choice{#traceroute-default-destination-response}
¿Qué suele poner fin a un traceroute UDP tradicional de Linux?

::option[Una respuesta ICMP Port Unreachable del destino.]{#traceroute-port-unreachable .correct explanation="Los puertos UDP altos normalmente no se utilizan, por lo que el destino puede identificarse mediante el error."}
::option[Una respuesta HTTP 200 obligatoria de cada router.]{#traceroute-http-every-router explanation="Los routers devuelven errores de control de red, no respuestas HTTP."}
::option[Una difusión Ethernet del destino a través de Internet.]{#traceroute-ethernet-broadcast explanation="Las difusiones de enlace no atraviesan rutas enrutadas."}
:::

## Interpretar los asteriscos

Un asterisco significa que no se observó una respuesta a esa prueba antes del tiempo de espera. El router puede reenviar tráfico en tránsito mientras filtra o limita la frecuencia de las respuestas de diagnóstico. Si responden saltos posteriores, está claro que el salto silencioso reenvió al menos algunas pruebas.

:::single-choice{#traceroute-asterisk-meaning}
¿Qué demuestra un `*` en un salto?

::option[Que el router descartó permanentemente todos los paquetes en tránsito.]{#traceroute-star-all-drop explanation="Las respuestas posteriores pueden demostrar que el reenvío continuó."}
::option[Únicamente que no llegó una respuesta coincidente antes del tiempo de espera.]{#traceroute-star-no-response .correct explanation="El filtrado, la limitación de frecuencia, la pérdida y los problemas de la ruta de retorno pueden producir silencio."}
::option[Que el destino no tiene dirección IP.]{#traceroute-star-no-address explanation="La prueba ya se dirige a una dirección y un salto silencioso no la elimina."}
:::

## Tiempos y variación de la ruta

Los tiempos por salto miden la ida y vuelta de las respuestas de control, no la latencia añadida por el enlace entre líneas impresas adyacentes. Los routers pueden dar menor prioridad a las respuestas del plano de control. El balanceo de carga puede enviar las pruebas por rutas distintas, y la resolución de nombres puede añadir retrasos a la presentación; `-n` evita las búsquedas inversas.

La ruta de retorno de cada respuesta ICMP puede diferir de la ruta de ida. Repite las pruebas y correlaciónalas con los tiempos de la aplicación en los extremos antes de identificar un cuello de botella.

:::single-choice{#traceroute-hop-rtt-limit}
¿Por qué no se deben restar los valores RTT de saltos adyacentes como si fueran la latencia exacta del enlace?

::option[Traceroute muestra todos los tiempos en bytes y no en milisegundos.]{#traceroute-times-bytes explanation="Los tiempos de las pruebas normalmente se muestran en milisegundos."}
::option[Las respuestas pueden utilizar rutas de retorno y procesamiento del plano de control diferentes.]{#traceroute-rtt-asymmetry .correct explanation="Las mediciones son recorridos independientes de ida y vuelta hasta cada salto, no muestras sincronizadas y unidireccionales de cada enlace."}
::option[Todos los routers tienen el mismo reloj que el origen.]{#traceroute-router-clock explanation="La medición no depende de sincronizar los relojes remotos."}
:::

## Comparar con la aplicación

Un traceroute puede alcanzar el destino mientras el servicio está bloqueado, y el servicio puede funcionar aunque los routers intermedios oculten sus respuestas. Prueba la misma familia de direcciones, destino, protocolo de transporte y puerto que la aplicación; después utiliza traceroute como evidencia complementaria sobre la ruta.

:::single-choice{#traceroute-service-proof}
¿Un traceroute completado demuestra que un servicio HTTPS funciona correctamente?

::option[Sí, porque cada salto valida el certificado del servidor.]{#traceroute-validates-cert explanation="Los routers no realizan la validación TLS del cliente."}
::option[No; el transporte, TLS y HTTP necesitan sus propias pruebas.]{#traceroute-not-app-proof .correct explanation="El descubrimiento de rutas y el estado de una aplicación son capas de diagnóstico diferentes."}
::option[Sí, pero solo si se muestran nombres DNS inversos.]{#traceroute-rdns-proof explanation="Los nombres no demuestran que una aplicación funcione."}
:::

## Resumen

Ahora puedes interpretar traceroute como una serie de pruebas con saltos limitados, no como un oráculo completo de la ruta.

1. Explica el descubrimiento de saltos mediante la caducidad de TTL o Hop Limit.
2. Anota si se utilizaron pruebas UDP, ICMP o TCP.
3. Trata los asteriscos como respuestas ausentes y no como caídas demostradas.
4. Evita deducir la latencia exacta de un enlace a partir de los RTT de saltos adyacentes.
5. Correlaciona la evidencia de la ruta con la aplicación real.
