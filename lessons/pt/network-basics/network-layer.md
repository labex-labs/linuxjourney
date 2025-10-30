---
index: 7
lang: "pt"
title: "Camada de Rede"
meta_title: "Camada de Rede - Fundamentos de Rede"
meta_description: "Aprenda sobre a camada de Rede no Linux, como os endereços IP roteiam pacotes através de sub-redes e seu papel na transmissão de dados. Comece sua jornada de rede Linux!"
meta_keywords: "Camada de rede, endereços IP, sub-redes, rede Linux, roteamento de pacotes, iniciante, tutorial, guia"
---

## Lesson Content

A camada de Rede determina o roteamento dos nossos pacotes do nosso host de origem para um host de destino. Felizmente, no nosso exemplo, o nosso pacote está a viajar apenas dentro da mesma rede, mas a Internet é composta por muitas redes. Estas redes mais pequenas que compõem a Internet são conhecidas como sub-redes. Todas as sub-redes ligam-se umas às outras de alguma forma, razão pela qual conseguimos aceder a `https://www.google.com` mesmo que esteja na sua própria rede. Não vou entrar em detalhes, pois temos um curso inteiro dedicado a sub-redes, mas por agora, no que diz respeito à nossa camada de Rede, saiba que os endereços IP definem as regras para viajar para diferentes sub-redes.

Na camada de Rede, ela recebe o segmento vindo da camada de Transporte e encapsula este segmento num pacote IP, depois anexa o endereço IP do host de origem e o endereço IP do host de destino ao cabeçalho do pacote. Assim, neste ponto, o nosso pacote tem informações sobre para onde vai e de onde veio. Agora ele envia o nosso pacote para a camada de hardware físico.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar a sua compreensão da camada de Rede, endereçamento IP e sub-redes:

1. **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Pratique a atribuição de endereços IP estáticos e o teste de conectividade dentro e entre diferentes sub-redes usando contêineres Docker.
2. **[Realizar Sub-redes IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine a sub-rede IP e a conversão binária, incluindo o cálculo de hosts utilizáveis e sub-redes, diretamente no terminal Linux.
3. **[Explorar Tipos de Endereços IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore vários tipos de endereços IP (privado, público, multicast) e teste a acessibilidade da rede usando `ping` e `ip a`.

Estes laboratórios irão ajudá-lo a aplicar os conceitos de endereçamento IP e sub-redes em cenários reais e a construir confiança com os fundamentos da camada de Rede.

## Quiz Question

Como são chamadas as redes menores que compõem a Internet?

## Quiz Answer

subnets
