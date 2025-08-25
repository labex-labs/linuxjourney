---
index: 5
lang: "es"
title: "arp"
meta_title: "arp - Configuración de red"
meta_description: "Aprende sobre el comando ARP de Linux y cómo ver tu caché ARP. Comprende el papel de ARP en la comunicación de red. Una guía para principiantes de ARP."
meta_keywords: "Linux ARP, caché ARP, ip neighbour show, comandos de red, redes Linux, Linux para principiantes, tutorial de Linux"
---

## Lesson Content

Recuerda que cuando buscamos una dirección MAC con ARP, primero verifica la caché ARP almacenada localmente en nuestro sistema. De hecho, puedes ver esta caché:

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

La caché ARP está realmente vacía cuando una máquina arranca; se llena a medida que se envían paquetes a otros hosts. Si enviamos un paquete a un destino que no está en la caché ARP, sucede lo siguiente:

1. El host de origen crea la trama Ethernet con un paquete de solicitud ARP.
2. El host de origen transmite esta trama a toda la red.
3. Si uno de los hosts de la red conoce la dirección MAC correcta, enviará un paquete de respuesta y una trama que contenga la dirección MAC.
4. El host de origen agrega la asignación de IP a dirección MAC a la caché ARP y luego procede con el envío del paquete.

También puedes ver tu caché ARP a través del comando `ip`:

```bash
ip neighbour show
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de ARP y la interacción de la capa de red:

1. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Usa los comandos `ping` y `arp` para observar cómo las direcciones IP se resuelven en direcciones MAC y cómo la puerta de enlace predeterminada maneja el tráfico.
2. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Aprende a usar el comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones MAC e IP, que son fundamentales para comprender ARP.
3. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/linux-manage-ip-addressing-in-linux-592736)** - Practica la administración del direccionamiento IP usando el comando `ip` y verifica la configuración de red con `arp` y `traceroute`.

Estos laboratorios te ayudarán a aplicar los conceptos de ARP y direccionamiento de red en escenarios reales y a generar confianza con las redes Linux.

## Quiz Question

¿Qué comando puedes usar para ver tu caché ARP?

## Quiz Answer

arp
