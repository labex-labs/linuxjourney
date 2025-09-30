---
index: 6
lang: "pt"
title: "NAT"
meta_title: "NAT - Sub-rede"
meta_description: "Aprenda sobre NAT (Network Address Translation) no Linux, como funciona e seu papel na segurança da rede. Entenda IPs privados vs. públicos. Guia de rede Linux."
meta_keywords: "NAT, Network Address Translation, rede Linux, IP privado, IP público, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Já mencionamos NAT (Network Address Translation) antes, mas não a abordamos. Quando estamos trabalhando em nossa rede, isso significa que a internet pode ver nosso endereço IP? Não exatamente.

NAT faz com que um dispositivo como nosso roteador atue como um intermediário entre a internet e uma rede privada. Assim, apenas um único e exclusivo endereço IP é necessário para representar um grupo inteiro de computadores.

Pense na NAT como uma recepcionista em um grande escritório. Se alguém quiser contatá-lo, eles só sabem o número do escritório inteiro. A recepcionista teria então que procurar seu número de ramal e encaminhar a chamada para você.

### Como funciona?

Um caso simples seria assim:

1. Patty quer se conectar a `www.google.com`, então sua máquina envia essa solicitação através do roteador.
2. O roteador pega essa solicitação e abre sua própria conexão para google.com, então ele envia a solicitação de Patty assim que estabelece uma conexão.
3. O roteador é o intermediário entre Patty e `www.google.com`. O Google não sabe sobre Patty; em vez disso, tudo o que pode ver é o roteador.

NAT e o roteamento de pacotes em geral podem ser bem complicados, mas não vamos nos aprofundar nos detalhes.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre endereçamento de rede e conectividade, que são fundamentais para entender conceitos como NAT:

1. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Pratique o uso do comando `ip a` para identificar informações de endereçamento de rede, incluindo endereços IPv4 e IPv6, em um sistema Linux.
2. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a gerenciar o endereçamento IP configurando IPs estáticos e dinâmicos, e verificando a configuração de rede, o que ajuda a entender como os dispositivos obtêm seus endereços.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de endereço IP (privado, público, multicast) e teste a acessibilidade da rede, fornecendo um contexto prático de como a NAT distingue entre endereços internos e externos.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança na configuração e solução de problemas de rede no Linux.

## Quiz Question

O que é usado para representar um único endereço privado para a internet?

## Quiz Answer

NAT
