---
lesson_id: "subnet-math"
course_id: "subnetting"
lang: "pt"
order_index: 3
title: "Cálculos de sub-redes"
description: "Aprenda a calcular rede, broadcast, intervalo e quantidade de endereços IPv4 a partir de um prefixo."
meta_title: "Cálculos de sub-redes - Sub-redes"
meta_description: "Domine os fundamentos dos cálculos de sub-redes. Este guia explica como calcular máscaras de sub-rede e a quantidade de hosts disponíveis em sua rede. Aprenda conceitos essenciais de endereçamento IP e binário para redes Linux."
meta_keywords: "cálculos de sub-redes, cálculo de máscara de sub-rede, endereço IP, máscara de sub-rede, hosts de rede, binário, redes Linux, cálculo de hosts, tutorial para iniciantes"
---

Os cálculos de sub-redes aplicam um comprimento de prefixo aos 32 bits de um endereço IPv4. O raciocínio binário evita erros em limites de prefixo que não coincidem com octetos decimais.

## Encontrando o endereço de rede

Use o endereço `192.168.1.165/24`:

```text
address  11000000.10101000.00000001.10100101
mask     11111111.11111111.11111111.00000000
network  11000000.10101000.00000001.00000000
```

Uma operação AND bit a bit mantém os bits do endereço onde a máscara é um e zera os bits do host. O resultado é `192.168.1.0/24`.

:::single-choice{#subnet-math-network-operation} Qual operação encontra um endereço de rede IPv4 a partir de um endereço e uma máscara?

::option[Concatenação de strings decimais.]{#subnet-math-concatenation explanation="Juntar os octetos impressos não aplica os bits do prefixo."}
::option[Subtração de portas de transporte.]{#subnet-math-port-subtraction explanation="As portas não têm relação com o prefixo de rede."}
::option[AND bit a bit.]{#subnet-math-bitwise-and .correct explanation="Os bits da rede permanecem, enquanto as posições de host mascaradas por zeros são zeradas."}
:::

## Contando endereços

Para o prefixo `/p`, a parte do host contém `32 - p` bits. A quantidade total de endereços é:

```text
2^(32 - p)
```

Portanto, um `/24` contém `2^8 = 256` endereços. Em uma sub-rede de broadcast tradicional, o valor de host formado apenas por zeros é o endereço de rede, e o valor formado apenas por uns é o broadcast direcionado, restando 254 endereços de host unicast comuns.

:::single-choice{#subnet-math-24-total} Quantos endereços totais existem em um `/24` IPv4?

::option[24]{#subnet-math-total-24 explanation="O comprimento do prefixo conta bits de rede, não endereços."}
::option[256]{#subnet-math-total-256 .correct explanation="Oito bits de host produzem 2^8 valores distintos de endereço."}
::option[254]{#subnet-math-total-254 explanation="Essa é a quantidade tradicional de hosts utilizáveis depois de dois endereços especiais, não o total."}
:::

## Encontrando o limite de um bloco

Para `/26`, a máscara é `255.255.255.192`. O tamanho do bloco no último octeto é `256 - 192 = 64`, portanto os limites das sub-redes são 0, 64, 128 e 192. O endereço `192.168.1.165/26` pertence a:

```text
network:   192.168.1.128
broadcast: 192.168.1.191
range:     192.168.1.129 through 192.168.1.190
```

:::single-choice{#subnet-math-165-network} Qual é o endereço de rede de `192.168.1.165/26`?

::option[`192.168.1.0`]{#subnet-math-network-zero explanation="Esse é o primeiro bloco `/26`, que abrange de 0 a 63."}
::option[`192.168.1.165`]{#subnet-math-network-self explanation="O endereço fornecido possui bits de host diferentes de zero dentro do `/26`."}
::option[`192.168.1.128`]{#subnet-math-network-128 .correct explanation="O valor 165 pertence ao bloco de 128 a 191."}
:::

## Considerando exceções de prefixos

O atalho `2^host_bits - 2` não é universal. Prefixos IPv4 `/31` são definidos para enlaces ponto a ponto nos quais ambos os endereços podem ser pontos de extremidade e nenhum broadcast direcionado é necessário. Um `/32` identifica uma rota de host ou um endereço de interface. A tecnologia de rede e o uso do protocolo determinam quais endereços podem ser atribuídos.

:::single-choice{#subnet-math-31-exception} Por que você não deve subtrair dois endereços de todo prefixo IPv4?

::option[Endereços IPv4 não contêm bits de host em nenhum prefixo.]{#subnet-math-no-host-bits explanation="A maioria dos prefixos deixa um ou mais bits de host."}
::option[Enlaces ponto a ponto `/31` podem usar os dois endereços como pontos de extremidade.]{#subnet-math-31-both .correct explanation="O modelo ponto a ponto não precisa das reservas tradicionais de endereço de rede e broadcast direcionado."}
::option[Todas as redes IPv4 usam multicast em vez de unicast.]{#subnet-math-all-multicast explanation="O endereçamento unicast comum continua sendo fundamental."}
:::

## Verificando os cálculos

Use uma ferramenta ou biblioteca independente para conferir o trabalho manual e depois compare com a configuração real das interfaces e rotas. Um prefixo matematicamente válido ainda pode entrar em conflito com outra sub-rede ou violar um plano de alocação.

:::single-choice{#subnet-math-valid-not-safe} O que um cálculo correto de sub-rede não consegue comprovar?

::option[Que o plano de endereços não possui sobreposição nem conflito de políticas.]{#subnet-math-no-conflict .correct explanation="Ainda são necessárias evidências operacionais da alocação e do roteamento."}
::option[Que endereços IPv4 contêm 32 bits.]{#subnet-math-proves-size explanation="O cálculo se baseia nesse tamanho fixo."}
::option[Que potências de dois determinam a quantidade de blocos.]{#subnet-math-powers explanation="As combinações de endereços binários usam inerentemente potências de dois."}
:::

## Resumo

Agora você pode calcular os limites de sub-redes IPv4 e reconhecer exceções comuns.

1. Encontre um endereço de rede com AND bit a bit.
2. Conte o total de endereços a partir da quantidade de bits de host.
3. Use tamanhos de bloco para localizar os limites de rede e broadcast.
4. Trate `/31` e `/32` de acordo com o uso pretendido.
5. Verifique os resultados matemáticos em relação ao plano de endereços real.
