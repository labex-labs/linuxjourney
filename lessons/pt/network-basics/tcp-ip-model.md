---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "pt"
order_index: 3
title: "Modelo TCP/IP"
description: "Aprenda como as camadas de aplicação, transporte, Internet e enlace cooperam no modelo TCP/IP."
meta_title: "Modelo TCP/IP - Fundamentos de rede"
meta_description: "Explore as camadas fundamentais do modelo TCP/IP, a base das redes modernas. Aprenda sobre as camadas de Aplicação, Transporte, Rede e Enlace para trabalhar de forma eficaz com redes TCP/IP."
meta_keywords: "modelo TCP/IP, camadas do modelo tcp ip, redes com tcp ip, camadas do protocolo tcp, camadas de rede, TCP, IP, redes Linux, projeto de protocolo do mundo real"
---

O modelo TCP/IP organiza os protocolos usados pelos hosts da Internet em camadas funcionais. Uma forma comum de quatro camadas usa Aplicação, Transporte, Internet e Enlace. Alguns modelos didáticos separam o meio físico da camada de enlace e, por isso, apresentam cinco camadas.

## Camada de aplicação

Os protocolos de aplicação definem mensagens e comportamentos para serviços como HTTP, DNS, SSH e SMTP. Essa camada também inclui muitas responsabilidades de representação e sessão que o modelo OSI apresenta separadamente.

:::single-choice{#tcpip-http-layer} Em qual camada TCP/IP o HTTP normalmente é classificado?

::option[Internet.]{#tcpip-http-internet explanation="A camada de Internet cuida do endereçamento IP e do encaminhamento de pacotes."}
::option[Enlace.]{#tcpip-http-link explanation="A camada de enlace transporta o tráfego em um meio local."}
::option[Aplicação.]{#tcpip-http-application .correct explanation="O HTTP define a semântica de solicitações e respostas da aplicação."}
:::

## Camada de transporte

Os protocolos de transporte fornecem comunicação entre pontos de extremidade das aplicações. O TCP oferece um fluxo de bytes confiável e ordenado, com controle de congestionamento e de fluxo. O UDP fornece datagramas independentes, sem as garantias de conexão, ordenação ou retransmissão do TCP. Os números de porta ajudam a identificar pontos de extremidade do transporte, mas um número de porta por si só não comprova qual aplicação está escutando.

:::single-choice{#tcpip-udp-property} Qual propriedade pertence ao UDP, e não ao TCP?

::option[Datagramas independentes sem garantias integradas de retransmissão.]{#tcpip-udp-datagrams .correct explanation="As aplicações que usam UDP decidem se e como adicionar confiabilidade."}
::option[Entrega garantida e em ordem de um único fluxo de bytes.]{#tcpip-udp-ordered explanation="Essa é uma propriedade do serviço TCP, sujeita ao sucesso da conexão."}
::option[Roteamento de pacotes entre redes IP diferentes.]{#tcpip-udp-routing explanation="O roteamento entre redes é uma função da camada de Internet."}
:::

## Camada de Internet

O Protocolo de Internet transporta pacotes usando endereços IP de origem e destino. Os roteadores examinam as informações de roteamento e reduzem os limites de saltos enquanto encaminham os pacotes em direção ao destino. O ICMP comunica informações de controle e erro para a operação do IP. A entrega continua sendo de melhor esforço; as camadas superiores ou as aplicações cuidam de qualquer recuperação necessária.

:::single-choice{#tcpip-router-layer} Qual camada fornece o destino IP usado pelos roteadores?

::option[Internet.]{#tcpip-router-internet .correct explanation="O cabeçalho IP contém o destino da camada de rede usado no encaminhamento roteado."}
::option[Aplicação.]{#tcpip-router-application explanation="As mensagens da aplicação são transportadas dentro dos dados de protocolo das camadas inferiores."}
::option[Enlace.]{#tcpip-router-link explanation="Os endereços de enlace selecionam o destino do quadro no próximo salto local."}
:::

## Camada de enlace e encapsulamento

A camada de enlace envia um pacote IP através de um enlace local usando Ethernet, Wi-Fi, um protocolo ponto a ponto ou outra tecnologia. À medida que os dados da aplicação descem, cada camada acrescenta as informações necessárias ao seu escopo. No receptor, as camadas validam e removem seu próprio encapsulamento antes de entregar os dados para cima.

Os cabeçalhos de enlace normalmente mudam em cada salto roteado; as conversas de transporte e aplicação são de ponta a ponta, a menos que um dispositivo intermediário as encerre ou transforme.

:::single-choice{#tcpip-link-scope} Qual é o escopo normal de um quadro da camada de enlace?

::option[Um enlace ou salto local.]{#tcpip-one-link .correct explanation="Um roteador remove o enquadramento recebido e cria outro para o próximo enlace."}
::option[Todas as sessões de aplicação na Internet global.]{#tcpip-global-frame explanation="Os quadros não permanecem inalterados através de redes roteadas."}
::option[Apenas a memória do processo de origem.]{#tcpip-process-memory explanation="Os quadros são transmitidos por um enlace de rede."}
:::

## Resumo

Agora você pode posicionar funções comuns da Internet no modelo TCP/IP.

1. Associe os protocolos de serviço à camada de aplicação.
2. Diferencie fluxos TCP de datagramas UDP.
3. Posicione o endereçamento IP e o roteamento na camada de Internet.
4. Trate o enquadramento de enlace como um encapsulamento do salto local.
