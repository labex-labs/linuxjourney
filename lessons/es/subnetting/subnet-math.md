---
index: 3
lang: "es"
title: "Matemáticas de Subredes"
meta_title: "Matemáticas de Subredes - Subnetting"
meta_description: "Domina los fundamentos de las matemáticas de subredes. Esta guía explica cómo realizar cálculos de máscara de subred para determinar el número de hosts disponibles en tu red. Aprende conceptos esenciales de direccionamiento IP y binario para redes Linux."
meta_keywords: "matemáticas de subredes, cálculo máscara subred, dirección IP, máscara de subred, hosts de red, binario, redes Linux, cálculo de hosts, tutorial principiantes"
---

## Lesson Content

Para determinar el número de hosts que una subred puede soportar, necesitas comprender algo de **matemáticas básicas de subredes**. La máscara de subred es la clave para este cálculo.

### El Papel de la Máscara de Subred

Usemos una dirección IP de **192.168.1.0** con una máscara de subred de **255.255.255.0**. La función principal de la máscara de subred es distinguir la porción de red de la dirección de la porción de host.

Para ver cómo funciona esto, podemos convertir estos valores a su forma binaria.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

### Realizando Matemáticas de Máscara de Subred

En la representación binaria anterior, los `1` en la máscara de subred corresponden a la porción de red de la dirección IP. Esta parte está "enmascarada" o fija. Los `0` en la máscara de subred corresponden a la porción de host, que representa el rango de direcciones que puedes asignar a los dispositivos.

En nuestro ejemplo, la porción de host es `00000000`. Este es un campo de 8 bits, y con 8 bits, puedes crear 2^8, o 256, combinaciones únicas (de 0 a 255).

### Calculando Hosts Disponibles

Aunque hay 256 combinaciones posibles, no todas pueden asignarse a hosts. En cualquier subred, dos direcciones están reservadas:

1.  **Dirección de Red:** La primera dirección, donde todos los bits de host son `0` (ejemplo: 192.168.1.0).
2.  **Dirección de Broadcast:** La última dirección, donde todos los bits de host son `1` (ejemplo: 192.168.1.255).

Por lo tanto, el número real de hosts utilizables es 256 - 2 = 254. Esto significa que para la red `192.168.1.0` con una máscara `255.255.255.0`, puedes asignar direcciones IP desde `192.168.1.1` hasta `192.168.1.254`. Este cálculo central es una parte fundamental de las **matemáticas de subredes**.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de direccionamiento IP y subredes:

1.  **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domina el subnetting IP y la conversión binaria, habilidades esenciales para la configuración y planificación de redes.
2.  **[Explorar Tipos de Direcciones IP y Alcance en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Profundiza tu comprensión de varios tipos de direcciones IP y cómo verificar la capacidad de alcance de la red usando comandos de Linux.
3.  **[Simular Conectividad de Capa de Red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aplica tus conocimientos simulando configuraciones de red y probando la conectividad entre diferentes subredes IP en un entorno práctico.

Estos laboratorios te ayudarán a aplicar los conceptos de direccionamiento IP, máscaras de subred y cálculo de hosts en escenarios del mundo real y a ganar confianza con los fundamentos de red.

## Quiz Question

¿Cuál es el equivalente binario de 255?

## Quiz Answer

11111111
