---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "es"
order_index: 6
title: "Protocolos de estado de enlace"
description: "Aprende cómo los protocolos de estado de enlace forman adyacencias, difunden información de topología y calculan rutas."
meta_title: "Protocolos de estado de enlace - Routing"
meta_description: "Aprende sobre protocolos de estado de enlace como OSPF para redes grandes. Comprende su rápida convergencia y cómo actualizan las tablas de enrutamiento."
meta_keywords: "protocolos de estado de enlace, OSPF, redes Linux, protocolos de enrutamiento, topología de red, principiante"
---

Los protocolos de estado de enlace describen los enlaces y prefijos locales, distribuyen esas descripciones por un ámbito de enrutamiento y permiten que cada router calcule rutas a partir de una base de datos de topología. OSPF e IS-IS son ejemplos habituales.

## Formar adyacencias

Los routers descubren vecinos compatibles y forman adyacencias del protocolo según el tipo de interfaz, el área, los temporizadores, la autenticación y otros parámetros. Ver paquetes hello no garantiza una adyacencia completa; una configuración que no coincida puede detener antes la máquina de estados.

:::single-choice{#link-state-hello-limit} ¿Qué no demuestra recibir un hello de OSPF?

::option[Que los routers hayan formado una adyacencia completa y sincronizada.]{#link-state-not-full .correct explanation="El área, los temporizadores, la autenticación, la MTU y otros estados pueden impedir el intercambio completo de bases de datos."}
::option[Que el vecino haya enviado al menos un mensaje del protocolo.]{#link-state-hello-sent explanation="Recibir el hello demuestra directamente ese hecho limitado."}
::option[Que una interfaz pueda recibir una trama.]{#link-state-frame-received explanation="El paquete recibido demuestra que funcionó alguna parte de la ruta de recepción local."}
:::

## Difundir información de estado de enlace

Cada router origina anuncios sobre su estado pertinente. Los vecinos difunden de forma fiable la información más reciente por el área o dominio definido, en lugar de mantener las actualizaciones únicamente entre la pareja original de vecinos. Los mecanismos de secuencia y envejecimiento distinguen la información actual y eliminan el estado obsoleto.

:::single-choice{#link-state-flooding-scope} ¿Por qué se difunde la información de estado de enlace más allá de un vecino?

::option[Todas las aplicaciones necesitan una copia de las contraseñas de los routers.]{#link-state-password-copy explanation="Las credenciales de las aplicaciones no son anuncios de topología."}
::option[Ethernet no puede enviar tramas unicast.]{#link-state-no-unicast explanation="Ethernet admite unicast; aquí la difusión es un mecanismo de distribución del protocolo de enrutamiento."}
::option[Los routers del ámbito de enrutamiento necesitan una base de datos de topología coherente.]{#link-state-consistent-database .correct explanation="Cada router calcula rutas a partir del conjunto compartido de anuncios actuales de estado de enlace."}
:::

## Calcular las rutas más cortas

Después de construir una base de datos de estado de enlace, el router ejecuta un algoritmo de primero la ruta más corta, normalmente el algoritmo de Dijkstra, utilizándose a sí mismo como raíz. OSPF suma los costes de las interfaces; las políticas y las reglas de igual coste influyen en los resultados que se instalan.

«Más corta» significa con menor coste del protocolo, no necesariamente con menos routers ni con menor latencia medida por la aplicación. El diseño de costes debe reflejar la intención operativa.

:::single-choice{#link-state-shortest-meaning} ¿Qué significa «más corta» en un cálculo de rutas de estado de enlace?

::option[La ruta cuyo prefijo tiene menos caracteres escritos.]{#link-state-shortest-text explanation="La longitud del texto no está relacionada con el coste de la topología."}
::option[La ruta con la menor suma de costes del protocolo.]{#link-state-lowest-cost .correct explanation="El modelo de costes puede corresponder o no directamente con la cantidad de saltos o la latencia actual."}
::option[La ruta que siempre tiene cero pérdidas de paquetes.]{#link-state-zero-loss explanation="Una ruta calculada no garantiza el rendimiento de la aplicación."}
:::

## Áreas y convergencia

Las áreas OSPF limitan el ámbito de difusión y cálculo de la topología; el área 0 sirve como backbone en un diseño normal entre áreas. La agregación y los tipos de áreas pueden proporcionar deliberadamente a distintos routers niveles diferentes de detalle en sus bases de datos.

Después de un cambio de enlace, la detección, la difusión de anuncios, el cálculo SPF, la instalación de rutas y la recuperación del reenvío requieren tiempo. Es posible converger más rápidamente que con un diseño sencillo de vector de distancia, pero no ocurre automáticamente ante todos los fallos o configuraciones.

:::single-choice{#link-state-convergence-stages} ¿Qué debe medirse durante una investigación de convergencia de OSPF?

::option[Únicamente el momento en que un administrador abrió una terminal.]{#link-state-terminal-time explanation="Eso no aísla las etapas del protocolo o del reenvío."}
::option[Únicamente el orden alfabético de los nombres de los routers.]{#link-state-router-names explanation="Los nombres no determinan los tiempos de convergencia."}
::option[La detección, la difusión, el cálculo, la instalación y la recuperación del reenvío.]{#link-state-all-stages .correct explanation="Separar las etapas revela dónde se produce el retraso o el fallo de convergencia."}
:::

## Resumen

Ahora puedes seguir el enrutamiento por estado de enlace desde el descubrimiento de vecinos hasta las rutas instaladas.

1. Distingue la recepción de un hello de una adyacencia completa.
2. Explica la difusión fiable a través de un ámbito de enrutamiento.
3. Interpreta la ruta más corta como el menor coste configurado del protocolo.
4. Mide todas las etapas de convergencia de los planos de control y de datos.
