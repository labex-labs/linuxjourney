---
index: 6
lang: "es"
title: "NAT"
meta_title: "NAT - Subnetting"
meta_description: "Aprenda sobre NAT (Network Address Translation) en Linux, cómo funciona y su papel en la seguridad de la red. Comprenda las IP privadas vs. públicas. Guía de redes de Linux."
meta_keywords: "NAT, Network Address Translation, redes Linux, IP privada, IP pública, tutorial Linux, guía para principiantes"
---

## Lesson Content

Hemos mencionado NAT (Network Address Translation) antes, pero no lo hemos abordado. Cuando estamos trabajando en nuestra red, ¿significa eso que internet puede ver nuestra dirección IP? No exactamente.

NAT hace que un dispositivo como nuestro router actúe como intermediario entre internet y una red privada. Así, solo se requiere una única dirección IP para representar a todo un grupo de computadoras.

Piense en NAT como una recepcionista en una oficina grande. Si alguien quiere contactarlo, solo conoce el número de toda la oficina. La recepcionista tendría que buscar su número de extensión y reenviarle la llamada.

### How does it work?

Un caso simple se vería así:

1. Patty quiere conectarse a <www.google.com>, por lo que su máquina envía esta solicitud a través del router.
2. El router toma esa solicitud y abre su propia conexión a google.com, luego envía la solicitud de Patty una vez que establece una conexión.
3. El router es el intermediario entre Patty y <www.google.com>. Google no sabe de Patty; en cambio, todo lo que puede ver es el router.

NAT y el enrutamiento de paquetes en general pueden volverse bastante complicados, pero no profundizaremos en los detalles.

## Exercise

No hay ejercicios para esta lección.

## Quiz Question

¿Qué se utiliza para representar una única dirección privada a internet?

## Quiz Answer

NAT
