---
index: 5
lang: "es"
title: "CIDR"
meta_title: "CIDR - Subnetting"
meta_description: "Una guía sobre la notación CIDR. Aprenda sobre el formato CIDR, subnetting CIDR y cómo calcular hosts para su red, incluso en un servidor Ubuntu. Domine el direccionamiento IP con CIDR."
meta_keywords: "CIDR, subnetting cidr, formato cidr, máscara de subred, direccionamiento IP, cidr de subred de servidor ubuntu, cidr de subred ubuntu, prefijo de red, redes Linux"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) es un método para asignar direcciones IP y enrutar paquetes del Protocolo de Internet. Ofrece una forma más compacta y eficiente de representar una máscara de subred, reemplazando el diseño de red con clases más antiguo. Comprender CIDR es esencial para la administración de redes modernas.

### El Formato CIDR

A menudo verá redes notadas usando el **formato CIDR**, donde una dirección IP es seguida por una barra y un número. Por ejemplo, una subred como `10.42.3.0` con una máscara de subred de `255.255.255.0` se escribe como `10.42.3.0/24`. Esta notación única incluye tanto la dirección de red como la longitud del prefijo.

El número después de la barra indica cuántos bits de la dirección IP se utilizan para el prefijo de red. Esta es una tarea común al configurar redes en un sistema como un **servidor Ubuntu**, donde podría definir una interfaz con una dirección de `ubuntu subnet cidr`.

### Subnetting CIDR y Cálculo de Hosts

Una dirección IPv4 consta de 4 bytes, lo que suma un total de 32 bits. El prefijo CIDR determina la división entre la porción de red y la porción de host de la dirección. Para un **cidr subnetting** efectivo, necesita saber cómo calcular el número de hosts disponibles.

Tomemos el ejemplo `123.12.24.0/23`. Esto significa que los primeros 23 bits son el prefijo de red. Para encontrar el número de hosts disponibles:

1.  Reste el prefijo CIDR del número total de bits (32): `32 - 23 = 9`. Esto deja 9 bits para la porción de host.
2.  Calcule el número total de direcciones en la subred: `2^9 = 512`.
3.  Reste 2 del total. Una dirección está reservada para la red en sí, y una es para la dirección de difusión. Esto deja `512 - 2 = 510` direcciones de host utilizables.

Otro ejemplo común es una red `/30`, que proporciona `32 - 30 = 2` bits de host. Esto da como resultado `2^2 = 4` direcciones totales, dejando solo 2 direcciones utilizables, lo que la hace ideal para enlaces punto a punto.

## Exercise

Para dominar estos conceptos, practique con algunos laboratorios prácticos que refuercen su comprensión de CIDR, direccionamiento IP y **cidr subnetting**:

1.  **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine el subnetting IP y la conversión binaria, incluida la traducción de máscaras CIDR y el cálculo de hosts utilizables.
2.  **[Simular Conectividad de Capa de Red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a asignar direcciones IP estáticas y observe cómo las subredes IP gobiernan la comunicación directa de red en un entorno simulado.
3.  **[Explorar Tipos de Direcciones IP y Alcanzabilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore el direccionamiento IP y la alcanzabilidad de la red usando comandos como `ping` e `ip a` para probar varios tipos de IP y conectividad.

Estos laboratorios le ayudarán a aplicar los conceptos de CIDR y direccionamiento IP en escenarios del mundo real y a ganar confianza con la configuración de red.
