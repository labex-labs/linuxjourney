---
index: 2
lang: "es"
title: "ping"
meta_title: "ping - Resolución de Problemas"
meta_description: "Aprende a usar el comando ping de Linux para probar la conectividad de red y solucionar problemas. Comprende ICMP, TTL y el tiempo de ida y vuelta para un diagnóstico de red efectivo."
meta_keywords: "Linux ping, conectividad de red, ICMP, TTL, redes Linux, Linux para principiantes, tutorial de Linux, comando ping"
---

## Lesson Content

Una de las herramientas de red más simples, **ping**, se utiliza para probar si un paquete puede llegar o no a un host. Funciona enviando paquetes ICMP echo request (Tipo 8) al host de destino y espera una respuesta ICMP echo reply (Tipo 0). Ping es exitoso cuando un host envía el paquete de solicitud y recibe una respuesta del objetivo. Veamos un ejemplo:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

En este ejemplo, estamos usando ping para verificar si podemos llegar a `www.google.com`. La bandera `-c` (count) se usa para dejar de enviar paquetes de solicitud de eco una vez que se ha alcanzado el conteo.

La primera parte dice que estamos enviando paquetes de 64 bytes a 74.125.239.112 (google.com), y el resto nos muestra los detalles del viaje. Por defecto, envía un paquete por segundo.

### icmp_seq

El campo `icmp_seq` se utiliza para mostrar el número de secuencia de los paquetes enviados. En este caso, envié 3 paquetes, y podemos ver que los 3 paquetes regresaron. Si haces un ping y te faltan algunos números de secuencia, eso significa que está ocurriendo algún problema de conectividad y no todos tus paquetes están llegando. Si el número de secuencia está desordenado, tu conexión es probablemente muy lenta, ya que tus paquetes están excediendo el valor predeterminado de un segundo.

### ttl

El campo Time To Live (TTL) se utiliza como un contador de saltos. A medida que realizas saltos, decrementa el contador en uno, y una vez que el contador de saltos llega a 0, nuestro paquete muere. Esto está destinado a darle una vida útil al paquete; no queremos que nuestros paquetes viajen para siempre.

### time

El tiempo de ida y vuelta que tomó desde que enviaste el paquete de solicitud de eco hasta que obtuviste una respuesta de eco.

## Exercise

Haz un ping a un sitio web y observa la salida que recibes.

## Quiz Question

¿Cuál es la unidad de medida del tiempo de ida y vuelta?

## Quiz Answer

ms
