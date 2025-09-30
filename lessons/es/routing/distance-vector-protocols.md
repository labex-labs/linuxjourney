---
index: 5
lang: "es"
title: "Protocolos de Vector de Distancia"
meta_title: "Protocolos de Vector de Distancia - Enrutamiento"
meta_description: "Aprenda sobre los protocolos de vector de distancia como RIP, cómo funcionan y sus limitaciones para el enrutamiento de red. Comprenda el conteo de saltos y la eficiencia de la red."
meta_keywords: "protocolos de vector de distancia, RIP, protocolo de información de enrutamiento, conteo de saltos, enrutamiento de red, redes Linux, guía para principiantes, tutorial"
---

## Lesson Content

Los protocolos de vector de distancia determinan la ruta a otras redes utilizando el número de saltos que un paquete realiza a través de la red. Por ejemplo, si la red A está a 3 saltos de distancia y la red B está al lado de la red A, entonces asumimos que la red B debe estar a 4 saltos de distancia. En los protocolos de vector de distancia, la siguiente ruta sería la que tenga el menor número de saltos.

Los protocolos de vector de distancia son excelentes para redes pequeñas. Sin embargo, cuando las redes comienzan a escalar, los enrutadores tardan más en converger porque envían periódicamente la tabla de enrutamiento completa a cada enrutador. Otra desventaja de los protocolos de vector de distancia es la eficiencia; eligen rutas que están más cerca en saltos, pero esto no siempre es la ruta más eficiente.

Uno de los protocolos de vector de distancia comunes es RIP (Routing Information Protocol). Este difunde la tabla de enrutamiento a cada enrutador en la red cada 30 segundos. Para una red grande, esto puede consumir recursos significativos. Debido a esto, RIP limita su conteo de saltos a 15.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del enrutamiento y la conectividad de red:

1. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Practique el uso de `ping` y `arp` para comprender cómo los dispositivos se descubren entre sí y cómo se enruta el tráfico en la capa de red.
2. **[Simular la conectividad de la capa de red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a asignar direcciones IP y probar la conectividad entre nodos Linux simulados, observando cómo las subredes IP influyen en la comunicación de red.
3. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Obtenga experiencia práctica configurando direcciones IP estáticas y dinámicas y estableciendo puertas de enlace predeterminadas, que son componentes esenciales del enrutamiento de red.

Estos laboratorios le ayudarán a aplicar los conceptos de direccionamiento y conectividad de red en escenarios reales, construyendo una base sólida para comprender cómo funcionan los protocolos de enrutamiento.

## Quiz Question

Verdadero o falso: ¿Los protocolos de vector de distancia utilizan la ruta con la menor cantidad de ancho de banda?

## Quiz Answer

False
