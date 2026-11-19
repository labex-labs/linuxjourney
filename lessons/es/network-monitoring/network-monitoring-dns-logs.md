---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "es"
order_index: 3
title: "Registros DNS"
description: "Aprende a distinguir una consulta DNS, su respuesta y una conexión posterior de la aplicación."
meta_title: "Registros DNS - Monitorización de redes"
meta_description: "Aprende a distinguir una consulta DNS, su respuesta y una conexión posterior de la aplicación."
meta_keywords: "registros DNS, monitorización de redes, ciberseguridad, Linux Journey"
---

Antes de conectarse a un servicio por su nombre, un cliente puede pedir a DNS una dirección. Un **resolvedor** busca nombres para los clientes y puede registrar la consulta y su resultado.

## Identificar la consulta

Un registro DNS puede contener la hora, la dirección del cliente, el nombre consultado y el tipo de registro solicitado. Una consulta de tipo `A` pide una dirección IPv4.

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

El primer resultado contiene una dirección para `site.example`. El segundo indica que DNS no encontró ningún nombre que coincidiera con `preview.example` en esa consulta.

:::single-choice{#network-monitoring-dns-logs-lookup-name} ¿Qué fila devolvió una dirección IPv4 para el nombre solicitado?

::option[La consulta de site.example.]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="Esa fila incluye una respuesta que contiene una dirección IPv4."}
::option[La consulta de preview.example.]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN indica que el nombre consultado no existe según la información a la que tuvo acceso el resolvedor."}
::option[Ambas filas, porque tienen el mismo cliente.]{#network-monitoring-dns-logs-lookup-name-c explanation="El cliente es el mismo, pero las consultas tienen resultados distintos."}
:::

## Interpretar el resultado

`NOERROR` significa que el intercambio de DNS no indicó un error de protocolo. Comprueba también el campo de respuesta. Una respuesta puede indicar `NOERROR` y no contener ningún registro de dirección del tipo solicitado. Una consulta fallida también puede aparecer con otro resultado, como un tiempo de espera agotado registrado por el cliente.

:::single-choice{#network-monitoring-dns-logs-no-answer} Una fila de DNS dice NOERROR, pero la respuesta no incluye una dirección. ¿Qué debes informar?

::option[El cliente recibió necesariamente una dirección IPv4.]{#network-monitoring-dns-logs-no-answer-a explanation="El campo de respuesta indica qué direcciones se devolvieron en la muestra."}
::option[El sitio rechazó con seguridad una conexión del navegador.]{#network-monitoring-dns-logs-no-answer-c explanation="Esta fila registra el resultado de DNS. Las peticiones del navegador se consultan por separado."}
::option[El intercambio terminó sin error de protocolo y esta fila no contiene una dirección.]{#network-monitoring-dns-logs-no-answer-b .correct explanation="El resultado y el campo de respuesta aportan datos distintos."}
:::

## Comprobar por separado si hubo una conexión

Un cliente puede consultar un nombre y luego decidir si se conecta. Para comprobar si hubo conexión, busca un registro de flujo o de conexión que coincida. Compara el extremo de la conexión y la hora. Los resultados de DNS pueden guardarse en caché, así que algunas conexiones pueden ocurrir sin que conste una consulta nueva en los registros disponibles.

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} ¿Qué mostraría mejor que un cliente se conectó después a la dirección recibida?

::option[Volver a consultar únicamente la respuesta DNS.]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="La respuesta indica una dirección que el cliente puede usar."}
::option[Un registro de conexión o flujo correspondiente que indique el destino.]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="Ese registro permite seguir el tráfico posterior por separado de la consulta."}
::option[Una segunda consulta DNS del mismo cliente.]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="Otra consulta confirma que el cliente hizo más de una resolución de nombres. La conexión posterior de la aplicación queda sin verificar."}
:::

## Resumen

Ya puedes distinguir lo que muestra un registro DNS de la actividad posterior en la red.

1. Identifica el cliente, la consulta y el tipo de registro solicitado.
2. Interpreta juntos el resultado y la respuesta.
3. Busca un registro independiente de la conexión posterior.
