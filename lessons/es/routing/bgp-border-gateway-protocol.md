---
index: 7
lang: "es"
title: "Protocolo de Pasarela Fronteriza"
meta_title: "Protocolo de Pasarela Fronteriza - Enrutamiento"
meta_description: "Explore los fundamentos del Protocolo de Pasarela Fronteriza (BGP), el protocolo central que habilita el enrutamiento de Internet. Aprenda cómo BGP facilita la comunicación entre sistemas autónomos y los principios del enrutamiento BGP."
meta_keywords: "BGP, Protocolo de Pasarela Fronteriza, enrutamiento BGP, enrutamiento de Internet, sistemas autónomos, redes Linux, tutorial BGP, protocolos de red"
---

## Lesson Content

### La Columna Vertebral de Internet

El último protocolo importante que cubriremos es el Protocolo de Pasarela Fronteriza (BGP). BGP es el protocolo fundamental que permite que Internet funcione al gestionar cómo se enrutan los paquetes de datos a través de su vasta colección de redes. Está diseñado específicamente para intercambiar información de enrutamiento y alcanzabilidad entre diferentes Sistemas Autónomos (AS).

### ¿Qué es un Sistema Autónomo?

Un Sistema Autónomo (AS) es una red grande o un grupo de redes administradas por una única entidad administrativa. Los ejemplos incluyen proveedores de servicios de Internet (ISP), grandes corporaciones, universidades y agencias gubernamentales. Sin BGP, estos sistemas estarían aislados y no podrían comunicarse entre sí. Mientras que otros protocolos gestionan el enrutamiento _dentro_ de un AS, BGP es responsable del enrutamiento _entre_ ellos.

### El Proceso del Enrutamiento del Protocolo de Pasarela Fronteriza

La función principal de BGP es el **enrutamiento del protocolo de pasarela fronteriza**. Consideremos un ejemplo. Imagine que usted está en su red doméstica y un amigo está usando el Wi-Fi en una cafetería. Cuando su amigo le envía un mensaje, el paquete de datos viaja primero a través de la red local de la cafetería. Sigue las tablas de enrutamiento internas hasta que llega a un router de "frontera" en el borde de esa red.

Este router fronterizo utiliza BGP para determinar la mejor ruta para que el paquete salga de su propio AS y viaje a través de otros sistemas autónomos hasta llegar finalmente al AS de su red doméstica. BGP no solo encuentra una ruta; toma decisiones de política para encontrar la ruta _óptima_ basándose en reglas configuradas por los administradores de red, asegurando un intercambio de datos eficiente y confiable a través de Internet global.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Qué protocolo básicamente hace funcionar a Internet? Por favor, responda usando el acrónimo en inglés en mayúsculas.

## Quiz Answer

BGP
