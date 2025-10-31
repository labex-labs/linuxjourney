---
index: 7
lang: "pt"
title: "Camada de Rede"
meta_title: "Camada de Rede - Fundamentos de Rede"
meta_description: "Explore a Camada de Rede em redes Linux. Este guia explica como endereços IP e sub-redes permitem o roteamento de pacotes para transmissão de dados entre redes."
meta_keywords: "Camada de rede, endereços IP, sub-redes, redes Linux, roteamento de pacotes, transmissão de dados, modelo OSI, pacote IP"
---

## Lesson Content

A Camada de Rede é responsável pelo endereçamento lógico e roteamento de pacotes de dados de um host de origem para um host de destino. Embora um pacote possa, às vezes, viajar dentro de uma única rede local, a internet é uma vasta coleção de redes interconectadas.

### O Papel do Roteamento de Pacotes

A função principal da Camada de Rede é determinar o caminho ideal para os dados viajarem. Este processo, conhecido como **roteamento de pacotes**, garante que a informação chegue ao seu destino pretendido de forma eficiente, mesmo que precise atravessar múltiplas fronteiras de rede. Em **redes Linux**, esta camada é fundamental para toda a comunicação pela internet.

### Entendendo Sub-redes e Endereços IP

As redes menores que constituem a internet são chamadas de **sub-redes** (subnets). Todas as sub-redes estão conectadas, o que permite que um dispositivo em uma rede se comunique com um dispositivo em outra, como acessar um site como `google.com`. As regras para viajar entre essas diferentes sub-redes são definidas pelos **endereços IP**. Um endereço IP fornece um identificador exclusivo para um dispositivo em uma rede, muito parecido com um endereço de rua para uma casa.

### Encapsulamento na Camada de Rede

Na Camada de Rede, o segmento de dados recebido da Camada de Transporte é encapsulado em uma nova unidade chamada pacote IP. Durante este processo, um cabeçalho é adicionado ao pacote, que inclui o endereço IP de origem (de onde o pacote veio) e o endereço IP de destino (para onde ele está indo). Com esta informação de endereçamento crucial anexada, o pacote agora tem tudo o que precisa para sua jornada e é passado para a Camada de Enlace de Dados para ser preparado para a transmissão física.

## Exercise

Prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da Camada de Rede, endereçamento IP e sub-redes:

1. **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Pratique a atribuição de endereços IP estáticos e teste a conectividade dentro e entre diferentes sub-redes usando contêineres Docker.
2. **[Realizar Sub-redes IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine a sub-rede IP e a conversão binária, incluindo o cálculo de hosts e sub-redes utilizáveis, diretamente no terminal Linux.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore vários tipos de endereços IP (privado, público, multicast) e teste a acessibilidade da rede usando `ping` e `ip a`.

Estes laboratórios ajudarão você a aplicar os conceitos de endereçamento IP e sub-redes em cenários reais e a construir confiança com os fundamentos da Camada de Rede.

## Quiz Question

Como são chamadas as redes menores que compõem a Internet? Por favor, responda usando uma única palavra em inglês em minúsculas.

## Quiz Answer

subnets
