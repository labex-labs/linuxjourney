---
lesson_id: "network-manager"
course_id: "network-config"
lang: "es"
order_index: 4
title: "NetworkManager"
description: "Aprende cómo NetworkManager separa los dispositivos, los perfiles de conexión persistentes y el estado activo durante la ejecución."
meta_title: "NetworkManager - Network Config"
meta_description: "Descubre la función del demonio NetworkManager en la gestión moderna de redes Linux. Aprende cómo automatiza la configuración y cómo interactuar con él mediante la potente utilidad nmcli."
meta_keywords: "NetworkManager, nm-tool, nmcli, gestor de red linux, networkmanager linux, gestión de redes linux, configuración de red, redes Linux"
---

NetworkManager gestiona dispositivos de red y activa perfiles de conexión en muchos escritorios y servidores Linux. No es universal, así que confirma que controla la interfaz de destino antes de utilizar `nmcli` para cambiar su configuración.

## Dispositivos y conexiones

Un dispositivo es una interfaz del kernel como `enp1s0` o `wlan0`. Una conexión es un perfil almacenado que contiene ajustes de IPv4, IPv6, DNS, Wi-Fi, enrutamiento y otros ámbitos. Un dispositivo puede tener varios perfiles, pero normalmente solo hay activo un perfil aplicable a la vez.

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile} ¿Qué es un perfil de conexión de NetworkManager?

::option[Un conector físico soldado a la tarjeta de red.]{#networkmanager-physical-connector explanation="Eso es hardware, no un perfil de NetworkManager."}
::option[Un conjunto almacenado de ajustes que puede activarse en un dispositivo.]{#networkmanager-stored-settings .correct explanation="Los perfiles conservan la configuración por separado del objeto de interfaz del kernel."}
::option[Un paquete capturado de todos los flujos activos.]{#networkmanager-packet-capture explanation="Los perfiles describen la configuración y no contienen todo el tráfico."}
:::

## Inspeccionar el estado efectivo

Muestra el perfil activo y los detalles del dispositivo:

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

Los ajustes del perfil, los resultados de DHCP durante la ejecución y el estado del kernel pueden diferir. Compáralos con `ip address`, `ip route` y el resolver. El obsoleto `nm-tool` no debe constituir la base de un flujo de trabajo actual.

:::single-choice{#networkmanager-active-command} ¿Qué comando lista los perfiles activos de NetworkManager?

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="Este no es un comando de inspección y sugiere una acción destructiva."}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="Filtra las conexiones almacenadas para mostrar las que están activadas actualmente."}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="Esto elimina el estado de enrutamiento en lugar de listar perfiles."}
:::

## Modificar y activar un perfil

Modifica explícitamente un perfil con nombre y actívalo después durante una ventana de mantenimiento:

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

La modificación cambia los datos persistentes del perfil; la activación puede sustituir las direcciones, rutas y DNS activos. Un cambio remoto necesita acceso mediante consola, los ajustes originales guardados y una reversión temporizada independiente. Nunca dependas de la conexión que estás cambiando para transportar su propio comando de recuperación.

:::single-choice{#networkmanager-modify-versus-up} ¿Cuál es la diferencia entre `connection modify` y `connection up`?

::option[Modify reinicia la máquina; up edita el código fuente de DNS.]{#networkmanager-reboot-source explanation="Ninguna descripción corresponde a los comandos."}
::option[Modify cambia los ajustes del perfil; up activa un perfil.]{#networkmanager-change-activate .correct explanation="La persistencia y la activación durante la ejecución son operaciones relacionadas, pero distintas."}
::option[Son alias de solo lectura que nunca pueden afectar a la conectividad.]{#networkmanager-readonly explanation="Ambos pueden modificar el estado en este flujo de trabajo."}
:::

## Comprobar y proteger los secretos

Después de la activación, comprueba el estado del perfil, las direcciones y rutas del kernel, DNS, ambas familias de direcciones y la aplicación prevista. Los perfiles de Wi-Fi, VPN, 802.1X y redes móviles pueden contener secretos. Limita los permisos de los perfiles y evita imprimir campos secretos en registros compartidos o transcripciones del shell.

:::single-choice{#networkmanager-verification} ¿Qué demuestra más que el estado «conectado» de NetworkManager?

::option[El nombre del perfil contiene la palabra Wired.]{#networkmanager-name-proof explanation="Una etiqueta no demuestra la salud de la ruta ni del servicio."}
::option[La ventana de terminal sigue abierta.]{#networkmanager-terminal-open explanation="Una terminal puede sobrevivir a algunos fallos parciales de red."}
::option[Las pruebas previstas de DNS y de la aplicación tienen éxito.]{#networkmanager-end-to-end .correct explanation="El estado del gestor debe correlacionarse con el comportamiento del kernel y del servicio."}
:::

## Resumen

Ahora puedes gestionar perfiles de NetworkManager sin confundirlos con objetos de interfaz.

1. Confirma que NetworkManager controla el dispositivo de destino.
2. Distingue los perfiles almacenados del estado activo durante la ejecución.
3. Inspecciona por separado los dispositivos, todos los perfiles y los perfiles activos.
4. Trata la modificación, la activación, la recuperación y la comprobación como pasos distintos.
