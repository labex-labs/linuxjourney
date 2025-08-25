---
index: 4
lang: "es"
title: "Protocolos de Enrutamiento"
meta_title: "Protocolos de Enrutamiento - Enrutamiento"
meta_description: "Aprende sobre protocolos de enrutamiento como vector de distancia y estado de enlace. Comprende la convergencia de red y cómo los routers se adaptan a los cambios. ¡Comienza tu viaje en redes Linux!"
meta_keywords: "protocolos de enrutamiento, convergencia de red, vector de distancia, estado de enlace, redes Linux, guía para principiantes, tutorial de red"
---

## Lesson Content

Sería un fastidio tener que configurar manualmente las rutas en una tabla de enrutamiento para cada dispositivo de su red. En su lugar, utilizamos lo que se conoce como protocolos de enrutamiento. Los protocolos de enrutamiento ayudan a nuestro sistema a adaptarse a los cambios de la red; aprenden diferentes rutas, las incorporan a la tabla de enrutamiento y luego enrutan nuestros paquetes de esa manera. Hay dos tipos principales de protocolos de enrutamiento: protocolos de vector de distancia y protocolos de estado de enlace.

### Convergencia

Antes de hablar de los protocolos, debemos repasar un término utilizado en el enrutamiento conocido como convergencia. Al utilizar protocolos de enrutamiento, los routers se comunican con otros routers para recopilar e intercambiar información sobre la red. Cuando se ponen de acuerdo sobre cómo debe ser una red, cada tabla de enrutamiento traza la topología completa de la red, "convergiendo" así. Cuando algo ocurre en la topología de la red, la convergencia se romperá temporalmente hasta que todos los routers estén al tanto de este cambio.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del enrutamiento de red y el direccionamiento IP:

1. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/linux-manage-ip-addressing-in-linux-592736)** - Practica la configuración de direcciones IP estáticas y dinámicas, el establecimiento de una puerta de enlace predeterminada y la verificación de las configuraciones de red, que son cruciales para comprender cómo se construyen y utilizan las tablas de enrutamiento.
2. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprende cómo interactúan los dispositivos en la capa de red, observando ARP y cómo la puerta de enlace predeterminada maneja el tráfico remoto, proporcionando información sobre los mecanismos que gestionan los protocolos de enrutamiento.
3. **[Simular la conectividad de la capa de red en Linux](https://labex.io/es/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Utiliza Docker para simular nodos de red, asignar direcciones IP y probar la conectividad entre subredes, aplicando directamente conceptos relacionados con los cambios de red y las decisiones de enrutamiento.

Estos laboratorios te ayudarán a aplicar los conceptos de configuración y conectividad de red en escenarios reales, generando confianza con los elementos fundamentales que automatizan los protocolos de enrutamiento.

## Quiz Question

¿Cuál es el término utilizado cuando todas las tablas de enrutamiento conocen la topología de la red?

## Quiz Answer

Convergence
