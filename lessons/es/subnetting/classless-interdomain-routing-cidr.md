---
index: 5
lang: "es"
title: "CIDR"
meta_title: "CIDR - Subredes"
meta_description: "Aprenda la notación CIDR para redes Linux. Comprenda las máscaras de subred, el direccionamiento IP y el cálculo de hosts con esta guía para principiantes. ¡Mejore sus habilidades de red!"
meta_keywords: "CIDR, máscara de subred, direccionamiento IP, prefijo de red, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) se utiliza para representar una máscara de subred de una manera más compacta. Es posible que vea subredes anotadas en notación CIDR, donde una subred como 10.42.3.0/255.255.255.0 se escribe como 10.42.3.0/24. Esta notación incluye tanto el prefijo de subred como la máscara de subred.

Recuerde, una dirección IP consta de 4 bytes o 32 bits. CIDR indica el número de bits utilizados como prefijo de red. Así, 123.12.24.0/23 significa que se utilizan los primeros 23 bits. ¿Qué significa eso? ¿Cuántos hosts son?

Un truco simple es restar la dirección CIDR (23) del número total de bits que puede tener una dirección IP (32). Esto deja 9 bits. Por lo tanto, 2^9 = 512. Sin embargo, debemos eliminar 2 direcciones (la dirección de subred y la dirección de difusión), por lo que tenemos 510 hosts utilizables.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de CIDR, direccionamiento IP y subredes:

1. **[Realizar Subredes IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine las subredes IP y la conversión binaria, incluyendo la traducción de máscaras CIDR y el cálculo de hosts utilizables.
2. **[Simular Conectividad de Capa de Red en Linux](https://labex.io/es/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a asignar direcciones IP estáticas y observe cómo las subredes IP rigen la comunicación de red directa en un entorno simulado.
3. **[Explorar Tipos de Direcciones IP y Accesibilidad en Linux](https://labex.io/es/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore el direccionamiento IP y la accesibilidad de la red utilizando comandos como `ping` e `ip a` para probar varios tipos de IP y conectividad.

Estos laboratorios le ayudarán a aplicar los conceptos de CIDR y direccionamiento IP en escenarios reales y a generar confianza con la configuración de red.

## Quiz Question

¡No hay preguntas, siga adelante!

## Quiz Answer
