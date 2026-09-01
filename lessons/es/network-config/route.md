---
lesson_id: "route"
course_id: "network-config"
lang: "es"
order_index: 2
title: "route"
description: "Aprende a inspeccionar, añadir, sustituir, eliminar y comprobar de forma segura rutas de Linux con ip."
meta_title: "route - Network Config"
meta_description: "Aprende a gestionar la tabla de enrutamiento de Linux. Esta guía explica cómo añadir y eliminar rutas de red mediante el comando moderno ip route y el comando antiguo route."
meta_keywords: "comando ip route en linux, comando linux ip route, añadir ruta, eliminar ruta, tabla de enrutamiento, enrutamiento de red, redes linux, ip route"
---

Las rutas manuales modifican la forma en que el kernel selecciona una interfaz de salida y un siguiente salto. Un error puede desconectar la máquina o redirigir tráfico sensible, así que inspecciona la ruta efectiva, el propietario de la configuración y la vía de recuperación antes de cambiar el estado.

## Inspeccionar la decisión actual

Registra las rutas pertinentes y pregunta al kernel cómo llega actualmente al destino:

```bash
$ ip -4 route show
$ ip route get 192.168.2.25
```

Inspecciona también las reglas de política y las tablas alternativas cuando existan. La consulta de ruta es una prueba local; no envía tráfico.

:::single-choice{#route-get-before-change} ¿Por qué debes ejecutar `ip route get DESTINATION` antes de cambiar una ruta?

::option[Registra la decisión local actual para compararla y poder revertirla.]{#route-get-baseline .correct explanation="La interfaz seleccionada, el siguiente salto y el origen ayudan a definir el cambio previsto."}
::option[Reserva permanentemente el destino en todos los routers.]{#route-get-reserves explanation="El comando realiza una consulta local y no cambia ningún estado remoto."}
::option[Deshabilita todas las reglas de enrutamiento por políticas.]{#route-get-disables-policy explanation="La consulta evalúa la política en lugar de eliminarla."}
:::

## Añadir o sustituir una ruta

Añade una ruta al prefijo canónico a través de un siguiente salto accesible:

```bash
$ sudo ip route add 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

La puerta de enlace debe ser accesible según el enlace pertinente o mediante un diseño explícito y válido que la considere en el enlace. `add` falla cuando ya existe una ruta equivalente. `replace` crea o cambia una ruta, lo que resulta útil para configuraciones idempotentes, pero puede sobrescribir un estado que funciona; revisa primero el objetivo exacto.

:::single-choice{#route-add-existing} ¿Qué suele ocurrir si `ip route add` se dirige a una ruta que ya existe?

::option[Elimina silenciosamente el prefijo de destino anterior.]{#route-add-deletes explanation="Add normalmente informa de un error de objeto existente en lugar de sustituirlo."}
::option[Falla en lugar de sustituir la ruta existente.]{#route-add-fails .correct explanation="Utiliza deliberadamente `replace` solo después de revisar qué entrada cambiará."}
::option[Reinicia la puerta de enlace seleccionada.]{#route-add-reboots explanation="La configuración local de rutas no puede solicitar así un reinicio remoto."}
:::

## Eliminar con precisión

Indica los atributos exactos de la ruta al eliminarla cuando pueda haber más de un candidato o tabla:

```bash
$ sudo ip route del 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

Una eliminación que solo indique el destino puede coincidir con más elementos de los previstos o ser ambigua. Captura antes de eliminarla el comando original necesario para restaurar la ruta.

:::single-choice{#route-delete-precision} ¿Por qué debes incluir el siguiente salto y el dispositivo al eliminar una ruta?

::option[Para identificar con mayor precisión la entrada prevista.]{#route-delete-exact .correct explanation="Los atributos explícitos reducen la posibilidad de eliminar otra ruta con el mismo prefijo."}
::option[Para eliminar también el adaptador de red físico.]{#route-delete-adapter explanation="Eliminar una ruta no suprime el objeto de enlace del kernel."}
::option[Para borrar la zona DNS del destino.]{#route-delete-dns explanation="El enrutamiento y los datos DNS autoritativos son sistemas independientes."}
:::

## Persistencia y seguridad remota

Un comando `ip route` solo cambia el estado actual del kernel. NetworkManager, systemd-networkd, netplan, ifupdown, DHCP, los demonios de enrutamiento o la orquestación pueden sustituirlo más adelante. Almacena la ruta en el propietario activo únicamente después de probar su comportamiento durante la ejecución.

En una máquina remota, conserva una consola independiente y utiliza una reversión que no dependa de la ruta que estás modificando. Después, comprueba la consulta de ruta, el estado de los vecinos, ambas direcciones del tráfico y el servicio real.

:::single-choice{#route-runtime-persistence} ¿Qué puede ocurrir con una ruta añadida manualmente después de que se recargue el gestor de red?

::option[Se convierte para siempre en una función inmutable del kernel.]{#route-manual-immutable explanation="Las rutas de ejecución pueden eliminarse o sustituirse."}
::option[Aparece automáticamente en todos los hosts de la subred.]{#route-manual-all-hosts explanation="El comando solo cambia el espacio de nombres de red actual."}
::option[Puede desaparecer si no figura en la política persistente.]{#route-manual-disappears .correct explanation="El gestor reconcilia el estado del kernel a partir de sus perfiles configurados."}
:::

## Resumen

Ahora puedes realizar un cambio acotado y recuperable en una ruta de Linux.

1. Captura las rutas, las reglas y la consulta efectiva actuales.
2. Usa un prefijo canónico y un siguiente salto accesible.
3. Distingue entre añadir y sustituir deliberadamente.
4. Elimina la ruta exacta y conserva un comando de restauración.
5. Hazla persistente mediante el gestor activo y comprueba ambas direcciones.
