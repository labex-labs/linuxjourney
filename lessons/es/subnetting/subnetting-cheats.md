---
index: 4
lang: "es"
title: "Trucos de Subnetting"
meta_title: "Trucos de Subnetting - Subredes"
meta_description: "Domina el subnetting con nuestra guía de trucos de conversión binaria. Aprende a usar la tabla 128+64+32+16+8+4+2+1 para convertir rápidamente direcciones IP de decimal a binario y viceversa. Esencial para entrevistas de redes y certificaciones."
meta_keywords: "subnetting, conversión binaria, dirección IP, red, redes Linux, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, decimal a binario, matemáticas de subredes, tutorial, guía"
---

## Lesson Content

En el networking moderno, rara vez realizarás cálculos de subredes a mano, ya que las herramientas y calculadoras automatizan el proceso. Sin embargo, comprender la conversión manual entre decimal y binario es crucial para las entrevistas de redes, los exámenes de certificación y para obtener una comprensión más profunda de cómo funciona el direccionamiento IP. Esta lección proporciona algunos trucos sencillos para ayudarte a dominarlo.

Primero, es muy beneficioso memorizar los cálculos de base 2, ya que forman la base de las matemáticas binarias.

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

### La Tabla de Conversión Binaria

Para convertir números fácilmente, utilizamos una tabla que representa el valor de cada bit en un octeto de 8 bits de una dirección IP.

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Esta tabla es tu herramienta principal. Cada número corresponde a la posición de un bit. La suma total, `128+64+32+16+8+4+2+1`, es igual a 255, que es el valor más alto posible en un octeto.

### Conversión de Decimal a Binario

Vamos a convertir la dirección IP `192.168.23.43` a binario. Analizaremos el primer octeto, `192`, para demostrar el proceso. Usamos los valores de nuestra tabla: `128 64 32 16 8 4 2 1`.

1. Comienza con el número `192`. ¿Puedes restarle 128? Sí (192 - 128 = 64). Por lo tanto, el primer bit es **1**.
2. Nuestro nuevo número es `64`. ¿Puedes restarle el siguiente valor, 64? Sí (64 - 64 = 0). El segundo bit es **1**.
3. Nuestro resto es ahora `0`. No podemos restar 32, 16, 8, 4, 2 ni 1. Por lo tanto, los bits restantes son todos **0**.

La forma binaria de 192 es `11000000`. Puedes aplicar este mismo método de resta a los otros octetos.

### Conversión de Binario a Decimal

Para convertir de binario a decimal, simplemente sumas los valores de la tabla donde aparece un `1` en el número binario. Convirtamos `11000000` de nuevo a decimal.

Observando la tabla `128 64 32 16 8 4 2 1`, los dos primeros bits son `1`. Esto significa que sumamos los dos primeros valores:

`128 + 64 = 192`

Como todos los demás bits son `0`, no sumamos ningún otro valor. La fórmula `128 + 64 + 0 + 0 + 0 + 0 + 0 + 0` nos da 192. ¡Es así de simple!

## Exercise

¡La práctica hace al maestro! Aunque los cálculos de subredes a menudo se automatizan en el mundo real, comprender las conversiones binarias subyacentes es crucial para las entrevistas y una comprensión más profunda del networking. Aquí tienes un laboratorio práctico para reforzar tu comprensión:

1. **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domina el subnetting IP y la conversión binaria utilizando Python en una terminal de Linux para convertir direcciones IP, traducir máscaras CIDR y calcular detalles de red.

Este laboratorio te ayudará a aplicar los conceptos de conversión binaria y subnetting en un escenario práctico y a ganar confianza con los fundamentos del direccionamiento de red.

## Quiz Question

¿Cuál es la conversión binaria de 123? Por favor, proporciona la respuesta usando caracteres en inglés (números).

## Quiz Answer

1111011
