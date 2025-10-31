---
index: 4
lang: "pt"
title: "Protocolos de Roteamento"
meta_title: "Protocolos de Roteamento - Roteamento"
meta_description: "Explore os fundamentos dos protocolos de roteamento em redes Linux. Este guia abrange protocolos de vetor de distância e estado de enlace, convergência de rede e como os roteadores constroem e mantêm tabelas de roteamento. Um tutorial perfeito para iniciantes."
meta_keywords: "protocolos de roteamento, convergência de rede, vetor de distância, estado de enlace, redes linux, tabela de roteamento, tutorial de rede, guia para iniciantes, comunicação de roteador"
---

## Lesson Content

Configurar rotas manualmente em uma tabela de roteamento para cada dispositivo em uma rede grande seria uma tarefa incrivelmente tediosa. Para automatizar esse processo, usamos **protocolos de roteamento** dinâmicos. Esses protocolos permitem que os roteadores se adaptem automaticamente às mudanças na rede, aprendendo diferentes rotas, construindo-as na tabela de roteamento e encaminhando pacotes de acordo. Existem dois tipos principais de protocolos de roteamento: vetor de distância e estado de enlace.

### Protocolos de Vetor de Distância

Os protocolos de vetor de distância operam sob o princípio de "roteamento por boato". Cada roteador compartilha sua tabela de roteamento inteira com seus vizinhos diretamente conectados em intervalos regulares. Quando um roteador recebe uma tabela de roteamento de um vizinho, ele atualiza a sua própria tabela com quaisquer rotas novas ou melhores. A "distância" é tipicamente medida por uma métrica como contagem de saltos (hop count). Este método é simples, mas pode ser lento para convergir e é suscetível a loops de roteamento. Um exemplo de protocolo de vetor de distância é o Protocolo de Informações de Roteamento (RIP).

### Protocolos de Estado de Enlace

Em contraste, os **protocolos de estado de enlace** fornecem a cada roteador um mapa completo da topologia da rede. Em vez de compartilhar toda a sua tabela de roteamento, os roteadores enviam informações sobre o estado de seus próprios enlaces (por exemplo, vizinhos conectados e o custo da conexão) para todos os outros roteadores na rede. Usando essas informações, cada roteador pode construir independentemente um mapa idêntico da rede e calcular o melhor caminho para cada destino. Essa abordagem leva a uma **convergência de rede** mais rápida e é mais escalável do que os protocolos de vetor de distância. Um exemplo é o protocolo Open Shortest Path First (OSPF).

### Convergência de Rede

Antes de discutirmos os protocolos em mais detalhes, é importante entender um conceito chave em roteamento conhecido como **convergência de rede**. Ao usar protocolos de roteamento, os roteadores se comunicam para coletar e trocar informações. Convergência é o estado em que todos os roteadores têm uma visão consistente e precisa da topologia da rede. Quando cada tabela de roteamento mapeia corretamente toda a rede, a rede é considerada "convergida". Se ocorrer uma mudança, como um enlace cair, a convergência é temporariamente quebrada até que todos os roteadores aprendam sobre a mudança e atualizem suas tabelas de roteamento.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de roteamento de rede e endereçamento IP:

1.  **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Pratique a configuração de endereços IP estáticos e dinâmicos, a definição de um gateway padrão e a verificação de configurações de rede, que são cruciais para entender como as tabelas de roteamento são construídas e utilizadas.
2.  **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como os dispositivos interagem na camada de rede, observando o ARP e como o gateway padrão lida com tráfego remoto, fornecendo insights sobre os mecanismos que os protocolos de roteamento gerenciam.
3.  **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Use o Docker para simular nós de rede, atribuir endereços IP e testar a conectividade entre sub-redes, aplicando diretamente conceitos relacionados a mudanças de rede e decisões de roteamento.

Esses laboratórios ajudarão você a aplicar os conceitos de configuração e conectividade de rede em cenários reais, aumentando a confiança nos elementos fundamentais que os protocolos de roteamento automatizam.

## Quiz Question

What is the term for the state where all routing tables on a network agree on the network topology? (Please answer in English, paying attention to capitalization.)

## Quiz Answer

Convergence
