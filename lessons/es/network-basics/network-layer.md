---
index: 7
lang: "es"
title: "Capa de Red"
meta_title: "Capa de Red - Fundamentos de Redes"
meta_description: "Explore la capa de Red en redes Linux. Esta guía explica cómo las direcciones IP y las subredes permiten el enrutamiento de paquetes para la transmisión de datos a través de redes."
meta_keywords: "Capa de red, direcciones IP, subredes, redes Linux, enrutamiento de paquetes, transmisión de datos, modelo OSI, paquete IP"
---

## Lesson Content

La capa de Red es responsable del direccionamiento lógico y el enrutamiento de los paquetes de datos desde un host de origen a un host de destino. Si bien un paquete a veces puede viajar dentro de una única red local, Internet es una vasta colección de redes interconectadas.

### El Papel del Enrutamiento de Paquetes

La función principal de la capa de Red es determinar la ruta óptima para que viajen los datos. Este proceso, conocido como **enrutamiento de paquetes**, asegura que la información llegue a su destino previsto de manera eficiente, incluso si necesita cruzar múltiples límites de red. En el **networking de Linux**, esta capa es fundamental para toda la comunicación por Internet.

### Comprensión de Subredes y Direcciones IP

Las redes más pequeñas que constituyen Internet se denominan **subredes**. Todas las subredes están conectadas, lo que permite que un dispositivo en una red se comunique con un dispositivo en otra, como acceder a un sitio web como `google.com`. Las reglas para viajar entre estas diferentes subredes se definen mediante las **direcciones IP**. Una dirección IP proporciona un identificador único para un dispositivo en una red, muy parecido a una dirección postal para una casa.

### Encapsulación en la Capa de Red

En la capa de Red, el segmento de datos recibido de la capa de Transporte se encapsula en una nueva unidad llamada paquete IP. Durante este proceso, se añade una cabecera al paquete, que incluye la dirección IP de origen (de dónde vino el paquete) y la dirección IP de destino (a dónde va). Con esta información de direccionamiento crucial adjunta, el paquete ahora tiene todo lo necesario para su viaje y se pasa a la capa de Enlace de Datos para ser preparado para la transmisión física.

## Exercise

¡La práctica hace la perfección! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la capa de Red, el direccionamiento IP y las subredes:

1. **[Simular Conectividad de Capa de Red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Practique la asignación de direcciones IP estáticas y pruebe la conectividad dentro y a través de diferentes subredes usando contenedores Docker.
2. **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine el subnetting IP y la conversión binaria, incluido el cálculo de hosts y subredes utilizables, directamente en la terminal de Linux.
3. **[Explorar Tipos de Direcciones IP y Alcance en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore varios tipos de direcciones IP (privadas, públicas, multicast) y pruebe el alcance de la red usando `ping` e `ip a`.

Estos laboratorios le ayudarán a aplicar los conceptos de direccionamiento IP y subnetting en escenarios reales y a ganar confianza con los fundamentos de la capa de Red.

## Quiz Question

¿Cómo se llaman las redes más pequeñas que componen Internet? Por favor, responda usando una sola palabra en inglés en minúsculas.

## Quiz Answer

subnets
