---
index: 4
lang: "pt"
title: "Dicas de Subnetting"
meta_title: "Subnetting Cheats - Subnetting"
meta_description: "Aprenda os fundamentos do subnetting e a conversão binária para redes. Entenda endereços IP e máscaras de sub-rede com este guia amigável para iniciantes. Comece a aprender agora!"
meta_keywords: "subnetting, conversão binária, endereço IP, rede, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

Odeio ter que adicionar esta seção. No mundo real, você provavelmente nunca precisaria fazer cálculos de sub-rede manualmente. No entanto, se você fosse entrevistado sobre isso, precisaria saber como converter de e para a forma binária para subnetting. Felizmente, existem algumas "trapaças" aritméticas que você pode memorizar.

Primeiro, memorize seus cálculos de base 2; apenas faça isso:

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

### Tabela de Decimal para Binário

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Existem muitas razões pelas quais a tabela a seguir se parece com o que parece. Se você está curioso para saber como funciona, há muitos recursos online.

Ok, memorizou isso? Vamos fazer uma rápida conversão de decimal para binário:

### Converter 192.168.23.43 para Binário

Lembre-se: 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Vamos percorrer a conversão do primeiro octeto para binário, e você entenderá como o resto funciona.

1. Você pode subtrair 192 - 128? Sim, então o primeiro bit é 1.
2. 192 - 128 = 64. O próximo número na tabela é 64. Você pode subtrair 64 - 64? Sim, então o segundo bit é 1.
3. Ficamos sem números para subtrair, então nossa forma binária de 192 é 11000000.

### Converter Binário 11000000 para Decimal

Para a conversão de binário para decimal, você soma os números que têm um 1, então:

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

A prática leva à perfeição! Embora a matemática de sub-rede seja frequentemente automatizada no mundo real, entender as conversões binárias subjacentes é crucial para entrevistas e para uma compreensão mais profunda de redes. Aqui está um laboratório prático para reforçar seu entendimento:

1. **[Realizar Subnetting IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine o subnetting IP e a conversão binária usando Python em um terminal Linux para converter endereços IP, traduzir máscaras CIDR e calcular detalhes de rede.

Este laboratório o ajudará a aplicar os conceitos de conversão binária e subnetting em um cenário prático e a construir confiança com os fundamentos de endereçamento de rede.

## Quiz Question

Qual é a conversão binária de 123?

## Quiz Answer

1111011
