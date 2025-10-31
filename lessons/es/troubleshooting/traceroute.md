---
index: 3
lang: "es"
title: "traceroute"
meta_title: "traceroute - Solución de problemas"
meta_description: "Domina el comando traceroute de Linux para trazar rutas de red y solucionar problemas de conectividad. Este tutorial explica cómo traceroute usa TTL para mapear la ruta que toman los paquetes hasta su destino."
meta_keywords: "traceroute, traceroute linux, redes Linux, solución de problemas de red, TTL, enrutamiento de paquetes, comandos Linux, principiante, tutorial"
---

## Lesson Content

El comando `traceroute` es una herramienta fundamental de diagnóstico de red utilizada para trazar la ruta que siguen los paquetes desde su computadora hasta un host de destino. Al revelar cada "salto" o router en el camino, ayuda a identificar cuellos de botella en la red y a solucionar problemas de conectividad. La utilidad `traceroute linux` es esencial para cualquier administrador de sistemas o ingeniero de redes.

### Cómo Funciona Traceroute

El mecanismo detrás de `traceroute` reside en su manipulación inteligente del campo Tiempo de Vida (TTL) en la cabecera de un paquete IP. El proceso funciona de la siguiente manera:

1. `traceroute` envía un paquete de sondeo con un valor TTL de 1.
2. El primer router en la ruta recibe el paquete, decrementa el TTL a 0 y lo descarta. Luego, el router envía un mensaje ICMP de "Tiempo Excedido" de vuelta a su computadora.
3. `traceroute` registra la dirección IP del router y el tiempo de ida y vuelta.
4. Luego envía otro paquete, esta vez con un TTL de 2. Este paquete pasa con éxito el primer router pero es descartado por el segundo router, que nuevamente envía un mensaje de "Tiempo Excedido".
5. Este proceso se repite, con el TTL incrementándose en uno por cada conjunto subsiguiente de paquetes. Al construir una lista de los routers que devuelven mensajes de "Tiempo Excedido", `traceroute` mapea toda la ruta.
6. El proceso concluye cuando los paquetes finalmente llegan al destino, el cual responde con un mensaje ICMP de "Respuesta de Eco".

### Entendiendo la Salida de Traceroute

Examinemos una salida de ejemplo al ejecutar `traceroute` en una terminal Linux:

```bash
$ traceroute google.com
traceroute a google.com (216.58.216.174), 30 saltos máx., paquetes de 60 bytes
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Cada línea numerada representa un salto a lo largo de la ruta de red. Así es como se interpreta la información:

- **Número de Salto:** La primera columna (ej. `1`, `2`, `3`) indica la secuencia del router en la ruta.
- **Nombre del Router y Dirección IP:** La siguiente parte muestra el nombre de host (si se puede resolver) y la dirección IP del router en ese salto.
- **Tiempos de Ida y Vuelta (RTT):** Las últimas tres columnas muestran el tiempo de ida y vuelta para cada uno de los tres paquetes de sondeo enviados a ese salto específico. Estos tiempos, medidos en milisegundos (ms), ayudan a evaluar la latencia en cada paso del viaje.

Usar el comando `traceroute linux` de manera efectiva proporciona una visión invaluable del rendimiento y la estructura de su red.

## Exercise

La práctica es clave para dominar el diagnóstico de redes. Los siguientes laboratorios prácticos le ayudarán a reforzar su comprensión del descubrimiento de rutas de red y la solución de problemas con herramientas como `traceroute`:

1. **[Administrar Direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practique el uso del comando `ip` para configurar ajustes de red y luego verifique la conectividad y las rutas de enrutamiento con `traceroute`.
2. **[Explorar la Interacción de la Capa de Red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda cómo funcionan juntos `ping` y `arp` para comprender las interacciones de la capa de red, que son conceptos fundamentales para el funcionamiento de `traceroute`.

Estos laboratorios le ayudarán a aplicar los conceptos de diagnóstico de red en escenarios del mundo real y a ganar confianza con las herramientas esenciales de redes en Linux.

## Quiz Question

What gets decremented by one when making hops across the network? (Please answer in English, paying attention to capitalization.)

## Quiz Answer

TTL
