---
index: 3
lang: "pt"
title: "Matemática de Sub-redes"
meta_title: "Matemática de Sub-redes - Subnetting"
meta_description: "Domine os fundamentos da matemática de sub-redes. Este guia explica como realizar cálculos de máscara de sub-rede para determinar o número de hosts disponíveis em sua rede. Aprenda conceitos essenciais de endereçamento IP e binário para redes Linux."
meta_keywords: "matemática de sub-rede, cálculo de máscara de sub-rede, endereço IP, máscara de sub-rede, hosts de rede, binário, redes Linux, cálculo de host, tutorial para iniciantes"
---

## Lesson Content

Para determinar o número de hosts que uma sub-rede pode suportar, você precisa entender um pouco de **matemática básica de sub-redes**. A máscara de sub-rede é a chave para este cálculo.

### O Papel da Máscara de Sub-rede

Vamos usar um endereço IP de **192.168.1.0** com uma máscara de sub-rede de **255.255.255.0**. A função principal da máscara de sub-rede é distinguir a porção de rede do endereço da porção de host.

Para ver como isso funciona, podemos converter esses valores para sua forma binária.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

### Realizando a Matemática da Máscara de Sub-rede

Na representação binária acima, os `1`s na máscara de sub-rede correspondem à porção de rede do endereço IP. Esta parte é "mascarada" ou fixa. Os `0`s na máscara de sub-rede correspondem à porção de host, que representa o intervalo de endereços que você pode atribuir aos dispositivos.

Em nosso exemplo, a porção de host é `00000000`. Este é um campo de 8 bits, e com 8 bits, você pode criar 2^8, ou 256, combinações únicas (de 0 a 255).

### Calculando Hosts Disponíveis

Embora existam 256 combinações possíveis, nem todas podem ser atribuídas a hosts. Em qualquer sub-rede, dois endereços são reservados:

1.  **Endereço de Rede:** O primeiro endereço, onde todos os bits de host são `0` (ex: 192.168.1.0).
2.  **Endereço de Broadcast:** O último endereço, onde todos os bits de host são `1` (ex: 192.168.1.255).

Portanto, o número real de hosts utilizáveis é 256 - 2 = 254. Isso significa que para a rede `192.168.1.0` com uma máscara `255.255.255.0`, você pode atribuir endereços IP de `192.168.1.1` a `192.168.1.254`. Este cálculo central é uma parte fundamental da **matemática de sub-redes**.

## Exercise

Praticar leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de endereçamento IP e subnetting:

1.  **[Realizar Subnetting IP e Conversão Binária no Terminal Linux](https://labex.io/pt/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domine o subnetting IP e a conversão binária, habilidades essenciais para configuração e planejamento de rede.
2.  **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Aprofunde sua compreensão de vários tipos de endereços IP e como verificar a acessibilidade da rede usando comandos Linux.
3.  **[Simular Conectividade da Camada de Rede no Linux](https://labex.io/pt/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Aplique seu conhecimento simulando configurações de rede e testando a conectividade entre diferentes sub-redes IP em um ambiente prático.

Estes laboratórios ajudarão você a aplicar os conceitos de endereçamento IP, máscaras de sub-rede e cálculo de hosts em cenários do mundo real e a construir confiança nos fundamentos de rede.

## Quiz Question

Qual é o equivalente binário de 255?

## Quiz Answer

11111111
