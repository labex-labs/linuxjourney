---
index: 5
lang: "es"
title: "Protocolos de Vector de Distancia"
meta_title: "Protocolos de Vector de Distancia - Enrutamiento"
meta_description: "Aprenda sobre los protocolos de vector de distancia como RIP, cómo funcionan y sus limitaciones para el enrutamiento de red. Comprenda el conteo de saltos y la eficiencia de la red."
meta_keywords: "protocolos de vector de distancia, RIP, protocolo de información de enrutamiento, conteo de saltos, enrutamiento de red, redes Linux, guía para principiantes, tutorial"
---

## Lesson Content

Los protocolos de vector de distancia determinan la ruta a otras redes utilizando el conteo de saltos que un paquete toma a través de la red. Por ejemplo, si la red A está a 3 saltos de distancia y la red B está al lado de la red A, entonces asumimos que la red B debe estar a 4 saltos de distancia. En los protocolos de vector de distancia, la siguiente ruta sería la que tenga el menor número de saltos.

Los protocolos de vector de distancia son excelentes para redes pequeñas. Sin embargo, cuando las redes comienzan a escalar, los routers tardan más en converger porque envían periódicamente la tabla de enrutamiento completa a cada router. Otra desventaja de los protocolos de vector de distancia es la eficiencia; eligen rutas que están más cerca en saltos, pero esto no siempre es la ruta más eficiente.

Uno de los protocolos de vector de distancia comunes es RIP (Routing Information Protocol). Este difunde la tabla de enrutamiento a cada router en la red cada 30 segundos. Para una red grande, esto puede consumir recursos significativos. Debido a esto, RIP limita su conteo de saltos a 15.

## Exercise

No exercises for this lesson.

## Quiz Question

Verdadero o falso: ¿Los protocolos de vector de distancia utilizan la ruta con la menor cantidad de ancho de banda?

## Quiz Answer

False
