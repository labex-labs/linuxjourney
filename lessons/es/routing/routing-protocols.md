---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "es"
order_index: 4
title: "Protocolos de enrutamiento"
description: "Aprende cómo los protocolos de enrutamiento dinámico intercambian accesibilidad y convergen en rutas de reenvío utilizables."
meta_title: "Protocolos de enrutamiento - Routing"
meta_description: "Explora los fundamentos de los protocolos de enrutamiento en redes Linux. Esta guía explica los protocolos de vector de distancia y de estado de enlace, la convergencia y cómo los routers mantienen sus tablas."
meta_keywords: "protocolos de enrutamiento, convergencia de red, vector de distancia, estado de enlace, redes linux, tabla de enrutamiento, tutorial de redes, guía para principiantes, comunicación entre routers"
---

Las rutas estáticas se configuran directamente, mientras que los protocolos de enrutamiento dinámico intercambian información de accesibilidad y topología para que los routers puedan adaptarse. El aprendizaje dinámico reduce el trabajo manual, pero introduce estados de protocolo, límites de confianza, temporizadores y modos de fallo que deben supervisarse.

## Plano de control y plano de reenvío

Un protocolo de enrutamiento aprende candidatos en su propia base de datos. El router selecciona rutas para una base de información de enrutamiento e instala siguientes saltos utilizables en una tabla de reenvío. Después, el hardware o el kernel reenvían paquetes a partir de esa tabla.

Que se haya establecido una adyacencia del protocolo no demuestra que el prefijo deseado se haya aprendido, seleccionado, instalado o permitido por la política de reenvío.

:::single-choice{#routing-protocols-adjacency-limit}
¿Qué no demuestra una adyacencia de enrutamiento establecida?

::option[Que todas las rutas deseadas estén instaladas y reenvíen correctamente.]{#routing-protocols-not-full-proof .correct explanation="El anuncio, la selección, la instalación, el filtrado y el funcionamiento del plano de datos son etapas independientes."}
::option[Que dos participantes del protocolo hayan intercambiado algún mensaje de control.]{#routing-protocols-no-messages explanation="Establecer una adyacencia normalmente requiere comunicación del protocolo."}
::option[Que exista un plano de control.]{#routing-protocols-no-control explanation="La adyacencia es en sí misma un estado del plano de control."}
:::

## Enrutamiento interior y exterior

Los protocolos de puerta de enlace interior operan dentro de un dominio administrativo de enrutamiento. Entre los ejemplos se encuentran RIP, OSPF e IS-IS. BGP intercambia accesibilidad controlada mediante políticas dentro de sistemas autónomos y entre ellos, y es el protocolo de enrutamiento exterior de Internet.

Las métricas tienen un significado específico de cada protocolo. Un coste OSPF, una cantidad de saltos RIP y un conjunto de atributos BGP no pueden compararse como si compartieran una escala numérica universal. Las implementaciones utilizan preferencias de ruta o distancias administrativas para elegir entre fuentes antes de la selección específica del protocolo o junto con ella.

:::single-choice{#routing-protocols-metric-comparison}
¿Puede compararse directamente una cantidad de saltos RIP con un coste OSPF?

::option[Sí, porque todas las métricas de enrutamiento utilizan las mismas unidades.]{#routing-protocols-universal-metric explanation="Cada protocolo define su propia métrica y su propio proceso de selección."}
::option[Sí, pero solo cuando ambos valores son cero.]{#routing-protocols-zero-metric explanation="Su semántica sigue siendo distinta con independencia del número mostrado."}
::option[No; tienen significados específicos de cada protocolo.]{#routing-protocols-specific-metric .correct explanation="La selección entre fuentes utiliza la política de la implementación en lugar de tratar métricas distintas como una única escala."}
:::

## Vector de distancia y estado de enlace

Los protocolos de vector de distancia anuncian accesibilidad y distancia mediante sus vecinos, y derivan las rutas de los informes de estos. Los protocolos de estado de enlace forman adyacencias, difunden información del estado de los enlaces en un ámbito, construyen una base de datos de topología y calculan árboles de rutas más cortas. Los protocolos modernos incluyen mejoras que hacen que las descripciones sencillas de las categorías sean incompletas.

:::single-choice{#routing-protocols-link-state-input}
¿Qué utiliza un router de estado de enlace para calcular sus rutas?

::option[Únicamente el nombre de host de su puerta de enlace predeterminada.]{#routing-protocols-hostname-only explanation="Un cálculo de topología necesita información de enlaces y prefijos."}
::option[Una base de datos sincronizada que describe los enlaces del ámbito de enrutamiento.]{#routing-protocols-link-database .correct explanation="El router ejecuta un algoritmo de la ruta más corta sobre la topología aprendida."}
::option[Las contraseñas de la capa de aplicación de todos los hosts.]{#routing-protocols-passwords explanation="El intercambio de topología de enrutamiento no requiere credenciales de los usuarios finales."}
:::

## Convergencia

Después de un cambio de topología o política, los routers lo detectan, propagan información de control, calculan rutas y actualizan el estado de reenvío. La convergencia es el periodo y el resultado mediante los cuales la red alcanza un enrutamiento estable y mutuamente utilizable para los destinos afectados. No exige que todos los routers tengan una tabla completa idéntica; las funciones y políticas pueden diferir deliberadamente.

Durante la convergencia pueden producirse pérdidas transitorias, bucles o agujeros negros. Mide por separado la detección, la propagación, el cálculo y la instalación, y comprueba el resultado mediante pruebas del plano de datos.

:::single-choice{#routing-protocols-convergence}
¿Qué es la convergencia del enrutamiento?

::option[El proceso de alcanzar un enrutamiento estable y utilizable después de un cambio.]{#routing-protocols-stable-routing .correct explanation="Incluye la propagación del control y las actualizaciones de reenvío resultantes."}
::option[La obligación de que todos los routers almacenen una tabla global idéntica.]{#routing-protocols-identical-table explanation="Las políticas, las áreas y las funciones pueden crear diferencias deliberadas."}
::option[La prevención permanente de todos los fallos de enrutamiento posibles.]{#routing-protocols-no-failure explanation="Una red convergida aún puede tener problemas de políticas o capacidad."}
:::

## Resumen

Ahora puedes situar la información de enrutamiento dinámico en la trayectoria que va del intercambio del protocolo al reenvío.

1. Distingue los candidatos aprendidos, las rutas seleccionadas y las entradas de reenvío.
2. Separa el enrutamiento interior del intercambio de políticas mediante BGP.
3. Compara las métricas únicamente dentro de la semántica de su protocolo.
4. Comprueba la convergencia tanto en el plano de control como en el de datos.
