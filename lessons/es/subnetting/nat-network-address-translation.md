---
index: 6
lang: "es"
title: "NAT"
meta_title: "NAT - Subredes"
meta_description: "Aprenda sobre NAT (Network Address Translation) en Linux, cómo funciona y su papel en la seguridad de la red. Comprenda las IPs privadas vs. públicas. Guía de redes de Linux."
meta_keywords: "NAT, Network Address Translation, redes Linux, IP privada, IP pública, tutorial Linux, guía para principiantes"
---

## Lesson Content

Ya hemos mencionado NAT (Network Address Translation) antes, pero no lo habíamos abordado. Cuando estamos trabajando en nuestra red, ¿significa eso que internet puede ver nuestra dirección IP? No exactamente.

NAT hace que un dispositivo como nuestro router actúe como intermediario entre internet y una red privada. Así, solo se requiere una única dirección IP para representar a todo un grupo de computadoras.

Piense en NAT como una recepcionista en una oficina grande. Si alguien quiere contactarlo, solo conoce el número de toda la oficina. La recepcionista tendría que buscar su número de extensión y reenviarle la llamada.

### ¿Cómo funciona?

Un caso simple se vería así:

1. Patty quiere conectarse a `www.google.com`, por lo que su máquina envía esta solicitud a través del router.
2. El router toma esa solicitud y abre su propia conexión a google.com, luego envía la solicitud de Patty una vez que establece una conexión.
3. El router es el intermediario entre Patty y `www.google.com`. Google no sabe de Patty; en cambio, todo lo que puede ver es el router.

NAT y el enrutamiento de paquetes en general pueden ser bastante complicados, pero no profundizaremos en los detalles.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del direccionamiento de red y la conectividad, que son fundamentales para comprender conceptos como NAT:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones IPv4 e IPv6, en un sistema Linux.
2. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/linux-manage-ip-addressing-in-linux-592736)** - Aprenda a administrar el direccionamiento IP configurando IPs estáticas y dinámicas, y verificando la configuración de red, lo que ayuda a comprender cómo los dispositivos obtienen sus direcciones.
3. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de direcciones IP (privadas, públicas, multidifusión) y pruebe la accesibilidad de la red, proporcionando un contexto práctico de cómo NAT distingue entre direcciones internas y externas.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la configuración y resolución de problemas de red en Linux.

## Quiz Question

¿Qué se utiliza para representar una única dirección privada a internet?

## Quiz Answer

NAT
