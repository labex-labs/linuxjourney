---
index: 1
lang: "es"
title: "¿Qué es un router?"
meta_title: "¿Qué es un router? - Enrutamiento"
meta_description: "Guía para principiantes sobre qué es un router en redes. Aprenda sobre enrutamiento, conmutación de paquetes, saltos y cómo los routers usan tablas de enrutamiento para reenviar datos a través de redes. Esta guía de redes es esencial para aprender sobre redes en Linux."
meta_keywords: "router, redes, enrutamiento, saltos, conmutación de paquetes, redes Linux, tutorial principiantes, guía de redes"
---

## Lesson Content

Un router es un dispositivo fundamental en las redes informáticas. Es probable que tengas uno en casa que te conecta a Internet. Su trabajo principal es permitir que las máquinas en una red se comuniquen entre sí y con otras redes. Este proceso es una parte central de lo que hace funcionar Internet y las redes locales.

### La función principal de un router

Un router doméstico típico tiene puertos LAN (Red de Área Local) para conectar tus dispositivos a una red local y un puerto WAN (Red de Área Amplia) que proporciona conexión a Internet. Cada fragmento de datos, o "paquete", que envías o recibes durante cualquier actividad de red debe pasar por el router. El router inspecciona estos paquetes de red y decide a dónde deben ir. Efectivamente, enruta el tráfico entre múltiples redes, asegurando que cada paquete viaje desde su origen hasta su destino final.

### El proceso de enrutamiento

Piense en el proceso de enrutamiento como la entrega de correo. Cuando envías una carta, la oficina de correos determina el destino general (por ejemplo, un estado o ciudad) y la envía allí. A partir de ese momento, se clasifica en regiones más pequeñas como códigos postales hasta que finalmente llega a la dirección de calle específica.

En redes, un router utiliza una **tabla de enrutamiento** para tomar estas decisiones. Esta tabla contiene un conjunto de reglas, o rutas, que le dicen al router cómo reenviar paquetes a un destino de red en particular. Por ejemplo, una regla podría decir: "Para llegar a la Red A, envíe los paquetes al Router B". Si no hay una regla específica para un destino, el router utiliza una **ruta predeterminada**, que generalmente dirige el tráfico hacia Internet. Este sistema es crucial tanto en configuraciones domésticas simples como en entornos complejos de **redes Linux**.

### Saltos (Hops)

A medida que los paquetes viajan a través de las redes, su recorrido se mide en **saltos** (hops). Un salto representa un paso del viaje en el que un paquete pasa por un dispositivo intermedio, como un router. Por ejemplo, si un paquete debe pasar por dos routers para ir del Host A al Host B, decimos que la ruta tiene una longitud de dos saltos. Los saltos proporcionan una métrica simple para medir la distancia entre un origen y un destino en una red.

### Conmutación de paquetes, enrutamiento e inundación

Para comprender cómo se mueven los datos, es útil conocer estos términos relacionados:

- **Conmutación de paquetes** es el método fundamental de recibir, procesar y reenviar paquetes de datos a su destino. Es lo que los routers hacen continuamente.
- **Enrutamiento** es el proceso inteligente de construir y mantener la tabla de enrutamiento. Un enrutamiento eficaz permite una conmutación de paquetes más eficiente y confiable.
- **Inundación (Flooding)** es un método más antiguo y menos eficiente que se utiliza cuando un router no sabe a dónde enviar un paquete. Envía el paquete entrante por todas las conexiones excepto por aquella por la que llegó, con la esperanza de que uno llegue al destino. Las redes modernas dependen del enrutamiento para evitar este tipo de ineficiencia.

## Exercise

¡La práctica hace la perfección! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la conectividad de red y el enrutamiento:

1.  **[Explorar tipos de direcciones IP y alcanzabilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Practique la prueba de la pila TCP/IP local, la identificación de IPs privadas y públicas, y la verificación de la alcanzabilidad de la red, que son clave para comprender cómo un router facilita la comunicación.
2.  **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda cómo los comandos `ping` y `arp` le ayudan a observar cómo interactúan las capas de red y de enlace de datos, y cómo la puerta de enlace predeterminada (router) maneja el tráfico remoto.
3.  **[Simular conectividad de capa de red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Use Docker para simular nodos de red y asignar direcciones IP, luego pruebe la conectividad para comprender cómo las subredes IP y el enrutamiento gobiernan la comunicación de red.

Estos laboratorios le ayudarán a aplicar los conceptos de comunicación de red, direccionamiento IP y el papel del enrutamiento en escenarios reales, aumentando su confianza con los fundamentos de red.

## Quiz Question

How do packets measure distance? (Please answer in English. The answer is case-sensitive.)

## Quiz Answer

Hops
