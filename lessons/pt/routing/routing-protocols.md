---
index: 4
lang: "pt"
title: "Protocolos de Roteamento"
meta_title: "Protocolos de Roteamento - Roteamento"
meta_description: "Aprenda sobre protocolos de roteamento como vetor de distância e estado de link. Entenda a convergência de rede e como os roteadores se adaptam às mudanças. Comece sua jornada de rede Linux!"
meta_keywords: "protocolos de roteamento, convergência de rede, vetor de distância, estado de link, rede Linux, guia para iniciantes, tutorial de rede"
---

## Lesson Content

Seria um incômodo ter que configurar manualmente as rotas em uma tabela de roteamento para cada dispositivo em sua rede. Em vez disso, usamos o que são conhecidos como protocolos de roteamento. Os protocolos de roteamento ajudam nosso sistema a se adaptar às mudanças na rede; eles aprendem diferentes rotas, as constroem na tabela de roteamento e, em seguida, roteiam nossos pacotes dessa forma. Existem dois tipos principais de protocolo de roteamento: protocolos de vetor de distância e protocolos de estado de link.

### Convergência

Antes de falarmos sobre os protocolos, devemos abordar um termo usado em roteamento conhecido como convergência. Ao usar protocolos de roteamento, os roteadores se comunicam com outros roteadores para coletar e trocar informações sobre a rede. Quando eles concordam sobre como uma rede deve ser, cada tabela de roteamento mapeia a topologia completa da rede, assim "convergindo". Quando algo ocorre na topologia da rede, a convergência será temporariamente quebrada até que todos os roteadores estejam cientes dessa mudança.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de roteamento de rede e endereçamento IP:

1. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Pratique a configuração de endereços IP estáticos e dinâmicos, definindo um gateway padrão e verificando as configurações de rede, que são cruciais para entender como as tabelas de roteamento são construídas e utilizadas.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como os dispositivos interagem na camada de rede, observando o ARP e como o gateway padrão lida com o tráfego remoto, fornecendo insights sobre os mecanismos que os protocolos de roteamento gerenciam.
3. **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Use o Docker para simular nós de rede, atribuir endereços IP e testar a conectividade entre sub-redes, aplicando diretamente conceitos relacionados a mudanças de rede e decisões de roteamento.

Esses laboratórios o ajudarão a aplicar os conceitos de configuração e conectividade de rede em cenários reais, construindo confiança com os elementos fundamentais que os protocolos de roteamento automatizam.

## Quiz Question

Qual é o termo usado quando todas as tabelas de roteamento conhecem a topologia da rede?

## Quiz Answer

Convergence
