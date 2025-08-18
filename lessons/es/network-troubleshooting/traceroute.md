---
lang: "es"
title: "traceroute"
meta_title: "traceroute - Resolución de Problemas"
meta_description: "Aprenda a usar el comando traceroute de Linux para rastrear rutas de red y solucionar problemas de conectividad. Comprenda TTL y el enrutamiento de paquetes para principiantes."
meta_keywords: "traceroute, redes Linux, solución de problemas de red, TTL, comandos Linux, principiante, tutorial"
---

## Lesson Content

El comando `traceroute` se utiliza para ver cómo se enrutan los paquetes. Funciona enviando paquetes con valores de TTL (Time To Live) crecientes, comenzando con 1. Así, el primer enrutador recibe el paquete y decrementa el valor de TTL en uno, descartando el paquete. El enrutador nos envía de vuelta un mensaje ICMP Time Exceeded. Luego, el siguiente paquete obtiene un TTL de 2, por lo que pasa el primer enrutador, pero cuando llega al segundo enrutador, el TTL es 0, y devuelve otro mensaje ICMP Time Exceeded. Traceroute funciona de esta manera porque a medida que envía y descarta paquetes, construye una lista de enrutadores que los paquetes atraviesan hasta que finalmente llega a su destino y recibe un mensaje ICMP Echo Reply.

Aquí hay un pequeño fragmento de un traceroute:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Cada línea representa un enrutador o máquina que se encuentra entre usted y su objetivo. Muestra el nombre del objetivo y su dirección IP, y las últimas tres columnas corresponden al tiempo de ida y vuelta de un paquete para llegar a ese enrutador. Por defecto, se envían tres paquetes a lo largo de la ruta.

## Exercise

Ejecute el comando `traceroute` en su máquina y observe la salida.

## Quiz Question

¿Qué se decrementa en uno al dar saltos a través de la red?

## Quiz Answer

TTL
