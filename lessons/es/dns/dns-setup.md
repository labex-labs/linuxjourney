---
lesson_id: "dns-setup"
course_id: "dns"
lang: "es"
order_index: 5
title: "Configuración de DNS"
description: "Aprende a elegir, proteger, validar y operar servicios DNS autoritativos o recursivos."
meta_title: "Configuración de DNS - DNS"
meta_description: "Aprende sobre servidores DNS populares para Linux como BIND, dnsmasq y PowerDNS. Descubre cómo elegir el servidor apropiado para tu red con esta guía para principiantes."
meta_keywords: "DNS Linux, BIND, dnsmasq, PowerDNS, configuración de servidor DNS, redes Linux, tutorial DNS, principiante"
---

El software DNS debe elegirse según la función y los requisitos operativos, no conforme a un «mejor servidor» universal. Un servicio autoritativo publica zonas; un servicio recursivo responde a los clientes resolviendo y almacenando en caché; un resolver de reenvío envía consultas a otro resolver. Combinar funciones cambia la superficie de ataque.

## Elegir una función y una implementación

- BIND puede proporcionar servicio autoritativo y recursivo con una amplia compatibilidad con los estándares.
- Unbound suele implantarse como resolver recursivo con validación.
- dnsmasq proporciona funciones ligeras de reenvío, caché y DHCP para redes controladas más pequeñas.
- PowerDNS ofrece productos autoritativos y recursivos independientes con varios sistemas de almacenamiento.

Las capacidades y los paquetes cambian, así que consulta la documentación oficial de la versión instalada. Implanta únicamente la función necesaria y deshabilita la recursión o el servicio de zonas no previstos.

:::single-choice{#dns-setup-authoritative-role}
¿Qué función publica los registros definitivos de las zonas que sirve?

::option[Servidor DNS autoritativo.]{#dns-setup-authoritative .correct explanation="Responde a partir de la autoridad de zona configurada en lugar de buscar recursivamente nombres arbitrarios."}
::option[Conmutador Ethernet.]{#dns-setup-switch explanation="Un conmutador reenvía tramas de la capa de enlace y no publica zonas DNS."}
::option[Un resolver recursivo que responde a consultas arbitrarias de clientes.]{#dns-setup-stub explanation="Un stub envía consultas a un servicio recursivo y no aloja zonas autoritativas."}
:::

## Diseñar antes de instalar

Define las zonas, los clientes, el volumen de consultas, el mecanismo de actualización, las necesidades de DNSSEC, el registro, la supervisión, las copias de seguridad y la recuperación. Las zonas autoritativas necesitan servidores redundantes y delegaciones registradas correctamente. El servicio recursivo necesita controles explícitos de acceso de clientes, políticas de caché, accesibilidad hacia servidores superiores o iterativos y protección frente a abusos.

Nunca expongas recursión sin restricciones a Internet. Los resolvers abiertos pueden utilizarse indebidamente para ataques de reflexión y consumir recursos locales.

:::single-choice{#dns-setup-open-recursion}
¿Por qué deben restringirse las consultas recursivas a clientes autorizados?

::option[DNS recursivo no puede almacenar ningún registro en caché.]{#dns-setup-no-cache explanation="La caché es una función esencial de los resolvers recursivos."}
::option[Las delegaciones autoritativas exigen que todos los usuarios sean root.]{#dns-setup-all-root explanation="Una delegación DNS no concede privilegios del sistema operativo."}
::option[La recursión abierta puede utilizarse para amplificación y consumo de recursos.]{#dns-setup-recursion-abuse .correct explanation="Los controles de acceso reducen el uso del resolver como infraestructura pública de ataques."}
:::

## Validar la configuración y los datos de las zonas

Utiliza las herramientas de comprobación de sintaxis y zonas de la implementación antes de recargar. Para BIND, algunos ejemplos habituales son:

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

Ejecuta los comandos con los permisos y rutas apropiados para la máquina. Que el analizador tenga éxito no demuestra la delegación, la propagación del serial, la cadena DNSSEC, la accesibilidad a través del cortafuegos ni la corrección de las respuestas, así que realiza después consultas controladas.

:::single-choice{#dns-setup-zone-validation-limit}
¿Qué no demuestra una comprobación sintáctica satisfactoria de una zona?

::option[Que funcionen la delegación y las respuestas autoritativas de extremo a extremo.]{#dns-setup-not-end-to-end .correct explanation="Los datos del padre, la activación del servicio, la política de red y la carga durante la ejecución son aspectos independientes."}
::option[Que el comprobador pueda analizar el texto de la zona.]{#dns-setup-parser-proves explanation="Esa es la prueba directa que proporciona el comprobador."}
::option[Que el archivo tenga un campo de propietario del registro.]{#dns-setup-record-owner explanation="El análisis de registros válidos ya comprueba aspectos estructurales."}
:::

## Aplicar y probar de forma segura

Conserva la configuración actual y el acceso de recuperación, valida y después recarga en lugar de reiniciar cuando sea compatible. Consulta directamente cada servidor autoritativo con la recursión deshabilitada y compara el serial SOA, el conjunto NS, los registros positivos, los nombres inexistentes y el comportamiento sobre UDP y TCP:

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

Para la recursión, prueba las redes de clientes permitidas y denegadas, la validación DNSSEC, el comportamiento de la caché y los fallos de las dependencias superiores.

:::single-choice{#dns-setup-norecurse-test}
¿Por qué debes consultar un servidor autoritativo con `+norecurse`?

::option[Para probar las respuestas autoritativas sin solicitar recursión.]{#dns-setup-authority-only .correct explanation="Esto separa el servicio de la zona de cualquier comportamiento recursivo."}
::option[Para eliminar todos los registros de su zona.]{#dns-setup-remove-records explanation="Una consulta no edita los datos autoritativos."}
::option[Para obligar a que todas las respuestas pasen por HTTP.]{#dns-setup-force-http explanation="La opción controla el indicador de recursión deseada de DNS."}
:::

## Operar el servicio

Supervisa los fallos de consultas, la latencia, el comportamiento de la caché, el uso de recursos, las transferencias de zonas, la coherencia de seriales, la caducidad de DNSSEC y la salud de las delegaciones. Guarda de forma segura copias de la configuración fuente y del material de firma, pero comprueba que una instancia nueva pueda cargar las zonas y servir respuestas correctas. Aplica parches a versiones compatibles y limita las interfaces de control, las actualizaciones dinámicas y el acceso a transferencias.

:::single-choice{#dns-setup-redundancy-verification}
¿Qué debe incluir la prueba de redundancia de DNS autoritativo?

::option[Consultar cada servidor y probar el funcionamiento cuando otro no esté disponible.]{#dns-setup-test-each-server .correct explanation="Enumerar varios registros NS no demuestra que cada servicio independiente sea accesible y esté actualizado."}
::option[Comprobar únicamente que todos los servidores tengan nombres de host parecidos.]{#dns-setup-hostname-similarity explanation="Los nombres no demuestran la sincronización de datos ni la disponibilidad."}
::option[Utilizar un único proceso y disco compartidos para todos los servidores anunciados.]{#dns-setup-shared-failure explanation="Un dominio de fallo compartido debilita la redundancia."}
:::

## Resumen

Ahora puedes diseñar una implantación DNS alrededor de funciones explícitas de autoridad o recursión.

1. Elige el software solo después de definir la función necesaria.
2. Restringe la recursión y las interfaces administrativas.
3. Valida la configuración y las zonas antes de recargar.
4. Prueba directamente la autoridad, la denegación, el transporte y la política de clientes.
5. Supervisa la redundancia, DNSSEC, la coherencia de los datos y la recuperación.
