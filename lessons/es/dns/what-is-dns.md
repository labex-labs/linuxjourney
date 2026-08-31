---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "es"
order_index: 1
title: "¿Qué es DNS?"
description: "Aprende cómo DNS organiza y resuelve nombres distribuidos y registros de recursos con tipos."
meta_title: "¿Qué es DNS? - DNS"
meta_description: "Comprender DNS es esencial para aprender redes Linux. Esta guía explica qué es el Sistema de nombres de dominio, cómo relaciona nombres con direcciones IP y por qué constituye una infraestructura fundamental de Internet."
meta_keywords: "DNS, sistema de nombres de dominio, dirección IP, aprender linux, aprendizaje linux, nombre de host, redes Linux, principiante, tutorial, guía, labex linux"
---

El Sistema de nombres de dominio es una base de datos distribuida y jerárquica, además de un protocolo de consultas. Permite que los clientes recuperen información con tipos asociada a nombres, incluidas direcciones, enrutamiento de correo, servidores autoritativos, datos de servicios y registros de verificación.

## Nombres y registros de recursos

DNS hace algo más que traducir un nombre de host en una dirección IP. Un registro `A` contiene una dirección IPv4, `AAAA` una dirección IPv6, `MX` datos de enrutamiento de correo, `NS` nombres de servidores autoritativos, y muchos otros tipos transportan datos distintos. Un nombre puede tener varios registros o no tener ningún registro de dirección.

:::single-choice{#dns-purpose-beyond-address}
¿Por qué DNS es algo más que una lista de nombres de host y direcciones?

::option[Asigna permanentemente direcciones MAC a todas las tramas Ethernet.]{#dns-mac-frames explanation="El descubrimiento de vecinos de la capa de enlace no utiliza DNS de esta manera."}
::option[Almacena registros con tipos para varias clases de datos de servicios y delegación.]{#dns-typed-records .correct explanation="Los registros de direcciones, correo, autoridad, alias y políticas tienen semánticas distintas."}
::option[Garantiza que todas las aplicaciones con nombre funcionen correctamente.]{#dns-health-guarantee explanation="Los datos DNS pueden resolverse aunque el servicio de destino no esté disponible."}
:::

## Nombres jerárquicos

Un nombre de dominio completo identifica una ruta en el árbol DNS. En `www.example.com.`, el punto final representa la raíz, `com` está debajo de ella, `example` está debajo de `com` y `www` es un nombre dentro de ese dominio. El punto final suele omitirse en las interfaces de usuario, pero importa al distinguir nombres absolutos de nombres localmente relativos en la configuración.

:::single-choice{#dns-trailing-dot}
¿Qué representa el punto final de `www.example.com.`?

::option[La raíz DNS y un nombre absoluto.]{#dns-root-dot .correct explanation="El punto termina la ruta completa desde el nodo indicado hasta la raíz."}
::option[Un comodín para todos los dominios de nivel superior.]{#dns-dot-wildcard explanation="Un comodín utiliza una etiqueta como `*`, no el terminador de la raíz."}
::option[Una instrucción para utilizar únicamente IPv4.]{#dns-dot-ipv4 explanation="El tipo de registro controla la familia de direcciones solicitada."}
:::

## Autoridad distribuida

La autoridad DNS se delega hacia abajo en la jerarquía. Los servidores raíz dirigen los resolvers a los servidores de los dominios de nivel superior, que a su vez los dirigen a los servidores autoritativos de las zonas delegadas. Las organizaciones gestionan sus propios datos autoritativos sin almacenar todo el espacio de nombres global en un único servidor central.

:::single-choice{#dns-authoritative-data}
¿Quién proporciona los datos definitivos de una zona DNS delegada?

::option[Cualquier navegador que haya visitado antes el sitio.]{#dns-browser-authority explanation="La caché de un navegador no es autoritativa para la zona."}
::option[Los servidores de nombres autoritativos configurados para la zona.]{#dns-authoritative-servers .correct explanation="La delegación identifica los servidores responsables de responder de forma autoritativa."}
::option[Todos los routers que transportan un paquete hacia la dirección.]{#dns-router-authority explanation="El reenvío de paquetes y la autoridad DNS son funciones independientes."}
:::

## Resolución y caché

El resolver stub de un host suele enviar una consulta a un resolver recursivo. Este puede responder desde una caché válida o consultar la jerarquía en nombre del cliente. Los TTL de los registros limitan durante cuánto tiempo pueden reutilizarse normalmente las entradas de la caché, lo que mejora la escalabilidad pero retrasa la visibilidad de los cambios hasta que se actualizan las cachés.

Que DNS funcione no demuestra la salud de la ruta, el transporte, TLS o la aplicación. Un fallo de DNS también puede producirse antes de cualquier consulta externa, porque `/etc/hosts`, los sufijos de búsqueda, las cachés locales o la política de servicios de nombres afectan al resolver del sistema.

:::single-choice{#dns-cache-ttl-role}
¿Qué controla principalmente el TTL de un registro DNS?

::option[Cuántos routers puede atravesar un paquete IP.]{#dns-ip-hop-limit explanation="El TTL o Hop Limit de IP es otro campo de protocolo."}
::option[Durante cuánto tiempo debe funcionar correctamente la aplicación.]{#dns-app-health-time explanation="La caché DNS no garantiza la disponibilidad del servicio."}
::option[Durante cuánto tiempo puede un resolver guardar normalmente el registro en caché.]{#dns-cache-lifetime .correct explanation="Una caché más corta o más larga afecta a la carga de consultas y a la propagación de cambios."}
:::

## Resumen

Ahora puedes describir DNS como un sistema jerárquico de datos con tipos y caché.

1. Distingue los tipos de registros de recursos DNS según su finalidad.
2. Interpreta un nombre completo desde la raíz hacia abajo.
3. Identifica la delegación y la responsabilidad autoritativa.
4. Separa la resolución de nombres de la conectividad de la aplicación.
