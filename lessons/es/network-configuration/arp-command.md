---
lang: "es"
title: "arp"
meta_description: "Aprende sobre el comando Linux ARP y cómo ver tu caché ARP. Comprende el papel de ARP en la comunicación de red. Una guía para principiantes de ARP."
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
2. El host de origen difunde esta trama a toda la red.
3. Si uno de los hosts de la red conoce la dirección MAC correcta, enviará un paquete de respuesta y una trama que contenga la dirección MAC.
4. El host de origen agrega la asignación de IP a dirección MAC a la caché ARP y luego procede con el envío del paquete.

También puedes ver tu caché ARP a través del comando `ip`:

```bash
ip neighbour show
```

## Exercise

Observa qué sucede con tu caché ARP cuando reinicias tu máquina y luego haces algo en la red.

## Quiz Question

¿Qué comando puedes usar para ver tu caché ARP?

## Quiz Answer

arp
