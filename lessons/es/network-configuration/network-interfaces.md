---
index: 1
lang: "es"
title: "Interfaces de red"
meta_title: "Interfaces de red - Configuración de red"
meta_description: "Aprenda sobre las interfaces de red de Linux, ifconfig y los comandos ip. Comprenda cómo configurar y administrar la configuración de red. ¡Comience su viaje en redes Linux!"
meta_keywords: "interfaces de red Linux, ifconfig, comando ip, configuración de red, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

Una interfaz de red es cómo el kernel enlaza el lado del software de la red con el lado del hardware. Ya hemos visto un ejemplo de esto:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### El comando ifconfig

La herramienta **ifconfig** nos permite configurar nuestras interfaces de red. Si no tenemos ninguna interfaz de red configurada, los controladores de dispositivo del kernel y la red no sabrán cómo comunicarse entre sí. Ifconfig se ejecuta al arrancar y configura nuestras interfaces a través de archivos de configuración, pero también podemos modificarlas manualmente. La salida de ifconfig muestra el nombre de la interfaz en el lado izquierdo, y el lado derecho muestra información detallada. Lo más común es ver interfaces llamadas eth0 (primera tarjeta Ethernet en la máquina), wlan0 (interfaz inalámbrica) y lo (interfaz de bucle invertido). La interfaz de bucle invertido se utiliza para representar su computadora; simplemente lo devuelve a usted mismo. Esto es bueno para depurar o conectarse a servidores que se ejecutan localmente.

El estado de las interfaces puede ser "up" (activo) o "down" (inactivo). Como puede suponer, si quisiera "apagar" una interfaz, puede configurarla para que se desactive. Los campos que probablemente verá más en la salida de ifconfig son HWaddr (dirección MAC de la interfaz), inet address (dirección IPv4) e inet6 (dirección IPv6). Por supuesto, puede ver que la máscara de subred y la dirección de difusión también están allí. También puede ver la información de la interfaz en /etc/network/interfaces.

### Para crear una interfaz y activarla

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Esto asigna una dirección IP y una máscara de red a la interfaz eth0 y también la activa.

### Para activar o desactivar una interfaz

```bash
ifup eth0
ifdown eth0
```

### El comando ip

El comando **ip** también nos permite manipular la pila de red de un sistema. Dependiendo de la distribución que esté utilizando, puede ser el método preferido para manipular la configuración de su red.

Aquí hay algunos ejemplos de su uso:

### Para mostrar información de todas las interfaces

```bash
ip link show
```

### Para mostrar las estadísticas de una interfaz

```bash
ip -s link show eth0
```

### Para mostrar las direcciones IP asignadas a las interfaces

```bash
ip address show
```

### Para activar y desactivar interfaces

```bash
ip link set eth0 up
ip link set eth0 down
```

### Para añadir una dirección IP a una interfaz

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de las interfaces de red y el direccionamiento IP:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluyendo direcciones MAC, IPv4 e IPv6 en un sistema Linux.
2. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a configurar direcciones IP estáticas y dinámicas, establecer una puerta de enlace predeterminada y verificar las configuraciones de red usando el comando `ip`.
3. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de direcciones IP (privadas, públicas, multidifusión) y pruebe la accesibilidad de la red usando `ping` e `ip a`.

Estos laboratorios le ayudarán a aplicar los conceptos de identificación de interfaz de red y direccionamiento IP en escenarios reales y a generar confianza con las redes Linux.

## Quiz Question

¿Cuál es el comando para configurar nuestras interfaces de red?

## Quiz Answer

ifconfig
