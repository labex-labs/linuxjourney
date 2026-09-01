---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "es"
order_index: 4
title: "/etc/hosts"
description: "Aprende cómo las correspondencias locales del archivo hosts participan en la resolución de nombres de Linux y cómo probarlas de forma segura."
meta_title: "/etc/hosts - DNS"
meta_description: "Explora la finalidad del archivo /etc/hosts en Linux. Aprende cómo relaciona nombres de host con direcciones IP, su función en la resolución local y cómo configurarlo en sistemas como Debian."
meta_keywords: "/etc/hosts, etc hosts linux, hosts debian, etc host linux, etc hosts, redes Linux, correspondencia de nombres de host, resolución DNS"
---

`/etc/hosts` proporciona entradas estáticas de direcciones y nombres a la pila local de servicios de nombres del sistema. Resulta útil para nombres loopback, dependencias de arranque y pruebas con un ámbito limitado, pero no publica registros para otros hosts ni actualiza DNS.

## Interpretar el archivo

Una línea comienza con una dirección IPv4 o IPv6 seguida de uno o varios nombres:

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

Los comentarios comienzan con `#`. Por convención, algunas herramientas tratan el primer nombre como canónico y los posteriores como alias, pero el comportamiento de las aplicaciones y las API de resolución varía. Evita entradas duplicadas o contradictorias para el mismo nombre.

:::single-choice{#hosts-file-entry-order} ¿Qué aparece primero en una línea normal de correspondencia de `/etc/hosts`?

::option[Una dirección IP.]{#hosts-file-address-first .correct explanation="Uno o varios nombres siguen a la dirección en la misma línea."}
::option[El TTL de un registro DNS.]{#hosts-file-ttl-first explanation="Las entradas del archivo hosts no utilizan campos TTL de DNS."}
::option[Un número de puerto de transporte.]{#hosts-file-port-first explanation="El archivo relaciona nombres y direcciones, no puertos de aplicaciones."}
:::

## Orden de resolución

La configuración de Name Service Switch, normalmente `/etc/nsswitch.conf`, determina cómo combinan las funciones del resolver del sistema `files`, DNS, sistemas multicast y otras fuentes. Una línea habitual es:

```text
hosts: files dns
```

No supongas que los archivos siempre se consultan primero sin inspeccionar la política. Las aplicaciones también pueden utilizar sus propias bibliotecas DNS, cachés, proxies o resolvers cifrados, y es posible que no sigan la ruta del sistema.

:::single-choice{#hosts-file-nss-order} ¿Qué determina si el resolver del sistema consulta `/etc/hosts` antes que DNS?

::option[El orden alfabético de los nombres de archivo de `/etc`.]{#hosts-file-alphabetical explanation="El orden del listado del sistema de archivos no define la política de servicios de nombres."}
::option[El orden de las fuentes en la política de Name Service Switch.]{#hosts-file-nss-policy .correct explanation="La línea de la base de datos `hosts:` controla el orden normal de fuentes del resolver de libc."}
::option[El tamaño de la ventana TCP del destino.]{#hosts-file-tcp-window explanation="El control de flujo del transporte no está relacionado con la búsqueda local de nombres."}
:::

## Probar mediante el resolver del sistema

Usa `getent` para ejercitar la ruta configurada de servicios de nombres del sistema:

```bash
$ getent ahosts app-test.example.net
```

`dig` consulta DNS directamente y normalmente no informa de las correspondencias de `/etc/hosts`. Esta diferencia resulta útil: que `getent` tenga éxito y `dig` no puede indicar una fuente local o una diferencia en la política del resolver.

:::single-choice{#hosts-file-getent-versus-dig} ¿Qué herramienta es mejor para comprobar si la resolución normal del sistema ve una entrada del archivo hosts?

::option[`dig`, porque siempre lee primero `/etc/hosts`.]{#hosts-file-dig-first explanation="Dig envía consultas DNS y omite la ruta de búsqueda del archivo hosts."}
::option[`getent ahosts`, porque utiliza las fuentes de servicios de nombres configuradas.]{#hosts-file-getent .correct explanation="Refleja la ruta del resolver que utilizan muchas aplicaciones nativas."}
::option[`ip route flush`, porque reconstruye todos los nombres.]{#hosts-file-flush-route explanation="Vaciar las rutas es destructivo y no está relacionado con las búsquedas del archivo hosts."}
:::

## Editar de forma segura

Conserva las entradas necesarias de localhost y de identidad del host, valida la dirección prevista y realiza un cambio recuperable mediante herramientas de edición con privilegios. Evita sobrescribir un dominio público real como prueba casual; puede redirigir inesperadamente credenciales o tráfico de aplicaciones. Utiliza un nombre de prueba dedicado y elimina la entrada después del experimento.

Después de editar, prueba la aplicación exacta porque puede conservar una caché o utilizar otro resolver. Documenta las anulaciones persistentes para que no sobrevivan silenciosamente a su propósito.

:::single-choice{#hosts-file-test-name} ¿Por qué debes utilizar un nombre de prueba dedicado en lugar de sobrescribir el nombre de un servicio público?

::option[Los nombres públicos no pueden contener puntos.]{#hosts-file-public-no-dots explanation="Los nombres de dominio suelen contener varias etiquetas separadas por puntos."}
::option[Los nombres dedicados crean automáticamente zonas DNS autoritativas.]{#hosts-file-auto-zone explanation="Una entrada del archivo hosts sigue siendo local y no publica una zona."}
::option[Reduce el riesgo de redirigir tráfico o credenciales reales.]{#hosts-file-reduce-redirection .correct explanation="Una anulación local puede afectar a cualquier cliente del resolver del sistema que utilice ese nombre público."}
:::

## Configuración de servidores resolver

`/etc/resolv.conf` contiene tradicionalmente los ajustes de los resolvers DNS, pero a menudo lo generan NetworkManager, systemd-resolved, DHCP u otro gestor. Inspecciona los enlaces simbólicos y los comentarios del archivo, y cambia la fuente de configuración propietaria en lugar de editar una salida generada que se sobrescribirá.

:::single-choice{#hosts-file-resolv-owner} ¿Qué debes hacer antes de editar `/etc/resolv.conf`?

::option[Eliminar `/etc/hosts` y todas las rutas de red.]{#hosts-file-delete-state explanation="Esos cambios destructivos no están relacionados y pueden eliminar la conectividad."}
::option[Suponer que todas las distribuciones almacenan allí directamente los ajustes permanentes.]{#hosts-file-assume-direct explanation="Muchos sistemas generan el archivo dinámicamente o lo enlazan a un stub gestionado."}
::option[Identificar si otro servicio lo genera y controla.]{#hosts-file-identify-resolver-owner .correct explanation="Los cambios persistentes de servidores DNS deben realizarse en la configuración del gestor activo."}
:::

## Resumen

Ahora puedes utilizar `/etc/hosts` como una entrada local y controlada del resolver.

1. Escribe correspondencias que comiencen por la dirección y utilicen nombres y alias deliberados.
2. Inspecciona el orden de Name Service Switch en lugar de suponerlo.
3. Prueba la resolución del sistema con `getent` y DNS por separado con `dig`.
4. Usa nombres temporales dedicados y comprueba la aplicación real.
5. Cambia los servidores resolver mediante el propietario de la configuración.
