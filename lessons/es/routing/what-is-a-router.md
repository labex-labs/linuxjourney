---
lesson_id: "what-is-a-router"
course_id: "routing"
lang: "es"
order_index: 1
title: "¿Qué es un router?"
description: "Aprende cómo los routers seleccionan siguientes saltos y reenvían paquetes IP entre redes."
meta_title: "¿Qué es un router? - Routing"
meta_description: "Guía para principiantes sobre qué es un router en redes. Aprende sobre enrutamiento, conmutación de paquetes, saltos y cómo los routers usan tablas de enrutamiento para reenviar datos entre redes."
meta_keywords: "router, redes, enrutamiento, saltos, conmutación de paquetes, redes Linux, tutorial para principiantes, guía de redes"
---

Un router conecta dominios de la capa de red y reenvía paquetes IP entre ellos. Un host Linux puede actuar como router cuando el reenvío está habilitado y sus interfaces, rutas, descubrimiento de vecinos y políticas de filtrado están configurados correctamente.

## Enrutamiento y reenvío

El enrutamiento construye o selecciona información sobre los prefijos accesibles. El reenvío aplica esa información a cada paquete: examina el destino, elige una ruta válida y un siguiente salto, reduce el límite de saltos y transmite por una interfaz de salida.

Son aspectos independientes de los planos de control y de datos. Puede existir una ruta mientras la política del cortafuegos bloquea el reenvío, o una interfaz de reenvío puede estar activa sin que exista una ruta válida.

:::single-choice{#router-forwarding-role}
¿Qué hace el reenvío de paquetes?

::option[Aplica la información de enrutamiento para enviar un paquete hacia su siguiente salto.]{#router-apply-route .correct explanation="El reenvío es la acción aplicada a cada paquete según la ruta y la política seleccionadas."}
::option[Crea un inicio de sesión permanente en la aplicación para todos los destinos.]{#router-create-login explanation="El enrutamiento no gestiona cuentas de aplicaciones remotas."}
::option[Copia todos los paquetes a todas las interfaces cuando no existe una ruta.]{#router-flood-no-route explanation="El reenvío IP ordinario descarta un paquete sin ruta en lugar de recurrir a una inundación similar a la de Ethernet."}
:::

## Tablas de enrutamiento y rutas predeterminadas

Una ruta asocia un prefijo de destino con una interfaz de salida, un siguiente salto, una métrica, una preferencia de origen u otros atributos. La coincidencia del prefijo más largo favorece una ruta válida más específica. Una ruta predeterminada, `/0` en IPv4 o `::/0` en IPv6, es la coincidencia menos específica y solo se utiliza cuando no gana ninguna ruta más específica.

Si no existe ninguna ruta válida, el router descarta el paquete y puede generar un mensaje ICMP de destino inaccesible. Una ruta predeterminada es opcional y no tiene por qué apuntar directamente a Internet público.

:::single-choice{#router-default-route}
¿Cuándo se selecciona una ruta predeterminada?

::option[Antes de comprobar cualquier prefijo específico del destino.]{#router-default-first explanation="Los prefijos válidos más específicos tienen prioridad."}
::option[Únicamente cuando el paquete es un broadcast Ethernet.]{#router-default-broadcast explanation="La selección de rutas IP se basa en destinos de la capa de red."}
::option[Cuando no coincide ninguna ruta válida más específica.]{#router-default-fallback .correct explanation="El prefijo de longitud cero es la ruta menos específica."}
:::

## Tráfico local y enrutado

Dos hosts de la misma subred en el enlace suelen intercambiar tramas sin enviar el paquete IP a través de un router. Un router interviene cuando la selección de ruta lo elige como siguiente salto o cuando la topología y la política fuerzan deliberadamente el recorrido enrutado.

Un «router» doméstico suele combinar un router IP, un conmutador Ethernet, un punto de acceso Wi-Fi, servicio DHCP, NAT y un cortafuegos. Cada función debe diagnosticarse por separado.

:::single-choice{#router-same-subnet-path}
¿Debe atravesar el router predeterminado el tráfico entre dos hosts situados en el mismo enlace?

::option[Sí, porque todos los paquetes deben llegar a un puerto WAN.]{#router-always-wan explanation="La entrega local en el enlace puede realizarse directamente."}
::option[Sí, salvo que ambos hosts tengan direcciones públicas.]{#router-public-required explanation="Que el ámbito sea público o privado no determina el reenvío básico en el enlace."}
::option[No; el emisor puede dirigirse directamente al destino en el enlace local.]{#router-direct-on-link .correct explanation="La tabla de enrutamiento identifica el prefijo conectado como situado en el enlace."}
:::

## Saltos y prevención de bucles

Un salto enrutado es un paso de reenvío en la capa de red. El TTL de IPv4 y el Hop Limit de IPv6 se reducen en cada router, lo que limita los bucles. La cantidad de saltos no es una medida completa de distancia o calidad: los enlaces difieren en ancho de banda, latencia, pérdidas, políticas y congestión.

:::single-choice{#router-hop-count-limit}
¿Qué no garantiza una cantidad menor de saltos?

::option[Que exista al menos un paso enrutado.]{#router-hop-exists explanation="Una cantidad positiva de saltos indica directamente un recorrido enrutado."}
::option[Una ruta de aplicación más rápida o mejor.]{#router-hop-not-quality .correct explanation="Menos routers aún pueden atravesar enlaces más lentos, congestionados o restringidos por políticas."}
::option[Que los campos de límite de saltos sean finitos.]{#router-hop-limit-finite explanation="Esos campos son finitos por diseño del protocolo."}
:::

## Resumen

Ahora puedes separar la selección de rutas de un router de su acción de reenvío.

1. Define los routers por el reenvío entre redes IP.
2. Distingue el enrutamiento del plano de control del reenvío del plano de datos.
3. Trata la ruta predeterminada como la alternativa menos específica.
4. Reconoce que la cantidad de saltos por sí sola no mide la calidad de la ruta.
