---
index: 3
lang: "pt"
title: "Matemática de Sub-rede"
meta_title: "Matemática de Sub-rede - Subnetting"
meta_description: "Aprenda os fundamentos da matemática de sub-redes e como calcular hosts disponíveis em uma rede. Entenda o endereçamento IP e as máscaras de sub-rede para iniciantes. Comece sua jornada no Linux!"
meta_keywords: "matemática de sub-rede, endereço IP, máscara de sub-rede, hosts de rede, binário, rede Linux, tutorial para iniciantes, guia"
---

## Lesson Content

Ok, sabemos que as máscaras de sub-rede são importantes para descobrir quantos hosts podemos ter em nossa sub-rede. Então, quantos hosts seriam?

Digamos que eu tenha um endereço IP de **192.168.1.0** e uma máscara de sub-rede de **255.255.255.0**. Agora, vamos alinhar esses números em formato binário. Por enquanto, use uma calculadora online para converter esses valores de decimal para binário.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

O endereço IP é mascarado pela nossa máscara de sub-rede. Quando você vê um 1, ele está mascarado, e nós fingimos que não o vemos. Então, os únicos hosts possíveis que podemos ter são da região `00000000`. Lembre-se, `11111111` em formato binário é igual a 255. Também consideramos 0 como um número de host, então há 256 opções possíveis. No entanto, pode parecer que temos 256 opções possíveis, mas na verdade subtraímos 2 hosts porque temos que considerar o endereço de broadcast e o endereço da sub-rede, deixando-nos com 254 hosts possíveis em nossa sub-rede. Então, sabemos que podemos ter hosts com endereços IP que variam de 192.168.1.1 a 192.168.1.254.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de endereçamento IP e subnetting:

1. **[Realizar Subnetting IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine o subnetting IP e a conversão binária, habilidades essenciais para configuração e planejamento de rede.
2. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Aprofunde sua compreensão sobre vários tipos de endereço IP e como verificar a acessibilidade da rede usando comandos Linux.
3. **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - Aplique seu conhecimento simulando configurações de rede e testando a conectividade entre diferentes sub-redes IP em um ambiente prático.

Esses laboratórios o ajudarão a aplicar os conceitos de endereçamento IP, máscaras de sub-rede e cálculo de hosts em cenários reais e a construir confiança com os fundamentos de rede.

## Quiz Question

Qual é o equivalente binário de 255?

## Quiz Answer

11111111
