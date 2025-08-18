---
index: 2
lang: "es"
title: "Tabla de Enrutamiento"
meta_title: "Tabla de Enrutamiento - Enrutamiento"
meta_description: "Aprenda a comprender la tabla de enrutamiento de Linux y cómo se enrutan los paquetes usando el comando route. Explore destinos, gateways e interfaces para los conceptos básicos de la red."
meta_keywords: "tabla de enrutamiento de Linux, comando route, enrutamiento de red, redes Linux, Linux para principiantes, tutorial de Linux, guía de red"
---

## Lesson Content

Observe la tabla de enrutamiento de su máquina:

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Destination

En el primer campo, tenemos una dirección IP de destino de 192.168.224.0. Esto significa que cualquier paquete que intente ir a esta red sale a través de mi cable Ethernet (eth0). Si yo fuera 192.168.224.5 y quisiera llegar a 192.168.224.7, simplemente usaría la interfaz de red eth0 directamente.

Observe que tenemos direcciones de **0.0.0.0**. Esto significa que no se especifica ninguna dirección o es desconocida. Entonces, si por ejemplo, quisiera enviar un paquete a la dirección IP 151.123.43.6, nuestra tabla de enrutamiento no sabe a dónde va, por lo que la denota como 0.0.0.0 y, por lo tanto, enruta nuestro paquete al Gateway.

### Gateway

Si estamos enviando un paquete que no está en la misma red, se enviará a esta dirección Gateway, que se denomina acertadamente como una puerta de enlace a otra red.

### Genmask

Esta es la subnet mask, utilizada para determinar qué direcciones IP coinciden con qué destino.

### Flags

- UG - Network is Up and is a Gateway
- U - Network is Up

### Iface

Esta es la interfaz por la que saldrá nuestro paquete. eth0 generalmente representa el primer dispositivo Ethernet en su sistema.

## Exercise

Observe su tabla de enrutamiento y vea a dónde pueden ir sus paquetes.

## Quiz Question

¿A dónde se enrutan los paquetes si nuestra tabla de enrutamiento no lo sabe?

## Quiz Answer

Gateway
