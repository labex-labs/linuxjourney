---
lesson_id: "osi-model"
course_id: "network-basics"
lang: "es"
order_index: 2
title: "Modelo OSI"
description: "Aprende cómo el modelo de referencia OSI de siete capas organiza las funciones de red y el lenguaje de diagnóstico."
meta_title: "Modelo OSI - Network Basics"
meta_description: "Explora el modelo OSI, un marco fundamental de siete capas para las redes. Aprende cómo este concepto teórico influye en el modelo TCP/IP y su importancia en las redes Linux."
meta_keywords: "osi linux, modelo OSI, conceptos de redes, TCP/IP, redes Linux, capas de red, modelo teórico, modelo de 7 capas"
---

El modelo de interconexión de sistemas abiertos es un marco de referencia de siete capas. Proporciona a los profesionales un vocabulario compartido para situar responsabilidades, interfaces y fallos; no es una descripción literal de todas las implementaciones.

## Las siete capas

De la más baja a la más alta, las capas OSI son:

1. Física: señales, medios, conectores y transmisión de bits.
2. Enlace de datos: tramas locales, direccionamiento de enlace y acceso al medio.
3. Red: direccionamiento lógico y reenvío entre redes.
4. Transporte: comunicación entre puntos finales o procesos.
5. Sesión: gestión de sesiones de comunicación.
6. Presentación: representación, transformación y codificación de datos.
7. Aplicación: servicios de red que utilizan las aplicaciones.

:::single-choice{#osi-network-layer-number} ¿Qué capa OSI gestiona el direccionamiento lógico y el reenvío entre redes?

::option[Capa 3, Red.]{#osi-layer-three .correct explanation="La capa de red describe el direccionamiento lógico y el reenvío entre redes."}
::option[Capa 1, Física.]{#osi-layer-one explanation="La capa física se ocupa de las señales y los medios."}
::option[Capa 7, Aplicación.]{#osi-layer-seven explanation="La capa de aplicación describe los servicios expuestos a las aplicaciones de red."}
:::

## Usar el modelo como vocabulario

Expresiones como «un bucle de capa 2» o «un puerto de capa 4» identifican un área funcional sin explicar todos los detalles de la implementación. Un protocolo real puede atravesar límites, y el cifrado, los túneles, los proxies o las redes superpuestas pueden crear varias capas anidadas.

:::single-choice{#osi-model-purpose} ¿Para qué resulta más útil el modelo OSI en el diagnóstico cotidiano?

::option[Para garantizar que todos los protocolos tengan exactamente siete cabeceras.]{#osi-seven-headers explanation="Las implementaciones no se corresponden una a una con siete cabeceras en la transmisión."}
::option[Para sustituir todas las capturas de paquetes por un diagrama.]{#osi-replace-captures explanation="El modelo orienta la investigación, pero no sustituye las pruebas."}
::option[Para proporcionar una forma compartida de clasificar las funciones de red.]{#osi-shared-vocabulary .correct explanation="El marco ayuda a los equipos a acotar el área funcional que se está analizando."}
:::

## Comparar OSI y TCP/IP

La suite de protocolos de Internet y el modelo de referencia OSI se desarrollaron mediante historias de estandarización distintas. El modelo práctico TCP/IP suele agrupar las responsabilidades de sesión y presentación de OSI en su capa de aplicación y combina los aspectos físicos y de enlace de datos en una capa de enlace o de acceso a la red. Las correspondencias son aproximadas, no demuestran que una pila se haya implementado directamente a partir de la otra.

:::single-choice{#osi-tcpip-mapping} ¿Cómo debe interpretarse una correspondencia entre las capas OSI y TCP/IP?

::option[Como una regla exacta que todos los protocolos deben obedecer.]{#osi-exact-rule explanation="Las responsabilidades de los protocolos suelen atravesar límites conceptuales."}
::option[Como prueba de que TCP/IP utiliza obligatoriamente siete capas durante la transmisión.]{#osi-tcp-seven explanation="TCP/IP suele describirse con cuatro o cinco capas."}
::option[Como una comparación aproximada entre modelos funcionales.]{#osi-approximate-map .correct explanation="Los modelos agrupan algunas responsabilidades de forma distinta."}
:::

## Diagnosticar entre capas

Empieza por el síntoma y comprueba los supuestos en lugar de revisar mecánicamente las capas en orden numérico. Un fallo web puede involucrar el estado del enlace local, el enrutamiento IP, la accesibilidad del transporte, TLS, la resolución de nombres, la autenticación o el comportamiento de la aplicación. Las pruebas de una capa pueden orientar la siguiente comprobación sin demostrar que las capas superiores funcionen.

:::single-choice{#osi-link-success-limit} ¿Qué demuestra que funcione un enlace Ethernet local?

::option[Que todos los servicios HTTP remotos funcionan correctamente.]{#osi-link-proves-http explanation="El estado del enlace local no permite determinar la salud de una aplicación remota."}
::option[Que DNS no contiene ningún registro incorrecto.]{#osi-link-proves-dns explanation="Los datos de nombres son independientes de la conectividad básica del enlace."}
::option[Únicamente que funcionan las condiciones pertinentes del enlace local.]{#osi-link-limited-proof .correct explanation="Aún puede haber fallos de enrutamiento, transporte, nombres, seguridad y aplicaciones."}
:::

## Resumen

Ahora puedes utilizar el modelo OSI como vocabulario de diagnóstico por capas.

1. Nombra las siete capas en orden.
2. Asocia cada capa con su responsabilidad general.
3. Trata las correspondencias con TCP/IP como aproximadas.
4. Usa las pruebas de cada capa para orientar las comprobaciones de extremo a extremo, no para sustituirlas.
