---
lesson_id: "dns-components"
course_id: "dns"
lang: "es"
order_index: 2
title: "Componentes de DNS"
description: "Aprende cómo los resolvers recursivos, los servidores autoritativos, las zonas y los registros de recursos dividen las responsabilidades de DNS."
meta_title: "Componentes de DNS - DNS"
meta_description: "Aprende sobre los componentes de DNS: servidores de nombres, archivos de zona y registros de recursos. Comprende cómo funciona DNS con esta guía para principiantes."
meta_keywords: "componentes DNS, servidor de nombres, archivo de zona, registros de recursos, tutorial DNS, redes Linux, guía para principiantes"
---

DNS separa la función de recursión orientada al cliente de la publicación autoritativa. Comprender ese límite evita confundir una respuesta almacenada en caché con el propietario de una zona.

## Resolvers stub y recursivos

Un resolver stub de una aplicación o sistema operativo envía consultas a un resolver recursivo configurado. Este devuelve una respuesta final, un error o el resultado de una referencia después de utilizar la caché y, cuando sea necesario, realizar consultas iterativas. Su respuesta solo puede incluir el indicador de respuesta autoritativa cuando el servidor que responde tiene autoridad sobre los datos; la recursión por sí sola no lo convierte en autoritativo.

:::single-choice{#dns-components-recursive-role}
¿Qué hace un resolver recursivo por un cliente stub?

::option[Obtiene un resultado DNS final mediante la caché y otros servidores de nombres.]{#dns-components-recursive-result .correct explanation="El cliente delega en el servicio recursivo el trabajo de búsqueda de varios pasos."}
::option[Sustituye todos los routers de la ruta de los paquetes.]{#dns-components-replaces-router explanation="La resolución de nombres y el reenvío IP son aspectos independientes."}
::option[Se convierte en autoritativo para todos los registros que almacena en caché.]{#dns-components-cache-authority explanation="Los datos en caché conservan la autoridad de su fuente; el resolver no es el propietario de la zona."}
:::

## Servidores de nombres autoritativos

Un servidor autoritativo responde a partir de los datos de las zonas sobre las que tiene autoridad. Una zona debe disponer de varios servidores autoritativos con datos sincronizados y consideraciones independientes sobre fallos. Un servidor exclusivamente autoritativo no tiene por qué realizar recursión para clientes arbitrarios.

:::single-choice{#dns-components-authoritative-role}
¿Qué hace que un servidor sea autoritativo para una zona?

::option[Consultó una vez la zona mediante un resolver público.]{#dns-components-once-queried explanation="Consultar o almacenar en caché no concede autoridad."}
::option[Sirve los datos de la zona según la delegación y configuración pertinentes.]{#dns-components-serves-zone .correct explanation="La autoridad procede de la delegación DNS y de la zona cargada en el servidor, no de tener una copia en caché."}
::option[Responde más rápido a un ping.]{#dns-components-fastest-ping explanation="El tiempo de ICMP no define la autoridad DNS."}
:::

## Zonas y almacenamiento de zonas

Una zona es una parte del espacio de nombres DNS servida administrativamente. Comienza en el vértice de la zona y puede delegar zonas hijas. Los datos de la zona pueden almacenarse en un archivo de texto, generarse a partir de una base de datos, cargarse mediante una API o sintetizarse mediante software; un «archivo de zona» no es una implementación física obligatoria.

El vértice de la zona normalmente tiene un registro SOA y un conjunto NS. Los datos de delegación en un padre identifican los servidores autoritativos de la zona hija, a veces acompañados de registros de dirección glue necesarios para llegar a nombres de servidores incluidos en la propia delegación.

:::single-choice{#dns-components-zone-meaning}
¿Qué es una zona DNS?

::option[Una parte del espacio de nombres servida administrativamente.]{#dns-components-admin-portion .correct explanation="Puede contener registros y delegaciones con independencia del sistema de almacenamiento."}
::option[Un único archivo de texto obligatorio en todos los clientes.]{#dns-components-client-file explanation="Las implementaciones autoritativas pueden utilizar varias formas de almacenamiento y los clientes no contienen todas las zonas."}
::option[Un dominio de broadcast Ethernet identificado mediante una VLAN.]{#dns-components-vlan explanation="Las zonas DNS y los segmentos de la capa de enlace son conceptos independientes."}
:::

## Campos de los registros de recursos

Un registro de recursos tiene un nombre de propietario, un TTL, una clase, un tipo y datos RDATA específicos del tipo. Por ejemplo:

```text
www.example.com.  300  IN  A  192.0.2.25
```

El propietario es `www.example.com.`, el TTL es de 300 segundos, la clase es Internet, el tipo es dirección IPv4 y RDATA es la dirección. La omisión de campos y las reglas de nombres relativos de la sintaxis de los archivos de zona exigen tratar cuidadosamente el origen.

:::single-choice{#dns-components-mx-type}
¿Qué tipo de registro publica la preferencia y los nombres de los servidores de correo?

::option[`A`]{#dns-components-a explanation="Un registro A almacena una dirección IPv4."}
::option[`NS`]{#dns-components-ns explanation="Los registros NS identifican servidores de nombres autoritativos."}
::option[`MX`]{#dns-components-mx .correct explanation="Los datos RDATA de MX incluyen una preferencia y el nombre de un servidor de correo."}
:::

## TTL y caché negativa

Los registros positivos utilizan TTL para limitar su reutilización desde la caché. Las respuestas negativas, como un nombre cuya inexistencia se ha demostrado, también pueden almacenarse en caché según reglas derivadas del SOA. Reducir un TTL poco antes de un cambio planificado solo afecta a los registros obtenidos después de que las cachés vean el valor menor; los TTL más largos que ya están almacenados permanecen hasta que caducan.

:::single-choice{#dns-components-lower-ttl-timing}
¿Por qué debes reducir un TTL de DNS con suficiente antelación a un cambio de dirección planificado?

::option[El TTL modifica la MTU Ethernet del servidor.]{#dns-components-ttl-mtu explanation="La duración de la caché y el tamaño de los paquetes del enlace no están relacionados."}
::option[Un TTL menor garantiza que la aplicación nueva funcione correctamente.]{#dns-components-ttl-health explanation="Afecta al comportamiento de la caché, no a la corrección del servicio."}
::option[Las cachés existentes necesitan tiempo para que caduquen los registros aprendidos con el TTL anterior más largo.]{#dns-components-old-cache-expiry .correct explanation="Cambiar los datos autoritativos no puede acortar retroactivamente el tiempo restante de un registro ya almacenado."}
:::

## Resumen

Ahora puedes separar la recursión DNS, la autoridad, la gestión del espacio de nombres y los registros en caché.

1. Identifica las funciones de los resolvers stub y recursivos.
2. Define la autoridad mediante el servicio de una zona delegada.
3. Trata una zona como responsabilidad sobre un espacio de nombres, no como un único archivo obligatorio.
4. Interpreta los campos propietario, TTL, clase, tipo y RDATA.
5. Planifica la duración de las cachés antes de realizar cambios en DNS.
