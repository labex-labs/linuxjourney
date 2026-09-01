---
lesson_id: "dns-tools"
course_id: "dns"
lang: "es"
order_index: 6
title: "Herramientas de DNS"
description: "Aprende a comparar la resolución del sistema con consultas DNS directas mediante getent, resolvectl y dig."
meta_title: "Herramientas de DNS - DNS"
meta_description: "Explora herramientas DNS esenciales de Linux como nslookup y el potente comando dig. Este tutorial para principiantes explica consultas DNS y técnicas de diagnóstico."
meta_keywords: "nslookup, comando dig, herramientas DNS, DNS Linux, diagnóstico DNS, consulta de servidor de nombres, tutorial Linux, Linux para principiantes"
---

El diagnóstico de DNS comienza identificando qué capa se está probando. Las herramientas del resolver del sistema incluyen archivos y políticas locales, mientras que `dig` y `nslookup` envían consultas DNS y pueden dirigirse directamente a un servidor concreto.

## Probar el resolver del sistema

Utiliza la ruta normal de servicios de nombres del host con:

```bash
$ getent ahosts www.example.com
```

En una máquina con systemd-resolved, inspecciona los servidores por enlace, los dominios de búsqueda y el estado del protocolo con:

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

Una aplicación aún puede utilizar una biblioteca de resolución privada o un proxy, así que reproduce el problema mediante la propia aplicación cuando las salidas difieran.

:::single-choice{#dns-tools-system-resolver} ¿Qué comando ejercita la ruta configurada de servicios de nombres del sistema?

::option[Únicamente `dig @SERVER NAME`.]{#dns-tools-dig-direct explanation="Dig envía una consulta DNS y normalmente no lee las correspondencias del archivo hosts."}
::option[`ip link set down`]{#dns-tools-link-down explanation="Esto interrumpe la interfaz en lugar de probar la resolución."}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="Puede reflejar `/etc/hosts`, DNS y otras fuentes de Name Service Switch."}
:::

## Consultar con dig

Indica un nombre y un tipo de registro:

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

La salida identifica el servidor que responde, el estado, los indicadores, la pregunta, la respuesta, la autoridad, los datos adicionales, el tiempo de la consulta y los metadatos del transporte. `+short` resulta práctico para scripts, pero oculta pruebas necesarias para diagnosticar.

:::single-choice{#dns-tools-record-type} ¿Qué consulta solicita registros de direcciones IPv6?

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="Los registros AAAA contienen direcciones IPv6."}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX solicita registros de servidores de correo."}
::option[`dig NAME PTR` sobre el nombre directo.]{#dns-tools-ptr-forward explanation="PTR suele consultarse mediante un nombre de búsqueda inversa."}
:::

## Seleccionar un servidor

Dirígete explícitamente a un resolver o servidor autoritativo:

```bash
$ dig @192.0.2.53 www.example.com A
```

Compara el resolver recursivo configurado, un segundo resolver autorizado y cada servidor autoritativo al aislar la caché de la autoridad. Un estado `NOERROR` puede no contener la respuesta solicitada; `NXDOMAIN` significa que el nombre consultado no existe, mientras que `SERVFAIL` indica que el servidor no pudo completar la consulta.

:::single-choice{#dns-tools-noerror-empty} ¿Puede `NOERROR` tener una sección de respuestas vacía?

::option[Sí, cuando el nombre existe pero carece de los datos del registro solicitado.]{#dns-tools-noerror-nodata .correct explanation="El estado y la cantidad de respuestas deben interpretarse conjuntamente."}
::option[No, garantiza al menos un registro de dirección.]{#dns-tools-noerror-always-answer explanation="El nombre puede existir sin datos del tipo solicitado."}
::option[No, las respuestas vacías siempre son fallos de Ethernet.]{#dns-tools-empty-ethernet explanation="La semántica DNS, no el encapsulado del enlace, explica una respuesta válida sin datos."}
:::

## Comprobar recursión y autoridad

`rd` en la consulta solicita recursión; `ra` en una respuesta indica que el servidor la ofrece. `aa` significa que la respuesta es autoritativa. Consulta un servidor autoritativo con `+norecurse` para evitar confundir la caché recursiva con los datos de la zona servida.

`dig +trace NAME` realiza su propio recorrido iterativo a partir de las referencias raíz. Puede diferir de un resolver de producción porque omite su caché, reenvío, política, validación DNSSEC y ubicación de red.

:::single-choice{#dns-tools-aa-flag} ¿Qué significa el indicador de respuesta `aa`?

::option[La consulta utilizó dos direcciones IPv4 idénticas.]{#dns-tools-two-addresses explanation="El indicador no está relacionado con la cantidad de respuestas ni con la familia de direcciones."}
::option[La respuesta se cifró mediante credenciales de aplicación.]{#dns-tools-aa-encrypted explanation="Los indicadores DNS no demuestran que el transporte esté cifrado."}
::option[La respuesta es autoritativa.]{#dns-tools-authoritative-answer .correct explanation="El servidor que responde afirma tener autoridad sobre los datos de la respuesta."}
:::

## Probar consultas inversas y TCP

Usa `-x` para construir una consulta PTR inversa:

```bash
$ dig -x 192.0.2.25
```

Prueba DNS sobre TCP al investigar truncados, transferencias de zonas o diferencias del cortafuegos:

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

DNS moderno puede utilizar el puerto 53 por UDP o TCP; ambos deben permitirse donde sean necesarios. Una respuesta UDP con el indicador de truncado provoca que los clientes compatibles vuelvan a intentarlo mediante un transporte apropiado.

:::single-choice{#dns-tools-tcp-test} ¿Qué cambia `dig +tcp`?

::option[Envía la consulta DNS mediante TCP en lugar del intento predeterminado por UDP.]{#dns-tools-use-tcp .correct explanation="Esto ayuda a aislar el filtrado del transporte y las respuestas que necesitan un flujo fiable de mayor tamaño."}
::option[Solicita únicamente registros de nombres de servicios TCP.]{#dns-tools-tcp-records explanation="El tipo DNS solicitado se especifica por separado."}
::option[Cambia permanentemente la configuración del resolver del servidor.]{#dns-tools-tcp-persistent explanation="Una consulta no edita los ajustes del servidor."}
:::

## Resumen

Ahora puedes elegir una herramienta DNS que corresponda con la capa del resolver investigada.

1. Usa `getent` para la ruta configurada del resolver del sistema.
2. Usa `dig` con tipos de registros y servidores explícitos.
3. Interpreta conjuntamente el estado, los indicadores, las secciones y el servidor que responde.
4. Separa la caché recursiva de los datos autoritativos.
5. Prueba las consultas inversas y ambos transportes DNS necesarios.
