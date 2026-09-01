---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "es"
order_index: 1
title: "Interfaces de red"
description: "Aprende a inspeccionar el estado, las direcciones, las estadísticas y la propiedad de la configuración persistente de las interfaces Linux."
meta_title: "Interfaces de red - Network Config"
meta_description: "Guía completa sobre las interfaces de red de Linux. Aprende a usar ifconfig y el comando moderno ip, y comprende archivos de configuración como /etc/network/interfaces, especialmente en sistemas Debian."
meta_keywords: "interfaz linux, interfaz de red linux, etc network interfaces, interfaces de red debian, ifconfig, comando ip, configuración de red, redes linux"
---

Una interfaz de red de Linux conecta un espacio de nombres de red con un dispositivo físico, una ruta loopback, un puente, un túnel, un dispositivo virtual u otro enlace. El estado de la interfaz, las direcciones, las rutas, DNS y la configuración persistente están relacionados, pero son aspectos distintos.

## Descubrir interfaces

Utiliza las herramientas modernas de iproute2:

```bash
$ ip -brief link show
$ ip -brief address show
```

Las interfaces pueden tener nombres predecibles derivados del hardware, como `enp1s0`, nombres tradicionales, como `eth0`, o nombres definidos por el administrador. Nunca supongas que existe `eth0` o que identifica un adaptador concreto.

:::single-choice{#interfaces-name-assumption} ¿Por qué debe un script descubrir la interfaz en lugar de suponer que es `eth0`?

::option[Todas las interfaces deben llamarse `lo`.]{#interfaces-all-loopback explanation="Loopback es una interfaz especial, no el nombre de todos los enlaces."}
::option[Los sistemas Linux pueden utilizar varios esquemas de nombres de interfaces.]{#interfaces-naming-varies .correct explanation="Los nombres derivados del hardware, virtuales y personalizados hacen que suponer `eth0` no sea fiable."}
::option[Los nombres de interfaces siempre son contraseñas remotas.]{#interfaces-name-password explanation="Los nombres identifican dispositivos del kernel y no son credenciales."}
:::

## Estado administrativo y operativo

`UP` significa que la interfaz está habilitada administrativamente. `LOWER_UP` suele indicar que la capa inferior informa de disponibilidad operativa, como la señal portadora de Ethernet. Ninguno de los indicadores por sí solo demuestra que funcionen una dirección IP, una ruta, DNS, un cortafuegos o la ruta de una aplicación.

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

La vista de estadísticas puede revelar errores, descartes y contadores, pero los contadores necesitan un intervalo de tiempo y un valor de referencia para resultar significativos.

:::single-choice{#interfaces-up-limit} ¿Qué no demuestra el estado administrativo `UP`?

::option[Que funcione la conectividad de extremo a extremo.]{#interfaces-up-not-connectivity .correct explanation="Aún puede haber fallos de capas inferiores, direccionamiento, enrutamiento, filtrado, nombres y servicios."}
::option[Que el administrador habilitó la interfaz.]{#interfaces-up-does-prove explanation="Ese es el significado directo del estado."}
::option[Que la interfaz tiene un objeto en el kernel.]{#interfaces-up-kernel-object explanation="El estado mostrado pertenece a una interfaz existente del kernel."}
:::

## Cambiar el estado durante la ejecución

Entre los comandos que modifican el estado activo se encuentran:

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

Estos cambios afectan al estado actual del kernel y pueden entrar en conflicto con un gestor de red que posteriormente vuelva a aplicar su perfil. Desactivar una interfaz de administración remota puede terminar el acceso de inmediato. Antes de cambiarla, comprueba el dispositivo exacto, conserva el acceso mediante consola, registra el estado actual y prepara una reversión temporizada o probada.

:::single-choice{#interfaces-ip-address-add-persistence} ¿Garantiza por sí solo `ip address add` que el cambio persista después de reiniciar?

::option[No; el sistema de configuración activo también debe almacenar el ajuste.]{#interfaces-manager-persistence .correct explanation="NetworkManager, systemd-networkd, ifupdown u otro propietario aplican la política persistente."}
::option[Sí, porque todos los cambios del kernel editan todos los perfiles de los gestores.]{#interfaces-runtime-always-persistent explanation="Los cambios del kernel durante la ejecución no actualizan universalmente la configuración persistente."}
::option[Únicamente cuando la dirección es una IPv4 privada.]{#interfaces-private-persistent explanation="El ámbito de la dirección no convierte un comando de ejecución en persistente."}
:::

## Identificar quién controla la configuración

Las rutas persistentes difieren entre distribuciones e instalaciones. Entre las posibilidades se encuentran los perfiles de NetworkManager, las unidades de systemd-networkd, la entrada de netplan, `/etc/network/interfaces`, cloud-init o un sistema de orquestación. Determina qué servicio gestiona el dispositivo antes de editar archivos:

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

Utiliza únicamente los comandos disponibles para el gestor identificado. Dos gestores que controlen el mismo enlace pueden competir y sobrescribir mutuamente su estado.

:::single-choice{#interfaces-config-owner} ¿Qué debe hacerse antes de cambiar de forma persistente una interfaz?

::option[Editar todos los archivos posibles de configuración de red.]{#interfaces-edit-all explanation="Las definiciones que compiten crean conflictos y reaplicaciones impredecibles."}
::option[Identificar qué gestor de red controla la interfaz.]{#interfaces-identify-owner .correct explanation="La fuente correcta de configuración y el método de aplicación dependen de ese control."}
::option[Eliminar todas las rutas actuales antes de inspeccionarlas.]{#interfaces-delete-routes explanation="Es una acción destructiva que puede eliminar el acceso de recuperación."}
:::

## Comprobar un cambio

Comprueba el estado del enlace, las direcciones asignadas y su duración, las rutas seleccionadas, el estado del resolver, la accesibilidad de los vecinos y la aplicación real. Para un cambio persistente, prueba un reinicio controlado del servicio o del sistema solo cuando exista una vía de recuperación.

:::single-choice{#interfaces-change-verification} ¿Qué proporciona pruebas mejores que ver la dirección nueva en `ip address`?

::option[El nombre de la interfaz contiene un dígito.]{#interfaces-digit explanation="El nombre no proporciona ninguna validación de extremo a extremo."}
::option[El indicador del shell conserva el mismo color.]{#interfaces-prompt-color explanation="El aspecto de la terminal no está relacionado con el funcionamiento de la red."}
::option[También funcionan las rutas, el estado del resolver y la aplicación prevista.]{#interfaces-end-to-end .correct explanation="Una configuración utilizable depende de toda la ruta y del comportamiento del servicio."}
:::

## Resumen

Ahora puedes inspeccionar y cambiar una interfaz sin confundir el estado durante la ejecución con la política persistente.

1. Descubre los nombres y las direcciones reales de las interfaces.
2. Distingue el estado administrativo de la conectividad operativa.
3. Trata los cambios directos mediante `ip` como estado actual del kernel.
4. Identifica al propietario activo de la configuración antes de realizar cambios persistentes.
5. Comprueba después el enrutamiento, la resolución y el comportamiento de la aplicación.
