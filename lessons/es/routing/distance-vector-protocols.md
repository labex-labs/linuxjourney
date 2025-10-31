---
index: 5
lang: "es"
title: "Protocolos de Vector Distancia"
meta_title: "Protocolos de Vector Distancia - Enrutamiento"
meta_description: "Guía para principiantes sobre protocolos de vector distancia en el enrutamiento de redes. Este tutorial explica cómo protocolos como RIP usan el conteo de saltos para determinar rutas y cubre sus limitaciones para el networking moderno en Linux."
meta_keywords: "protocolos vector distancia, enrutamiento de red, RIP, protocolo de información de enrutamiento, conteo de saltos, networking Linux, guía principiantes, tutorial"
---

## Lesson Content

Los protocolos de vector distancia son una categoría fundamental de protocolos de enrutamiento utilizados en redes informáticas. Determinan la mejor ruta para los paquetes de datos basándose en la distancia, que generalmente se mide por el **conteo de saltos** (hop count). En este tipo de **enrutamiento de red**, cada router mantiene una tabla de la "distancia" a todas las redes conocidas.

### Cómo Funcionan los Protocolos de Vector Distancia

El principio central de un protocolo de vector distancia es sencillo: los routers comparten su información de enrutamiento con sus vecinos inmediatos. Este proceso a veces se denomina "enrutamiento por rumor". Por ejemplo, si el Router A sabe que está a 3 saltos de la Red X, y el Router B es un vecino directo del Router A, el Router B puede inferir que está a 4 saltos de la Red X a través del Router A. Cuando existen múltiples rutas hacia el mismo destino, el protocolo siempre elegirá la ruta con el **conteo de saltos** más bajo.

### Ventajas y Desventajas

Los **protocolos de vector distancia** son simples de configurar y funcionan bien en redes pequeñas y estables. Sin embargo, tienen limitaciones significativas que los hacen menos adecuados para entornos más grandes y complejos.

Una gran desventaja es la convergencia lenta. Los routers transmiten periódicamente toda su tabla de enrutamiento a sus vecinos, lo que puede consumir un ancho de banda y una potencia de procesamiento considerables, especialmente a medida que la red crece. Si ocurre un cambio en la red, puede llevar mucho tiempo que esa información se propague a todos los routers.

Otra desventaja clave es que el camino más corto en términos de **conteo de saltos** no siempre es el más eficiente. Un camino con menos saltos podría tener enlaces más lentos (por ejemplo, 10 Mbps) en comparación con un camino con más saltos que utiliza enlaces más rápidos (por ejemplo, 1 Gbps). Los protocolos de vector distancia generalmente desconocen la velocidad del enlace, lo que lleva a decisiones de enrutamiento subóptimas.

### RIP Un Ejemplo Común

Uno de los **protocolos de vector distancia** más conocidos es el **Protocolo de Información de Enrutamiento (RIP)**. Es un ejemplo clásico que demuestra claramente los principios y limitaciones de esta familia de protocolos.

- **Actualizaciones Periódicas:** RIP transmite toda su tabla de enrutamiento a todos los vecinos cada 30 segundos.
- **Límite de Conteo de Saltos:** Para prevenir bucles de enrutamiento y controlar el tráfico de red, RIP impone un **conteo de saltos** máximo de 15. Cualquier ruta que requiera 16 saltos se considera inalcanzable.

Debido a estas características, RIP rara vez se utiliza en redes de producción modernas, pero sirve como una excelente herramienta de aprendizaje en una **guía para principiantes** sobre **redes Linux** y conceptos de enrutamiento.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del enrutamiento de red y la conectividad:

1. **[Explorar la Interacción de la Capa de Red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Practique el uso de `ping` y `arp` para comprender cómo los dispositivos se descubren entre sí y cómo se enrutan los datos en la capa de red.
2. **[Simular la Conectividad de la Capa de Red en Linux](https://labex.io/es/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a asignar direcciones IP y probar la conectividad entre nodos Linux simulados, observando cómo las subredes IP influyen en la comunicación de red.
3. **[Administrar Direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Obtenga experiencia práctica configurando direcciones IP estáticas y dinámicas y estableciendo puertas de enlace predeterminadas, que son componentes esenciales del enrutamiento de red.

Estos laboratorios le ayudarán a aplicar los conceptos de direccionamiento de red y conectividad en escenarios reales, construyendo una base sólida para comprender cómo funcionan los protocolos de enrutamiento.

## Quiz Question

¿Verdadero o falso: Los protocolos de vector distancia utilizan la ruta con la menor cantidad de ancho de banda?

## Quiz Answer

False
