---
index: 3
lang: "es"
title: "Matemáticas de Subred"
meta_title: "Matemáticas de Subred - Subnetting"
meta_description: "Aprende los conceptos básicos de las matemáticas de subredes y cómo calcular los hosts disponibles en una red. Comprende el direccionamiento IP y las máscaras de subred para principiantes. ¡Comienza tu viaje en Linux!"
meta_keywords: "matemáticas de subred, dirección IP, máscara de subred, hosts de red, binario, redes Linux, tutorial para principiantes, guía"
---

## Lesson Content

Bien, sabemos que las máscaras de subred son importantes para determinar cuántos hosts podemos tener en nuestra subred. Entonces, ¿cuántos hosts serían?

Digamos que tengo una dirección IP de **192.168.1.0** y una máscara de subred de **255.255.255.0**. Ahora, alineemos estos números en formato binario. Por ahora, usa una calculadora en línea para convertir estos valores de decimal a binario.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

La dirección IP está enmascarada por nuestra máscara de subred. Cuando ves un 1, está enmascarado, y fingimos que no lo vemos. Así que los únicos hosts posibles que podemos tener son de la región `00000000`. Recuerda, `11111111` en formato binario es igual a 255. También contamos 0 como un número de host, por lo que hay 256 opciones posibles. Sin embargo, puede parecer que tenemos 256 opciones posibles, pero en realidad restamos 2 hosts porque tenemos que tener en cuenta la dirección de difusión (broadcast address) y la dirección de subred (subnet address), lo que nos deja con 254 hosts posibles en nuestra subred. Así que sabemos que podemos tener hosts con direcciones IP que van desde 192.168.1.1 hasta 192.168.1.254.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del direccionamiento IP y el subnetting:

1. **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domina el subnetting IP y la conversión binaria, habilidades esenciales para la configuración y planificación de redes.
2. **[Explorar Tipos de Direcciones IP y Accesibilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Profundiza tu comprensión de varios tipos de direcciones IP y cómo verificar la accesibilidad de la red usando comandos de Linux.
3. **[Simular Conectividad de Capa de Red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aplica tus conocimientos simulando configuraciones de red y probando la conectividad entre diferentes subredes IP en un entorno práctico.

Estos laboratorios te ayudarán a aplicar los conceptos de direccionamiento IP, máscaras de subred y cálculo de hosts en escenarios reales y a construir confianza con los fundamentos de red.

## Quiz Question

¿Cuál es el equivalente binario de 255?

## Quiz Answer

11111111
