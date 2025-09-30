---
index: 2
lang: "es"
title: "Subredes"
meta_title: "Subredes - Subnetting"
meta_description: "Aprende sobre subredes y máscaras de subred en redes Linux. Comprende los prefijos de red y cómo las subredes segmentan el tráfico. ¡Empieza con esta guía para principiantes!"
meta_keywords: "subredes, máscara de subred, prefijo de red, redes Linux, dirección IP, principiante, tutorial, ifconfig"
---

## Lesson Content

¿Cómo puedo saber si estoy en la misma red que Patty? Bueno, podemos simplemente mirar la subred, abreviatura de subnetwork. Una subred es un grupo de hosts con direcciones IP que son similares de cierta manera. Estos hosts suelen estar en una ubicación cercana entre sí, y puedes enviar datos fácilmente hacia y desde hosts en la misma subred. Piénsalo como enviar correo en el mismo código postal; es mucho más fácil que enviar correo a un estado diferente.

Por ejemplo, todos los hosts con una dirección IP que comienza con 123.45.67 estarían en la misma subred. Mi host tiene una IP de 123.45.67.8, y el de Patty tiene una IP de 123.45.67.9. Los números comunes son mi prefijo de red, y el 8 y el 9 son nuestros hosts; por lo tanto, mi red es la misma que la de Patty. Una subred se divide en un prefijo de red, como 123.45.67.0, y una máscara de subred.

### Máscaras de subred

Las máscaras de subred determinan qué parte de tu dirección IP es la porción de red y qué parte es la porción de host.

Una máscara de subred típica puede verse así:

```plaintext
255.255.255.0
```

La porción 255 es en realidad nuestra máscara. Para que esto sea un poco más fácil de entender, ¿recuerdas cómo nos referimos a cada octeto como 8 bits? En ciencias de la computación, un bit se denota con un 0 o un 1 en formato binario. Cuando se usan números binarios, 1 significa encendido y 0 significa apagado. Entonces, ¿a qué equivalen 8 ceros o unos?

Busca en Google "calculadora binario a decimal" y convierte 11111111 a formato decimal. ¿Qué obtienes? ¡255! Así que un octeto va de 0 a 255. Entonces, si tuviéramos una máscara de subred de 255.255.255.0 y una dirección IP de 192.168.1.0, ¿cuántos hosts hay en esa subred? Descubriremos la respuesta a eso en nuestra lección de matemáticas de subredes.

Además, cuando hablamos de nuestra subred, comúnmente la denotamos por el prefijo de red seguido de la máscara de subred:

```plaintext
123.234.0.0/255.255.0.0
```

### ¿Por qué?

¿Por qué diablos hacemos subredes? El subnetting se utiliza para segmentar redes y controlar el flujo de tráfico dentro de esa red. Así, un host en una subred no puede interactuar con otro host en una subred diferente.

Pero espera un minuto, ¿qué pasa si quiero conectarme a otros hosts como yahoo.com? Entonces necesitas conectar subredes entre sí. Para conectar subredes, solo necesitas encontrar los hosts que están conectados a más de una subred. Por ejemplo, si mi host en 192.168.1.129 está conectado a una red local de 192.168.1.129/24, puede alcanzar cualquier host en esa red. Para alcanzar hosts en el resto de Internet, necesita comunicarse a través del router. Tradicionalmente, en la mayoría de las redes con una máscara de subred de 255.255.255.0, el router suele estar en la dirección 1 de la subred, es decir, 192.168.1.1. Ahora ese router tendrá un puerto que lo conecta a otra subred (más en el curso de Enrutamiento). Ciertas direcciones IP (redes privadas) no son visibles para Internet, y tenemos cosas como NAT implementadas (más sobre esto más adelante).

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del direccionamiento IP y el subnetting:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practica el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones IPv4, lo cual es fundamental para comprender las subredes.
2. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Aprende a explorar diferentes tipos de direcciones IP y a probar la accesibilidad de la red, lo que te ayudará a verificar si los hosts están en la misma red.
3. **[Realizar subnetting IP y conversión binaria en la terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domina el subnetting IP y la conversión binaria, aplicando directamente los conceptos de prefijos de red e identificación de hosts discutidos en la lección.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con el direccionamiento de red y el subnetting.

## Quiz Question

Verdadero o falso, una subred consta de una máscara de subred y un prefijo de red.

## Quiz Answer

True
