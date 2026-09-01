---
lesson_id: "subnet-math"
course_id: "subnetting"
lang: "es"
order_index: 3
title: "Cálculos de subredes"
description: "Aprende a calcular la red, el broadcast, el intervalo y la cantidad de direcciones IPv4 a partir de un prefijo."
meta_title: "Cálculos de subredes - Subnetting"
meta_description: "Domina los fundamentos de los cálculos de subredes. Esta guía explica cómo utilizar una máscara para calcular el número de hosts disponibles y los conceptos binarios esenciales del direccionamiento IP."
meta_keywords: "cálculos de subredes, cálculos de máscaras de subred, dirección IP, máscara de subred, hosts de red, binario, redes Linux, cálculo de hosts, tutorial para principiantes"
---

Los cálculos de subredes aplican una longitud de prefijo a los 32 bits de una dirección IPv4. Razonar en binario evita errores en los límites de prefijo que no coinciden con octetos decimales.

## Encontrar la dirección de red

Utiliza la dirección `192.168.1.165/24`:

```text
address  11000000.10101000.00000001.10100101
mask     11111111.11111111.11111111.00000000
network  11000000.10101000.00000001.00000000
```

Una operación AND bit a bit conserva los bits de la dirección donde la máscara vale uno y pone a cero los bits de host. El resultado es `192.168.1.0/24`.

:::single-choice{#subnet-math-network-operation} ¿Qué operación obtiene una dirección de red IPv4 a partir de una dirección y una máscara?

::option[Concatenación de cadenas decimales.]{#subnet-math-concatenation explanation="Unir los octetos mostrados no aplica los bits del prefijo."}
::option[Resta de puertos de transporte.]{#subnet-math-port-subtraction explanation="Los puertos no están relacionados con el prefijo de red."}
::option[AND bit a bit.]{#subnet-math-bitwise-and .correct explanation="Los bits de red permanecen, mientras que las posiciones de host enmascaradas con ceros se borran."}
:::

## Contar direcciones

Para el prefijo `/p`, la parte de host contiene `32 - p` bits. La cantidad total de direcciones es:

```text
2^(32 - p)
```

Por tanto, un `/24` contiene `2^8 = 256` direcciones. En una subred tradicional con broadcast, el valor de host con todos los bits a cero es la dirección de red y el valor con todos los bits a uno es el broadcast dirigido, por lo que quedan 254 direcciones ordinarias de host unicast.

:::single-choice{#subnet-math-24-total} ¿Cuántas direcciones totales contiene un `/24` de IPv4?

::option[24]{#subnet-math-total-24 explanation="La longitud del prefijo cuenta bits de red, no direcciones."}
::option[256]{#subnet-math-total-256 .correct explanation="Ocho bits de host producen 2^8 valores de dirección distintos."}
::option[254]{#subnet-math-total-254 explanation="Esa es la cantidad tradicional de hosts utilizables después de reservar dos direcciones especiales, no el total."}
:::

## Encontrar el límite de un bloque

Para `/26`, la máscara es `255.255.255.192`. El tamaño del bloque en el último octeto es `256 - 192 = 64`, por lo que los límites de las subredes son 0, 64, 128 y 192. La dirección `192.168.1.165/26` se encuentra en:

```text
network:   192.168.1.128
broadcast: 192.168.1.191
range:     192.168.1.129 through 192.168.1.190
```

:::single-choice{#subnet-math-165-network} ¿Cuál es la dirección de red de `192.168.1.165/26`?

::option[`192.168.1.0`]{#subnet-math-network-zero explanation="Ese es el primer bloque `/26`, que abarca de 0 a 63."}
::option[`192.168.1.165`]{#subnet-math-network-self explanation="La dirección proporcionada tiene bits de host distintos de cero dentro del `/26`."}
::option[`192.168.1.128`]{#subnet-math-network-128 .correct explanation="El valor 165 se encuentra en el bloque que abarca de 128 a 191."}
:::

## Tener en cuenta las excepciones de prefijos

El atajo `2^host_bits - 2` no es universal. Los prefijos IPv4 `/31` están definidos para enlaces punto a punto donde ambas direcciones pueden ser puntos finales y no se necesita broadcast dirigido. Un `/32` identifica una ruta de host o una dirección de interfaz. La tecnología de red y el uso del protocolo determinan qué direcciones pueden asignarse.

:::single-choice{#subnet-math-31-exception} ¿Por qué no debes restar dos direcciones de todos los prefijos IPv4?

::option[Las direcciones IPv4 no contienen bits de host en ningún prefijo.]{#subnet-math-no-host-bits explanation="La mayoría de los prefijos dejan uno o varios bits de host."}
::option[Los enlaces punto a punto `/31` pueden utilizar ambas direcciones como puntos finales.]{#subnet-math-31-both .correct explanation="El modelo punto a punto no necesita las reservas tradicionales de red y broadcast dirigido."}
::option[Todas las redes IPv4 utilizan multicast en lugar de unicast.]{#subnet-math-all-multicast explanation="El direccionamiento unicast ordinario sigue siendo fundamental."}
:::

## Comprobar los cálculos

Utiliza una herramienta o biblioteca independiente para comprobar el trabajo manual y compáralo después con la configuración real de las interfaces y las rutas. Un prefijo matemáticamente válido aún puede entrar en conflicto con otra subred o incumplir un plan de asignación.

:::single-choice{#subnet-math-valid-not-safe} ¿Qué no demuestra un cálculo correcto de subred?

::option[Que el plan de direcciones no tenga solapamientos ni conflictos de políticas.]{#subnet-math-no-conflict .correct explanation="Aún se necesitan pruebas de la asignación operativa y el enrutamiento."}
::option[Que las direcciones IPv4 contengan 32 bits.]{#subnet-math-proves-size explanation="El cálculo se basa en ese tamaño fijo."}
::option[Que las potencias de dos determinen la cantidad de bloques.]{#subnet-math-powers explanation="Las combinaciones de direcciones binarias utilizan inherentemente potencias de dos."}
:::

## Resumen

Ahora puedes calcular los límites de las subredes IPv4 y reconocer las excepciones habituales.

1. Obtén una dirección de red mediante AND bit a bit.
2. Cuenta las direcciones totales a partir del número de bits de host.
3. Usa los tamaños de bloque para localizar los límites de red y broadcast.
4. Trata `/31` y `/32` según el uso previsto.
5. Comprueba los resultados matemáticos con el plan de direcciones real.
