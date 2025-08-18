---
lang: "pt"
title: "Protocolos de Vetor de Distância"
meta_title: "Protocolos de Vetor de Distância - Roteamento"
meta_description: "Aprenda sobre protocolos de vetor de distância como o RIP, como eles funcionam e suas limitações para o roteamento de rede. Entenda a contagem de saltos e a eficiência da rede."
meta_keywords: "protocolos de vetor de distância, RIP, protocolo de informação de roteamento, contagem de saltos, roteamento de rede, rede Linux, guia para iniciantes, tutorial"
---

## Lesson Content

Os protocolos de vetor de distância determinam o caminho para outras redes usando a contagem de saltos que um pacote leva através da rede. Por exemplo, se a rede A está a 3 saltos de distância e a rede B está ao lado da rede A, então assumimos que a rede B deve estar a 4 saltos de distância. Em protocolos de vetor de distância, a próxima rota seria aquela com o menor número de saltos.

Os protocolos de vetor de distância são ótimos para redes pequenas. No entanto, quando as redes começam a escalar, leva mais tempo para os roteadores convergirem porque eles enviam periodicamente a tabela de roteamento inteira para cada roteador. Outra desvantagem dos protocolos de vetor de distância é a eficiência; eles escolhem rotas que estão mais próximas em saltos, mas isso nem sempre pode ser a rota mais eficiente.

Um dos protocolos de vetor de distância comuns é o RIP (Routing Information Protocol). Ele transmite a tabela de roteamento para cada roteador na rede a cada 30 segundos. Para uma rede grande, isso pode consumir recursos significativos. Por causa disso, o RIP limita sua contagem de saltos a 15.

## Exercise

No exercises for this lesson.

## Quiz Question

Verdadeiro ou falso: Os protocolos de vetor de distância usam a rota com a menor quantidade de largura de banda?

## Quiz Answer

False
