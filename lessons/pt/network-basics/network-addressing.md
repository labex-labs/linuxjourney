---
index: 4
lang: "pt"
title: "Endereçamento de Rede"
meta_title: "Endereçamento de Rede - Fundamentos de Rede"
meta_description: "Descubra os fundamentos do endereçamento de rede. Este guia explica endereços MAC, endereços IP e nomes de host, conceitos chave para entender como os dispositivos se comunicam em redes Linux."
meta_keywords: "endereçamento de rede, endereço MAC, endereço IP, nome de host, identificadores de rede, redes Linux, fundamentos de rede, iniciante, tutorial, guia"
---

## Lesson Content

Antes de explorarmos como os pacotes de dados viajam por uma rede, é essencial entender alguma terminologia central. Assim como uma carta física precisa de um endereço de destino e de retorno, os pacotes de rede exigem informações semelhantes para alcançar seu alvo. Em redes de computadores, os dispositivos são identificados usando endereços MAC (Controle de Acesso ao Meio) e endereços IP. Para simplificar as coisas para os humanos, também usamos nomes de host.

### Endereços MAC

Um endereço MAC é um identificador de hardware exclusivo e permanente atribuído a uma placa de interface de rede (NIC). Este endereço é gravado no dispositivo durante a fabricação e não muda. Todo dispositivo que se conecta a uma rede, como seu computador ou smartphone, possui uma NIC com um endereço MAC distinto. Este endereço de hardware é crucial para a comunicação em um segmento de rede local. Um endereço MAC Ethernet geralmente se parece com isto: `00:C4:B5:45:B2:43`. Os primeiros três bytes do endereço formam o Identificador Único Organizacional (OUI), que identifica o fabricante. Por exemplo, a Dell usa o OUI `00-14-22`, então uma NIC Dell pode ter um endereço MAC como `00-14-22-34-B2-C2`.

### Endereços IP

Um endereço IP é um identificador lógico para um dispositivo em uma rede, tornando-o alcançável em diferentes redes, incluindo a internet. Ao contrário de um endereço MAC, um endereço IP não está vinculado ao hardware e pode ser atribuído dinamicamente. Vamos nos concentrar no IPv4 por enquanto, onde um endereço se parece com `10.24.12.4`. Os endereços IP são fundamentais para o lado do software da rede, possibilitando roteamento e comunicação global. Embora os endereços IP públicos sejam exclusivos em toda a internet, eles podem mudar, e tecnologias como a Tradução de Endereços de Rede (NAT) permitem endereços privados e não exclusivos dentro de uma rede local. É importante lembrar que tanto os endereços MAC (hardware) quanto os IP (software) são necessários para uma comunicação de rede bem-sucedida.

### Nomes de Host

Embora os endereços IP sejam eficazes para computadores, eles são difíceis de memorizar para os humanos. Os nomes de host resolvem esse problema mapeando um nome amigável ao usuário para um endereço IP. Por exemplo, é muito mais fácil lembrar `meuhost.com` do que seu endereço IP correspondente, como `192.12.41.4`. Esse mapeamento é tratado pelo Sistema de Nomes de Domínio (DNS), que atua como a lista telefônica da internet, traduzindo nomes de host memoráveis para os endereços IP numéricos necessários para o roteamento de rede.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de identificadores de rede como endereços MAC, endereços IP e nomes de host:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços MAC e IP, em um sistema Linux.
2. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de endereços IP e teste a acessibilidade da rede usando `ping` e `ip a`.
3. **[Gerenciar a Resolução de Nome de Host Local no Linux](https://labex.io/pt/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Aprenda a gerenciar a resolução de nome de host local editando o arquivo `/etc/hosts` e testando suas alterações.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança com os fundamentos de rede do Linux.

## Quiz Question

Quantos bytes há em um endereço IPv4?

## Quiz Answer

4
