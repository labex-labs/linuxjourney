---
lang: "es"
title: "ICMP"
meta_title: "ICMP - Resolución de Problemas"
meta_description: "Aprenda los conceptos básicos del protocolo ICMP, los tipos de mensajes y los códigos para la resolución de problemas de red. Comprenda cómo funciona ICMP para depurar problemas de red."
meta_keywords: "ICMP, protocolo ICMP, resolución de problemas de red, tipos ICMP, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

El Protocolo de Mensajes de Control de Internet (ICMP) forma parte del conjunto de protocolos TCP/IP. Se utiliza para enviar actualizaciones y mensajes de error y es un protocolo extremadamente útil para depurar problemas de red, como la entrega fallida de paquetes.

Cada mensaje ICMP contiene un campo de tipo, código y suma de verificación (checksum). El campo `type` indica el tipo de mensaje ICMP, el `code` es un subtipo que proporciona más información sobre el mensaje, y el `checksum` se utiliza para detectar cualquier problema con la integridad del mensaje.

Veamos algunos tipos comunes de ICMP:

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

Cuando un paquete no puede llegar a un destino, se genera un mensaje ICMP Type 3. Dentro del Type 3, hay 16 valores de `code` que describen con más detalle por qué no puede llegar al destino:

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  etc...etc...

Estos mensajes tendrán más sentido a medida que utilicemos algunas herramientas de solución de problemas de red.

## Exercise

No hay ejercicios para esta lección.

## Quiz Question

¿Cuál es el tipo de ICMP para una solicitud de eco?

## Quiz Answer

8
