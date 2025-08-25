---
index: 9
lang: "pt"
title: "Visão Geral do DHCP"
meta_title: "Visão Geral do DHCP - Fundamentos de Rede"
meta_description: "Aprenda sobre DHCP (Dynamic Host Configuration Protocol) no Linux. Entenda como o DHCP atribui endereços IP e seu processo de quatro etapas. Comece sua jornada de rede Linux!"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, rede Linux, endereço IP, tutorial DHCP, iniciante, guia"
---

## Lesson Content

Um conceito importante de rede que ainda não abordamos é o DHCP (Dynamic Host Configuration Protocol).

O DHCP atribui endereços IP, máscaras de sub-rede e gateways às nossas máquinas. Por exemplo, digamos que você tenha um celular e queira obter um número de celular para começar a falar com as pessoas. Você precisa ligar para sua operadora de telefone, e eles lhe darão um número. Enquanto você pagar suas contas, poderá continuar usando seu telefone. O DHCP é a operadora de telefone neste caso; ele lhe dá um endereço IP para que você possa se comunicar com outros endereços IP. Você também recebe um endereço IP alugado; estes duram por um certo período de tempo, e então serão renovados dependendo de como você configurou suas configurações de aluguel.

O DHCP é ótimo por muitas razões: ele permite que um administrador de rede não se preocupe em atribuir endereços IP, e também os impede de configurar endereços IP duplicados. Toda rede física deve ter seu próprio servidor DHCP para que um host possa solicitar um endereço IP. Em um ambiente doméstico comum, o roteador geralmente atua como o servidor DHCP.

A forma como o DHCP obtém todas as suas informações de host dinâmico é:

1. DHCP DISCOVER - Esta mensagem é transmitida para procurar um servidor DHCP.
2. DHCP OFFER - O servidor DHCP na rede responde com uma mensagem de oferta. A oferta contém um pacote com tempo de aluguel DHCP, máscara de sub-rede, endereço IP, etc.
3. DHCP REQUEST - O cliente envia outra transmissão para informar a todos os servidores DHCP qual oferta ele aceitou.
4. DHCP ACK - O reconhecimento é enviado pelo servidor.

O DHCP é mais complexo do que isso, mas esta é a essência.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do endereçamento IP dinâmico e da configuração de rede:

1. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/linux-manage-ip-addressing-in-linux-592736)** - Pratique o uso do comando `ip` para inspecionar interfaces e, especificamente, use `dhclient` para obter um endereço IP dinâmico, aplicando diretamente seu conhecimento de DHCP.
2. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Aprenda a usar o comando `ip a` para identificar informações de endereçamento de rede, incluindo os endereços IP atribuídos pelo DHCP, e inspecionar interfaces de rede.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore o endereçamento IP e a acessibilidade da rede usando `ping` e `ip a`, ajudando você a entender como os IPs atribuídos dinamicamente funcionam dentro de uma rede.

Esses laboratórios o ajudarão a aplicar os conceitos de atribuição dinâmica de IP e configuração de rede em cenários reais e a construir confiança com a rede Linux.

## Quiz Question

Quais são as etapas em uma solicitação DHCP?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
