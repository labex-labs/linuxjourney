---
index: 4
lang: "pt"
title: "Dicas de Subnetting"
meta_title: "Dicas de Subnetting - Subnetting"
meta_description: "Aprenda os fundamentos do subnetting e a conversão binária para redes. Entenda endereços IP e máscaras de sub-rede com este guia para iniciantes. Comece a aprender agora!"
meta_keywords: "subnetting, conversão binária, endereço IP, rede, redes Linux, iniciante, tutorial, guia"
---

## Lesson Content

Odeio ter que adicionar esta seção. No mundo real, você provavelmente nunca precisaria fazer cálculos de subnetting manualmente. No entanto, se você fosse entrevistado sobre isso, precisaria saber como converter de e para a forma binária para subnetting. Felizmente, existem algumas "trapaças" aritméticas que você pode memorizar.

Primeiro, memorize seus cálculos de base-2; apenas faça isso:

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

### Decimal to Binary Chart

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Existem muitas razões pelas quais o gráfico a seguir se parece com o que é. Se você está curioso para saber como funciona, há muitos recursos online.

Ok, memorizou isso? Vamos fazer uma rápida conversão de decimal para binário:

### Convert 192.168.23.43 to Binary

Lembre-se: 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Vamos percorrer a conversão do primeiro octeto para binário, e você entenderá como o resto funciona.

1. Você pode subtrair 192 - 128? Sim, então o primeiro bit é 1.
2. 192 - 128 = 64. O próximo número na tabela é 64. Você pode subtrair 64 - 64? Sim, então o segundo bit é 1.
3. Ficamos sem números para subtrair, então nossa forma binária de 192 é 11000000.

### Convert Binary 11000000 to Decimal

Para a conversão de binário para decimal, você soma os números que têm um 1, então:

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

Observe seu endereço IP e máscara de sub-rede e veja quantos hosts você pode ter em sua sub-rede.

## Quiz Question

Qual é a conversão binária de 123?

## Quiz Answer

1111011
