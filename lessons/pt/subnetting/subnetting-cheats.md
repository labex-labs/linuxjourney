---
index: 4
lang: "pt"
title: "Cola de Sub-redes"
meta_title: "Cola de Sub-redes - Sub-redes"
meta_description: "Domine o subnetting com nosso guia de truques de conversão binária. Aprenda a usar a tabela 128+64+32+16+8+4+2+1 para converter rapidamente endereços IP de decimal para binário e vice-versa. Essencial para entrevistas e certificações de rede."
meta_keywords: "subnetting, conversão binária, endereço IP, rede, rede Linux, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, decimal para binário, matemática de sub-rede, tutorial, guia"
---

## Lesson Content

Na rede moderna, raramente você fará a matemática de sub-redes manualmente, pois ferramentas e calculadoras automatizam o processo. No entanto, entender a conversão manual entre decimal e binário é crucial para entrevistas de rede, exames de certificação e para obter uma compreensão mais profunda de como funciona o endereçamento IP. Esta lição fornece alguns truques simples para ajudá-lo a dominá-la.

Primeiro, é altamente benéfico memorizar os cálculos de base 2, pois eles formam a base da matemática binária.

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

### A Tabela de Conversão Binária

Para converter números facilmente, usamos uma tabela que representa o valor de cada bit em um octeto de 8 bits de um endereço IP.

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

Esta tabela é sua principal ferramenta. Cada número corresponde à posição de um bit. A soma total, `128+64+32+16+8+4+2+1`, é igual a 255, que é o maior valor possível em um octeto.

### Conversão de Decimal para Binário

Vamos converter o endereço IP `192.168.23.43` para binário. Vamos percorrer o primeiro octeto, `192`, para demonstrar o processo. Usamos os valores da nossa tabela: `128 64 32 16 8 4 2 1`.

1. Comece com o número `192`. Você pode subtrair 128 dele? Sim (192 - 128 = 64). Portanto, o primeiro bit é **1**.
2. Nosso novo número é `64`. Você pode subtrair o próximo valor, 64, dele? Sim (64 - 64 = 0). O segundo bit é **1**.
3. Nosso resto agora é `0`. Não podemos subtrair 32, 16, 8, 4, 2 ou 1. Portanto, os bits restantes são todos **0**.

A forma binária de 192 é `11000000`. Você pode aplicar este mesmo método de subtração aos outros octetos.

### Conversão de Binário para Decimal

Para converter de binário de volta para decimal, você simplesmente soma os valores da tabela onde aparece um `1` no número binário. Vamos converter `11000000` de volta para decimal.

Olhando para a tabela `128 64 32 16 8 4 2 1`, os dois primeiros bits são `1`. Isso significa que somamos os dois primeiros valores:

`128 + 64 = 192`

Como todos os outros bits são `0`, não somamos nenhum outro valor. A fórmula `128 + 64 + 0 + 0 + 0 + 0 + 0 + 0` nos dá 192. É simples assim!

## Exercise

A prática leva à perfeição! Embora a matemática de sub-redes seja frequentemente automatizada no mundo real, entender as conversões binárias subjacentes é crucial para entrevistas e uma compreensão mais profunda de redes. Aqui está um laboratório prático para reforçar sua compreensão:

1. **[Realizar Sub-redes IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine a sub-rede IP e a conversão binária usando Python em um terminal Linux para converter endereços IP, traduzir máscaras CIDR e calcular detalhes de rede.

Este laboratório ajudará você a aplicar os conceitos de conversão binária e sub-redes em um cenário prático e a construir confiança com os fundamentos de endereçamento de rede.

## Quiz Question

Qual é a conversão binária de 123? Por favor, forneça a resposta em caracteres em inglês (números).

## Quiz Answer

01111011
