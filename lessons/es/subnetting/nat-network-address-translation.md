---
lesson_id: "nat-network-address-translation"
course_id: "subnetting"
lang: "es"
order_index: 6
title: "NAT"
description: "Aprende cómo las traducciones de origen, destino y puertos modifican los flujos IPv4 y el estado de las conexiones."
meta_title: "NAT - Subnetting"
meta_description: "Aprende qué es NAT, o traducción de direcciones de red, cómo funciona en Linux y qué función desempeña. Comprende las direcciones IP privadas y públicas con esta guía de redes Linux."
meta_keywords: "NAT, traducción de direcciones de red, redes Linux, IP privada, IP pública, tutorial Linux, guía para principiantes"
---

La traducción de direcciones de red reescribe campos de direcciones y, a menudo, puertos de transporte cuando los paquetes atraviesan un dispositivo traductor. Se utiliza ampliamente para conectar redes IPv4 con direcciones privadas mediante un conjunto más pequeño de direcciones enrutables externamente.

## Traducción de origen

NAT de origen sustituye la dirección de origen de un paquete cuando sale de una red. Las implantaciones de muchos a uno también traducen los puertos de origen para que varios flujos internos puedan compartir una dirección externa. Esta modalidad que tiene en cuenta los puertos suele llamarse NAPT, PAT o enmascaramiento cuando la dirección externa puede cambiar.

El traductor mantiene las correspondencias para poder volver a traducir los paquetes de respuesta al punto final interno original. Normalmente reenvía el mismo flujo de transporte; no tiene que abrir una conexión proxy independiente como haría un proxy de aplicación.

:::single-choice{#nat-source-translation} ¿Qué cambia NAT de origen en un paquete saliente?

::option[Únicamente los permisos de archivo de la aplicación de destino.]{#nat-file-permissions explanation="NAT opera sobre las cabeceras de red y transporte, no sobre sistemas de archivos remotos."}
::option[La dirección de origen y, en el uso de muchos a uno, normalmente también el puerto de origen.]{#nat-source-fields .correct explanation="La correspondencia permite asociar el tráfico de retorno con el flujo interno original."}
::option[El nombre DNS almacenado permanentemente por el cliente.]{#nat-dns-name explanation="La traducción no reescribe la base de datos de servicios de nombres del cliente."}
:::

## Traducción de destino

NAT de destino reescribe la dirección o el puerto de destino, normalmente para publicar un servicio interno mediante un punto final externo. Una regla de reenvío de puertos puede asignar un puerto TCP externo a otra dirección y puerto internos. El tráfico de retorno necesita una traducción inversa coherente.

:::single-choice{#nat-port-forward} ¿Qué modalidad de NAT suele implementar un reenvío de puertos entrante?

::option[Únicamente NAT de origen, antes de consultar la ruta.]{#nat-snat-port-forward explanation="Publicar un destino interno requiere traducir los campos del destino."}
::option[Ninguna traducción de direcciones o puertos.]{#nat-no-translation explanation="Una regla de reenvío de puertos es, por definición, una política de traducción."}
::option[NAT de destino.]{#nat-dnat .correct explanation="DNAT asigna el destino externo al punto final seleccionado del servicio interno."}
:::

## NAT y la política del cortafuegos

NAT no es un cortafuegos. Un traductor con estado puede carecer de una correspondencia para tráfico entrante no solicitado, pero el reenvío explícito, la traducción de destino, el filtrado y la exposición de las aplicaciones determinan qué es accesible. La política de seguridad debe expresarse y auditarse mediante reglas de cortafuegos, servicios con privilegios mínimos y controles de extremo a extremo, no deducirse de la reescritura de direcciones.

:::single-choice{#nat-not-firewall} ¿Por qué no debe tratarse NAT como una política de seguridad por sí sola?

::option[NAT cifra automáticamente todas las cargas útiles.]{#nat-encrypts explanation="La traducción de direcciones no proporciona confidencialidad de la carga útil."}
::option[Las reglas de traducción y las reglas de filtrado del tráfico tienen finalidades distintas.]{#nat-filter-separate .correct explanation="La accesibilidad y la autorización requieren políticas explícitas de filtrado y de servicios incluso cuando existe traducción."}
::option[NAT impide que los administradores definan reglas de cortafuegos.]{#nat-prevents-firewall explanation="La traducción y las políticas de cortafuegos suelen coexistir."}
:::

## Consecuencias operativas

NAT puede agotar las correspondencias de direcciones y puertos, complicar los protocolos entre pares, ocultar a las aplicaciones los orígenes reales y exigir un tratamiento especial para los protocolos que incorporan direcciones. Los registros deben conservar las marcas de tiempo y los detalles de las correspondencias de traducción si es necesario rastrear los flujos.

En Linux, las políticas modernas suelen configurarse mediante nftables y seguimiento de conexiones. Inspecciona el conjunto de reglas real antes de cambiarlo:

```bash
$ sudo nft list ruleset
$ sudo conntrack -L
```

El segundo comando requiere las herramientas conntrack y privilegios. Los cambios en el conjunto de reglas pueden interrumpir el acceso remoto, así que utiliza recuperación mediante consola, configuración atómica, validación y reversión.

:::single-choice{#nat-trace-flow} ¿Qué pruebas se necesitan para rastrear un flujo de dirección compartida hasta un cliente interno?

::option[Únicamente la dirección externa, sin hora ni puerto.]{#nat-address-only explanation="Muchos clientes y flujos pueden compartir esa dirección."}
::option[Únicamente el nombre de host que muestra el cliente.]{#nat-hostname-only explanation="El traductor asigna tuplas de paquetes, no necesariamente nombres de host."}
::option[Una correspondencia de traducción correlacionada temporalmente que incluya el protocolo y los puertos.]{#nat-correlated-mapping .correct explanation="La tupla completa y la marca de tiempo distinguen los flujos traducidos simultáneos."}
:::

## Resumen

Ahora puedes distinguir la traducción de direcciones del enrutamiento, los proxies y las políticas del cortafuegos.

1. Identifica la traducción de origen en los flujos salientes.
2. Identifica la traducción de destino en los servicios publicados.
3. Comprende cómo las correspondencias de puertos permiten compartir direcciones.
4. Aplica un filtrado explícito en lugar de tratar NAT como seguridad.
5. Conserva las pruebas de las correspondencias y el acceso de recuperación durante los cambios.
