---
index: 5
lang: "pt"
title: "CIDR"
meta_title: "CIDR - Sub-redes"
meta_description: "Aprenda a notação CIDR para redes Linux. Entenda máscaras de sub-rede, endereçamento IP e cálculo de hosts com este guia para iniciantes. Melhore suas habilidades de rede!"
meta_keywords: "CIDR, máscara de sub-rede, endereçamento IP, prefixo de rede, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) é usado para representar uma máscara de sub-rede de uma forma mais compacta. Você pode ver sub-redes anotadas na notação CIDR, onde uma sub-rede como 10.42.3.0/255.255.255.0 é escrita como 10.42.3.0/24. Esta notação inclui tanto o prefixo da sub-rede quanto a máscara da sub-rede.

Lembre-se, um endereço IP consiste em 4 bytes ou 32 bits. O CIDR indica o número de bits usados como prefixo de rede. Assim, 123.12.24.0/23 significa que os primeiros 23 bits são usados. O que isso significa? Quantos hosts são?

Um truque simples é subtrair o endereço CIDR (23) do número total de bits que um endereço IP pode ter (32). Isso deixa 9 bits. Portanto, 2^9 = 512. No entanto, devemos remover 2 endereços (o endereço da sub-rede e o endereço de broadcast), então temos 510 hosts utilizáveis.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de CIDR, endereçamento IP e sub-redes:

1. **[Realizar Sub-redes IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine a sub-rede IP e a conversão binária, incluindo a tradução de máscaras CIDR e o cálculo de hosts utilizáveis.
2. **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a atribuir endereços IP estáticos e observe como as sub-redes IP governam a comunicação direta de rede em um ambiente simulado.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore o endereçamento IP e a acessibilidade da rede usando comandos como `ping` e `ip a` para testar vários tipos de IP e conectividade.

Esses laboratórios o ajudarão a aplicar os conceitos de CIDR e endereçamento IP em cenários reais e a construir confiança com a configuração de rede.

## Quiz Question

Sem perguntas, siga em frente!

## Quiz Answer
