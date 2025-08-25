---
index: 2
lang: "es"
title: "Tabla de Enrutamiento"
meta_title: "Tabla de Enrutamiento - Enrutamiento"
meta_description: "Aprenda a comprender la tabla de enrutamiento de Linux y cómo se enrutan los paquetes usando el comando route. Explore destinos, puertas de enlace e interfaces para los conceptos básicos de red."
meta_keywords: "tabla de enrutamiento de Linux, comando route, enrutamiento de red, redes en Linux, Linux para principiantes, tutorial de Linux, guía de red"
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

### Destino

En el primer campo, tenemos una dirección IP de destino de 192.168.224.0. Esto indica que cualquier paquete que intente ir a esta red sale a través de mi cable Ethernet (eth0). Si yo fuera 192.168.224.5 y quisiera llegar a 192.168.224.7, simplemente usaría la interfaz de red eth0 directamente.

Observe que tenemos direcciones de **0.0.0.0**. Esto significa que no se especifica ninguna dirección o que es desconocida. Entonces, si por ejemplo, quisiera enviar un paquete a la dirección IP 151.123.43.6, nuestra tabla de enrutamiento no sabe a dónde va, por lo que lo denota como 0.0.0.0 y, por lo tanto, enruta nuestro paquete a la Puerta de Enlace (Gateway).

### Puerta de Enlace

Si estamos enviando un paquete que no está en la misma red, se enviará a esta dirección de Puerta de Enlace, que se denomina apropiadamente como una Puerta de Enlace a otra red.

### Máscara de Generación (Genmask)

Esta es la máscara de subred, utilizada para determinar qué direcciones IP coinciden con qué destino.

### Banderas (Flags)

- UG - La red está activa (Up) y es una Puerta de Enlace (Gateway)
- U - La red está activa (Up)

### Interfaz (Iface)

Esta es la interfaz por la que saldrá nuestro paquete. `eth0` generalmente representa el primer dispositivo Ethernet en su sistema.

## Exercise

¡La práctica hace al maestro! Aquí tiene algunos laboratorios prácticos para reforzar su comprensión del enrutamiento de red y el direccionamiento IP:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluyendo direcciones IP e interfaces de red, que son componentes clave de una tabla de enrutamiento.
2. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/linux-manage-ip-addressing-in-linux-592736)** - Aprenda a administrar el direccionamiento IP, configurar IPs estáticas, establecer puertas de enlace predeterminadas y verificar configuraciones de red, lo que se relaciona directamente con las entradas encontradas en una tabla de enrutamiento.
3. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore el direccionamiento IP y la accesibilidad de la red usando `ping` e `ip a`, lo que le ayudará a comprender cómo interactúan los diferentes tipos de IP y cómo se determina la accesibilidad de la red, lo cual se refleja en las decisiones de enrutamiento.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con la configuración y resolución de problemas de red.

## Quiz Question

¿A dónde se enrutan los paquetes si nuestra tabla de enrutamiento no lo sabe?

## Quiz Answer

Gateway
