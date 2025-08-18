---
lang: "es"
title: "Capa de red"
meta_description: "Aprende sobre la capa de red en Linux, cómo las direcciones IP enrutan paquetes a través de subredes y su papel en la transmisión de datos. ¡Comienza tu viaje en redes Linux!"
meta_keywords: "Capa de red, direcciones IP, subredes, redes Linux, enrutamiento de paquetes, principiante, tutorial, guía"
---

## Lesson Content

La capa de red determina el enrutamiento de nuestros paquetes desde nuestro host de origen a un host de destino. Afortunadamente, en nuestro ejemplo, nuestro paquete solo viaja dentro de la misma red, pero Internet está compuesta por muchas redes. Estas redes más pequeñas que componen Internet se conocen como subnets. Todas las subnets se conectan entre sí de alguna manera, por lo que podemos acceder a <https://www.google.com> aunque esté en su propia red. No entraré en detalles, ya que tenemos un curso completo dedicado a las subnets, pero por ahora, en lo que respecta a nuestra capa de red, sepa que las IP addresses definen las reglas para viajar a diferentes subnets.

En la capa de red, recibe el segment que viene de la Transport layer y encapsula este segment en un IP packet, luego adjunta la IP address del host de origen y la IP address del host de destino al packet header. Así que en este punto, nuestro paquete tiene información sobre a dónde va y de dónde viene. Ahora envía nuestro paquete a la physical hardware layer.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cómo se llaman las redes más pequeñas que componen Internet?

## Quiz Answer

subnets
