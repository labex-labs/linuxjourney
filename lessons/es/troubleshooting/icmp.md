---
lesson_id: "icmp"
course_id: "troubleshooting"
lang: "es"
order_index: 1
title: "ICMP"
description: "Aprende cómo ICMP informa de errores IP, ayuda al diagnóstico y permite funciones esenciales de IPv4 e IPv6."
meta_title: "ICMP - Resolución de problemas"
meta_description: "Este tutorial de Linux explica el protocolo ICMP y sus tipos y códigos de mensaje para diagnosticar problemas de red con eficacia."
meta_keywords: "ICMP, protocolo ICMP, resolución de problemas de red, tipos ICMP, redes Linux, aprender Linux, tutorial Linux, principiantes, guía"
---

Internet Control Message Protocol transporta información de control, error y diagnóstico junto con IP. ICMP para IPv4 e ICMPv6 son protocolos relacionados pero distintos, con números de tipo de mensaje y responsabilidades diferentes.

## Tipos, códigos y sumas de comprobación

Un mensaje ICMP tiene un tipo, un código más específico cuando corresponde y una suma de comprobación. Los mensajes de error normalmente incluyen parte del paquete que los provocó para que el emisor pueda asociar el error con un flujo.

:::single-choice{#icmp-code-purpose}
¿Qué aporta un código ICMP?

::option[Un nombre DNS permanente para el router que informa.]{#icmp-code-dns explanation="La resolución de nombres no es la finalidad codificada en este campo."}
::option[Un significado más específico dentro de un tipo de mensaje ICMP.]{#icmp-code-specific .correct explanation="Por ejemplo, los códigos de destino inalcanzable distinguen varios motivos de fallo."}
::option[La carga útil completa de todos los paquetes anteriores.]{#icmp-code-all-payload explanation="Según las reglas del protocolo, un error solo cita la parte del paquete causante necesaria para identificarlo."}
:::

## Mensajes de eco y error

En ICMPv4, Echo Request es el tipo 8 y Echo Reply el tipo 0. Destination Unreachable es el tipo 3 y Time Exceeded el tipo 11. ICMPv6 utiliza números de tipo diferentes, por lo que siempre debes identificar la familia de direcciones antes de interpretar una captura.

:::single-choice{#icmpv4-echo-request-type}
¿Cuál es el tipo de Echo Request de ICMPv4?

::option[0]{#icmp-type-zero explanation="El tipo cero es Echo Reply de ICMPv4."}
::option[11]{#icmp-type-eleven explanation="El tipo once es Time Exceeded de ICMPv4."}
::option[8]{#icmp-type-eight .correct explanation="Ping normalmente envía este mensaje ICMPv4 para solicitar una respuesta de eco."}
:::

## MTU de ruta e ICMP esencial

ICMP no es simplemente tráfico ping opcional. Los errores de fragmentación necesaria de IPv4 y los mensajes Packet Too Big de ICMPv6 permiten descubrir la MTU de la ruta. ICMPv6 también transporta Neighbor Discovery y Router Advertisements. Por tanto, bloquear todo ICMP puede crear agujeros negros e impedir el funcionamiento de IPv6.

Filtra por el tipo, la dirección, la frecuencia y el alcance necesarios en lugar de aplicar una regla indiscriminada. Los atacantes pueden falsificar algunos mensajes ICMP, así que valida el contexto del paquete citado y contrástalo con las rutas y capturas locales.

:::single-choice{#icmp-block-all-risk}
¿Por qué bloquear todo ICMP puede interrumpir tráfico válido?

::option[Cada respuesta HTTP se transporta dentro de un Echo Reply ICMP.]{#icmp-http-echo explanation="HTTP normalmente utiliza TCP o QUIC en vez de eco ICMP."}
::option[ICMP almacena todas las contraseñas de las aplicaciones.]{#icmp-passwords explanation="No es una base de datos de credenciales."}
::option[ICMP transporta información de control necesaria para la MTU de ruta e IPv6.]{#icmp-essential-control .correct explanation="Suprimir estos mensajes puede impedir el dimensionamiento correcto de paquetes o el descubrimiento de vecinos y routers."}
:::

## Interpretar el silencio

La ausencia de una respuesta ICMP puede deberse a filtrado, limitación de frecuencia, enrutamiento asimétrico, falta de una ruta de retorno, un host caído o un dispositivo que simplemente no responde a ese mensaje. A la inversa, un dispositivo intermedio, y no el destino final, puede generar un error ICMP.

:::single-choice{#icmp-silence-meaning}
¿Qué demuestra por sí sola la ausencia de Echo Reply?

::option[Que la aplicación de destino está detenida con certeza.]{#icmp-silence-app-down explanation="El servicio puede funcionar mientras el tráfico de eco se filtra o ignora."}
::option[Que el nombre del destino se eliminó del DNS.]{#icmp-silence-dns-deleted explanation="Una prueba con una dirección numérica puede no recibir respuesta independientemente del DNS."}
::option[Únicamente que no se observó respuesta en este intercambio de eco.]{#icmp-silence-limited .correct explanation="Se necesitan más pruebas de ruta, transporte, aplicación y captura para identificar la causa."}
:::

## Resumen

Ahora puedes interpretar ICMP como evidencia de control y no como un veredicto binario sobre la conectividad.

1. Lee el tipo y el código en la familia IP correcta.
2. Reconoce las funciones de eco, destino inalcanzable y tiempo excedido.
3. Conserva el ICMP necesario para la MTU de ruta y el funcionamiento de IPv6.
4. Correlaciona los errores y el silencio con otras pruebas de la ruta.
