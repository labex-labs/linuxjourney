---
index: 1
lang: "es"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Aprende sobre las direcciones IPv4, su estructura y cómo encontrar tu IP usando ifconfig. Comprende los conceptos básicos de red para principiantes en Linux."
meta_keywords: "IPv4, dirección IP, ifconfig, conceptos básicos de red, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

Sabemos que los hosts de red tienen una dirección única en la que se pueden encontrar. Estas direcciones se conocen como direcciones IP. Una dirección IPv4 se ve algo así:

```
204.23.124.23
```

Esta dirección en realidad contiene dos partes: la porción de red que nos dice en qué red está, y la porción de host que nos dice qué host es en esa red. Para este curso, discutiremos principalmente las direcciones IPv4, que son las que comúnmente verá al referirse a las direcciones IP.

Una dirección IP está separada en octetos por puntos. Así que hay 4 octetos en una dirección IPv4. Si sabes un poco de informática, un octeto son 8 bits, y 8 bits en realidad equivalen a 1 byte, por lo que también nos referimos a una dirección IPv4 como si tuviera 4 bytes. Usamos bits con frecuencia cuando tratamos con subredes y direcciones IP.

Puedes ver tu dirección IP con el comando `ifconfig -a`:

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

Como puedes ver, mi dirección IPv4 es: 192.168.1.129

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del direccionamiento IP y la identificación de redes en Linux:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practica el uso del comando `ip a` para identificar información de direccionamiento de red, incluyendo direcciones IPv4 e IPv6, en un sistema Linux.
2. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explora diferentes tipos de direcciones IP y prueba la accesibilidad de la red usando comandos como `ping` e `ip a`.
3. **[Realizar subnetting IP y conversión binaria en la terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domina el subnetting IP y la conversión binaria, esenciales para una comprensión más profunda de cómo se estructuran las direcciones IP y las redes a nivel de bit.

Estos laboratorios te ayudarán a aplicar los conceptos de direccionamiento IP en escenarios reales y a ganar confianza con la configuración y resolución de problemas de red en Linux.

## Quiz Question

¿Cuántos bytes hay en una dirección IPv4?

## Quiz Answer

4
