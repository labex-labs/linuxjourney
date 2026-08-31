---
lesson_id: "classless-interdomain-routing-cidr"
course_id: "subnetting"
lang: "pt"
order_index: 5
title: "CIDR"
description: "Aprenda como prefixos CIDR representam intervalos de endereços, limites de sub-redes e rotas agregadas."
meta_title: "CIDR - Sub-redes"
meta_description: "Um guia para a notação CIDR. Aprenda sobre o formato CIDR, a divisão em sub-redes com CIDR e como calcular hosts para sua rede, inclusive em um servidor Ubuntu. Domine o endereçamento IP com CIDR."
meta_keywords: "CIDR, sub-redes CIDR, formato CIDR, máscara de sub-rede, endereçamento IP, cidr de sub-rede em servidor ubuntu, cidr de sub-rede ubuntu, prefixo de rede, redes Linux"
---

O Roteamento Entre Domínios sem Classes representa um intervalo de endereços com um comprimento de prefixo, em vez de depender das classes de endereços históricas. O CIDR permite alocações de tamanho variável, divisão em sub-redes e agregação de rotas para IPv4 e IPv6.

## Lendo a notação de prefixo

Em `10.42.3.17/24`, os primeiros 24 bits são o prefixo de rede, e restam oito bits para posições dentro do intervalo. A rede canônica é `10.42.3.0/24`; o endereço do host fornecido ainda pode ser escrito com o prefixo ao configurar uma interface.

:::single-choice{#cidr-prefix-meaning}
O que `/24` especifica em um valor CIDR IPv4?

::option[Vinte e quatro bits iniciais do prefixo de rede.]{#cidr-24-prefix-bits .correct explanation="Os oito bits restantes dos 32 bits do IPv4 variam dentro do prefixo."}
::option[Vinte e quatro endereços utilizáveis em cada sub-rede.]{#cidr-24-addresses explanation="Um `/24` contém 256 valores totais de endereço."}
::option[A porta TCP de destino da rede.]{#cidr-24-port explanation="CIDR e portas de transporte são independentes."}
:::

## Calculando o tamanho do intervalo

O prefixo IPv4 `/23` deixa nove bits de host e, portanto, abrange `2^9 = 512` endereços no total. O prefixo alinhado `123.12.24.0/23` abrange:

```text
first: 123.12.24.0
last:  123.12.25.255
```

No uso tradicional de broadcast, o primeiro é o endereço de rede, e o último, o broadcast direcionado. Não aplique indiscriminadamente o atalho de “menos dois” hosts utilizáveis a enlaces ponto a ponto `/31` ou rotas de host `/32`.

:::single-choice{#cidr-23-total}
Quantos endereços IPv4 totais um `/23` contém?

::option[512]{#cidr-total-512 .correct explanation="Nove bits variáveis criam 2^9 combinações."}
::option[23]{#cidr-total-23 explanation="O número do prefixo conta bits fixos, não endereços."}
::option[510]{#cidr-total-510 explanation="Essa é uma quantidade utilizável tradicional após os pontos de extremidade especiais, não o tamanho total do intervalo."}
:::

## Verificando o alinhamento

Um prefixo deve começar em seu limite binário. Um `/23` avança em blocos de dois no terceiro octeto quando os octetos anteriores são fixos; portanto, `123.12.24.0/23` está alinhado, mas `123.12.25.0/23` é canonizado para o mesmo intervalo `123.12.24.0/23`.

:::single-choice{#cidr-canonical-25}
Qual é a rede `/23` canônica que contém `123.12.25.0`?

::option[Apenas `123.12.25.0/23`, começando em 25.]{#cidr-25-unaligned explanation="O último bit do prefixo agrupa os valores do terceiro octeto em pares alinhados."}
::option[`123.12.0.0/23`]{#cidr-third-zero explanation="Isso descreve um intervalo `/23` diferente."}
::option[`123.12.24.0/23`]{#cidr-24-canonical .correct explanation="Os valores 24 e 25 do terceiro octeto compartilham o mesmo prefixo alinhado de 23 bits."}
:::

## Agregando rotas

O CIDR pode anunciar um agregado para vários prefixos contíguos, de mesmo tamanho e corretamente alinhados. Por exemplo, `192.0.2.0/25` e `192.0.2.128/25` se combinam em `192.0.2.0/24`. A agregação só é segura quando o roteador anunciante consegue alcançar corretamente todo o agregado ou possui uma política para evitar loops e buracos negros.

:::single-choice{#cidr-aggregate-two-25s}
Qual agregado abrange as duas metades de `192.0.2.0/24`?

::option[`192.0.2.0/26`]{#cidr-aggregate-26 explanation="Um `/26` abrange apenas 64 endereços, menos do que cada metade."}
::option[`192.0.3.0/25`]{#cidr-aggregate-other explanation="Isso está fora do intervalo de endereços indicado."}
::option[`192.0.2.0/24`]{#cidr-aggregate-24 .correct explanation="Os dois intervalos `/25` contíguos e alinhados diferem apenas no bit seguinte e compartilham o prefixo `/24`."}
:::

## Roteamento por prefixo mais longo

Quando as rotas se sobrepõem, o encaminhamento normalmente seleciona a rota elegível com o prefixo correspondente mais longo. Uma rota `/24` é mais específica do que uma `/16` que a abrange, enquanto uma rota padrão `/0` só vence quando nenhuma rota elegível mais específica é escolhida.

:::single-choice{#cidr-route-specificity}
Para o destino `10.42.3.8`, qual rota elegível é mais específica?

::option[`10.42.3.0/24`]{#cidr-route-24 .correct explanation="A correspondência de 24 bits é mais longa e, portanto, mais específica do que `/8`."}
::option[`10.0.0.0/8`]{#cidr-route-8 explanation="Ela corresponde, mas fixa menos bits do destino."}
::option[`0.0.0.0/0`]{#cidr-default explanation="A rota padrão é o prefixo IPv4 menos específico possível."}
:::

## Resumo

Agora você pode usar a notação CIDR tanto para intervalos de endereços quanto para seleção de rotas.

1. Interprete o valor após a barra como uma contagem de bits iniciais do prefixo.
2. Calcule o tamanho total do intervalo a partir dos bits restantes.
3. Canonize um prefixo para seu limite de rede alinhado.
4. Agregue apenas intervalos contíguos e alinhados com acessibilidade válida.
5. Prefira o prefixo elegível mais longo durante a consulta de rotas.
