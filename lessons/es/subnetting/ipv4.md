---
index: 1
lang: "es"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Comienza tu viaje con nuestro tutorial completo de Linux sobre direcciones IPv4. Esta guía para usuarios principiantes de Linux es la mejor manera de aprender redes en Linux, cubriendo la estructura IP y herramientas esenciales de línea de comandos como ip addr."
meta_keywords: "IPv4, dirección IP, linux para principiantes, mejor forma de aprender linux, tutorial completo de linux, mejor curso de linux online gratis, cursos de certificación linux gratis, redes linux, ifconfig, ip addr"
---

## Lesson Content

Todo dispositivo en una red tiene un identificador único llamado dirección IP (Protocolo de Internet). Esta lección, una parte clave de nuestro `tutorial completo de linux`, se centra en las direcciones IPv4, el tipo más común que encontrará. Para cualquier `usuario principiante de linux`, comprender IPv4 es un primer paso fundamental en el mundo de las redes.

### Por qué IPv4 es Esencial

Aprender sobre IPv4 es fundamental para cualquiera que se tome en serio la administración de sistemas o la gestión de redes. Constituye la columna vertebral de la mayor parte de la comunicación de red. Esta guía ofrece la `mejor manera de aprender linux` networking desde cero. Si bien este no es uno de esos `cursos gratuitos de certificación linux`, dominar estos conceptos básicos es un paso clave hacia la certificación profesional.

### Estructura de la Dirección IPv4

Una dirección IPv4 es un número de 32 bits, pero generalmente se muestra en un formato legible para humanos como este:

```
204.23.124.23
```

Esta dirección tiene dos partes principales: la **porción de red**, que identifica la red, y la **porción de host**, que identifica el dispositivo específico en esa red. La dirección se divide en cuatro secciones separadas por puntos, y cada sección se denomina **octeto**. Un octeto es un grupo de 8 bits, lo que significa que una dirección IPv4 tiene 4 bytes (32 bits) de longitud. Comprender esta estructura es crucial para la configuración y solución de problemas de red.

### Encontrar su Dirección IP

Una de las primeras tareas para cualquier usuario de Linux es encontrar la dirección IP de su sistema. Puede hacerlo utilizando herramientas sencillas de línea de comandos. El comando tradicional para esto es `ifconfig`. Aunque todavía se encuentra en muchos sistemas, se considera una herramienta heredada.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

En la salida anterior, la dirección IPv4 es `192.168.1.129`.

### Uso del Comando ip addr

El método moderno y recomendado utiliza el comando `ip`. El comando `ip addr` ha reemplazado a `ifconfig` y es el estándar en la mayoría de las distribuciones Linux actuales. Proporciona información más detallada y es la herramienta en la que debe centrarse en aprender.

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

Aquí, puede encontrar la misma dirección IPv4, `192.168.1.129`, listada junto a `inet` para la interfaz `eth0`.

## Exercise

Practique sus habilidades con estos laboratorios prácticos para reforzar su comprensión del direccionamiento IP y la identificación de red en Linux:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones IPv4 e IPv6, en un sistema Linux.
2. **[Explorar tipos de direcciones IP y capacidad de alcance en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de direcciones IP y pruebe la capacidad de alcance de la red utilizando comandos como `ping` y `ip a`.
3. **[Realizar subnetting IP y conversión binaria en la terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine el subnetting IP y la conversión binaria, esenciales para una comprensión más profunda de cómo se estructuran las direcciones y redes IP a nivel de bit.

Estos laboratorios le ayudarán a aplicar los conceptos de direccionamiento IP en escenarios reales y a ganar confianza con la configuración y solución de problemas de red en Linux.

## Quiz Question

¿Cuántos bytes hay en una dirección IPv4?

## Quiz Answer

4
