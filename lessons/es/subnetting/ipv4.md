---
index: 1
lang: "es"
title: "IPv4"
meta_title: "IPv4 - Subnetting"
meta_description: "Descubra la mejor manera de aprender redes Linux entendiendo las direcciones IPv4. Esta guía para principiantes cubre la estructura de IP y cómo encontrar su IP usando la línea de comandos."
meta_keywords: "IPv4, dirección IP, linux para principiantes, mejor forma de aprender linux, línea de comandos linux para principiantes, ifconfig, ip addr, conceptos básicos de red"
---

## Lesson Content

Cada dispositivo conectado a una red tiene una dirección única, conocida como dirección IP (Protocolo de Internet). Para este curso, nos centraremos en las direcciones IPv4, que son el tipo más común que encontrará. Comprenderlas es una parte fundamental del aprendizaje de redes en Linux.

Una dirección IPv4 es un número de 32 bits que normalmente se representa en un formato legible para humanos, como este:

```
204.23.124.23
```

Esta dirección contiene dos partes distintas: la porción de **red**, que identifica la red específica en la que se encuentra el dispositivo, y la porción de **host**, que identifica el dispositivo específico en esa red.

### La Estructura de una Dirección IP

Una dirección IPv4 se divide en cuatro secciones separadas por puntos. Cada sección se denomina **octeto**. En informática, un octeto es un grupo de 8 bits, y dado que 8 bits equivalen a 1 byte, una dirección IPv4 tiene 4 bytes de longitud. Esta estructura es fundamental, y dominarla es uno de los `mejores recursos para aprender la línea de comandos de linux para principiantes` en redes.

### Encontrar su Dirección IP en Linux

Para cualquier usuario de `beginner linux` (linux para principiantes), una de las primeras tareas es encontrar la dirección IP del sistema. Puede hacerlo utilizando herramientas de línea de comandos.

El comando tradicional para esto es `ifconfig`. Aunque todavía se encuentra en muchos sistemas, se considera una herramienta heredada (legacy).

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

En la salida anterior, la dirección IPv4 es `192.168.1.129`.

### El Enfoque Moderno con ip addr

La `mejor manera de aprender linux` en redes hoy en día implica el uso del comando moderno `ip`. El comando `ip addr` ha reemplazado a `ifconfig` y es el estándar en la mayoría de las distribuciones Linux actuales.

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

Practique sus habilidades con estos laboratorios prácticos para reforzar su comprensión del direccionamiento IP y la identificación de redes en Linux:

1. **[Identificar Direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones IPv4 e IPv6, en un sistema Linux.
2. **[Explorar Tipos de Direcciones IP y Alcance de Red en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de direcciones IP y pruebe el alcance de la red utilizando comandos como `ping` e `ip a`.
3. **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine el subnetting IP y la conversión binaria, esenciales para una comprensión más profunda de cómo se estructuran las direcciones IP y las redes a nivel de bit.

Estos laboratorios le ayudarán a aplicar los conceptos de direccionamiento IP en escenarios reales y a ganar confianza con la configuración y solución de problemas de red en Linux.

## Quiz Question

¿Cuántos bytes tiene una dirección IPv4?

## Quiz Answer

4
