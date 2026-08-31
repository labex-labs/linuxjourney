---
lesson_id: "dns-process"
course_id: "dns"
lang: "es"
order_index: 3
title: "Proceso de DNS"
description: "Aprende cómo un resolver stub y uno recursivo utilizan la caché, las referencias, los registros glue y la autoridad para responder una consulta DNS."
meta_title: "Proceso de DNS - DNS"
meta_description: "Explora paso a paso el proceso de resolución DNS, desde los servidores raíz hasta el servidor autoritativo. Comprende cómo encuentra un dominio un servidor Linux, un concepto esencial en producción."
meta_keywords: "proceso DNS, consulta DNS, resolución de dominios, dns linux, servidor de producción, alojamiento de dominios, servidor dns, TLD, servidores raíz, dns autoritativo"
---

Una aplicación normal consulta el resolver stub del sistema operativo, que aplica la política local de servicios de nombres y envía una consulta recursiva a un resolver configurado. El resolver recursivo solo recorre la jerarquía cuando no existe una respuesta válida en caché.

## Comenzar por la política local y la caché

El resolver del sistema puede consultar `/etc/hosts`, DNS y otras fuentes en el orden configurado. Los sufijos de búsqueda pueden transformar un nombre corto en varios nombres candidatos. Después, un resolver recursivo comprueba las entradas positivas y negativas de la caché antes de enviar tráfico hacia servidores superiores.

:::single-choice{#dns-process-cache-first}
¿Por qué puede un resolver recursivo no contactar con ningún servidor autoritativo para una consulta?

::option[DNS exige que todas las consultas fallen primero de forma local.]{#dns-process-requires-failure explanation="Un resolver puede responder inmediatamente desde la caché."}
::option[Tiene una respuesta en caché que sigue siendo válida.]{#dns-process-valid-cache .correct explanation="La caché evita repetir el recorrido de la jerarquía hasta que caduca la duración del registro."}
::option[Los servidores autoritativos solo aceptan tramas Ethernet de los clientes.]{#dns-process-authoritative-ethernet explanation="DNS opera mediante transportes IP a través de redes enrutadas."}
:::

## Consultar un servidor raíz

Cuando no hay una entrada en caché, un resolver recursivo puede consultar un servidor raíz. La raíz DNS tiene 13 identidades de servidores con nombre, de la A a la M, atendidas por muchas instancias físicas mediante anycast y otras técnicas de implantación resistentes. La respuesta suele remitir al resolver a los servidores autoritativos del dominio de nivel superior pertinente en lugar de devolver la dirección final del host.

:::single-choice{#dns-process-root-response}
¿Qué devuelve normalmente un servidor raíz para una consulta sin caché de `www.example.com`?

::option[Una referencia hacia los servidores del dominio de nivel superior `com`.]{#dns-process-root-referral .correct explanation="La jerarquía delega la responsabilidad en lugar de almacenar todos los registros finales de hosts en la raíz."}
::option[La página web alojada en `www.example.com`.]{#dns-process-root-webpage explanation="DNS devuelve datos de registros de recursos, no contenido de aplicaciones."}
::option[La dirección MAC Ethernet del destino.]{#dns-process-root-mac explanation="Las direcciones MAC se resuelven en enlaces locales, no mediante la jerarquía DNS."}
:::

## Seguir referencias TLD y autoritativas

El resolver consulta un servidor autoritativo de `com`, que devuelve los servidores de nombres autoritativos delegados para `example.com`. La referencia puede incluir registros de dirección glue cuando sean necesarios para llegar a un servidor cuyo nombre se encuentre dentro de la zona hija delegada. Después, el resolver consulta a un servidor autoritativo el registro solicitado.

:::single-choice{#dns-process-glue-purpose}
¿Qué problema ayudan a resolver los registros glue de DNS?

::option[Cifrar las cargas útiles HTTP después de la resolución DNS.]{#dns-process-glue-http explanation="TLS u otros mecanismos de seguridad de aplicaciones se ocupan del cifrado de la carga útil."}
::option[Elegir el puerto más rápido de un conmutador Ethernet.]{#dns-process-glue-switch explanation="Glue contiene datos de direcciones de delegación, no políticas de reenvío del enlace."}
::option[Llegar a un servidor incluido en la propia zona sin una resolución circular.]{#dns-process-glue-reachability .correct explanation="El padre proporciona los datos de dirección necesarios para contactar con un servidor cuyo nombre está dentro de la zona hija."}
:::

## Seguir alias y tipos de registros

Una respuesta puede contener un alias CNAME que exija consultar otro nombre o registros específicos de una aplicación que conduzcan a más consultas. Solicitar `A` solo devuelve registros de direcciones IPv4 y los datos relacionados de la cadena; una consulta independiente `AAAA` obtiene direcciones IPv6. La respuesta final contiene un estado como `NOERROR`, `NXDOMAIN` o `SERVFAIL`, cada uno con un significado distinto.

:::single-choice{#dns-process-nxdomain-meaning}
¿Qué informa `NXDOMAIN`?

::option[Que el nombre de dominio consultado no existe según un resultado autoritativo.]{#dns-process-name-does-not-exist .correct explanation="Esto difiere de un nombre existente que simplemente carezca del tipo de registro solicitado."}
::option[Que el nombre existe y siempre tiene un registro A vacío.]{#dns-process-empty-a explanation="Un nombre existente sin los datos solicitados normalmente produce una respuesta sin datos, no NXDOMAIN."}
::option[Que el resolver alcanzó el tamaño máximo de una trama Ethernet.]{#dns-process-frame-size explanation="El estado se refiere a la existencia del nombre."}
:::

## Validación, caché y uso por la aplicación

Un resolver recursivo validador puede utilizar firmas DNSSEC y la cadena de confianza para comprobar una denegación autenticada o la integridad de los registros. DNSSEC no cifra las consultas ni demuestra que la aplicación de la dirección devuelta sea de confianza.

El resolver almacena los resultados en caché según las reglas de TTL y los devuelve al stub. La aplicación elige después una dirección e intenta utilizar sus propios protocolos de red y seguridad.

:::single-choice{#dns-process-dnssec-limit}
¿Qué no proporciona la validación DNSSEC?

::option[Integridad y autenticación del origen de los datos DNS firmados.]{#dns-process-dnssec-does-integrity explanation="Esos son objetivos esenciales de DNSSEC."}
::option[Denegación autenticada para datos inexistentes firmados.]{#dns-process-authenticated-denial explanation="Los mecanismos de denegación firmada pueden proporcionar esa validación."}
::option[Confidencialidad para la consulta y la respuesta DNS.]{#dns-process-no-confidentiality .correct explanation="El cifrado requiere un transporte DNS protegido independiente, como DoT o DoH."}
:::

## Resumen

Ahora puedes seguir una consulta DNS recursiva desde la política local hasta una respuesta final en caché.

1. Comprueba primero las fuentes locales y la caché del resolver.
2. Sigue las referencias de la raíz y del dominio de nivel superior.
3. Utiliza glue para llegar a los servidores delegados apropiados.
4. Distingue los alias, las respuestas sin datos y los nombres inexistentes.
5. Separa la integridad DNSSEC de la confidencialidad del transporte.
