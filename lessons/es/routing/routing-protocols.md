---
index: 4
lang: "es"
title: "Protocolos de Enrutamiento"
meta_title: "Protocolos de Enrutamiento - Enrutamiento"
meta_description: "Explore los fundamentos de los protocolos de enrutamiento en redes Linux. Esta guía cubre protocolos de vector distancia y estado de enlace, convergencia de red, y cómo los routers construyen y mantienen tablas de enrutamiento. Un tutorial perfecto para principiantes."
meta_keywords: "protocolos de enrutamiento, convergencia de red, vector distancia, estado de enlace, redes linux, tabla de enrutamiento, tutorial de red, guía para principiantes, comunicación de router"
---

## Lesson Content

Configurar rutas manualmente en una tabla de enrutamiento para cada dispositivo en una red grande sería una tarea increíblemente tediosa. Para automatizar este proceso, utilizamos **protocolos de enrutamiento** dinámicos. Estos protocolos permiten a los enrutadores adaptarse automáticamente a los cambios de la red aprendiendo diferentes rutas, construyéndolas en la tabla de enrutamiento y reenviando paquetes en consecuencia. Hay dos tipos principales de protocolos de enrutamiento: vector distancia y estado de enlace.

### Protocolos de Vector Distancia

Los protocolos de vector distancia operan bajo el principio de "enrutamiento por rumor". Cada enrutador comparte su tabla de enrutamiento completa con sus vecinos conectados directamente a intervalos regulares. Cuando un enrutador recibe una tabla de enrutamiento de un vecino, actualiza la suya con cualquier ruta nueva o mejor. La "distancia" generalmente se mide con una métrica como el conteo de saltos. Este método es simple, pero puede ser lento para converger y es susceptible a bucles de enrutamiento. Un ejemplo de protocolo de vector distancia es el Protocolo de Información de Enrutamiento (RIP).

### Protocolos de Estado de Enlace

En contraste, los protocolos de **estado de enlace** proporcionan a cada enrutador un mapa completo de la topología de la red. En lugar de compartir toda su tabla de enrutamiento, los enrutadores envían información sobre el estado de sus propios enlaces (por ejemplo, vecinos conectados y el costo de la conexión) a todos los demás enrutadores de la red. Usando esta información, cada enrutador puede construir de forma independiente un mapa idéntico de la red y calcular la mejor ruta a cada destino. Este enfoque conduce a una **convergencia de red** más rápida y es más escalable que los protocolos de vector distancia. Un ejemplo es el protocolo Open Shortest Path First (OSPF).

### Convergencia de Red

Antes de discutir más a fondo los protocolos, es importante comprender un concepto clave en el enrutamiento conocido como **convergencia de red**. Cuando se utilizan protocolos de enrutamiento, los enrutadores se comunican para recopilar e intercambiar información. La convergencia es el estado en el que todos los enrutadores tienen una visión consistente y precisa de la topología de la red. Cuando cada tabla de enrutamiento mapea correctamente toda la red, se considera que la red está "convergida". Si ocurre un cambio, como la caída de un enlace, la convergencia se rompe temporalmente hasta que todos los enrutadores se enteran del cambio y actualizan sus tablas de enrutamiento.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del enrutamiento de red y el direccionamiento IP:

1. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practique la configuración de direcciones IP estáticas y dinámicas, el establecimiento de una puerta de enlace predeterminada y la verificación de configuraciones de red, que son cruciales para comprender cómo se construyen y utilizan las tablas de enrutamiento.
2. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda cómo interactúan los dispositivos en la capa de red, observando ARP y cómo la puerta de enlace predeterminada maneja el tráfico remoto, lo que proporciona información sobre los mecanismos que gestionan los protocolos de enrutamiento.
3. **[Simular la conectividad de la capa de red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Utilice Docker para simular nodos de red, asignar direcciones IP y probar la conectividad a través de subredes, aplicando directamente conceptos relacionados con los cambios de red y las decisiones de enrutamiento.

Estos laboratorios le ayudarán a aplicar los conceptos de configuración y conectividad de red en escenarios reales, aumentando la confianza con los elementos fundamentales que automatizan los protocolos de enrutamiento.

## Quiz Question

What is the term for the state where all routing tables on a network agree on the network topology? (Please answer in English, paying attention to capitalization.)

## Quiz Answer

Convergence
