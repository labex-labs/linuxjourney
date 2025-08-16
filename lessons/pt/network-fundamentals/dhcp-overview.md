---
lang: "pt"
title: "Visão Geral do DHCP"
description: "Aprenda sobre DHCP (Dynamic Host Configuration Protocol) no Linux. Entenda como o DHCP atribui endereços IP e seu processo de quatro etapas. Comece sua jornada de rede Linux!"
keywords: "DHCP, Dynamic Host Configuration Protocol, rede Linux, endereço IP, tutorial DHCP, iniciante, guia"
---

## Lesson Content

Um conceito de rede importante que ainda não abordamos é o DHCP (Dynamic Host Configuration Protocol).

O DHCP atribui endereços IP, máscaras de sub-rede e gateways às nossas máquinas. Por exemplo, digamos que você tenha um telefone celular e queira obter um número de telefone celular para começar a falar com as pessoas. Você precisa ligar para sua operadora de telefone, e eles lhe darão um número. Enquanto você pagar suas contas, poderá continuar usando seu telefone. O DHCP é a operadora de telefone neste caso; ele lhe dá um endereço IP para que você possa se comunicar com outros endereços IP. Você também recebe um endereço IP alugado; estes duram por um certo período de tempo, e depois serão renovados dependendo de como você configurou suas configurações de aluguel.

O DHCP é ótimo por muitas razões: ele permite que um administrador de rede não se preocupe em atribuir endereços IP, e também os impede de configurar endereços IP duplicados. Cada rede física deve ter seu próprio servidor DHCP para que um host possa solicitar um endereço IP. Em um ambiente doméstico comum, o roteador geralmente atua como o servidor DHCP.

A forma como o DHCP obtém todas as suas informações de host dinâmico é:

1. DHCP DISCOVER - Esta mensagem é transmitida para procurar um servidor DHCP.
2. DHCP OFFER - O servidor DHCP na rede responde com uma mensagem de oferta. A oferta contém um pacote com tempo de concessão DHCP, máscara de sub-rede, endereço IP, etc.
3. DHCP REQUEST - O cliente envia outra transmissão para informar a todos os servidores DHCP qual oferta ele aceitou.
4. DHCP ACK - O reconhecimento é enviado pelo servidor.

O DHCP é mais complexo do que isso, mas esta é a essência.

## Exercise

No exercises for this lesson.

## Quiz Question

Quais são as etapas em uma solicitação DHCP?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
