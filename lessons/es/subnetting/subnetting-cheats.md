---
lesson_id: "subnetting-cheats"
course_id: "subnetting"
lang: "es"
order_index: 4
title: "Atajos para calcular subredes"
description: "Aprende métodos compactos con binarios y tamaños de bloque para comprobar cálculos de subredes IPv4."
meta_title: "Atajos para calcular subredes - Subnetting"
meta_description: "Domina las subredes con esta guía de atajos de conversión binaria. Aprende a usar la tabla 128+64+32+16+8+4+2+1 para convertir rápidamente direcciones IP entre decimal y binario."
meta_keywords: "subredes, conversión binaria, dirección IP, red, redes Linux, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, decimal a binario, cálculos de subred, tutorial, guía"
---

Las calculadoras de subredes son útiles, pero un pequeño conjunto de patrones binarios facilita comprobar sus resultados. Estos métodos sirven como comprobaciones, no sustituyen la confirmación de la asignación real y la política de enrutamiento.

## Valores de los bits de un octeto

Un octeto IPv4 utiliza estos valores posicionales:

```text
bit:    1   1   1   1   1  1  1  1
value: 128  64  32  16   8  4  2  1
```

La suma de los ocho valores produce 255. El decimal 192 es `128 + 64`, por lo que su representación binaria es `11000000`.

:::single-choice{#subnet-cheats-binary-192}
¿Cuál es la representación binaria de ocho bits del decimal 192?

::option[`11000000`]{#subnet-cheats-192-correct .correct explanation="Las posiciones 128 y 64 están activadas y las restantes valen cero."}
::option[`10101000`]{#subnet-cheats-168 explanation="Este patrón equivale a 168."}
::option[`11111111`]{#subnet-cheats-255 explanation="Las ocho posiciones activadas equivalen a 255."}
:::

## Máscaras habituales de octetos parciales

Los bits de prefijo contiguos producen una secuencia breve de máscaras:

```text
bits set: 0    1    2    3    4    5    6    7    8
decimal:  0  128  192  224  240  248  252  254  255
```

Por ejemplo, `/19` contiene 16 bits de prefijo completos y tres bits en el tercer octeto, por lo que su máscara es `255.255.224.0`.

:::single-choice{#subnet-cheats-prefix-19}
¿Qué máscara corresponde al `/19` de IPv4?

::option[`255.255.224.0`]{#subnet-cheats-mask-19 .correct explanation="Dieciséis bits completos y tres más producen 255, 255 y 224."}
::option[`255.255.19.0`]{#subnet-cheats-literal-19 explanation="Una longitud de prefijo es una cantidad de bits, no un octeto decimal de la máscara."}
::option[`255.255.255.19`]{#subnet-cheats-tail-19 explanation="Esta no es una máscara contigua de 19 bits."}
:::

## Tamaños de bloque

En el primer octeto de la máscara que no sea 255, resta su valor de 256 para obtener el incremento de la subred. Una máscara `/27` termina en 224, lo que da un tamaño de bloque de `256 - 224 = 32`. Por tanto, los límites del último octeto son 0, 32, 64, 96, 128, 160, 192 y 224.

La dirección `198.51.100.77/27` se encuentra en el bloque que abarca de 64 a 95.

:::single-choice{#subnet-cheats-77-network}
¿Cuál es la dirección de red de `198.51.100.77/27`?

::option[`198.51.100.32`]{#subnet-cheats-network-32 explanation="Ese bloque abarca los valores del último octeto de 32 a 63."}
::option[`198.51.100.77`]{#subnet-cheats-network-77 explanation="La dirección contiene bits de host y no es el límite del bloque."}
::option[`198.51.100.64`]{#subnet-cheats-network-64 .correct explanation="El bloque `/27` que comienza en 64 abarca de 64 a 95."}
:::

## Convertir un octeto arbitrario

Para convertir el decimal 123, selecciona los valores restantes más grandes sin sobrepasarlo:

```text
123 = 64 + 32 + 16 + 8 + 2 + 1
    = 01111011
```

Para volver a convertirlo, suma únicamente los valores posicionales cuyos bits valgan uno. Conserva siempre las ocho posiciones al trabajar dentro de un octeto IPv4.

:::single-choice{#subnet-cheats-binary-123}
¿Qué valor de ocho bits equivale al decimal 123?

::option[`1111011`]{#subnet-cheats-123-seven-bit explanation="El valor numérico es equivalente, pero la representación del octeto debe conservar ocho posiciones."}
::option[`01111011`]{#subnet-cheats-123-correct .correct explanation="Las posiciones activadas suman 64 + 32 + 16 + 8 + 2 + 1."}
::option[`01111100`]{#subnet-cheats-124 explanation="Este patrón activa la posición 4 en lugar de 2 y 1, lo que produce 124."}
:::

## Resumen

Ahora puedes comprobar cálculos IPv4 habituales mediante patrones binarios compactos.

1. Usa los ocho valores posicionales del octeto, desde 128 hasta 1.
2. Recuerda la secuencia de máscaras contiguas de octetos parciales.
3. Obtén el tamaño del bloque restando la máscara parcial de 256.
4. Conserva ocho bits al convertir octetos individuales.
