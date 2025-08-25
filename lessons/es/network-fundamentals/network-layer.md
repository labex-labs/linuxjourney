---
index: 7
lang: "es"
title: "Capa de red"
meta_title: "Capa de red - Conceptos básicos de red"
meta_description: "Aprenda sobre la capa de red en Linux, cómo las direcciones IP enrutan paquetes a través de subredes y su papel en la transmisión de datos. ¡Comience su viaje en redes Linux!"
meta_keywords: "Capa de red, direcciones IP, subredes, redes Linux, enrutamiento de paquetes, principiante, tutorial, guía"
---

## Lesson Content

La capa de red determina el enrutamiento de nuestros paquetes desde nuestro host de origen a un host de destino. Afortunadamente, en nuestro ejemplo, nuestro paquete solo viaja dentro de la misma red, pero Internet está compuesta por muchas redes. Estas redes más pequeñas que componen Internet se conocen como subredes. Todas las subredes se conectan entre sí de alguna manera, por lo que podemos acceder a `https://www.google.com` aunque esté en su propia red. No entraré en detalles, ya que tenemos un curso completo dedicado a las subredes, pero por ahora, en lo que respecta a nuestra capa de red, sepa que las direcciones IP definen las reglas para viajar a diferentes subredes.

En la capa de red, recibe el segmento que viene de la capa de transporte y encapsula este segmento en un paquete IP, luego adjunta la dirección IP del host de origen y la dirección IP del host de destino al encabezado del paquete. Así que en este punto, nuestro paquete tiene información sobre a dónde va y de dónde viene. Ahora envía nuestro paquete a la capa de hardware físico.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la capa de red, el direccionamiento IP y las subredes:

1. **[Simular conectividad de capa de red en Linux](https://labex.io/es/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Practique la asignación de direcciones IP estáticas y la prueba de conectividad dentro y entre diferentes subredes usando contenedores Docker.
2. **[Realizar subredes IP y conversión binaria en la terminal de Linux](https://labex.io/es/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine las subredes IP y la conversión binaria, incluido el cálculo de hosts y subredes utilizables, directamente en la terminal de Linux.
3. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore varios tipos de direcciones IP (privadas, públicas, multidifusión) y pruebe la accesibilidad de la red usando `ping` e `ip a`.

Estos laboratorios le ayudarán a aplicar los conceptos de direccionamiento IP y subredes en escenarios reales y a generar confianza con los fundamentos de la capa de red.

## Quiz Question

¿Cómo se llaman las redes más pequeñas que componen Internet?

## Quiz Answer

subnets
