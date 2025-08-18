---
index: 4
lang: "es"
title: "Protocolos de Enrutamiento"
meta_title: "Protocolos de Enrutamiento - Enrutamiento"
meta_description: "Aprenda sobre los protocolos de enrutamiento como el vector de distancia y el estado de enlace. Comprenda la convergencia de la red y cómo los enrutadores se adaptan a los cambios. ¡Comience su viaje en redes Linux!"
meta_keywords: "protocolos de enrutamiento, convergencia de red, vector de distancia, estado de enlace, redes Linux, guía para principiantes, tutorial de red"
---

## Lesson Content

Sería un fastidio tener que configurar manualmente las rutas en una tabla de enrutamiento para cada dispositivo de su red. En su lugar, utilizamos lo que se conoce como routing protocols. Los routing protocols ayudan a nuestro sistema a adaptarse a los cambios de la red; aprenden diferentes rutas, las incorporan a la routing table y luego enrutan nuestros paquetes de esa manera. Hay dos tipos principales de routing protocol: distance vector protocols y link state protocols.

### Convergence

Antes de hablar de los protocols, debemos repasar un término utilizado en el enrutamiento conocido como convergence. Al usar routing protocols, los routers se comunican con otros routers para recopilar e intercambiar información sobre la red. Cuando están de acuerdo en cómo debe ser una red, cada routing table traza la topología completa de la red, "convergiendo" así. Cuando algo ocurre en la network topology, la convergence se romperá temporalmente hasta que todos los routers sean conscientes de este cambio.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuál es el término utilizado cuando todas las tablas de enrutamiento conocen la topología de la red?

## Quiz Answer

Convergence
