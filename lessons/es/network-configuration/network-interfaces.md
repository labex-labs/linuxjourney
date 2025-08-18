---
lang: "es"
title: "Interfaces de Red"
meta_description: "Aprende sobre las interfaces de red de Linux, ifconfig y los comandos ip. Comprende cómo configurar y gestionar los ajustes de red. ¡Comienza tu viaje en las redes de Linux!"
meta_keywords: "interfaces de red de Linux, ifconfig, comando ip, configuración de red, redes de Linux, principiante, tutorial, guía"
---

## Lesson Content

Una interfaz de red es cómo el kernel enlaza el lado del software de la red con el lado del hardware. Ya hemos visto un ejemplo de esto:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### The ifconfig command

La herramienta **ifconfig** nos permite configurar nuestras interfaces de red. Si no tenemos ninguna interfaz de red configurada, los device drivers del kernel y la red no sabrán cómo comunicarse entre sí. Ifconfig se ejecuta al iniciar y configura nuestras interfaces a través de config files, pero también podemos modificarlas manualmente. La salida de ifconfig muestra el nombre de la interfaz en el lado izquierdo, y el lado derecho muestra información detallada. Lo más común es que veas interfaces llamadas eth0 (primera tarjeta Ethernet en la máquina), wlan0 (interfaz inalámbrica) y lo (interfaz de loopback). La interfaz de loopback se utiliza para representar tu computadora; simplemente te devuelve a ti mismo. Esto es bueno para depurar o conectarse a servers que se ejecutan localmente.

El estado de las interfaces puede ser up o down. Como puedes adivinar, si quisieras "apagar" una interfaz, puedes configurarla para que baje. Los campos que probablemente mirarás más en la salida de ifconfig son el HWaddr (MAC address de la interfaz), inet address (IPv4 address) e inet6 (IPv6 address). Por supuesto, puedes ver que la subnet mask y la broadcast address también están allí. También puedes ver la información de la interfaz en /etc/network/interfaces.

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Esto asigna una IP address y netmask a la interfaz eth0 y también la activa.

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

El comando **ip** también nos permite manipular el networking stack de un sistema. Dependiendo de la distribución que estés utilizando, puede ser el método preferido para manipular tus network settings.

Aquí hay algunos ejemplos de su uso:

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

Intenta cambiar el estado de tus network interfaces a up o down y observa qué sucede.

¿Puedes cambiar tus network interfaces con los comandos ifconfig e ip?

## Quiz Question

¿Cuál es el comando para configurar nuestras interfaces de red?

## Quiz Answer

ifconfig
