---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "es"
order_index: 2
title: "Flujos de red"
description: "Aprende a interpretar las direcciones, los puertos, los tiempos y el recuento de bytes en un resumen de flujo."
meta_title: "Flujos de red - Monitorización de redes"
meta_description: "Aprende a interpretar las direcciones, los puertos, los tiempos y el recuento de bytes en un resumen de flujo."
meta_keywords: "flujos de red, monitorización de redes, ciberseguridad, Linux Journey"
---

Un **flujo** agrupa el tráfico que comparte propiedades como las direcciones de red, los puertos y el protocolo. Los sistemas de monitorización pueden contar los bytes o paquetes de un flujo sin guardar todo su contenido.

## Identificar los dos extremos

En este resumen simulado, el sistema de recogida de datos registra el sentido del tráfico desde el origen hasta el destino. Los protocolos de transporte como TCP incluyen números de puerto que pueden identificar un servicio en escucha en el extremo receptor.

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

La primera línea corresponde al tráfico hacia el puerto 443. La segunda muestra el sentido inverso. Algunos sistemas de recogida agrupan ambos sentidos, así que comprueba qué formato estás leyendo.

:::single-choice{#network-monitoring-flows-endpoint-direction} En la primera fila, ¿qué dirección y puerto reciben el tráfico registrado?

::option[192.0.2.10:51600.]{#network-monitoring-flows-endpoint-direction-a explanation="Ese es el extremo desde el que se envía el tráfico en el primer sentido."}
::option[Ambos extremos de la lista son destinos.]{#network-monitoring-flows-endpoint-direction-c explanation="Cada fila de esta muestra registra un solo sentido del tráfico."}
::option[192.0.2.20:443.]{#network-monitoring-flows-endpoint-direction-b .correct explanation="El campo de destino indica adónde se envió el tráfico."}
:::

## Comparar los recuentos

La muestra indica más bytes en el sentido que sale del puerto 443. Una respuesta más grande puede ser normal en una página web. El recuento por sí solo no indica el contenido de la página, la cuenta ni el motivo de ese volumen.

:::single-choice{#network-monitoring-flows-byte-count} ¿Qué significan los 8200 bytes de la segunda fila?

::option[El texto exacto del mensaje de respuesta.]{#network-monitoring-flows-byte-count-b explanation="El resumen de flujo indica el volumen y omite el mensaje."}
::option[La cantidad registrada en ese sentido.]{#network-monitoring-flows-byte-count-a .correct explanation="El recuento de bytes resume el tráfico y el origen y el destino indican su sentido."}
::option[La garantía de que la página se cargó correctamente.]{#network-monitoring-flows-byte-count-c explanation="El volumen no indica el resultado HTTP."}
:::

## Añadir contexto

Usa lo que sepas del servicio y la hora para determinar qué flujos son pertinentes. Si necesitas saber qué devolvió el servidor web, compara el flujo con sus registros de acceso para la misma hora y conexión, si están disponibles.

:::single-choice{#network-monitoring-flows-next-source} Quieres saber el estado HTTP de la petición web. ¿Qué otra fuente te ayudaría?

::option[Un registro de acceso web correspondiente a la petición.]{#network-monitoring-flows-next-source-c .correct explanation="El registro de acceso del servidor puede indicar el resultado HTTP."}
::option[El recuento de bytes del flujo redondeado a la centena más cercana.]{#network-monitoring-flows-next-source-a explanation="El redondeo cambia la precisión y no aporta el estado de la respuesta."}
::option[Otro resumen de flujo para los mismos extremos.]{#network-monitoring-flows-next-source-b explanation="Un resumen de flujo puede confirmar más observaciones del tráfico. Por lo general, no indica el estado de la respuesta HTTP."}
:::

## Resumen

Ya puedes interpretar los campos principales de un resumen de flujo.

1. Identifica las direcciones y los puertos de los extremos.
2. Interpreta el recuento de bytes en el sentido indicado.
3. Elige otra fuente cuando necesites saber el resultado de una operación de la aplicación.
