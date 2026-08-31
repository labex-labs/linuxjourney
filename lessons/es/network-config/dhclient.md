---
lesson_id: "dhclient"
course_id: "network-config"
lang: "es"
order_index: 3
title: "dhclient"
description: "Aprende cuándo y cómo usar dhclient sin entrar en conflicto con el gestor de red del sistema."
meta_title: "dhclient - Network Config"
meta_description: "Aprende qué es dhclient, cómo obtiene direcciones IP mediante DHCP y cómo gestiona arrendamientos de red. Comprende los archivos dhclient.conf y dhclient.leases."
meta_keywords: "dhclient, DHCP, redes Linux, dirección IP, configuración de red, tutorial Linux, guía para principiantes"
---

`dhclient` es un cliente DHCP de ISC presente en algunos sistemas Linux. Muchas instalaciones actuales permiten que NetworkManager, systemd-networkd u otro servicio ejecute su propio cliente DHCP. Iniciar un segundo cliente en una interfaz gestionada puede crear direcciones, rutas, ajustes DNS y estados de arrendamiento que compitan entre sí.

## Identificar el cliente activo

Antes de invocar `dhclient`, inspecciona el propietario de la configuración y los procesos:

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

Utiliza las herramientas que existan en la máquina. Si un gestor controla la interfaz, solicita DHCP mediante ese gestor en lugar de iniciar otro cliente.

:::single-choice{#dhclient-second-client-risk}
¿Por qué debes evitar iniciar `dhclient` en una interfaz ya gestionada?

::option[DHCP solo puede asignar direcciones loopback.]{#dhclient-loopback-only explanation="DHCP suele asignar configuraciones de red que no son loopback."}
::option[Dos clientes pueden competir por las direcciones, las rutas, DNS y los arrendamientos.]{#dhclient-competing-state .correct explanation="Normalmente, solo el propietario identificado de la configuración debe reconciliar la interfaz."}
::option[Todas las solicitudes DHCP vuelven a formatear el disco local.]{#dhclient-reformats explanation="El protocolo cambia el estado de la red, no el formato del disco."}
:::

## Solicitar explícitamente un arrendamiento

En una interfaz de prueba no gestionada donde `dhclient` sea el propietario previsto, indica la interfaz y utiliza la salida detallada:

```bash
$ sudo dhclient -v enp1s0
```

La ejecución sin indicar una interfaz puede actuar sobre varias interfaces válidas. Las rutas de configuración y arrendamientos varían según el paquete y la invocación; entre los nombres habituales se encuentran `dhclient.conf` y `dhclient.leases`, pero no supongas que existe una única ubicación fija.

:::single-choice{#dhclient-interface-operand}
¿Por qué debes indicar `enp1s0` en una solicitud manual?

::option[Para dirigirte únicamente a la interfaz de red prevista.]{#dhclient-scope-interface .correct explanation="Una invocación del cliente sin especificar puede tener en cuenta más interfaces de las previstas."}
::option[Para seleccionar el puerto TCP 1 para DHCP.]{#dhclient-tcp-port explanation="DHCP utiliza UDP y el nombre de la interfaz no es un puerto."}
::option[Para hacer permanente el arrendamiento.]{#dhclient-permanent explanation="La configuración DHCP sigue siendo un estado de arrendamiento con tiempo limitado."}
:::

## Liberar un arrendamiento

`dhclient -r INTERFACE` solicita la liberación y puede eliminar una configuración utilizable. Es una operación que causa interrupciones y no garantiza que el servidor sea accesible para recibir la liberación. No liberes un arrendamiento únicamente para inspeccionarlo, sobre todo si forma parte de una ruta de administración remota.

:::single-choice{#dhclient-release-effect}
¿Cuál es el riesgo operativo de `dhclient -r enp1s0`?

::option[Solo muestra el arrendamiento actual sin realizar cambios.]{#dhclient-release-readonly explanation="La liberación es una acción que modifica el estado."}
::option[Renueva todos los arrendamientos durante un periodo ilimitado.]{#dhclient-release-renews explanation="Liberar y renovar son operaciones opuestas."}
::option[Puede eliminar la conectividad DHCP actual.]{#dhclient-release-connectivity .correct explanation="El flujo de liberación renuncia al estado del arrendamiento y puede terminar el acceso remoto."}
:::

## Comprobar el arrendamiento aplicado

Después de una solicitud controlada, comprueba algo más que la dirección:

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

Inspecciona los registros del gestor o del cliente y la duración del arrendamiento, y después prueba la resolución de nombres y la aplicación previstas. Un DHCPACK puede contener opciones incorrectas, y asignar correctamente una dirección no demuestra que la puerta de enlace o DNS sean accesibles.

:::single-choice{#dhclient-verify-state}
¿Qué debe comprobarse después de obtener un arrendamiento?

::option[La dirección, las rutas, DNS, el arrendamiento y el comportamiento de la aplicación.]{#dhclient-complete-verify .correct explanation="El arrendamiento configura varios componentes relacionados que deben funcionar conjuntamente."}
::option[Únicamente que aparezca una cadena de dirección.]{#dhclient-address-only explanation="Las rutas, DNS, la duración y el funcionamiento de extremo a extremo aún pueden ser incorrectos."}
::option[Únicamente el fondo del escritorio.]{#dhclient-wallpaper explanation="El aspecto del escritorio no está relacionado con el estado DHCP."}
:::

## Resumen

Ahora puedes utilizar `dhclient` únicamente cuando sea el propietario previsto de una interfaz.

1. Descubre el gestor de red y el cliente DHCP activos.
2. Evita clientes que compitan en una misma interfaz.
3. Limita una solicitud manual a una interfaz de prueba con nombre.
4. Trata la liberación como una operación que causa interrupciones y comprueba el resultado completo del arrendamiento.
