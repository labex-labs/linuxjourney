---
lang: "es"
title: "Matemáticas de Subredes"
description: "Aprende los conceptos básicos de las matemáticas de subredes y cómo calcular los hosts disponibles en una red. Comprende el direccionamiento IP y las máscaras de subred para principiantes. ¡Comienza tu viaje en Linux!"
keywords: "matemáticas de subred, dirección IP, máscara de subred, hosts de red, binario, redes Linux, tutorial para principiantes, guía"
---

## Lesson Content

Bien, sabemos que las subnet masks son importantes para determinar cuántos hosts podemos tener en nuestra subred. Entonces, ¿cuántos hosts serían?

Digamos que tengo una dirección IP de **192.168.1.0** y una subnet mask de **255.255.255.0**. Ahora, alineemos estos números en formato binario. Por ahora, usa una calculadora en línea para convertir estos valores de decimal a binario.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

La dirección IP está enmascarada por nuestra subnet mask. Cuando ves un 1, está enmascarado, y pretendemos no verlo. Así que los únicos hosts posibles que podemos tener son de la región `00000000`. Recuerda, `11111111` en formato binario es igual a 255. También contamos el 0 como un número de host, por lo que hay 256 opciones posibles. Sin embargo, aunque parezca que tenemos 256 opciones posibles, en realidad restamos 2 hosts porque tenemos que considerar la dirección de broadcast y la dirección de subred, lo que nos deja con 254 hosts posibles en nuestra subred. Así que sabemos que podemos tener hosts con direcciones IP que van desde 192.168.1.1 hasta 192.168.1.254.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuál es el equivalente binario de 255?

## Quiz Answer

11111111
