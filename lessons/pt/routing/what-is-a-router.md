---
index: 1
lang: "pt"
title: "O que é um roteador?"
meta_title: "O que é um roteador? - Roteamento"
meta_description: "Guia para iniciantes sobre o que é um roteador em redes. Aprenda sobre roteamento, comutação de pacotes, saltos (hops) e como roteadores usam tabelas de roteamento para encaminhar dados entre redes. Este guia de rede é essencial para aprender sobre redes Linux."
meta_keywords: "roteador, redes, roteamento, saltos, comutação de pacotes, redes Linux, tutorial iniciante, guia de rede"
---

## Lesson Content

Um roteador é um dispositivo fundamental em redes de computadores. Você provavelmente tem um em sua casa conectando você à internet. Sua função principal é permitir que máquinas em uma rede se comuniquem entre si e com outras redes. Este processo é uma parte central do que faz a internet e as redes locais funcionarem.

### A Função Central de um Roteador

Um roteador doméstico típico possui portas LAN (Rede Local) para conectar seus dispositivos a uma rede local e uma porta WAN (Rede de Longa Distância) que fornece conexão com a internet. Cada pedaço de dado, ou "pacote", que você envia ou recebe durante qualquer atividade de rede deve passar pelo roteador. O roteador inspeciona esses pacotes de rede e decide para onde eles devem ir. Ele efetivamente roteia o tráfego entre múltiplas redes, garantindo que cada pacote viaje de sua origem até seu destino final.

### O Processo de Roteamento

Pense no processo de roteamento como a entrega de correspondência. Quando você envia uma carta, os correios determinam o destino geral (por exemplo, um estado ou cidade) e a enviam para lá. A partir desse ponto, ela é classificada em regiões menores, como códigos postais, até finalmente chegar ao endereço de rua específico.

Em redes, um roteador usa uma **tabela de roteamento** para tomar essas decisões. Esta tabela contém um conjunto de regras, ou rotas, que dizem ao roteador como encaminhar pacotes para um determinado destino de rede. Por exemplo, uma regra pode dizer: "Para alcançar a Rede A, envie pacotes para o Roteador B." Se não houver uma regra específica para um destino, o roteador usa uma **rota padrão**, que geralmente direciona o tráfego para a internet. Este sistema é crucial tanto em configurações domésticas simples quanto em ambientes complexos de **redes Linux**.

### Saltos (Hops)

À medida que os pacotes viajam através das redes, sua jornada é medida em **saltos** (hops). Um salto representa uma etapa da jornada onde um pacote passa por um dispositivo intermediário, como um roteador. Por exemplo, se um pacote precisa passar por dois roteadores para ir do Host A ao Host B, dizemos que o caminho tem dois saltos de comprimento. Os saltos fornecem uma métrica simples para medir a distância entre uma origem e um destino em uma rede.

### Comutação de Pacotes, Roteamento e Inundação (Flooding)

Para entender como os dados se movem, é útil conhecer estes termos relacionados:

- **Comutação de Pacotes** (Packet Switching) é o método fundamental de receber, processar e encaminhar pacotes de dados para seu destino. É o que os roteadores fazem continuamente.
- **Roteamento** é o processo inteligente de construir e manter a tabela de roteamento. O roteamento eficaz permite uma comutação de pacotes mais eficiente e confiável.
- **Inundação** (Flooding) é um método mais antigo e menos eficiente usado quando um roteador não sabe para onde enviar um pacote. Ele envia o pacote recebido por todas as conexões, exceto aquela pela qual chegou, na esperança de que um alcance o destino. As redes modernas dependem do roteamento para evitar esse tipo de ineficiência.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de conectividade de rede e roteamento:

1. **[Explorar Tipos de Endereço IP e Alcançabilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Pratique testar a pilha TCP/IP local, identificar IPs privados e públicos e verificar a alcançabilidade da rede, que são fundamentais para entender como um roteador facilita a comunicação.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como os comandos `ping` e `arp` ajudam você a observar como as camadas de rede e de enlace de dados interagem, e como o gateway padrão (roteador) lida com o tráfego remoto.
3. **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Use o Docker para simular nós de rede e atribuir endereços IP, em seguida, teste a conectividade para entender como as sub-redes IP e o roteamento governam a comunicação em rede.

Esses laboratórios ajudarão você a aplicar os conceitos de comunicação de rede, endereçamento IP e o papel do roteamento em cenários reais, aumentando sua confiança nos fundamentos de rede.

## Quiz Question

How do packets measure distance? (Please answer in English. The answer is case-sensitive.)

## Quiz Answer

Hops
