---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "es"
order_index: 2
title: "ping"
description: "Aprende a ejecutar pruebas ping acotadas y a interpretar respuestas, pérdidas, RTT, TTL y limitaciones."
meta_title: "ping - Resolución de problemas"
meta_description: "Aprende a utilizar la orden ping de Linux para probar la conectividad de red e interpretar icmp_seq, TTL y el tiempo de ida y vuelta."
meta_keywords: "ping Linux, conectividad de red, ICMP, TTL, orden ping, icmp_seq, secuencia ping, significado icmp_seq, redes Linux"
---

`ping` envía solicitudes ICMP Echo Request e informa de las respuestas observadas. Prueba una ruta de mensajes de control hacia una dirección; no demuestra que funcionen TCP, UDP, DNS, la autenticación ni una aplicación.

## Ejecutar una prueba acotada

Envía tres solicitudes IPv4 con un tiempo de espera de dos segundos por paquete en las implementaciones comunes de iputils:

```bash
$ ping -4 -c 3 -W 2 example.com
```

Utiliza `-6` para seleccionar IPv6. Anota la dirección resuelta porque un nombre de host puede devolver varias y distintas ejecuciones pueden elegir direcciones diferentes.

:::single-choice{#ping-count-option} ¿Qué solicita `-c 3`?

::option[Una carga útil de paquete de exactamente tres megabytes.]{#ping-three-megabytes explanation="El tamaño del paquete utiliza otra opción."}
::option[Tres rutas permanentes hacia el destino.]{#ping-three-routes explanation="Ping prueba tráfico y no instala rutas."}
::option[Tres Echo Request antes de que la orden termine normalmente.]{#ping-three-requests .correct explanation="Un número finito hace que el diagnóstico sea acotado y repetible."}
:::

## Secuencia y pérdida

`icmp_seq` identifica las solicitudes dentro de una ejecución. Las respuestas ausentes contribuyen a la pérdida observada, mientras que las respuestas desordenadas pueden reflejar retrasos variables. Las muestras pequeñas son ruidosas; compara varios intervalos acotados y la propia tasa de errores de la aplicación.

La pérdida puede producirse en cualquiera de las dos direcciones, y la limitación de frecuencia de ICMP puede hacer que la pérdida de ping difiera de la que experimenta la aplicación.

:::single-choice{#ping-sequence-gap} ¿Qué puede indicar la ausencia de una respuesta `icmp_seq`?

::option[Que el destino cambió permanentemente su dirección MAC.]{#ping-sequence-mac explanation="Un hueco en la secuencia no permite por sí solo llegar a esa conclusión sobre la capa de enlace."}
::option[Que la solicitud o la respuesta se perdió, se filtró, llegó después de la espera o se limitó por frecuencia.]{#ping-sequence-possibilities .correct explanation="El hueco identifica una respuesta no observada, pero no la dirección ni la causa exactas."}
::option[Que el disco de origen no tiene inodos libres.]{#ping-sequence-inodes explanation="El estado de los inodos del sistema de archivos no guarda relación con una respuesta de secuencia ICMP."}
:::

## Tiempo de ida y vuelta

El campo `time` es el tiempo de ida y vuelta, en milisegundos, desde que se envía la solicitud hasta que se recibe la respuesta. Combina el retraso de salida, el procesamiento remoto y el retraso de retorno. No puede revelar la latencia en un solo sentido sin mediciones sincronizadas en los extremos.

:::single-choice{#ping-rtt-meaning} ¿Qué mide un valor `time=23.7 ms`?

::option[Únicamente la latencia de la ruta de salida en un solo sentido.]{#ping-outbound-only explanation="Ping mide el intervalo completo de solicitud y respuesta."}
::option[El tiempo de actividad del sistema de destino.]{#ping-target-uptime explanation="El valor mide la prueba, no el tiempo desde el arranque."}
::option[El tiempo de ida y vuelta de ese eco.]{#ping-round-trip .correct explanation="Incluye ambas direcciones y el procesamiento del extremo."}
:::

## TTL o límite de saltos

El TTL de IPv4 o Hop Limit de IPv6 mostrado es el valor restante en la respuesta recibida. Sin conocer el valor inicial del emisor y la ruta de retorno, restarlo no proporciona un número exacto de saltos. Un cambio puede reflejar otro emisor, otro valor inicial u otra ruta de retorno.

:::single-choice{#ping-received-ttl} ¿Qué es el TTL mostrado en una respuesta Echo Reply de IPv4?

::option[El valor restante cuando la respuesta llegó al host local.]{#ping-remaining-ttl .correct explanation="Cada router de la ruta de retorno redujo el valor inicial del emisor."}
::option[Un número exacto de routers en ambas direcciones.]{#ping-exact-hop-count explanation="Este campo por sí solo no establece el TTL inicial ni la ruta en cada dirección."}
::option[La duración en caché del registro DNS.]{#ping-dns-ttl explanation="El TTL de DNS y el TTL de los paquetes IP son campos diferentes."}
:::

## Probar la capa correcta

Si ping funciona pero un servicio falla, prueba el puerto, TLS, el protocolo y la solicitud reales. Si ping falla, inspecciona la resolución de nombres, `ip route get`, el estado de los vecinos, la política del cortafuegos y las capturas antes de declarar caído el host.

:::single-choice{#ping-success-limit} ¿Qué no demuestra un ping correcto?

::option[Que funcionó alguna ruta de solicitud y respuesta ICMP.]{#ping-icmp-worked explanation="Esa es la evidencia directa que proporcionan las respuestas."}
::option[Que la respuesta contenía un número de secuencia.]{#ping-sequence-present explanation="La salida normal informa directamente de la secuencia de la respuesta."}
::option[Que la aplicación prevista acepta y completa solicitudes.]{#ping-app-not-proven .correct explanation="El comportamiento de la aplicación y el transporte requiere una prueba adecuada para esa aplicación."}
:::

## Resumen

Ahora puedes utilizar ping como una medición ICMP acotada con límites explícitos.

1. Selecciona la familia de direcciones y anota la dirección resuelta.
2. Acota el número de solicitudes y el tiempo de espera para obtener pruebas repetibles.
3. Interpreta la pérdida sin presuponer su dirección o causa.
4. Trata el RTT como bidireccional y el TTL como un valor restante.
5. Prueba por separado la aplicación real.
