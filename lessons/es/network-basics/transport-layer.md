---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "es"
order_index: 6
title: "Capa de transporte"
description: "Aprende cómo TCP y UDP utilizan puertos y distintas semánticas de entrega entre los puntos finales de las aplicaciones."
meta_title: "Capa de transporte - Network Basics"
meta_description: "Explora la capa de transporte en las redes Linux. Esta lección explica protocolos como TCP y UDP, la función de los puertos, la segmentación de datos y el intercambio inicial de TCP para transferir datos de forma fiable."
meta_keywords: "capa de transporte Linux, TCP, UDP, handshake TCP, puertos de red, segmentación de datos, redes Linux, protocolos de red, transferencia fiable de datos"
---

La capa de transporte conecta los puntos finales de las aplicaciones a través de una red IP. TCP y UDP utilizan números de puerto de 16 bits, pero ofrecen a las aplicaciones modelos de comunicación y garantías diferentes.

## Puertos y sockets

Un puerto de destino ayuda al sistema operativo a entregar el tráfico a un socket a la escucha. Una conexión o un flujo se identifica mediante algo más que un puerto: importan el protocolo, las direcciones de origen y destino y los puertos de origen y destino. Por tanto, un mismo puerto de servidor puede atender simultáneamente a muchos clientes.

:::single-choice{#transport-layer-many-clients}
¿Cómo puede un único puerto de servidor TCP atender a varios clientes a la vez?

::option[Cada conexión tiene una combinación distinta de direcciones y puertos de sus puntos finales.]{#transport-layer-connection-tuple .correct explanation="La tupla completa de transporte distingue las conexiones simultáneas que comparten un puerto a la escucha."}
::option[El servidor cambia permanentemente el nombre de su puerto después de cada paquete.]{#transport-layer-renames-port explanation="El puerto a la escucha puede permanecer estable mientras las conexiones aceptadas tienen tuplas de pares distintas."}
::option[IP elimina todas las direcciones de origen antes de la entrega.]{#transport-layer-removes-source explanation="Las direcciones de origen forman parte de la identificación del par y de la ruta."}
:::

## Flujos de bytes TCP

TCP proporciona un flujo de bytes ordenado y fiable mientras la conexión siga siendo viable. Utiliza números de secuencia, confirmaciones, retransmisiones, control de flujo y control de congestión. TCP no conserva los límites de los mensajes de la aplicación: una escritura puede llegar mediante varias lecturas, o una lectura puede devolver varias escrituras. Las aplicaciones definen su propio formato de delimitación.

Fiabilidad no significa entrega absoluta. Una conexión puede agotar su tiempo de espera, restablecerse o fallar, y una confirmación no demuestra que una aplicación haya guardado los datos de forma duradera.

:::single-choice{#transport-layer-tcp-boundaries}
¿Qué ocurre con los límites de los mensajes de una aplicación en TCP?

::option[TCP expone un flujo de bytes ordenado sin conservar los límites de las escrituras.]{#transport-layer-byte-stream .correct explanation="El protocolo de aplicación debe definir cómo se delimitan o dimensionan los mensajes."}
::option[Cada escritura se convierte exactamente en un paquete IP y una lectura.]{#transport-layer-one-write-packet explanation="La segmentación, el almacenamiento en búfer y las API de recepción no conservan esa correspondencia."}
::option[TCP convierte cada mensaje en un registro DNS.]{#transport-layer-tcp-dns explanation="DNS es un protocolo de aplicación independiente."}
:::

## El intercambio inicial de TCP

Una conexión TCP normal comienza con un intercambio de tres pasos:

1. El iniciador envía `SYN` con su información de secuencia inicial.
2. El receptor responde con `SYN-ACK`, su propia información de secuencia y una confirmación.
3. El iniciador devuelve `ACK`.

Esto establece el estado de transporte en ambos puntos finales. No autentica al servidor de la aplicación ni demuestra que la operación solicitada a la aplicación vaya a tener éxito.

:::single-choice{#transport-layer-handshake-order}
¿Cuál es el orden normal del intercambio TCP de tres pasos?

::option[SYN, SYN-ACK, ACK.]{#transport-layer-syn-order .correct explanation="El intercambio sincroniza y confirma el estado inicial de la conexión en ambas direcciones."}
::option[ACK, ACK, SYN.]{#transport-layer-ack-ack-syn explanation="El iniciador solicita primero la sincronización."}
::option[SYN, FIN, RST.]{#transport-layer-syn-fin-rst explanation="FIN y RST cierran o cancelan el estado en lugar de formar un intercambio inicial normal."}
:::

## Datagramas UDP

UDP conserva los límites de los datagramas y proporciona detección de errores mediante sumas de comprobación, pero no ofrece el estado de conexión, el orden, la retransmisión, el control de flujo ni el control de congestión de TCP. Una aplicación puede añadir por sí misma la fiabilidad o el comportamiento de congestión que necesite. UDP no es automáticamente más rápido; el rendimiento depende del diseño del protocolo, la carga de trabajo, la ruta y la implementación.

:::single-choice{#transport-layer-udp-boundaries}
¿Qué propiedad ofrece UDP a las aplicaciones?

::option[Un flujo de bytes ordenado que se retransmite automáticamente.]{#transport-layer-udp-stream explanation="Eso describe servicios similares a TCP, no UDP básico."}
::option[La conservación de los límites entre los datagramas enviados.]{#transport-layer-udp-datagrams .correct explanation="Un datagrama UDP recibido corresponde a un datagrama enviado, salvo que se pierda."}
::option[La entrega garantizada antes de un plazo fijo.]{#transport-layer-udp-deadline explanation="UDP no garantiza ningún plazo de entrega."}
:::

## Inspeccionar puntos finales de transporte

Usa `ss` para inspeccionar sockets a la escucha y conectados sin modificarlos:

```bash
$ ss -lntup
$ ss -tn state established
```

Los detalles de los procesos pueden requerir privilegios. Un socket a la escucha solo demuestra disponibilidad local en el límite de transporte; el cortafuegos, el enrutamiento, la familia de direcciones, TLS y la salud de la aplicación aún requieren las pruebas apropiadas.

:::single-choice{#transport-layer-listener-proof}
¿Qué establece un socket TCP a la escucha?

::option[Que todos los cortafuegos remotos permiten la conexión.]{#transport-layer-all-firewalls explanation="El estado del socket local no revela todas las políticas de la ruta."}
::option[Que la aplicación ha superado todas las comprobaciones de salud.]{#transport-layer-all-health explanation="Escuchar constituye una prueba más débil que una transacción satisfactoria de la aplicación."}
::option[Que un proceso local está preparado para aceptar conexiones TCP coincidentes.]{#transport-layer-local-listener .correct explanation="La accesibilidad remota y las respuestas correctas de la aplicación siguen siendo cuestiones independientes."}
:::

## Resumen

Ahora puedes distinguir el comportamiento de los flujos TCP del de los datagramas UDP.

1. Identifica un flujo mediante el protocolo, las direcciones y los puertos.
2. Trata TCP como un flujo de bytes fiable y ordenado sin límites de mensajes.
3. Reconoce qué demuestra y qué no demuestra el intercambio inicial de TCP.
4. Trata la fiabilidad y el comportamiento de congestión de UDP como decisiones de diseño de la aplicación.
5. Comprueba la salud de la aplicación más allá del estado del socket local.
