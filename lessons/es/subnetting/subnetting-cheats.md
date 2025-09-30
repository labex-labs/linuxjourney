---
index: 4
lang: "es"
title: "Trucos de Subnetting"
meta_title: "Trucos de Subnetting - Subnetting"
meta_description: "Aprende los conceptos básicos de subnetting y la conversión binaria para redes. Comprende las direcciones IP y las máscaras de subred con esta guía para principiantes. ¡Empieza a aprender ahora!"
meta_keywords: "subnetting, conversión binaria, dirección IP, red, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

Odio tener que añadir esta sección. En el mundo real, lo más probable es que nunca tengas que hacer cálculos de subredes a mano. Sin embargo, si te entrevistaran sobre esto, tendrás que saber cómo convertir a y desde la forma binaria para el subnetting. Afortunadamente, hay algunos trucos aritméticos que puedes memorizar.

Primero, memoriza tus cálculos de base 2; simplemente hazlo:

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256
- 2^9 = 512
- 2^10 = 1024
- 2^11 = 2048
- 2^12 = 4096

### Tabla de Decimal a Binario

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Hay muchas razones por las que la siguiente tabla se ve como se ve. Si tienes curiosidad sobre cómo funciona, hay muchos recursos en línea.

Bien, ¿los tienes memorizados? Hagamos una conversión rápida de decimal a binario:

### Convertir 192.168.23.43 a Binario

Recuerda: 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Vamos a ver cómo convertir el primer octeto a binario, y entenderás cómo funciona el resto.

1. ¿Puedes restar 192 - 128? Sí, entonces el primer bit es 1.
2. 192 - 128 = 64. El siguiente número en la tabla es 64. ¿Puedes restar 64 - 64? Sí, entonces el segundo bit es 1.
3. Nos hemos quedado sin números para restar, así que nuestra forma binaria de 192 es 11000000.

### Convertir Binario 11000000 a Decimal

Para la conversión de binario a decimal, sumas los números que tienen un 1, así:

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

¡La práctica hace al maestro! Si bien las matemáticas de subredes a menudo se automatizan en el mundo real, comprender las conversiones binarias subyacentes es crucial para las entrevistas y para una comprensión más profunda de las redes. Aquí tienes un laboratorio práctico para reforzar tu comprensión:

1. **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domina el subnetting IP y la conversión binaria usando Python en una terminal de Linux para convertir direcciones IP, traducir máscaras CIDR y calcular detalles de red.

Este laboratorio te ayudará a aplicar los conceptos de conversión binaria y subnetting en un escenario práctico y a generar confianza con los fundamentos del direccionamiento de red.

## Quiz Question

¿Cuál es la conversión binaria de 123?

## Quiz Answer

1111011
