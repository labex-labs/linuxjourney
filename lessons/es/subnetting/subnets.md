---
lang: "es"
title: "Subnets"
meta_description: "Aprende sobre subnets y subnet masks en redes Linux. Comprende los prefijos de red y cómo las subnets segmentan el tráfico. ¡Empieza con esta guía para principiantes!"
meta_keywords: "subnets, subnet mask, network prefix, Linux networking, IP address, principiante, tutorial, ifconfig"
---

## Lesson Content

¿Cómo puedo saber si estoy en la misma red que Patty? Bueno, podemos simplemente mirar la subnet, abreviatura de subred. Una subnet es un grupo de hosts con direcciones IP que son similares de cierta manera. Estos hosts suelen estar en una ubicación próxima entre sí, y puedes enviar datos fácilmente a y desde hosts en la misma subnet. Piensa en ello como enviar correo en el mismo código postal; es mucho más fácil que enviar correo a un estado diferente.

Por ejemplo, todos los hosts con una dirección IP que comienza con 123.45.67 estarían en la misma subnet. Mi host tiene una IP de 123.45.67.8, y el de Patty tiene una IP de 123.45.67.9. Los números comunes son mi network prefix, y el 8 y el 9 son nuestros hosts; por lo tanto, mi red es la misma que la de Patty. Una subnet se divide en un network prefix, como 123.45.67.0, y una subnet mask.

### Subnet Masks

Las subnet masks determinan qué parte de tu dirección IP es la porción de red y qué parte es la porción de host.

Una subnet mask típica puede verse algo así:

```plaintext
255.255.255.0
```

La porción 255 es en realidad nuestra mask. Para que esto sea un poco más fácil de entender, ¿recuerdas cómo nos referimos a cada octeto como 8 bits? En ciencias de la computación, un bit se denota con un 0 o un 1 en forma binaria. Cuando se usan números binarios, 1 significa encendido y 0 significa apagado. Entonces, ¿a qué equivalen 8 ceros u 8 unos?

Busca en Google "calculadora binario a decimal" y convierte 11111111 a forma decimal. ¿Qué obtienes? ¡255! Así que un octeto varía de 0 a 255. Entonces, si tuviéramos una subnet mask de 255.255.255.0, y una dirección IP de 192.168.1.0, ¿cuántos hosts hay en esa subnet? Descubriremos la respuesta a eso en nuestra lección de matemáticas de subredes.

Además, cuando hablamos de nuestra subnet, comúnmente la denotamos por el network prefix seguido de la subnet mask:

```plaintext
123.234.0.0/255.255.0.0
```

### Why?

¿Por qué diablos hacemos subnets? El subnetting se utiliza para segmentar redes y controlar el flujo de tráfico dentro de esa red. Así, un host en una subnet no puede interactuar con otro host en una subnet diferente.

Pero espera un minuto, ¿qué pasa si quiero conectarme a otros hosts como yahoo.com? Entonces necesitas conectar subnets entre sí. Para conectar subnets, solo necesitas encontrar los hosts que están conectados a más de una subnet. Por ejemplo, si mi host en 192.168.1.129 está conectado a una red local de 192.168.1.129/24, puede alcanzar cualquier host en esa red. Para alcanzar hosts en el resto de Internet, necesita comunicarse a través del router. Tradicionalmente, en la mayoría de las redes con una subnet mask de 255.255.255.0, el router suele estar en la dirección 1 de la subnet, es decir, 192.168.1.1. Ahora ese router tendrá un puerto que lo conecta a otra subnet (más en el curso de Routing). Ciertas direcciones IP (private networks) no son visibles para Internet, y tenemos cosas como NAT (más sobre esto más adelante).

## Exercise

Use `ifconfig` para ver su subnet mask.

## Quiz Question

Verdadero o falso, una subnet consiste en una subnet mask y un network prefix.

## Quiz Answer

True
