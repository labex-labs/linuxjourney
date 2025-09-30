---
index: 5
lang: "pt"
title: "Protocolos de Vetor de Distância"
meta_title: "Protocolos de Vetor de Distância - Roteamento"
meta_description: "Aprenda sobre protocolos de vetor de distância como o RIP, como eles funcionam e suas limitações para o roteamento de rede. Entenda a contagem de saltos e a eficiência da rede."
meta_keywords: "protocolos de vetor de distância, RIP, protocolo de informação de roteamento, contagem de saltos, roteamento de rede, rede Linux, guia para iniciantes, tutorial"
---

## Lesson Content

Os protocolos de vetor de distância determinam o caminho para outras redes usando a contagem de saltos que um pacote leva através da rede. Por exemplo, se a rede A está a 3 saltos de distância e a rede B está ao lado da rede A, então assumimos que a rede B deve estar a 4 saltos de distância. Em protocolos de vetor de distância, a próxima rota seria aquela com o menor número de saltos.

Os protocolos de vetor de distância são ótimos para redes pequenas. No entanto, quando as redes começam a escalar, leva mais tempo para os roteadores convergirem porque eles enviam periodicamente a tabela de roteamento inteira para cada roteador. Outra desvantagem dos protocolos de vetor de distância é a eficiência; eles escolhem rotas que estão mais próximas em saltos, mas isso pode nem sempre ser a rota mais eficiente.

Um dos protocolos de vetor de distância comuns é o RIP (Routing Information Protocol). Ele transmite a tabela de roteamento para cada roteador na rede a cada 30 segundos. Para uma rede grande, isso pode consumir recursos significativos. Por causa disso, o RIP limita sua contagem de saltos a 15.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre roteamento e conectividade de rede:

1. **[Explore a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Pratique o uso de `ping` e `arp` para entender como os dispositivos se descobrem e como o tráfego é roteado na camada de rede.
2. **[Simule a Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a atribuir endereços IP e testar a conectividade entre nós Linux simulados, observando como as sub-redes IP influenciam a comunicação de rede.
3. **[Gerencie o Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Ganhe experiência prática configurando endereços IP estáticos e dinâmicos e definindo gateways padrão, que são componentes essenciais do roteamento de rede.

Esses laboratórios o ajudarão a aplicar os conceitos de endereçamento e conectividade de rede em cenários reais, construindo uma base sólida para entender como os protocolos de roteamento funcionam.

## Quiz Question

Verdadeiro ou falso: Os protocolos de vetor de distância usam a rota com a menor largura de banda?

## Quiz Answer

False
