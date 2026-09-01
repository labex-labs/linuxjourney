---
lesson_id: "subnetting-cheats"
course_id: "subnetting"
lang: "pt"
order_index: 4
title: "Atalhos para sub-redes"
description: "Aprenda métodos binários compactos e de tamanho de bloco para conferir cálculos de sub-redes IPv4."
meta_title: "Atalhos para sub-redes - Sub-redes"
meta_description: "Domine a divisão em sub-redes com nosso guia de atalhos para conversão binária. Aprenda a usar a tabela 128+64+32+16+8+4+2+1 para converter rapidamente endereços IP de decimal para binário e vice-versa. Essencial para entrevistas e certificações de redes."
meta_keywords: "divisão em sub-redes, conversão binária, endereço IP, rede, redes Linux, 128+64+32+16+8+4+2+1, 128 64 32 16 8 4 2 1, decimal para binário, cálculos de sub-redes, tutorial, guia"
---

Calculadoras de sub-redes são úteis, mas um pequeno conjunto de padrões binários facilita a conferência de seus resultados. Esses métodos servem para verificação, não substituem a confirmação da alocação real e da política de roteamento.

## Valores dos bits de um octeto

Um octeto IPv4 usa estes valores posicionais:

```text
bit:    1   1   1   1   1  1  1  1
value: 128  64  32  16   8  4  2  1
```

A soma dos oito valores produz 255. O decimal 192 é `128 + 64`, portanto sua representação binária é `11000000`.

:::single-choice{#subnet-cheats-binary-192} Qual é a representação do decimal 192 em binário de oito bits?

::option[`11000000`]{#subnet-cheats-192-correct .correct explanation="As posições 128 e 64 estão definidas, e as demais são zero."}
::option[`10101000`]{#subnet-cheats-168 explanation="Esse padrão equivale a 168."}
::option[`11111111`]{#subnet-cheats-255 explanation="As oito posições definidas equivalem a 255."}
:::

## Máscaras comuns em octetos parciais

Bits de prefixo contíguos produzem uma pequena sequência de máscaras:

```text
bits set: 0    1    2    3    4    5    6    7    8
decimal:  0  128  192  224  240  248  252  254  255
```

Por exemplo, `/19` contém 16 bits completos de prefixo e mais três bits no terceiro octeto, portanto sua máscara é `255.255.224.0`.

:::single-choice{#subnet-cheats-prefix-19} Qual máscara corresponde ao IPv4 `/19`?

::option[`255.255.224.0`]{#subnet-cheats-mask-19 .correct explanation="Dezesseis bits completos e mais três resultam em 255, 255 e 224."}
::option[`255.255.19.0`]{#subnet-cheats-literal-19 explanation="Um comprimento de prefixo é uma contagem de bits, não um octeto decimal da máscara."}
::option[`255.255.255.19`]{#subnet-cheats-tail-19 explanation="Essa não é uma máscara contígua de 19 bits."}
:::

## Tamanhos de bloco

No primeiro octeto da máscara que não seja 255, subtraia o valor da máscara de 256 para obter o incremento da sub-rede. Uma máscara `/27` termina em 224, gerando o tamanho de bloco `256 - 224 = 32`. Assim, os limites no último octeto são 0, 32, 64, 96, 128, 160, 192 e 224.

O endereço `198.51.100.77/27` pertence ao bloco de 64 a 95.

:::single-choice{#subnet-cheats-77-network} Qual é o endereço de rede de `198.51.100.77/27`?

::option[`198.51.100.32`]{#subnet-cheats-network-32 explanation="Esse bloco abrange os valores de 32 a 63 no octeto final."}
::option[`198.51.100.77`]{#subnet-cheats-network-77 explanation="O endereço inclui bits de host e não é o limite do bloco."}
::option[`198.51.100.64`]{#subnet-cheats-network-64 .correct explanation="O bloco `/27` iniciado em 64 abrange de 64 a 95."}
:::

## Convertendo um octeto arbitrário

Para converter o decimal 123, selecione os maiores valores restantes sem ultrapassá-lo:

```text
123 = 64 + 32 + 16 + 8 + 2 + 1
    = 01111011
```

Para converter de volta, some apenas os valores posicionais cujos bits são um. Sempre mantenha as oito posições ao trabalhar dentro de um octeto IPv4.

:::single-choice{#subnet-cheats-binary-123} Qual valor de oito bits equivale ao decimal 123?

::option[`1111011`]{#subnet-cheats-123-seven-bit explanation="O valor numérico é semelhante, mas a representação do octeto deve manter oito posições."}
::option[`01111011`]{#subnet-cheats-123-correct .correct explanation="As posições definidas somam 64 + 32 + 16 + 8 + 2 + 1."}
::option[`01111100`]{#subnet-cheats-124 explanation="Esse padrão define a posição 4 em vez de 2 e 1, produzindo 124."}
:::

## Resumo

Agora você pode conferir cálculos comuns de IPv4 com padrões binários compactos.

1. Use os oito valores posicionais do octeto, de 128 a 1.
2. Memorize a sequência das máscaras contíguas de octetos parciais.
3. Obtenha o tamanho do bloco subtraindo a máscara parcial de 256.
4. Mantenha oito bits ao converter octetos individuais.
