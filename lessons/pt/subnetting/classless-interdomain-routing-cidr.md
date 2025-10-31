---
index: 5
lang: "pt"
title: "CIDR"
meta_title: "CIDR - Sub-redes"
meta_description: "Um guia para a notação CIDR. Aprenda sobre o formato CIDR, sub-redes CIDR e como calcular hosts para sua rede, inclusive em um servidor Ubuntu. Domine o endereçamento IP com CIDR."
meta_keywords: "CIDR, sub-rede CIDR, formato CIDR, máscara de sub-rede, endereçamento IP, sub-rede Ubuntu servidor CIDR, sub-rede Ubuntu CIDR, prefixo de rede, rede Linux"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) é um método para alocar endereços IP e rotear pacotes do Protocolo de Internet. Ele oferece uma maneira mais compacta e eficiente de representar uma máscara de sub-rede, substituindo o design de rede classful mais antigo. Entender o CIDR é essencial para a administração de rede moderna.

### O Formato CIDR

Você frequentemente verá redes notadas usando o **formato CIDR**, onde um endereço IP é seguido por uma barra e um número. Por exemplo, uma sub-rede como `10.42.3.0` com uma máscara de sub-rede de `255.255.255.0` é escrita como `10.42.3.0/24`. Esta notação única inclui tanto o endereço de rede quanto o comprimento do prefixo.

O número após a barra indica quantos bits do endereço IP são usados para o prefixo de rede. Esta é uma tarefa comum ao configurar redes em um sistema como um **servidor Ubuntu**, onde você pode definir uma interface com um endereço `ubuntu subnet cidr`.

### Sub-redes CIDR e Cálculo de Hosts

Um endereço IPv4 consiste em 4 bytes, totalizando 32 bits. O prefixo CIDR determina a divisão entre a porção de rede e a porção de host do endereço. Para um **cidr subnetting** eficaz, você precisa saber como calcular o número de hosts disponíveis.

Vamos pegar o exemplo `123.12.24.0/23`. Isso significa que os primeiros 23 bits são o prefixo de rede. Para encontrar o número de hosts disponíveis:

1. Subtraia o prefixo CIDR do número total de bits (32): `32 - 23 = 9`. Isso deixa 9 bits para a porção de host.
2. Calcule o número total de endereços na sub-rede: `2^9 = 512`.
3. Subtraia 2 do total. Um endereço é reservado para a própria rede e um é para o endereço de broadcast. Isso deixa `512 - 2 = 510` endereços de host utilizáveis.

Outro exemplo comum é uma rede `/30`, que fornece `32 - 30 = 2` bits de host. Isso resulta em `2^2 = 4` endereços totais, deixando apenas 2 endereços utilizáveis, tornando-a ideal para links ponto a ponto.

## Exercise

Para dominar esses conceitos, pratique com alguns laboratórios práticos que reforcem sua compreensão de CIDR, endereçamento IP e **cidr subnetting**:

1. **[Realizar Sub-redes IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine a sub-rede IP e a conversão binária, incluindo a tradução de máscaras CIDR e o cálculo de hosts utilizáveis.
2. **[Simular Conectividade de Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aprenda a atribuir endereços IP estáticos e observe como as sub-redes IP governam a comunicação direta de rede em um ambiente simulado.
3. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore o endereçamento IP e a acessibilidade de rede usando comandos como `ping` e `ip a` para testar vários tipos de IP e conectividade.

Esses laboratórios ajudarão você a aplicar os conceitos de CIDR e endereçamento IP em cenários do mundo real e a ganhar confiança na configuração de rede.

## Quiz Question

Quantos bits um endereço IPv4 possui?

## Quiz Answer

32
